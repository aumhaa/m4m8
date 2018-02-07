autowatch = 1;

inlets = 1;
outlets = 1;

var finder;
var control_surface;
var m4lcomp = 0;
var M4LCOMPONENT=new RegExp(/(M4LInterface)/);
var control_names = [];
var controls = {};
var excluded = ['control', 'control_names', 'done'];
var control_surface_type = jsarguments[1]||'None';

var script = this;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = true;
aumhaa.init(this);


if(typeof(String.prototype.trim) === "undefined")
{
	String.prototype.trim = function()
	{
		return String(this).replace(/^\s+|\s+$/g, '');
	}
}


function init()
{
	debug('m4lcomponent init');
	finder = new LiveAPI(callback, 'control_surfaces');
	control_surface = new LiveAPI(callback, 'control_surfaces');
	var number_children = parseInt(finder.children[0]);
	debug('control_surfaces length:', number_children);
	for(var i=0;i<number_children;i++)
	{
		debug('Checking control surface #:', i);
		finder.goto('control_surfaces', i);
		control_surface.goto('control_surfaces', i);
		debug('type is:', finder.type);
		if(finder.type == control_surface_type)
		{
			var components = finder.get('components');
			for (var i in components)
			{
				debug('component is:', finder.type);
				finder.id = components[i];
				if(M4LCOMPONENT.test(finder.type)>0)
				{
					m4lcomp = finder.id;
					break;
				}
			}
			if (m4lcomp)
			{
				debug('found m4linterface');
				var names = finder.call('get_control_names');
				for (var i in names)
				{
					var name = names[i];
					if((name!='control_names')&&(name!='control')&&(name!='done'))
					{
						try
						{
							controls[names[i]] = 0;
						}
						catch(err)
						{
						}
					}
				}
				//control_surface.id = finder.id;
				debug('control_surface is:', control_surface.path);
				deprivatize_script_functions(script);
			}
			outlet(0, 'path', finder.path);
			return;
		}
	}
}

function get_control_names()
{
	for(var i in controls)
	{
		outlet(0, i);
	}
}

function make_callback(name)
{
	var callback = function(args)
	{
		//debug('callback closure:', args);
		outlet(0, name, args);
	}
	return callback;
}

function _grab(name)
{
	if(controls[name]!=undefined)
	{
		if(controls[name]==0)
		{
			var control = finder.call('get_control', name);
			debug('control is:', control);
			controls[name] = new LiveAPI(make_callback(name), control);
			debug('control:', control, controls[name].id);
		}
		finder.call('grab_control', 'id', controls[name].id);
		controls[name].property = 'value';
	}
	else
	{
		debug('Control name:', name, 'isnt registered.');
	}
}

function _release(name)
{
	if(controls[name]!=undefined)
	{
		if(controls[name]!=0)
		{
			controls[name].property = '';
			finder.call('release_control', 'id', controls[name].id);
		}
		else
		{
			debug('Control name:', name, 'hasnt been registered yet.  You need to grab it first.');
		}
	}
	else
	{
		debug('Control name:', name, 'isnt registered.');
	}
}

function _send_value()
{
	var args = arrayfromargs(arguments)
	var obj = controls[args[0]]
	if((obj)&&(obj.property!=''))
	{
		debug('args', args.slice(1));
		obj.call('send_value', args[1], args[2], args[3]);
	}
}

function _call_function()
{
	var args = arrayfromargs(arguments);
	func = args[0] ? args[0] : undefined;
	debug('call_function:', func, 'args:', args);
	try
	{
		control_surface.call.apply(control_surface, args);
	}
	catch(err)
	{
		debug('_call_function error:', err, args);
	}
}

function callback(args){}

function anything(){}

forceload(this);