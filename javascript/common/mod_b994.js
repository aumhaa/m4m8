/*
mods_b994.js by amounra a.k.a. James Westfall 082612

This js is used to connect a Max4Live patch to a Monomodular Python MIDI Remote Script.

None of the public connection methods should be modified in any way.  The nature of Max6's and Live's interaction when switching between
	edit and plugin modes, as well as idiosyncracies that occur when saving patches, have required the need for some very convoluted 
	routines to maintain proper initialization order without causing MxDCore to become unstable.  I highly advise leaving things in the 
	top section of this patch alone....its taken me a great deal of tinkering to get things working in all modes.

Additianal private functions can be added as needed to accomodate further revisions to the Monomodular host environment, or facilitate 
	custom interactions of the preexisting methods. 

For help or further info:  aumhaa@gmail.com
*/

autowatch = 1;

inlets = 8;
outlets = 5;


setinletassist(0, 'init patch input');
setinletassist(1, 'freebang');
setinletassist(2, 'connection menu left outlet');
setinletassist(3, 'grid input');
setinletassist(4, 'key input');
setinletassist(5, 'ring input');
setinletassist(6, 'button input');
setinletassist(7, 'anything');
setoutletassist(0, 'grid output');
setoutletassist(1, 'key output');
setoutletassist(2, 'dial output');
setoutletassist(3, 'button output');
setoutletassist(4, 'status and raw output');

const DEBUG = 0;
const DEBUGCNX = 0;

const version = 'b994';
const CLIENT_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];	  //the api object numbers of the Client class instances that this script will connect (part of surface)
const SWITCHBOARD = 16;
const color_maps = ['OhmRGB', 'Monochrome', 'AumPad', 'Launchpad'];
const MONOMOD=new RegExp(/(Monomodular)/);
const NUMBER = new RegExp(/(\D)/);
const wheel_param = {'value':0, 'mode':1, 'green':2, 'white':3, 'custom':4}
var patch_type = jsarguments[1];
var unique = jsarguments[2];
var wiki_addy = 'http://www.aumhaa.com/wiki/index.php?title='+patch_type;

var reconnect = new Task(connect, this);
var reinit = new Task(init, this);

var script = this;

var preview = false;
var connected = false;
var initialized = false;
var in_live = this.max.isplugin;

//API Objects
var live_set;
var surface;
var device;
var switchboard;

var cs = -1;
var client_number = 16;
var this_id = 0;

var client_menu;
var autoselect = 0;

var tasks = [];
var swing_val = .5;
var offset_report = 0;
var channel = 0;
var local_ring_control = 1;	   //used for Code and CNTRLR
var absolute_mode = 1;
var device_type = jsarguments[1];
var device_parent;
var device_chain;
var device_device;

var stored_color_maps = [];
var stored_grid = [];
var i=15;do{
	stored_grid[i]=[];
	var j=15;do{
		stored_grid[i][j] = 0;
	}while(j--);
}while(i--);
var stored_keys = [];						 //array to store key values received when the script is either dead or disconnected
var k=7;do{
	stored_keys[k]=0;
}while(k--);
var default_color_map = [];
var l=127;do{
	default_color_map[l]=l;
}while(l--);

/*	VERY IMPORTANT!! : This code utilizes a naming convention for private functions:  any function 
preceeded by an underscore is considered private, but will have a public property reference	 
assigned to it AFTER the script has distribute an initiallization call.  That means that any 
function that shouldn't be accessed before initialization can be created as a private function without 
the need to use an internal test to find out whether the script has init()ed.  

Example:

If we create _private_function(), and before init a call from max comes in to private_function(), that call 
will be funneled to anything().	 After init(), however, all calls to private_function() will be forwarded to 
_private_function().

Note:  It is necessary to only address these private functions by their actual names in the script, since calling aliased 
names will not be routed to anything().  Any function that shouldn't be called before initialization should only be called
from outside the js by an aliased private function.*/

