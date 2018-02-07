/*
c_mods_b994 by amounra a.k.a. James Westfall
This js is a modified version of Monomodular's mod.js, and is capable of connecting to the Monomodular host embedded inside the CNTRL:R Python script.
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

const version = 'b994';							//this is used for value checking - if this version # is not compatible with the Python version, the switchboard will refuse connection
const CLIENT_NUMBERS = [109, 110, 111, 112];	//the api object numbers of the Client class instances that this script will connect (part of surface)
const SWITCHBOARD = 113;
const CNTRLR=new RegExp(/(Cntrlr)/);
const NUMBER = new RegExp(/(\D)/);
const wheel_param = {'value':0, 'mode':1, 'green':2, 'white':3, 'custom':4}		   //used for addressing the Python interpreter due to limitation of outgoing message formatting
var patch_type = jsarguments[1];				//string used for reporting Max Window messages
var unique = jsarguments[2];					//numeric used for messaging - should always be entered as '---', which is converted to a unique 3 digit prefix in m4l

var reconnect = new Task(connect, this);
var reinit = new Task(init, this);

var script = this;								//this, in the context of the entire script (dir type functions can be ran through it, as every function instance is a property of it)

var preview = false;							//preview is set to 0 when the patch isn't active, and 1 when it is.  This state changes depending upon whether the editor has been opened or not.	
var connected = false;							//connected is set to True after the patch has been connected to the switchboard.
var initialized = false;						//initialized is set to true after live.this_device has sent out it's initial bang from its left output
var in_live = this.max.isplugin;				//gathered from max obejct, and lets the script know whether this instance is in m4l or Live

//API Objects
var live_set;									//api object for 'path live_set'
var surface;									//becomes api object for the 'path control_surfaces' + CNTRLR
var device;										//api object for the m4l device this script resides in
var switchboard;								//api object for the switchboard class inside the linked Python Script

var cs = -1;									//the numerical designation for the Python CS script
var client_number = 4;							//the Client # that is linked to from switchboard
var this_id = 0;								//device id of the current m4l device the script resides in

var client_menu;								//the menu object connected to the third inlet of this js object 
var autoselect = 0;								//whether or not choosing the mod via the surface causes the DeviceComponent to lock to its parameters

var local_ring_control = 1;						//used for Code and CNTRLR
var absolute_mode = 1;
var monomodular = 0;
var device_type = jsarguments[1];
var device_parent;
var device_chain;
var device_device;
var mod_color = 127;							//color displayed for a loaded mod on the CNTRLR's top row of endless encoders
var raw_enabled = 0;


var stored_grid = [];							//array to store grid values received when the script is either dead or disconnected
var stored_color_maps = [];						//array to store 128 register color map, allowing multiple controllers to share the same patches, but retain unique color schemes for each one
var i=3;do{
	stored_grid[i]=[];
	var j=3;do{
		stored_grid[i][j] = 0;
	}while(j--);
}while(i--);
var stored_keys = [];						 	//array to store key values received when the script is either dead or disconnected
var k=31;do{
	stored_keys[k]=0;
}while(k--);
var stored_rings = [];
var stored_buttons = [];
var m=3;do{
	stored_rings[m]=[];
	stored_buttons[m]=[];
	var n=2;do{
		stored_rings[m][n]=0;
		stored_buttons[m][n]=0;
	}while(n--);
}while(m--);
var stored_raw = [];

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

//reveal private functions to the containing patch after connection
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

//hide private function from the containing patch at disconnection
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

//called whenever a m4l patch is saved - dissolves patch so that it can be reinitialized correctly
function save()
{
	if(DEBUG){post('saved', '\n');}
	dissolve();
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
			//post('new_att', new_att, jsarguments[i+1], '\n');
		}
	}
}

//initializes above methods
function loadbang()
{
	if(DEBUG){post('loadbang, initialized:', initialized, 'connected:', connected, 'preview:', preview, '\n');}
	assign_attributes();
	this.patcher.getnamed('clientlivid');
	//client_number = client_menu.getvalueof();
}

//dummy callback for API objects - workaround for Max6 js API Object behavior
function callback(){}

//create the essential API objects and find the Monomodular CS instance
function init()
{
	if(DEBUG||DEBUGCNX){post('init_b994\n');}
	tasks = [];				   //reset task buffer
	client_menu=this.patcher.getnamed('clientlivid');
	switchboard = new LiveAPI(callback, 'control_surfaces');
	for(var i= 0;i<6;i++)
	{
	   switchboard.goto('control_surfaces', i);
		//find the CNTRLR surface through regexp test of its Type (returns Class)
		if(CNTRLR.test(switchboard.type)==1)
		{
			cs = i;
			device = new LiveAPI(callback, 'this_device');
			this_id = device.id;
			surface = new LiveAPI(pipe, 'control_surfaces', cs);
			switchboard.goto('control_surfaces', cs, 'controls', SWITCHBOARD);
			connected = true;
			post(patch_type, unique, 'is connected to CNTRL\:R\'s Switchboard\n');
			connect();
			break;
		}
	}
	if(connected == false)
	{
		client_menu.message('set', 4);
	}
}

//request a client address from the switchboard
function connect()
{
	if(DEBUG||DEBUGCNX){post('connect', client_number, '\n');}
	if((initialized==true)&&(preview==true)&&(connected==true))
	{
		var new_client;
		//if the client_number received from the menu was 4, that means we are 'asking' for an open slot, so we use request_connection
		if((client_number==4)||(in_live==0))
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
			new_client = 4;
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
	if(client_number < 4)
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
		client_menu.message('set', 4);
		hide_functions();
	}
}

//reset to initial state and send a message to the containing patch 
function dissolve()
{
	hide_functions();
	post(patch_type, unique, ' mod.js dissolved!\n');
	initialized = false;
	preview = false;
	connected = false;
	messnamed(unique+'alive', 0);
	outlet(4, 'alive', 0);
}

//send the stored values received while disconnected
function send_stored_data()
{
	surface.call('set_raw_enabled', raw_enabled);		//notify the monoclient whether it should send and recieve in raw data formatting
	surface.call('set_local_ring_control', local_ring_control);		   //set up local ring control for the CS Script
	surface.call('set_absolute_mode', absolute_mode);						//set up whether the encoders should send relative or absolute values
	surface.call('set_monomodular', monomodular);						//tell the CNTRLR whether this mod is meant to work in conjunction with an instance of Monomodular
	surface.call('receive_mod_color', mod_color);						 //send the color thqt will be indicated on the single led below the mods volume encoder
	surface.call('receive_device', 'set_mod_device_parent', 'id', device_parent);
	surface.call('receive_device', 'set_mod_device_type', patch_type);
	if(device_chain>0){
		surface.call('receive_device', 'set_mod_device_chain', device_chain);
	}
	if(device>0){
		surface.call('receive_device', 'set_mod_device', 'id', device_device);
	}
	var x=3;do{
		var y=3;do{
			_grid(x, y, stored_grid[x][y]);
		}while(y--);
	}while(x--);
	var k=31;do{
		_key(k, stored_keys[k]);
	}while(k--);
	var r=3;do{
		var t=2;do{
			_ring(r, t, stored_rings[r][t]);
		}while(t--);
	}while(r--);
	var b=3;do{
		var w=2;do{
			_button(b, w, stored_buttons[b][w]);
		}while(w--);
	}while(b--);
	if(DEBUG){post('stored_raw', stored_raw, '\n');}
	while(stored_raw.length>0){
		var item = stored_raw.pop();
		_raw(item[0], item[1], item[2]);
		if(DEBUG){post('stored raw', item[0], item[1], item[2], '\n');}
	}
	stored_raw=[];
}

//pipe is the Python callback from the monoclient instance;  all data from Python is sent through it
function pipe(args)
{
	if(DEBUG){post('pipe', this.id, client_number, unique, args, '\n');}
	if(args[0]=='value')
	{
		switch(args[1])
		{
			case('reconnect'):
				if(DEBUGCNX){post('reconnect', unique, '\n');}
				surface.id = 0;
				hide_functions();
				messnamed(unique+'alive', 0);
				outlet(4, 'alive', 0);
				client_menu.message('set', 4);
				client_number = 4;
				reconnect.schedule(200);
				break;
			case('disconnect'):
				if(DEBUGCNX){post('disconnect', unique, '\n');}
				hide_functions();
				client_menu..message('set', 4);
				break;
			case('bang'):
				if(DEBUGCNX){post('bang\n');}
				post(patch_type, unique, 'mod.js is connected to CNTRL\:R client', client_number, '\n');
				break;
			case('grid'):
				messnamed(unique + 'in', args[2], args[3], args[4]);
				outlet(0, args[2], args[3], args[4]);
				break;
			case('key'):
				messnamed(unique + 'key', args[2], args[3], args[4]);
				outlet(1, args[2], args[3]);
				break;
			case('knob'):
				messnamed(unique + 'knob', args[2], args[3], args[4]);
				outlet(4, args[2], args[3]);
				break;
			case('dial'):
				messnamed(unique + 'wheel', 'dial', args[2], args[3], args[4]);
				outlet(2, 'dial', args[2], args[3], args[4]);
				break;
			case('dial_button'):
				messnamed(unique + 'wheel', 'button', args[2], args[3], args[4]);
				outlet(3, 'button', args[2], args[3], args[4]);
				break;
			case ('raw'):
				outlet(4, 'raw', args[2], args[3], args[4]);
				break;
			case('lcd'):
				messnamed(unique + 'lcd', 'lcd', args[2], args[3], args[4]);
				outlet(0, 'lcd', args[2], args[3], args[4]);
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


//used for initiating and dissolving the patches functionality when the enclosing patch opens or closes
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
				stored_grid[args[1]][args[2]] = args[3];
			}
			break;
		case 4:
			if(args.length > 1){
				stored_keys[args[1]] = args[2];
			}
			break;
		case 5:
			if(args.length > 2){
				stored_rings[args[1]][args[2]] = args[3];
			}
			break;
		case 6:
			if(args.length > 2){
				stored_buttons[args[1]][args[2]] = args[3];
			}
			break;	
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
					var i=3;do{
						stored_grid[i]=[];
						var j=3;do{
							stored_grid[i][j] = args[1];
						}while(j--)
					}while(i--)
					break;
			}
			break;
		case 'raw':
			stored_raw.unshift([args[1], args[2], args[3]]);
			if(stored_raw.length > 500){
				stored_raw.length = 500;
			}
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
		case 'set_device':
			device_device = args[1];
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
		default:
			//script[args[0]](args[1]);
			break;
	}
}

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

//call from any control, sent with the type and identifier and distributed by backend methods
function _raw(type, id, value)
{
	if(DEBUG){post('_raw', type, id, value, '\n');}
	surface.call('receive_raw', type, id, value);
}

//call from the patch 4x4, to be sent to the controller
function _grid(x, y, val)
{
	if(DEBUG){post('_grid', x, y, val, '\n');}
	surface.call('receive_grid', x, y, val);
	stored_grid[x][y] = val;
}

//call from the patch to the 2x16, addressed as 0-31
function _key(num, val)
{
	if(DEBUG){post('_key', num, val, '\n');}
	surface.call('receive_key', num, val);
	stored_keys[num] = val;
}

//call from patch to the 4x3 lights below the encoders
function _button(x, y, val)
{
	if(DEBUG){post('_button', x, y, val, '\n');}
	to_wheel(x, y, 'white', val);
	stored_buttons[x][y]=val;
}

//call from the patch to the 4x3 encoder rings
function _ring(x, y, val)
{
	if(DEBUG){post('_ring', x, y, val, '\n');}
	to_wheel(x, y, 'value', val);
	stored_rings[x][y]=val;
}

//call from patch to the 4x3 endless encoders
function _to_wheel(x, y, parameter, value)
{
	if(DEBUG){post('_to_wheel', x, y, parameter, value, '\n');}
	surface.call('receive_wheel', x + (y * 4), parameter, value);	 
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
			var i=3;do{
				stored_grid[i]=[];
				var j=3;do{
					stored_grid[i][j] = args[1];
				}while(j--)
			}while(i--)
			break;
	}
}

//set the color of the led indicator below the moddial
function _set_mod_color(val)
{
	mod_color = val;
	surface.call('receive_mod_color', mod_color);
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
function _exclusive(args)
{
	//post('exclusive', args.join(' '), '\n');
	if(args[0] == patch_type)
	{
		messnamed(unique+'hotline', args.slice(1));
	}
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

