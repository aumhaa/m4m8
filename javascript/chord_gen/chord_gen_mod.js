autowatch = 1;

var script = this;
var KEY_COLORS = {0:1, 1:0, 2:1, 3:0, 4:1, 5:1, 6:0, 7:1, 8:0, 9:1, 10:0, 11:1, 12:1};

var finder;
var mod;
var mod_finder;

var unique = jsarguments[1];

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);


var Mod = ModComponent.bind(script);

function init()
{
	mod = new Mod(script, 'chord_gen', unique, false);
	//mod.debug = debug;
	mod_finder = new LiveAPI(mod_callback, 'this_device');
	mod.assign_api(mod_finder);
}

function mod_callback(args)
{
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		//debug('mod callback:', args);
		if(args[1] in script)
		{
			script[args[1]].apply(script, args.slice(2));
		}
		if(args[1]=='disconnect')
		{
			mod.restart.schedule(3000);
		}
	}
}

function alive(val)
{
	initialize(val);
}

function initialize()
{
	setup_translations();
	for(var i = 0;i < 32; i++)
	{
		mod.Send('receive_translation', 'grid_'+i, 'value', KEY_COLORS[i%12]);
		//mod.Send('receive_translation', 'grid_'+i, 'identifier', i + 36);
		//mod.Send('receive_translation', 'grid_'+i, 'channel', 2);
		mod.Send('receive_translation', 'grid_'+i, 'identifier', -1);
		mod.Send('receive_translation', 'grid_'+i, 'channel', -1);
	}
	deprivatize_script_functions(this);
	debug('chord_gen initialized!')
}

function setup_translations()
{
	//Base stuff:
	for(var i = 0;i < 32;i++)
	{
		mod.Send( 'add_translation', 'grid_'+i, 'base_grid', 'base_pads', i%8, Math.floor(i/8));
	}
}

function setup_colors()
{
	mod.Send( 'fill_color_map', 'Monochrome', 0, 1, 1, 1, 8, 1);
}

function _base_grid(x, y, value)
{
	debug('base_grid:', x, y, value);
	var note = x + (y*8);
	mod.Send('receive_translation', 'grid_'+note, 'value', value ? 5 : KEY_COLORS[note%12])
	if(value)
	{
		outlet(0, 36+note);
	}
}

function _grid(x, y, value)
{
	debug('grid:', x, y, value);
	var note = x + (y*8);
	mod.Send('receive_translation', 'grid_'+note, 'value', value ? 5 : KEY_COLORS[note%12])
	if(value)
	{
		outlet(0, 36+note);
	}
}




forceload(this);