assign_default_functions();

//assign the default routing functions used when the patch isn't connected to a control surface
function assign_default_functions()
{
	script['list'] = script['List'];
	script['anything'] = script['Anything'];
}

function reveal_functions()
{
	if(DEBUGCNX){post('reveal_functions\n');}
	script['list']=script['_list'];
	script['anything']=script['_anything'];
	for(var i in script)
	{
		if((/^_/).test(i))
		{
			script[i.replace('_', '')] = script[i];
		}
	}
}

function hide_functions()
{
	if(DEBUGCNX){post('hide_functions\n');}
	for(var i in script)
	{
		if((/^_/).test(i))
		{
			script[i.replace('_', "")] = Anything;
		}
		assign_default_functions();
	}
}

function make_maps(maps)
{
	for (var index in maps)
	{
		var map = maps[index];
		if(typeof(script[map])==typeof(undefined))
		{
			script[map] = default_color_map.slice();
			script[map]._name = map;
		}
		//var get_func = make_get_map(map);
		//var set_func = make_set_map(map);
		//declareattribute(map,	 get_func, set_func);
	}
}

function make_get_map(map)
{
	script[map+'_get'] = function()
	{
		return script[map];
		//post('get', map, '\n');
	}
	return (map+'_get');
}

function make_set_map(map)
{
	script[map+'_set'] = function()
	{
		args = arrayfromargs(arguments);
		//post('set', map, args, '\n');
		script[map] = args;
		send_color_map(map, args);
		notifyclients();
	}
	return (map+'_set');
}

//called whenever a m4l patch is saved - prevents things from happening before initialization by live.this_device
function save()
{
	if(DEBUG){post('saved', '\n');}
	dissolve();
	//for(var j=0;j<color_maps.length;j++)
	//{
	//	  var store_name = color_maps[j];
	  //  var store_colors = script[color_maps[j]].slice();
		//post('color map', store_name, store_colors, '\n');
		//embedmessage('restore_color_map', store_name, store_colors);
	//}
}

function restore_color_map()
{
	//post('restore_color_map');
	var args = arrayfromargs(arguments);
	var stored_name = args[0];
	var stored_map = args.slice(1, args.length);
	//post('args', args, '\n');
	//post('restore_color_map', stored_name, stored_map, '\n');
	script[stored_name] = stored_map;
	script[stored_name]._name = stored_name;
	var get_func = make_get_map(stored_name);
	var set_func = make_set_map(stored_name);
	declareattribute(stored_name,  get_func, set_func);
	notifyclients();
}

//assigns patcher arguments to properties of script(i.e. js.this)
function assign_attributes()
{
	for(var i=0;i<jsarguments.length;i++)
	{
		if(jsarguments[i].toString().charAt(0) == '@')
		{
			var new_att = jsarguments[i].slice(1).toString();
			script[new_att] = jsarguments[i+1];
			//declareattribute(new_att);
		}
	}
}

//initializes above mehtods
function loadbang()
{
	if(DEBUG){post('loadbang, initialized:', initialized, 'connected:', connected, 'preview:', preview, '\n');}
	//declareattribute('autoselect', null, null, 1);
	//declareattribute('offset_report', null, null, 1);
	make_maps(color_maps);
	assign_attributes();
	client_menu = this.patcher.getnamed('client');
	//client_number = client_menu.getvalueof();
}

//dummy callback for API objects - workaround for Max6 js API Object behavior
function callback(){}

