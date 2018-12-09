autowatch = 1;

inlets = 1;
outlets = 1;

var finder;
var control_surface;
var return_value;
var control_names = [];
var controls = {};
var EXCLUDED = ['control', 'control_names', 'done'];
var control_surface_type = jsarguments[1]||'None';

var script = this;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
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
	control_surface = new LiveAPI(function(args){debug('control_surface callback:', args);}, 'control_surfaces');
	var number_children = parseInt(finder.children[0]);
	debug('control_surfaces length:', number_children);
	for(var i=0;i<number_children;i++)
	{
		debug('Checking control surface #:', i);
		finder.goto('control_surfaces', i);
		control_surface.goto('control_surfaces', i);
		debug('looking for:', control_surface_type, 'type is:', finder.type);
		if(finder.type == control_surface_type)
		{
			debug('found corresponding control surface:', finder.type)
			var names = finder.call('get_control_names').filter(function(element){return EXCLUDED.indexOf(element)<0;}).slice(1);
			//debug('names:', names);
			for (var i in names)
			{
				debug(i, 'name:', names[i]);
				var name = names[i];
				try
				{
					controls[names[i]] = 0;
				}
				catch(err)
				{
				}
			}
			control_surface.id = finder.id;
			control_surface.property = 'received_midi';
			debug('control_surface is:', control_surface.path);
			deprivatize_script_functions(script);
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
		debug('callback closure:', name, args);
		outlet(0, name, args);
	}
	return callback;
}

function _grab(name)
{

	debug('_grab:', name);
	if(controls[name]!=undefined)
	{
		if(controls[name]==0)
		{
			var control = finder.call('get_control', name);
			debug('control is:', control);
			var obj = new LiveAPI(make_callback(name), control);
			obj.property = 'value';
			controls[name] = obj;
			//debug('control:', obj.get('name'), obj.get('value'), obj.id);
			//debug('checking:', controls[name].get('name'), controls[name].get('value'));
			//controls[name].property = 'value';
		}
		//finder.call('grab_control', 'id', controls[name].id);
		finder.call('grab_control', name);
		//controls[name].property = 'value';

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
