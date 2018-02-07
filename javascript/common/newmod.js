autowatch = 1;
outlets = 2;

var finder;
var this_device;
var patch_type = jsarguments[1]||'info';
var unique = jsarguments[2]||'';
var wiki_addy = 'http://www.aumhaa.com/wiki/index.php?title='+patch_type;
var script = this;
var MONOMODULAR=new RegExp(/(monomodular)/);
var FUNCTION = new RegExp(/(function)/);
var PROPERTY = new RegExp(/(property)/);
var WS = new RegExp('');
var modFunctions = [];
var modAddresses = [];
var this_device_id = 0;
var stored_messages = [];
var legacy = false;
var control_surface_ids = {0:true};
var restart = new Task(init, this);

var DEBUG = true;
var debug = (DEBUG&&Debug) ? Debug : function(){};

var FORCELOAD = false;
var forceload = (FORCELOAD&&Forceload) ? Forceload : function(){};

function init()
{

	debug('patch:', patch_type, 'init');
	var found = false;
	debug('init_b996');
	assign_attributes();
	if(!(finder instanceof LiveAPI))
	{
		finder = new LiveAPI(callback, 'control_surfaces');
	}
	finder.goto('this_device');
	this_device_id = parseInt(finder.id);
	debug('this device id:', this_device_id);
	finder.goto('control_surfaces');
	var number_children = parseInt(finder.children[0]);
	debug('control_surfaces length:', number_children);
	for(var i=0;i<number_children;i++)
	{
		debug('Checking control surface #:', i);
		finder.goto('control_surfaces', i);
		if(!control_surface_ids[parseInt(finder.id)])
		{
			debug('Control surface #:', i, 'was NOT in list of excluded surfaces.');
			var children = finder.info.toString().split(new RegExp("\n"));
			var functions = [];
			var properties = [];
			for(var item in children)
			{
				if(FUNCTION.test(children[item]))
				{
					//debug('adding function:', children[item].replace('function ', ''));
					functions.push(children[item].replace('function ', ''));
				}
				if(PROPERTY.test(children[item]))
				{
					//debug('adding property:', children[item].replace('property ', ''));
					properties.push(children[item].replace('property ', ''));
				}	
			}
			for(var item in properties)
			{
				debug('\nProperty #', item, ':', properties[item]);
				if(MONOMODULAR.test(properties[item])>0)
				{
					debug('in there');
					found = true;
					var new_id = finder.get('monomodular');
					debug('found, focusing on', new_id);
					finder.id = parseInt(new_id[1]);
					debug('new object name is', finder.get('name'));
					finder.id = parseInt(finder.call('add_mod', 'id', this_device_id)[1]);
					debug('client id returned is: ', finder.id);
					finder.property = 'value';
					var children = finder.info.toString().split(new RegExp("\n"));	
					for(var item in children)
					{
						if(FUNCTION.test(children[item]))
						{
							debug('adding function:', children[item].replace('function ', ''));
							modFunctions.push(children[item].replace('function ', ''));
						}	
					}
					modAddresses = finder.call('addresses');
					debug('addresses:', modAddresses);
					for(var address in modAddresses)
					{
						debug('address length', modAddresses[address].length);
						debug('making func:', modAddresses[address]);
						script[modAddresses[address]] = make_receive_func(modAddresses[address]);
					}
					for(var func in modFunctions)
					{
						script[modFunctions[func]] = make_func(modFunctions[func]);
					}
					if(legacy)
					{
						finder.call('set_legacy', 1);
					}
					outlet(1, 'init');
					send_stored_messages();
					//return;
				}
				else
				{
					control_surface_ids[parseInt(finder.id)] = true;
				}
			}
		}
		else
		{
			debug('Control surface #:', i, 'WAS in list of excluded surfaces.');
		}
		if(found)
		{
			break;
		}
	}
	if(!found)
	{
		restart.schedule(10000);
	}
}

function _disconnect()
{
	for(var address in modAddresses)
	{
		script[modAddresses[address]] = anything;
	}
	for(var func in modFunctions)
	{
		script[modFunctions[func]] = anything;
	}
	restart.schedule(3000);
}

function assign_attributes()
{
	for(var i=0;i<jsarguments.length;i++)
	{
		if(jsarguments[i].toString().charAt(0) == '@')
		{
			var new_att = jsarguments[i].slice(1).toString();
			script[new_att] = jsarguments[i+1];
		}
	}
}

function make_receive_func(address)
{
	var func = function()
	{
		debug('accessing func', address);
		var args = arrayfromargs(arguments);
		finder.call('receive', address, args[0], args.slice(1).join('^'));
	}
	return func;
}

function make_func(address)
{
	var func = function()
	{
		var args = arrayfromargs(arguments);
		debug('accessing func', address, args.join('^'));
		//finder.apply(address, args);
		finder.call('distribute', address, args.join('^'))
	}
	return func;
}

function anything()
{
	var args = arrayfromargs(arguments);
	debug('anything', messagename, args);
	if(finder == null)
	{
		debug('adding to stack:', messagename, args);
		if(stored_messages.length>500)
		{
			stored_messages.shift();
		}
		stored_messages.push([messagename, args]);
		debug('added:', stored_messages[0]);
	}
}

function list_functions()
{
	outlet(1, 'available_functions', modFunctions);
}

function list_addresses()
{
	outlet(1, 'available_addresses', modAddresses);
}

function callback(args)
{
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		debug('from client:', args);
		outlet(0, args.slice(1));
		if(args[1]=='disconnect')
		{
			_disconnect();
		}
	}
}

function dummy_callback(){}

function send_stored_messages()
{
	debug('send_stored_messages()');
	for(index in stored_messages)
	{
		debug('sending stored message:', stored_messages[index]);
		if(stored_messages[index][0] in script)
		{
			debug('found function in script.');
			script[stored_messages[index][0]].apply(this, (stored_messages[index][1]));
		}
	}
	stored_messages = [];
}

function send_explicit()
{
	var args = arrayfromargs(arguments);
	debug('send explicit', args);
	//post('finder.call('+args[0], args[1], args[2], args[3], args[4], args[5]+');');
	finder.call.apply(finder, args);
}

function debug(){}

forceload(script);