//this is called from anything() when a bang is received in the first inlet from live.this_device's left outlet
function init()
{
	if(DEBUG||DEBUGCNX){post('init_b994\n');}
	tasks = [];				   //reset task buffer
	client_menu=this.patcher.getnamed('client');
	switchboard = new LiveAPI(callback, 'control_surfaces');
	for(var i= 0;i<6;i++)
	{
	   switchboard.goto('control_surfaces', i);
		//find the Monomodular surface through regexp test of its Type (returns Class)
		if(MONOMOD.test(switchboard.type)==1)
		{
			cs = i;
			device = new LiveAPI(callback, 'this_device');
			this_id = device.id;
			surface = new LiveAPI(pipe, 'control_surfaces', cs);
			switchboard.goto('control_surfaces', cs, 'controls', SWITCHBOARD);
			connected = true;
			post(patch_type, 'is connected to Monomodular\'s Switchboard\n');
			connect();
			break;
		}
	}
	if(connected == false)
	{
		client_menu.message('set', 16);
	}
}

//now we try to connect to an instance of the Client class through the switchboard
function connect()
{
	if(DEBUG||DEBUGCNX){post('connect', client_number, '\n');}
	if((initialized==true)&&(preview==true)&&(connected==true))
	{
		var new_client;
		//if the client_number received from the menu was 0, that means we are 'asking' for an open slot, so we use request_connection
		if((client_number==16)||(in_live==0))
		{
			new_client = switchboard.call('request_connection', 'id', this_id, version, in_live);
		}
		else
		{
			new_client = switchboard.call('force_connection', 'id', this_id, client_number, version);
		}
		//at this point, Python will have returned either the connected client number (0-3 if connected, or 4 if there was no slot available),
		//or if there was a version mismatch, it will have returned its own version number to compare as a string
		if(typeof(new_client)=='string')
		{
			post('Monomod version mismatch!\nmod.js:', version, '\nMonomodular.py:', new_client, '\nMake sure you\'re using compatible versions of these files.');
			new_client = 16;
		}
		set_client_number(new_client);
	}
}

//if connection was successful, this is the final step to set things up
function set_client_number(num)
{
	if(DEBUG||DEBUGCNX){post('set_client_number\n');}
	client_number = num;
	client_menu.message('set', client_number);	  //send the current client number to the client menu UI object
	if(client_number < 16)
	{
		surface.goto('control_surfaces', cs, 'controls', parseInt(CLIENT_NUMBERS[client_number]));		  //surface now becomes the Client class instance of the CS script, where it will stay until we disconnect or reconnect to another client
		surface.property = 'value';	
		reveal_functions();
		send_stored_data();							//send any values received and stored by the script while it was languishing (either because it hadn't inititated yet, or because it was disconnected)
		messnamed(unique+'alive', 1);
		outlet(4, 'alive', 1);
		messnamed(unique + 'refresh', 'bang');		//used to refresh state of controller after it is initially connected, use it to send your current data)
	}
	else
	{
		//if the client is disconnected (client_number = 0), we need to turn off the callback that its connected Client instance was reporting to
		surface.id = 0;
		client_menu.message('set', 16);
		hide_functions();
	}
}

//turn off all API callbacks when changing modes (edit vs. Live) or deleting m4l patch
function dissolve()
{
	hide_functions();
	post(patch_type, ' mod.js dissolved!\n');
	iniitiated = false;
	preview = false;
	connected = false;
	messnamed(unique+'alive', 0);
	outlet(4, 'alive', 0);
}

//send the stored values received while dead or disconnected
function send_stored_data()
{
	//surface.call('set_raw_enabled', raw_enabled);		//notify the monoclient whether it should send and recieve in raw data formatting
	surface.call('set_local_ring_control', local_ring_control);		   //set up local ring control for the CS Script
	surface.call('set_absolute_mode', absolute_mode);						//set up whether the encoders should send relative or absolute values
	//surface.call('receive_device', 'set_mod_device_parent', 'id', device_parent);
	//surface.call('receive_device', 'set_mod_device_type', patch_type);
	for (var map in color_maps)
	{
		send_color_map(color_maps[map], script[color_maps[map]]);
	}
	var x=15;do{
		var y=15;do{
			_grid(x, y, stored_grid[x][y]);
		}while(y--);
	}while(x--);
	var k=7;do{
		_key(k, stored_keys[k]);
	}while(k--);
	/*var r=3;do{
		var t=2;do{
			_ring(r, t, stored_rings[r][t]);
		}while(t--);
	}while(r--);*/
	/*var b=3;do{
		var w=2;do{
			_button(b, w, stored_buttons[b][w]);
		}while(w--);
	}while(b--);*/
	/*while(stored_raw.length>0){
		var item = raw.pop();
		_raw(item[i][0], item[i][1], item[i][2]);
		if(DEBUG){post('stored raw', item[i][0], item[i][1], item[i][2], '\n');}
	}
	stored_raw=[];*/
	_set_channel(channel);
	_set_report_offset(offset_report);
}

//pipe is the single callback instance that everything in the Python Script report through
//all commands are distributed through the outlets of the js as well as unique-prefixed sends
//in addition, ping commands are sent through this port direct from the client when another mod.js instance forces connection to a port that this instance is connected
function pipe(args)
{
	if(DEBUG){post('pipe', client_number, unique, args, '\n');}
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		switch(args[1])
		{
			case('reconnect'):
				if(DEBUGCNX){post('reconnect', unique, '\n');}
				surface.id = 0;
				hide_functions();
				messnamed(unique+'alive', 0);
				outlet(4, 'alive', 0);
				client_menu.message('set', 16);
				client_number = 16;
				reconnect.schedule(200);
				break;
			case('disconnect'):
				if(DEBUGCNX){post('disconnect', unique, '\n');}
				hide_functions();
				client_menu..message('set', 16);
				break;
			case('bang'):
				if(DEBUGCNX){post('bang\n');}
				post(patch_type, unique, 'mod.js is connected to client', client_number, '.\n');
				break;
			case('grid'):
				messnamed(unique + 'in', args[2], args[3], args[4]);
				outlet(0, args[2], args[3], args[4]);
				break;
			case('key'):
				messnamed(unique + 'key', args[2], args[3], args[4]);
				outlet(1, args[2], args[3]);
				break;
			/*case('knob'):
				messnamed(unique + 'knob', args[2], args[3], args[4]);
				outlet(4, args[2], args[3]);
				break;*/
			case('dial'):
				messnamed(unique + 'wheel', 'dial', args[2], args[3], args[4]);
				outlet(3, 'dial', args[2], args[3], args[4]);
				break;
			case('dial_button'):
				messnamed(unique + 'wheel', 'button', args[2], args[3], args[4]);
				outlet(3, 'button', args[2], args[3], args[4]);
				break;
			case('column_button'):
				//post('column', args[2], args[3], '\n');
				messnamed(unique + 'wheel', 'column', args[2], args[3]);
				outlet(3, 'column', args[2], args[3]);
				break;
			case('row_button'):
				//post('row', args[2], args[3], '\n');
				messnamed(unique + 'wheel', 'row', args[2], args[3]);
				outlet(3, 'row', args[2], args[3]);
				break;
			case('channel'):
				messnamed(unique + 'channel', args[2]);
				outlet(2, args[2]);
				break;
			case('swing'):
				messnamed(unique + 'swing', args[2]);
				break;
			case('autoselect'):
				//post('autoselect');
				//autoselect_ack();
				break;
			case('offset'):
				messnamed(unique + 'offset', 'surface_offset', args[2], args[3]);
				break;
			case('alt'):
				messnamed(unique + 'alt', args[2]);
				break;
			case('toggle_mute'):
				messnamed(unique + 'toggle_mute', 'bang');
				break;
			/*case ('raw'):
				outlet(4, 'raw', args[2], args[3], args[4]);
				break;*/
			case('lcd'):
				messnamed(unique + 'lcd', 'lcd', args[2], args[3], args[4]);
				outlet(4, 'lcd', args[2], args[3], args[4]);
				break;
			case('hotline'):
				//hotline is a new function that allows different mod.js instances to talk to one another
				if(DEBUG){post('hotline', args[2], args[3], '\n');}
				if(args[3].length>1)
				{
					var new_args = args[3].split('^');
				}
				else
				{
					var new_args = [args[3]];
				}
				for(var i in new_args)
				{
					if(isNumeric(new_args[i])==true)
					{
						new_args[i] = parseFloat(new_args[i]);
					}
				}
				if(script[args[2]])
				{
					script[args[2]](new_args);
				}
				else
				{
					messnamed(unique+'hotline', args[2], new_args);
				}
				break;
			default:
				if(DEBUG){post('pipe receive', args, '\n');}
				break;
		}
	}
}


/*/////////////////////////////////////
///     Public Generic functions  /////
/////////////////////////////////////*/

//These functions are referenced when the js instance initially loads, and are replaced by their corresponding
//private functions after the js instance is born via live.this_device bang and the Python connection routines.
//The private functions are again replaced by these after the connection is dropped or the patch is destroyed via 
//freebang.

//used for initiating and dissolving the patches functionality when the enclosing patch 
//opens or closes
function bang()
{
	if(DEBUG){post('bang, inlet:', inlet, '\n');}
	if(inlet==0)
	{
		initialized = true;
		preview = true;
		init();
	}
	else if(inlet==1)
	{
		dissolve();
	}
}

//default list function used when the js isn't connected to a control surface
function List()
{
	var args = arrayfromargs(arguments);
	if(DEBUG){post('List:', args, 'Inlet:', inlet, '\n');}
	switch(inlet)
	{	   
		case 0:
			switch(args[0])
			{
				case 0:
					initialized = true;
					if(preview==true)
					{
						if(connected==false)
						{
							init();
						}
						else
						{
							connect();
						}
					}
					break;
				case 1:
					if(parseInt(args[1])!=parseInt(preview))
					{
						if(DEBUG){post('preview in:', args[1], '!= preview stored', preview, '\n');}
						preview = (args[1]>0);
						if((initialized==true)&&(preview==true))
						{
							if(connected==false)
							{
								if(DEBUG){post('not connected but preview true and intialized true, reinit...\n');}
								reinit.schedule(1000);
							}
							else if(in_live)
							{	
								if(DEBUG){post('connected, preview and  intialized true, connect...\n');}	
								connect();
							}
							else
							{
								if(DEBUG){post('connected, preview and  intialized true, reconnect...\n');}
								reconnect.schedule(1000);
							}
						}
					}
					break;
			}
			if(DEBUGCNX){post('inlet 0 end:', args, 'initialized', initialized, 'preview', preview, 'connected', connected, '\n');}
			break;
		case 2:
			if(DEBUGCNX){post('client number received', args[0], '\n');}
			client_number = parseInt(args[0]);
			if((initialized==true)&&(preview==true)&&(connected==true))
			{
				if(DEBUGCNX){post('client number to connect()\n');}
				connect();
			}
			break;
		case 3:
			if(args.length > 2){
				stored_grid[args[0]][args[1]] = args[2];
			}
			break;
		case 4:
			if(args.length > 1){
				stored_keys[args[0]] = args[1];
			}
			break;
		/*case 5:
			if(args.length > 2){
				stored_rings[args[0]][args[1]] = args[2];
			}
			break;*/
		/*case 6:
			if(args.length > 2){
				stored_buttons[args[0]][args[1]] = args[2];
			}
			break;*/		
	}
}

//default anything function used when the js isn't connected to a control surface
function Anything()
{
	args = arrayfromargs(messagename, arguments);
	if(DEBUG){post('Anything', args, '\n');}
	switch(args[0])
	{
		case 'grid':
			stored_grid[args[1]][args[2]] = args[3];
			break;
		case 'key':
			stored_keys[args[1]] = args[2];
			break;
		case 'button':
			stored_buttons[args[1]][args[2]] = args[3];
			break;
		case 'ring':
			stored_rings[args[1]][args[2]] = args[3];
			break;
		case 'batch':
			switch(args[1])
			{
				case 'grid':
					var i=15;do{
						stored_grid[i]=[];
						var j=15;do{
							stored_grid[i][j] = args[1];
						}while(j--)
					}while(i--)
					break;
			}
		case 'swing':
			swing_val = args[1];
			break;
		case 'set_report_offset':
			offset_report = args[1];
			break;
		/*case 'raw':
			stored_raw.unshift([args[1], args[2], args[3]]);
			if(stored_raw.length > 500){
				stored_raw.length = 500;
			}
			break;*/
		case 'set_channel':
			channel = args[1];
			break;
		case 'set_device_type':
			device_type = args[1];
			break;
		case 'set_device_parent':
			device_parent = args[1];
			break;
		case 'set_device_chain':
			device_chain = args[1];
			break;
		case 'set_color_map':
			var newargs = args.splice(1);
			var stored_name = newargs[0];
			var stored_map = newargs.slice(1, newargs.length);
			script[stored_name] = stored_map;
			script[stored_name]._name = stored_name;
			make_maps(color_maps);
			break;
		default:
			break;
	}
}

/*/////////////////////////////////////
///        Private functions      /////
/////////////////////////////////////*/

//When this patch is 'initialized', i.e. when it is delivered a bang from live.this_device's leftmost output,
//any function beginning with an underscore will be reassigned as a public function with a name
//that is accessible from outside the js without the underscore.  Prior to initialization, however, the following 
//functions should be considered private.  They should never be externally called by their internal names. 
//Anything sent to their public names will automatically be re-routed to Anything() prior to patch "connection".

//connected list function used when the js is connected to a control surface
function _list()
{
	var args = arrayfromargs(messagename, arguments);
	if(DEBUG){post('_list', args, '\n');}
	switch(inlet)
	{	   
		case 0:
			switch(args[0])
			{
				case 1:
					if(parseInt(args[1])!=parseInt(preview))
					{
						preview = (args[1]>0);
						if(DEBUGCNX){post('preview', preview, '\n');}
						switch(preview)
						{
							case 0:
								hide_functions();
								break;
						}
						if(DEBUGCNX){post('_list:', args, 'initialized', initialized, 'preview', preview, 'connected', connected, '\n');}
						if((initialized==true)&&(preview==true)&&(connected==false))
						{
							connect();
						}
						break;
					}
				case 2:
					dissolve();
					break;
			}
			break;
		case 2:
			if(DEBUGCNX){post('new client number:', args[0], '\n');}
			client_number = (parseInt(args[0]));
			if((initialized==true)&&(preview==true)&&(connected==true))
			{
				connect();
			}
			break;
		case 3:
			_grid(args[0], args[1], args[2]);
			break;
		case 4:
			_key(args[0], args[1]);
			break;
		case 5:
			_ring(args[0], args[1], args[2]);
			break;
		case 6:
			_button(args[0], args[1], args[2]);
			break;	
	}
}

//connected anything function used when the js is connected to a control surface
function _anything()
{
	args = arrayfromargs(messagename, arguments);
	if(DEBUG){post('_anything', args, '\n');}
	switch(args[0])
	{
		case 'wheel':
			//post('wheel', args[1], args[2], args[3], args[4]);
			if(args[3] == 'custom')
			{
				to_wheel(args[1], args[2], args[3], 'x' + args.slice(4, -1).join(''));
			}
			else
			{	  
				if(args.length==5)
				{	  
					to_wheel(args[1], args[2], args[3], args[4]);
				}
			}
			break;
		case 'column':
			to_wheel(args[1], 4, 'white', args[2]);
			break;
		case 'row':
			to_wheel(8, args[1], 'white', args[2]);
			break;
		default:
			//script[args[0]](args[1]);
			break;
	}
}

//call from the patch 8x8, to be sent to the controller
function _grid(x, y, val)
{
	surface.call('receive_grid', x, y, val);
	stored_grid[x][y] = val;
}

//call from the patch to the 8 keys, addressed as 0-7
function _key(num, val)
{
	surface.call('receive_key', num, val);
	stored_keys[num] = val;
}

//call from patch to the 4x3 lights below the encoders
function _button(x, y, val)
{
	to_wheel(x, y, 'white', val);
	stored_buttons[x][y]=val;
}

//call from the patch to the 4x3 encoder rings
function _ring(x, y, val)
{
	to_wheel(x, y, 'value', val);
	stored_rings[x][y]=val;
}

//call from patch to the 4x3 endless encoders
function _to_wheel(x, y, parameter, value)
{
	if(DEBUG){post('to_wheel', x, y, parameter, value, '\n');}
	surface.call('receive_wheel', x + (y * 9), parameter, value);	 
}

//call from the patch to clear the 4x4 (shortcut to 'batch grid 0')
function _clear()
{
	switch(inlet)
	{
		case 3:
			batch('grid', 0);
		case 4:
			batch('key', 0);
	}
}

//allows a different value to be sent to the controller without changing its stored value
function _mask()
{
	args = arrayfromargs(arguments);
	switch(args[0])
	{
		case 'key':
			surface.call('receive_mask_key', args[1], args[2]);
			break;
		case 'grid':
			surface.call('receive_mask_grid', args[1], args[2], args[3]);
			break;
		case 'column':
			surface.call('receive_mask_column', args[1], args[2]);
			break;
		case 'row':
			surface.call('receive_mask_row', args[1], args[2]);
			break;
	}
}

//allows the entire grid or key area to be lit at once, or to send a column or row as one value
function _batch()
{
	args = arrayfromargs(arguments);
	switch(args[0])
	{
		case 'grid':
			surface.call('receive_grid_all', args[1]);
			var i=15;do{
				stored_grid[i]=[];
				var j=15;do{
					stored_grid[i][j] = args[1];
				}while(j--)
			}while(i--);
			break;
		case 'column':
			surface.call('receive_grid_column', args[1], args[2]);
			var i=15;do{
				stored_grid[args[1]][i] = args[2];
			}while(i--);
			break;
		case 'row':
			surface.call('receive_grid_row', args[1], args[2]);
			var i=15;do{
				stored_grid[i][args[1]] = args[2];
			}while(i--);
			break;
	}
}

//used to send messages to other mod.js instances through the switchboard
//basically, allows you to control another mod instance from this script
function _send_hotline()
{
	args = arrayfromargs(arguments);
	surface.call('receive_hotline', args[0], args[1], args.slice(2).join('^'));
}

//special hotline-callable function that is always available and returns its args 
//to the patch this js is in.  Example:	 calling 'hotline blah exclusive how bout that'
//will cause the message 'bout that' to be sent out a receive object named '---how' 
//in a patch containing a mod.js instance named 'blah'....tricky, but very useful
function exclusive(args)
{
	//post('exclusive', unique, patch_type, args[0], args[1], args[2], args.join(' '), '\n');
	if(args[0] == patch_type)
	{
		messnamed(unique+'hotline', args.slice(1));
	}
}

function _swing(val)
{
	swing_val = val;	
	switchboard.call('receive_swing', client_number, swing_val);
}

function _set_report_offset(val)
{
	offset_report = val;
	surface.call('set_report_offset', val);
}

//used to send the device type to the MonoDeviceComponent; 
//derived from the js's first argument, patch_type
function _set_device_type(dtype)
{
	device_type = dtype;
	surface.call('receive_device', 'set_mod_device_type', device_type);
}

//used to send the parent device of chain-holding devices
function _set_device_parent(dparent)
{
	device_parent = dparent;
	surface.call('receive_device', 'set_mod_device_parent', 'id', device_parent);
}

//used to send a single device in case it is chain-holding but will not use nesting features
function _set_device_single(dparent)
{
	device_parent = dparent;
	surface.call('receive_device', 'set_mod_device_parent', 'id', device_parent, 1);
}

//used to set the device assignment of the monodevicecomponent
function _set_device(dev)
{
	mod_device = dev;
	surface.call('receive_device', 'set_mod_device', 'id', dev);
}

//used to send the currently selected chain when a valid parent device is used
function _set_device_chain(dchain)
{
	device_chain = dchain;
	surface.call('receive_device', 'set_mod_device_chain', device_chain);
}

//set the currently controlled chain/devices parameter value
function _set_parameter_value(num, val)
{
	surface.call('receive_device', 'set_parameter_value', num, val);
}

//set the currently selected MonoDeviceComponent's bank index
function _set_device_bank(bank_index)
{
	surface.call('receive_device', 'set_device_bank', bank_index);
}

//turn on/off local ring control for the selected modClient
function _set_local_ring_control(val)
{
	surface.call('set_local_ring_control', val);
}

//turn on/off absolute mode for the encoders of the selected modClient
function _set_absolute_mode(val)
{
	surface.call('set_absolute_mode', val);
}
	
function _send_color_map(host_name, color_map)
{
	if((initialized==true)&&(connected==true)&&(preview==true))
	{
		var new_map = default_color_map.slice();
		if (color_map[0] == 'fill')
		{
			if(DEBUG){post('filling', host_name, '\n');}
			for(var i = 1;i<128;i++)
			{
				new_map[i] = color_map[(i%(color_map.length-1))+1];
			}
			surface.call('set_color_map', host_name, new_map.join('*'));
		}
		else
		{
			for(i = 1;i<(color_map.length);i++)
			{
				new_map[i] = color_map[i];
			}
			surface.call('set_color_map', host_name, new_map.join('*'));
		}
	}
}

function _set_color_map()
{
	args = arrayfromargs(arguments);
	var stored_name = args[0];
	var stored_map = args.slice(1, args.length);
	script[stored_name] = stored_map;
	script[stored_name]._name = stored_name;
	make_maps(color_maps);
	_send_color_map(script[stored_name]._name, script[stored_name]);
}

function _set_channel(val)
{
	surface.call('receive_channel', val);
	channel = val;
}

function _send_midi()
{
	var args = arrayfromargs(arguments);
	surface.call('send_midi', args.join('^'));
}

//the following two methods are used for distributing tasks via an external metronome
function schedule(task)
{
	var found = false;
	for(var a in tasks)
	{
		if(tasks[a]==task)
		{
			found=true;
		}
	}
	if(found == false)
	{
		tasks.push(task);
	 }
}

//distribute tasks and clear task buffer; to be called from external timing source
function clock()
{
	for(var a in tasks)
	{
		if (script[tasks[a]] instanceof Function)
		{
			script[tasks[a]].apply(tasks[a],[]);
		}
	}
	tasks = [];
}

function wiki()
{
	this.max.launchbrowser(wiki_addy);
}

//utility function used by hotline to determine whether an array index is 
//numeric or a string, since all tuples are sent from Python containing strings
function isNumeric(sText) 
{
	var isNumber=true;
	var numDecimals = 0;
	var validChars = "0123456789.-";
	var thisChar;
	for (i = 0; i < sText.length && isNumber == true; i++) 
	{  
		thisChar = sText.charAt(i); 
		if ((thisChar == "-") && (i > 0))
		{
			isNumber = false;
		}
		if (thisChar == ".")
		{
			numDecimals = numDecimals + 1;
			if ((i==0) || (i == sText.length-1)) 
			{
				isNumber = false;
			}
			if (numDecimals > 1)
			{
				isNumber = false;
			}
		}
		if (validChars.indexOf(thisChar) == -1)
		{
			isNumber = false;
		}
	}
	return isNumber;
}
