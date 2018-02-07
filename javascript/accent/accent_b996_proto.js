//binary_steppr, aka Hexadecimal
//by amounra
//aumhaa@gmail.com --- http://www.aumhaa.com


/*This script is the result of collaboration with Peter Nyboer @ Livid Instruments and 
represents a great deal of effort to gain some speed and stability from the original Steppr
without sacrificing too much readability.  The majority of the functionality for the entire patch 
can be modified in this js or the accompanying poly~ object, "steppr_wheel", without ever opening 
the actual containing patch in the m4l editor (this is crucial for speeding up the development process).  
Because of this, the functionality of the patch can be radically altered merely by modifying the 
poly~ or adding some lines of code in to this js.  As an example, the poly~ used as the base for 
this patch is only a slightly modified version of the "binary" mod (from Monomodular), and the 
majority of processes in this script are maintained between both versions.*/

/*It should be noted that many of the processes used in "binary" are still available and unused 
in this script, offering some excellent prospects for future development of this mod.*/

autowatch = 1;

outlets = 4;
inlets = 5;

aumhaa = require('_base');

var FORCELOAD = false;
var NEW_DEBUG = false;
var DEBUG = false;
var DEBUG_NEW = false;
var DEBUG_LCD = 0;
var DEBUG_PTR = 0;
var DEBUG_STEP = 0;
var DEBUG_BLINK = 0;
var DEBUG_REC = 0;
var DEBUG_LOCK = 0;
var DEBUG_FRWL = 0;
var SHOW_POLYSELECTOR = 0;

aumhaa.init(this);

var debuglcd = (DEBUG_LCD&&Debug) ? Debug : function(){};
var debugptr = (DEBUG_PTR&&Debug) ? Debug :function(){};
var debugstep = (DEBUG_STEP&&Debug) ? Debug : function(){};
var debugblink = (DEBUG_BLINK&&Debug) ? Debug : function(){};
var debugrec = (DEBUG_REC&&Debug) ? Debug : function(){};

var unique = jsarguments[1];

var WIKI = 'http://wiki.lividinstruments.com/wiki/Accent'


//this array contains the scripting names of objects in the top level patcher.	To include an new object to be addressed 
//in this script, it's only necessary to add its name to this array.  It can then be addressed as a direct variable
var Vars = ['storage', 'poly', 'pipe', 'selected_filter', 'storepattr', 'preset_selector',
 			'padgui', 'padmodegui','keygui', 'keygui2', 'stepmodegui', 'padmodeadv',
			'RepeatLen', 'Groove', 'Random', 'RotSize', 
			'rotleftgui', 'rotrightgui', 'notevaluesgui', 'notetypegui', 
			'timeupgui', 'timedngui', 'pitchupgui', 'pitchdngui', 'repeatgui',
			'transposegui', 'playgui', 'recgui', 'directiongui', 'lockgui',
			'running_status', 'transport_change', 'presetdisplaygui', 'confirmgui']; 

//Vars trash: 'step'

//this array contains the scripting names of objects in each of the polys.	To include an new object to be addressed 
//in the poly, it's only necessary to add its name to this array.  It can then be addressed as part[poly number].obj[its scripting name]
var Objs = {'pattern':{'Name':'pattern', 'Type':'list', 'pattr':'pattern'}, 
			'duration':{'Name':'duration', 'Type':'list', 'pattr':'duration'},
			'velocity':{'Name':'velocity', 'Type':'list', 'pattr':'velocity'},
			'swing':{'Name':'swing', 'Type':'float', 'pattr':'swingpattr'},
			'steps':{'Name':'steps', 'Type':'int', 'pattr':'stepspattr'},
			'channel':{'Name':'channel', 'Type':'int', 'pattr':'hidden'},
			'direction':{'Name':'direction', 'Type':'int', 'pattr':'directionpattr'},
			'noteoffset':{'Name':'noteoffset', 'Type':'int', 'pattr':'hidden'}, 
			'random':{'Name':'random', 'Type':'int', 'pattr':'randompattr'},
			'repeatenable':{'Name':'repeatenable', 'Type':'int', 'pattr':'object'},
			'ticks':{'Name':'ticks', 'Type':'int', 'pattr':'hidden'},
			'notevalues':{'Name':'notevalues', 'Type':'int', 'pattr':'hidden'}, 
			'notetype':{'Name':'notetype', 'Type':'int', 'pattr':'hidden'},
			'quantize':{'Name':'quantize', 'Type':'int', 'pattr':'hidden'},
			'active':{'Name':'active', 'Type':'int', 'pattr':'hidden'},
			'offset':{'Name':'offset', 'Type':'int', 'pattr':'hidden'},
			'addnote':{'Name':'addnote', 'Type':'int', 'pattr':'object'}, 
			'patterncoll':{'Name':'patterncoll', 'Type':'list', 'pattr':'object'},
			'clutch':{'Name':'clutch', 'Type':'int', 'pattr':'object'},
			'restart':{'Name':'restart', 'Type':'bang', 'pattr':'object'},
			'repeat':{'Name':'repeat', 'Type':'int', 'pattr':'hidden'},
			'phasor':{'Name':'phasor', 'Type':'float', 'pattr':'object'},
			};

var Modes=[4, 2, 3, 5, 1];
var RemotePModes=[0, 1, 4];
var Funcs = ['stepNote', 'stepVel', 'stepDur', 'stepExtra1', 'stepExtra2'];
var default_pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var default_step_pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var default_duration = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var default_note = [[1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]];
var default_velocity = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80];
var empty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var modes = [[0, 2, 4, 5, 7, 9, 11, 12], [0, 2, 3, 5, 7, 9, 10, 12], [0, 1, 3, 5, 7, 8, 10, 12], [0, 2, 4, 6, 7, 9, 11, 12], [0, 2, 4, 5, 7, 9, 10, 12], [0, 2, 3, 5, 7, 8, 10, 12], [0, 1, 3, 5, 6, 8, 10, 12]];
var Colors = [0, 1, 2, 3, 4, 5, 6, 127];
var StepColors = [127, 3, 3, 3, 127, 3, 3, 3, 127, 3, 3, 3, 127, 3, 3, 3 ];
var GUI_StepColors = [7, 3, 3, 3, 7, 3, 3, 3, 7, 3, 3, 3, 7, 3, 3, 3 ];
var SelectColors = [1, 5, 4, 6];
var AddColors = [6, 1];
var Blinks=[-1, 2];
var partTRANS=[12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3];
var TRANSLATE = [{'note':'128n', 'ticks':15, 'speed':1, 'notevalue': 0, 'notetype': 0},
			 {'note':'64n','ticks':30, 'speed':2, 'notevalue':1, 'notetype':0}, 
			{'note':'32nt','ticks':40, 'speed':3, 'notevalue':2, 'notetype':2}, 
			{'note':'64nd','ticks':45, 'speed':4, 'notevalue':1, 'notetype':1}, 
			{'note':'32n','ticks':60, 'speed':5, 'notevalue':2, 'notetype':0},
			{'note':'16nt','ticks':80, 'speed':6, 'notevalue':3, 'notetype':2}, 
			{'note':'32nd','ticks':90, 'speed':7, 'notevalue':2, 'notetype':1},
			{'note':'16n', 'ticks':120, 'speed':8, 'notevalue':3, 'notetype':0},
			{'note':'8nt', 'ticks':160, 'speed':9, 'notevalue':4, 'notetype':2},
			{'note':'16nd', 'ticks':180, 'speed':10, 'notevalue':3, 'notetype':1}, 
			{'note':'8n', 'ticks':240, 'speed':11, 'notevalue':4, 'notetype':0},
			{'note':'4nt', 'ticks':320, 'speed':12, 'notevalue':5, 'notetype':2},
			{'note':'8nd', 'ticks':360, 'speed':13, 'notevalue':4, 'notetype':1}, 
			{'note':'4n', 'ticks':480, 'speed':14, 'notevalue':5, 'notetype':0},
			{'note':'2nt', 'ticks':640, 'speed':15, 'notevalue':6, 'notetype':2},
			{'note':'4nd', 'ticks':720, 'speed':16, 'notevalue':5, 'notetype':1}, 
			{'note':'2n', 'ticks':960, 'speed':17, 'notevalue':6, 'notetype':0},
			{'note':'1nt', 'ticks':1280, 'speed':18, 'notevalue':7, 'notetype':2},
			{'note':'2nd', 'ticks':1440, 'speed':19, 'notevalue':6, 'notetype':1},
			{'note':'1n', 'ticks':1920, 'speed':20, 'notevalue':7, 'notetype':0}, 
			{'note':'1nd', 'ticks':2880, 'speed':21, 'notevalue':7, 'notetype':1}];

var TRANS = [[15, 15, 15], [30, 30, 30], [60, 45, 80], [120, 180, 80], [240, 360, 160], [480, 720, 320], [960, 1440, 640], [1920, 2880, 1280]];

var ACCENTS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2];
var ACCENT_VALS = [87, 111, 127];

/*Naming the js instance as script allows us to create scoped variables 
(properties of js.this) without specifically declaring them with var
during the course of the session. This allows dynamic creation of 
objects without worrying about declaring them beforehand as globals
presumably gc() should be able to do its job when the patch closes, or 
if the variables are redclared.	 I'd love to know if this works the 
way I think it does.*/
var script = this;
var autoclip;

var mod;
var mod_finder;

var part =[];

//var live_set;
//var song_tempo = 120;


var step_mode = 0;
var pad_mode = 0;
var key_mode = 0;
var solo_mode = 0;
var last_mode = 1;
var last_key_mode = 0;
var last_pad_mode = 0;
var locked = 0;
//var play_mode = 0;

var selected;
var presets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
var devices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var preset = 0;
var last_mask = 0;
var global_offset = 36;
var global_chain_offset = 0;
var pad_invoked_key_mode = 3;
var timing_immediate = 0;
var transpose_steps = 16;
var record_enabled = 0;
var play_enabled = 0;
var randomize_global = 0;
var last_blink = 0;
var rot_length = 16;
var step_value = [];
var key_pressed = -1;
var pad_pressed = -1;
var current_step = 0;
var autoclip;
var time1 = 6;
var time2 = 4;

var shifted = false;

/*/////////////////////////////////////////
///// script initialization routines //////
/////////////////////////////////////////*/


/*	VERY IMPORTANT!! : This code utilizes a naming convention for private functions:  any function 
preceeded by an underscore is considered private, but will have a public property reference	 
assigned to it AFTER the script has received an initiallization call from mod.js.  That means that any 
function that shouldn't be accessed before initialization can be created as a private function without 
the need to use an internal test to find out whether the script has init()ed. 

Any calls to uninitiated private functions that require a response should be defined by the anything() parsing
routine.

Example:

If we create _private_function(), and before init a call from max comes in to private_function(), that call 
will be funneled to anything().	 After init(), however, all calls to private_function() will be forwarded to 
_private_function().  

Note:  It is best to only address these private functions by their actual names in the script, since calling aliased 
names will not be routed to anything()*/

var GRIDMAP =[	[undefined, undefined, undefined, undefined, 'pads_0', 'pads_1', 'pads_2', 'pads_3'],
				['buttons_0', 'buttons_1', 'buttons_2', 'buttons_3', 'pads_4', 'pads_5', 'pads_6', 'pads_7'],
				['buttons_4', 'buttons_5', 'buttons_6', 'buttons_7', 'pads_8', 'pads_9', 'pads_10', 'pads_11'],
				[undefined, undefined, undefined, undefined, 'pads_12', 'pads_13', 'pads_14', 'pads_15'],
				['keys_0', 'keys_1', 'keys_2', 'keys_3', 'keys_4', 'keys_5', 'keys_6', 'keys_7'],
				['keys2_0', 'keys2_1', 'keys2_2', 'keys2_3', 'keys2_4', 'keys2_5', 'keys2_6', 'keys2_7'],
				['keys_8', 'keys_9', 'keys_10', 'keys_11', 'keys_12', 'keys_13', 'keys_14', 'keys_15'],
				['keys2_8', 'keys2_9', 'keys2_10', 'keys2_11', 'keys2_12', 'keys2_13', 'keys2_14', 'keys2_15']]

var BUTTON_COLORS = [0, 0, 3, 3, 5, 0, 4, 4];

function setup_colors()
{
	mod.Send( 'fill_color_map', 'Monochrome', 1, 8, 1, 1, 8, 1);
}

function setup_translations()
{
	for(var i = 0;i < 16;i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'cntrlr_grid', 'cntrlr_pads', i%4, Math.floor(i/4));
		mod.Send( 'add_translation', 'keys_'+i, 'cntrlr_key', 'cntrlr_keys', i, 0);
		mod.Send( 'add_translation', 'keys2_'+i, 'cntrlr_key', 'cntrlr_keys2', i, 1);

		mod.Send( 'add_translation', 'pads_'+i, 'base_grid', 'base_pads', i%4, Math.floor(i/4));
		mod.Send( 'add_translation', 'keys_'+i, 'base_grid', 'base_keys', (i%4)+4, Math.floor(i/4));
		mod.Send( 'add_translation', 'keys2_'+i, 'base_grid', 'base_keys2', (i%4)+4, Math.floor(i/4));


		mod.Send( 'add_translation', 'pads_'+i, 'code_grid', 'code_pads', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys_'+i, 'code_grid', 'code_keys', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys2_'+i, 'code_grid', 'code_keys2', i%8, Math.floor(i/8)+2);


		/*mod.Send( 'add_translation', 'pads_'+i, 'grid', 'push_pads', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys_'+i, 'grid', 'push_keys', i%8, Math.floor(i/8)+2);
		mod.Send( 'add_translation', 'keys2_'+i, 'grid', 'push_keys2', i%8, Math.floor(i/8)+4);*/

		mod.Send( 'add_translation', 'pads_'+i, 'grid', 'ohm_pads', (i%4)+4, Math.floor(i/4));
		mod.Send( 'add_translation', 'keys_'+i, 'grid', 'ohm_keys', i%8, (i < 8 ? 4 : 6));
		mod.Send( 'add_translation', 'keys2_'+i, 'grid', 'ohm_keys2', i%8, (i < 8 ? 5 : 7));
	}
	mod.Send( 'enable_translation_group', 'base_keys', 0);
	mod.Send( 'enable_translation_group', 'code_keys', 0);

	for(var i=0;i<8;i++)
	{
		//mod.Send( 'add_translation', 'buttons_'+i, 'base_grid', 'base_buttons', (i%4), i/4);
		mod.Send( 'add_translation', 'buttons_'+i, 'key', 'keys', i);
		
		//mod.Send( 'add_translation', 'extras_'+i, 'base_grid', 'base_extras', (i%4), (i/4)+2);

		mod.Send( 'add_translation', 'buttons_'+i, 'cntrlr_encoder_button_grid', 'cntrlr_buttons', i%4, Math.floor(i/4));
		//mod.Send( 'add_translation', 'extras_'+i, 'base_grid', i, 3);


		mod.Send( 'add_translation', 'buttons_'+i, 'code_grid', 'code_buttons', i, 2);
		mod.Send( 'add_translation', 'extras_'+i, 'code_grid', 'code_extras', i, 3);


		//mod.Send( 'add_translation', 'buttons_'+i, 'grid', i, 6);
		//mod.Send( 'add_translation', 'extras_'+i, 'grid', i, 7);
		mod.Send( 'add_translation', 'buttons_'+i, 'grid', 'ohm_buttons', i%4, Math.floor(i/4)+1);
	}
	mod.Send( 'enable_translation_group', 'code_buttons', 0);
	mod.Send( 'enable_translation_group', 'code_extras', 0);
}

var Mod = ModComponent.bind(script);

function init()
{
	mod = new Mod(script, 'accent', unique, false);
	//mod.debug = debug;
	mod.wiki_addy = WIKI;
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
			//debug('in script:', args[1]);
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
	debug('alive', val);
	initialize(val);
}

//called when mod.js is finished loading for the first time
function initialize(val)
{
	if(val>0)
	{
		//live_set = new LiveAPI(this.patcher, cb_tempo, 'live_set');
		//live_set.property = 'tempo';
		debug('accent init\n');
		setup_translations();
		setup_colors();
		mod.Send('set_legacy', 0);
		for(var i in Vars)
		{
			script[Vars[i]] = this.patcher.getnamed(Vars[i]);
		}
		for(var i = 0; i < 16; i++)
		{
			var poly_num = i;
			//storage.message('priorty', 'poly.'+(poly_num+1), 'tickspattr', 10);
			storage.message('priorty', 'poly.'+(poly_num+1),  'notetypepattr', 11);
			storage.message('priorty', 'poly.'+(poly_num+1),  'notevaluepattr', 12);
			part[i] = {'n': 'part', 'num':i, 'nudge':0, 'offset':0, 'channel':0, 'len':16, 'start':0, 
						'jitter':0, 'active':1, 'swing':.5, 'lock':1, 'ticks':480, 'notevalues':5, 'notetype':0, 
						'pushed':0, 'direction':0, 'root':i, 'octave':0, 'add':0, 'quantize':1, 'repeat':6, 
						'random':0, 'note':i, 'steps':15};//'speed':480,'notevalue':'4n'
			part[i].num = parseInt(i);
			part[i].pattern = default_pattern.slice();
			part[i].step_pattern = default_step_pattern.slice();
			part[i].duration = default_duration.slice();
			part[i].velocity = default_velocity.slice();
			//part[i].note = default_pattern.slice();
			part[i].obj = [];
			part[i].obj.set = [];
			part[i].obj.get = [];
			part[i].triggered = [];
			for(var j in Objs)
			{
				//post(Objs[j].Name, '\n');
				part[i].obj[Objs[j].Name] = this.patcher.getnamed('poly').subpatcher(poly_num).getnamed(Objs[j].Name);
				part[i].obj.set[Objs[j].Name] = make_obj_setter(part[i], Objs[j]);
				part[i].obj.get[Objs[j].Name] = make_obj_getter(part[i], Objs[j]);
			}
			part[i].funcs = make_funcs(part[i]);
		}
		//script.rulemap = this.patcher.getnamed('settings').subpatcher().getnamed('rulemap');
		this.patcher.getnamed('poly').message('target', 0);
		selected_filter.message('offset', 1);
		autoclip = new LiveAPI(callback, 'live_set');
		//step.message('int', 1);
		messnamed(unique+'restart', 1);
		var i=0;do{
			part[i].obj.offset.message('int', 0);
		}while(i--);
		transport_change.message('int', -1);
		selected = part[0];
		for(var i in script)
		{
			if((/^_/).test(i))
			{
				script[i.replace('_', "")] = script[i];
			}
		}
		//alive = 1;
		clear_surface();
		storage.message('recall', 1);
		init_device();
		select_pattern(0);
		mod.Send('receive_device', 'set_mod_device_type', 'Simple');
		mod.Send('receive_device', 'set_number_params', 16);
		//needs changed---
		//var i=3;do{
		//	mod.Send('to_wheel', i, 2, 'mode', 0);
		//}while(i--);
		var i=8;do{
			mod.Send('key', 'value', i, BUTTON_COLORS[i]);
		}while(i--);
		change_transpose(36);
		post("Accent initialized.\n");
		this.patcher.getnamed('polyselector').hidden = Math.abs(SHOW_POLYSELECTOR-1);
	}
	else
	{
		_dissolve();
	}
}

//make a closure to hold the setter function for any object in the poly patcher that is contained in the Objs dict
function make_obj_setter(part, obj)
{
	if(obj.pattr == 'hidden')
	{
		var setter = function(val)
		{	
			if(val!=undefined)
			{
				//post('setter hidden\n');
				var num = part.num;
				part[obj.Name] = val;
				part.obj[obj.Name].message(obj.Type, val);
			}
		}
	}
	else if(obj.pattr == 'object')
	{
		if(obj.Type == 'bang')
		{
			var setter = function(val)
			{
				if(val!=undefined)
				{
					//post('setter bang\n');
					part[obj.Name].message('bang');
				}
			}
		}
		else
		{
			var setter = function(val)
			{	
				//post('setter object\n');
				if(val!=undefined)
				{
					part[obj.Name] = val;
					part.obj[obj.Name].message(obj.Type, val);
				}
			}
		}
	}
	else
	{
		var setter = function(val, pset)
		{	
			if(val!=undefined)
			{
				//post('setter pattr\n');
				var num = part.num;
				if(!pset){
					var pset = presets[num];
					part[obj.Name] = val;
					part.obj[obj.Name].message(obj.Type, val);
				}
				//post('storing', obj.Name, 'in', obj.pattr, 'at', pset, 'with', val, '\n');
				storage.setstoredvalue('poly.'+(num+1)+'::'+obj.pattr, pset, val);
			}
		}
	}
	return setter;	
}

//make a closure to hold the getter function for any object in the poly patcher that is contained in the Objs dict
function make_obj_getter(part, obj)
{
	if(part.obj[obj.Name].understands('getvalueof'))
	{
		var getter = function()
		{
			part[obj.Name] = part.obj[obj.Name].getvalueof();
		}
	}
	else
	{
		var getter = function()
		{
			return;
		}
	}
	return getter;
}

//dummy callback to compensate for api bug in Max6
function callback()
{
	//if(DEBUG){post('callback', arguments, '\n');}
}

//called by init to initialize state of polys
function init_poly()
{	 
	//poly.message('target', 0);
	mod.Send( 'batch', 'grid', 0);
	for(var i=0;i<16;i++)
	{
		part[i].obj.quantize.message('int', part[i].quantize);
		part[i].obj.active.message('int', part[i].active);
		part[i].obj.swing.message('float', part[i].swing);
		part[i].obj.ticks.message(part[i].ticks);
		part[i].obj.phasor.lock = 1;
		//part[i].obj.polyenable.message('int', part[i].polyenable);
		part[i].obj.phasor.message('float', 0);
		part[i].obj.noteoffset.message('int', (part[i].octave *12) + part[i].root);
		part[i].obj.pattern.message('list', part[i].pattern);
		//part[i].obj.note.message('list', part[i].note);
		part[i].obj.velocity.message('list', part[i].velocity);
		part[i].obj.duration.message('list', part[i].duration);
		part[i].obj.notetype.message('int', part[i].notetype);
		part[i].obj.notevalues.message('int', part[i].notevalues);
		part[i].obj.channel.message('int', part[i].channel);
		//update_note_pattr(part[i]);
		
	}
}

//called by init to initialize state of gui objects
function _clear_surface()
{
	//if(DEBUG){post('clear_surface\n');}
	stepmodegui.message('int', 0);
}

//should be called on freebang, currently not implemented
function _dissolve()
{
	for(var i in script)
	{
		if((/^_/).test(i))
		{
			script[i.replace('_', "")] = script['anyting'];
		}
	}
	//alive=0;
	post('Simple dissolved.\n');	   
}


/*/////////////////////////////////
///// api callbacks and input /////
/////////////////////////////////*/


//main input sorter
//any calls made to _private_functions before initialization should be dealt with by this parser
//if not defined, they will be handled by "default"
function anything()
{
	var args = arrayfromargs(arguments);
	//post('anything', messagename, arguments, '\n');
	switch(messagename)
	{
		case 'settingsgui':
			switch(args[0])
			{
				case 0:
					pad_invoked_key_mode = args[1]+3;
					break;
				case 1:
					timing_immediate = args[1];
					break;
				case 2:
					//global_chain_offset = args[1];
					break;
				case 4:
					//transpose_steps = args[1];
					break;
				case 14:
					time1 = args[1];
					break;
				case 15:
					time2 = args[1];
					break;
			}
			break;
		case 'guibuttons':
			switch(args[0])
			{
				case 10:
					pad_mode = args[1];
					break;
				case 11:
					key_mode = args[1];
					break;
				case 12:
					global_offset = (Math.max(Math.min(args[1], 112), 0));
					break;
				case 14:
					locked = args[1];
					break;
			}
			break;			
		default:
			//if(DEBUG){post('anything', messagename, args, '\n');}
			break;
	}
}

//this sorts grid presses
function _grid(x, y, val)
{
	debug('grid', x, y, val)
	if(y<4)
	{
		if(x>3)
		{
			grid_in(x-4, y, val);
		}
		else if((y>0)&&(y<3))
		{
			button_in(x, y-1, val);
		}
	}
	else
	{
		switch(y)
		{
			case 4:
				key_in(x, val);
				break;
			case 5:
				key_in(x + 16, val);
				break;
			case 6:
				key_in(x + 8, val);
				break;
			case 7:
				key_in(x + 24, val);
				break;
		}
	}
}

function _base_grid(x, y, val)
{
	debug('_base_grid', x, y, val);
	if(shifted)
	{
		if(x>3)
		{
			key_in(x%4 + (4*(y)), val);
		}
		else if(y>1)
		{
			button_in(x, Math.floor(x/4)-2, val);
		}
		else if(val>0)
		{
			keymodegui.message('int', x + (y*4));
		}
	}
	else if (x<4)
	{
		grid_in(x, y, val);
	}
	else
	{
		key_in((x%4) + (4*y) + 16, val);
	}
}

function _cntrlr_grid(x, y, val)
{
	grid_in(x, y, val);
}

function _cntrlr_key (x, y, val)
{
	debug('cntrlr_key', x, y, val);
	key_in(x+(y*16), val);
}

function _cntrlr_encoder_button_grid(x, y, val)
{
	button_in(x, y, val);
}

function _shift(val)
{
	debug('shift:', val);
	var i=8;do{
		mod.Send('key', i, BUTTON_COLORS[i]);
	}while(i--);
	if(val!=shifted)
	{
		shifted = val;
		for(var i=0;i<16;i++)
		{
			mod.Send( 'enable_translation', 'keys_'+i, 'base_grid', Math.floor(shifted));
			mod.Send( 'enable_translation', 'pads_'+i, 'base_grid', Math.floor(!shifted));
			mod.Send( 'enable_translation', 'keys2_'+i, 'base_grid', Math.floor(!shifted));
		}
		for(var i=0;i<8;i++)
		{
			mod.Send( 'enable_translation', 'buttons_'+i, 'base_grid', Math.floor(shifted));
			mod.Send( 'enable_translation', 'extras_'+i, 'base_grid', Math.floor(shifted));
		}
		refresh_grid();
		refresh_keys();
		update_time_bg();
	}
}

function _key(x, val)
{
	debug('key', x, val);
	button_in(x%4, Math.floor(x/4), val);
}

//distribute presses received from mod.js
function button_in(x, y, val)
{
	debug('button_in', x, y, val);
	switch(y)
	{
		case 0:
			switch(x)
			{
				case 0:
					timedngui.message('int', val);
					break;
				case 1:
					timeupgui.message('int', val);
					break;
				case 2:
					pitchdngui.message('int', val);
					break;
				case 3:
					pitchupgui.message('int', val);
					break;
			}
			break;
		case 1:
			switch(x)
			{
				case 0:
					repeatgui.message('int', val);
					break;
				case 1:
					padmodeadv.message('int', val);
					break;
				case 2:
					rotleftgui.message('int', val);
					break;
				case 3:
					rotrightgui.message('int', val);
					break;
			}
			break;
	}	 
}

//distribute presses received from mod.js
function grid_in(x, y, val)
{
	switch(pad_mode)
	{
		default:
			if((val>0)&&(pad_pressed<0))
			{
				pad_pressed = x + (y*4);
				select_pattern(partTRANS[pad_pressed]);
				//last_key_mode = key_mode;
				pipe.message('int', pad_pressed);
			}
			else if((x + (y*4) == pad_pressed)&&(val<1))
			{
				pad_pressed = -1;
				change_key_mode(0);
			}
			else
			{
				var slave = part[x + (y*4)];
				sync_wheels(selected, slave);
			}
			break;
		case 1:
			if(val>0)
			{
				var p = partTRANS[x + (y*4)];
				add_note(part[p]);
				if(p != selected.num)
				{
					select_pattern(p);
				}
			}
			else if((x + (y*4) == pad_pressed)&&(val<1))
			{
				pad_pressed = -1;
				change_key_mode(last_key_mode);
			}
			break;
		case 2:
			var num = partTRANS[x + (y*4)];
			if(val>0)
			{
				//part[num].active = Math.abs(part[num].active-1);
				//part[num].obj.active.message('int', part[num].active);
				part[num].obj.set.active(Math.abs(part[num].active-1));
				refresh_grid();
				if(key_mode==0){refresh_keys();}
				add_automation(part[num], 'mute', part[num].active);
			}
			break;
			refresh_grid();
			break;
	}
}

//from mod.js
function key_in(num, val)
{
	//if(DEBUG){post('key in', num, val, '\n');}
	if((num>15)&&(val>0))
	{
		num -= 16;
		selected.pattern[num] = Math.abs(selected.pattern[num]-1);
		//selected.obj.pattern.message('list', selected.pattern);
		selected.obj.set.pattern(selected.pattern);
		refresh_keys();	
	}	 
	else
	{
		switch(key_mode)
		{
			default:
				if(val>0)
				{
					selected.velocity[num] = ACCENT_VALS[(ACCENTS[Math.floor(selected.velocity[num]/8)]+1)%3];
					////if(DEBUG){post('new vel =', selected.velocity[num], '\n');}
					//selected.obj.velocity.message(selected.velocity);
					selected.obj.set.velocity(selected.velocity);
					refresh_keys();
				}
				break;
			case 'old_default':
				if(val>0)
				{
					//part[num].active = Math.abs(part[num].active-1);
					//part[num].obj.active.message('int', part[num].active);
					part[num].obj.set.active(Math.abs(part[num].active-1));
					refresh_keys();
					if(pad_mode==2){refresh_grid();}
					add_automation(part[num], 'mute', part[num].active);
				}
				break;
			case 1:
				if((key_pressed == num)&&(val==0))
				{
					key_pressed = -1;
				}
				if((key_pressed < 0)&&(val>0)&&(num>=selected.nudge))
				{
					key_pressed = num;
					change_Out(num);
					//step.message('loop', parseInt(selected.nudge+1), parseInt(key_pressed+1));
				}
				else if((key_pressed > -1)&&(val>0)&&(num<=key_pressed))
				{
					change_In(num);
					//step.message('loop', num, parseInt(key_pressed+1))
				}
				update_step();
				refresh_keys();
				break;
			case 2:
				if(val>0)
				{
					//selected.behavior[num] = (selected.behavior[num]+1)%8;
					//part[selected.num].obj.behavior.message('list', selected.behavior);
					update_step();
					refresh_keys();
					break;
				}
			case 3:
				if(val>0)
				{
					presets[selected.num] = num+1;
					storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
				}
				break;
			case 4:
				if(val>0)
				{
					preset = num+1;
					for(var i=0;i<16;i++)
					{
						presets[i] = preset;
					}
					storage.message(preset);
				}
				break;
		}
	}
}

//this is mainly for the select-hold
function _msg_int(val)
{
	//if(DEBUG){post('msg_int', args, '\n');}
	if((inlet==2)&&(pad_pressed==val))
	{
		change_key_mode(pad_invoked_key_mode);
	}
}

//this sorts key and grid input
function _list()
{
	var args=arrayfromargs(arguments);
	switch(inlet)
	{
		case 0:
			grid_in(args[0], args[1], args[2]);
			break;
		case 1:
			key_in(args[0], args[1]);
			break;
	}
}

//this sorts encoderbutton presses
function _button(x, y, val)
{
	var args = arrayfromargs(arguments);
	button_in(x, y, val);
}

//called by gui object, sets visible portion of live.step
function _mode(val)
{
	step_mode = val;
	//step.message('mode', Modes[step_mode]);
}

//from live.step	
function _step_in()
{
	/*var args = arrayfromargs(arguments);
	//if(DEBUG_STEP){post('step_in', args, '\n');}
	switch(args[0])
	{
		case 0:
			break;
		case 1:
			break;
		case 2:
			switch(args[1])
			{
				case 'changed':
					var new_value = step.getvalueof();
					outlet(3, step_value);
					//if(DEBUG_STEP){post('old', step_value);} 
					outlet(2, new_value);
					break;
			}
		case 3:
			break;
	}*/
}

//distributes input from gui button and menu elements
function _guibuttons(num, val)
{
	//if(DEBUG){post('gui_buttons', num, val, '\n');}
	switch(num)
	{
		case 1:
			selected.obj.repeatenable.message('int', val);
			break;
		case 0:
			padmodegui.message('int', Math.abs(pad_mode-1));
			break;
		case 2:
			rotate_pattern(selected, rot_length, -1);
			break;
		case 3:
			rotate_pattern(selected, rot_length, 1);
			break;
		case 4:
			selected.notevalues = val;
			if(timing_immediate)
			{
				selected.obj.notevalues.message('int', val);
			}
			else
			{
				selected.obj.notevalues.message('set', val);
				selected.obj.restart.message('bang');
			}
			break;
		case 5:
			selected.notetype = val;
			if(timing_immediate)
			{
				selected.obj.notetype.message('int', val);
				selected.obj.notevalues.message('int', selected.notevalues);
			}
			else
			{
				selected.obj.notetype.message('int', val);
				selected.obj.restart.message('bang');
			}
			break;
		case 6:
			if(time1 == 8)
			{
				notevaluesgui.message('int', Math.max(Math.min(8, selected.notevalues+1), 0));
			}
			else
			{
				if(selected.notevalues!=time1)
				{
					notevaluesgui.message('int', time1);
				}
				else
				{
					notevaluesgui.message('int', 3);
				}
			}
			update_time_bg();
			break;
		case 7:
			if(time2 == 8)
			{
				notevaluesgui.message('int', Math.max(Math.min(8, selected.notevalues-1), 0));
			}
			else
			{
				if(selected.notevalues!=time2)
				{
					notevaluesgui.message('int', time2);
				}
				else
				{
					notevaluesgui.message('int', 3);
				}
			}
			update_time_bg();
			break;
		case 8:
			if(global_offset >= 104)
			{
				change_transpose(100, 0);
				//transposegui.message(100);
			}
			else
			{
				change_transpose(Math.max(Math.min(global_offset - transpose_steps, 112), 0));
				//transposegui.message('set', Math.max(Math.min(global_offset - transpose_steps, 112), 0));
				debug('transpose', (Math.max(Math.min(global_offset - transpose_steps, 112), 0)));
			}
			break;
		case 9:
			if(global_offset < 4)
			{
				change_transpose(4, 0);
				//transposegui.message(4);
			}
			else
			{
				change_transpose(Math.max(Math.min(global_offset + transpose_steps, 112), 0));
				//debug('transpose', (Math.max(Math.min(global_offset + transpose_steps, 112), 0)));
			}
			break;
		case 10:
			change_pad_mode(val);
			break;
		case 11:
			change_key_mode(val);
			break;
		case 12:
			//change_transpose(val);
			break;
		case 13:
			//selected.direction = val;
			//selected.obj.direction.message('int', val);
			selected.obj.set.direction(val);
			break;
		case 14:
			//if(DEBUG){post('lock', val, '\n');}
			locked = val;
			break;
		case 15:
			detect_devices();
			break;
		case 16:
			record(val);
			break;
		case 17:
			play_enabled = val;
			locked = 1;
			break;
	}
}

//distributes input from gui grid element
function _padgui_in(val)
{
	//if(DEBUG){post('padguiin', val, '\n');}
	grid_in(val%4, Math.floor(val/4), 1);
	grid_in(val%4, Math.floor(val/4), 0);
}

//distributes input from bottom gui key element
function _keygui_in(val)
{
	//if(DEBUG){post('keyguiin', val, '\n');}
	key_in(val, 1);
	key_in(val, 0);
	
}

//distributes input from top gui key element
function _keygui2_in(val)
{
	//if(DEBUG){post('key2in', val, '\n');}
	key_in(val+16, 1);
	key_in(val+16, 0);
}

//displays played notes on grid
function _blink(val)
{
	//if(DEBUG_BLINK){post('blink', val, '\n');}
	mod.Send( 'receive_translation', 'keys2_'+last_mask, 'mask', -1);
	mod.Send( 'receive_translation', 'keys2_'+val,  'mask', 5); 
	last_mask = val;
}

//displays played notes on keys
function _vblink(num, val)
{
	////if(DEBUG_BLINK){post('vblink', val, '\n');}
	/*if(key_mode==0)
	{
		mod.Send( 'mask', 'key', num, val);
	}
	mod.Send( 'mask', 'grid', num%4, Math.floor(num/4), Blinks[Math.floor(val>0)]);*/
}

//evaluate and distribute data recieved from the settings menu
function _settingsgui(num, val)
{
	switch(num)
	{
		case 0:
			pad_invoked_key_mode = val+3;
			break;
		case 1:
			timing_immediate = val;
			break;
		case 2:
			//global_chain_offset = val;
			//_select_chain(selected.num);
			break;
		case 3:
			break;
		case 4:
			transpose_steps = val;
			break;
		case 5:
			randomize_pattern(randomize_global);
			break;
		case 6:
			randomize_velocity(randomize_global);
			break;
		case 7:
			randomize_duration(randomize_global);
			break;
		case 8:
			randomize_behavior(randomize_global);
			break;
		case 9:
			randomize_rulebends(randomize_global);
			break;
		case 10:
			reset_data(randomize_global);
			break;
		case 12:
			randomize_global = val;
			break;
		case 11:
			randomize_pattern(randomize_global);
			randomize_velocity(randomize_global);
			randomize_duration(randomize_global);
			randomize_behavior(randomize_global);
			randomize_rulebends(randomize_global);
			break;
		case 13:
			randomize_rules();
			break;
		case 14:
			//if(DEBUG){post('time1:', val, '\n');}
			time1 = val;
			break;
		case 15:
			//if(DEBUG){post('time2:', val, '\n');}
			time2 = val;
			break;
	}
}

//distribute MIDI remote control assignments to their destination
function _remote(num, val)
{
	switch(num<16)
	{
		case 0:
			grid_in(num%4, Math.floor(num/4), 1);
			break;
		case 1:
			key_in(num-16, val);
			break;
	}
}

//distribute 
function _receive_automation(num, val)
{
	if((play_enabled>0)&&(num>110)&&(val!==0))
	{
		num-=111;
		//if(DEBUG_REC){post('receive auto:', num, val, '\n');}
		if(val>9)
		{
			presets[part[num].num] = val-10;
			//if(DEBUG_REC){post('preset change:', part[num].num+1, presets[part[num].num], '\n');}
			storage.message('recall', 'poly.'+(part[num].num+1), presets[part[num].num]);
		}
		else if(val>0)
		{
			part[num].active = val-1;
			part[num].obj.active.message('int', part[num].active);
			if(pad_mode==2)
			{
				refresh_grid();
			}
			if(key_mode==0)
			{
				refresh_keys();
			}
		}
	}
}

//reset the selected in the current preset gui button
function _init_seq(val)
{
	selected.obj.set.pattern(default_pattern.slice());
	selected.obj.set.velocity(default_velocity.slice());
	selected.obj.set.duration(default_duration.slice());
	selected.obj.set.swing(0);
	selected.obj.set.random(0);
	selected.obj.set.direction(0);
	selected.obj.set.notevalues(3);
	selected.obj.set.notetype(0);
	refresh_keys();
	update_gui();
}

//randomize the values of the currently selected voice
function _randomize()
{
	var j=15;do{
		selected.pattern[j]=Math.round(Math.random());
		selected.velocity[j]=Math.floor(Math.random()*127);
	}while(j--);
	selected.obj.set.velocity(selected.velocity);
	selected.obj.set.pattern(selected.pattern);
	refresh_keys();
}

function _pset_up()
{
	if(pad_invoked_key_mode==3)
	{
		presets[selected.num] = Math.max(Math.min(16, presets[selected.num]+1), 1);
		storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
	}
	else if(pad_invoked_key_mode==4)
	{
		preset = Math.max(Math.min(16, preset+1), 1);
		for(var i=0;i<16;i++)
		{
			presets[i]=preset;
		}
		storage.message(preset);
	}
	refresh_keys();
}

function _pset_dn()
{
	if(pad_invoked_key_mode==3)
	{
		presets[selected.num] = Math.max(Math.min(16, presets[selected.num]-1), 1);
		storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
	}
	else if(pad_invoked_key_mode==4)
	{
		preset = Math.max(Math.min(16, preset-1), 1);
		for(var i=0;i<16;i++)
		{
			presets[i]=preset;
		}
		storage.message(preset);
	}
	refresh_keys();
}

/*/////////////////////////////
///// data syncronization /////
/////////////////////////////*/


//called by pattr when it recalls a preset
function _recall()
{	 
	//if(DEBUG_PTR){post('recall\n');}
	if(pad_invoked_key_mode == 3)
	{
		for(var item in Objs)
		{
			////if(DEBUG_PTR){post(Objs[item], typeof(selected[Objs[item]]), 'retrieving...\n');}
			selected.obj.get[Objs[item].Name]();
		}
	}
	else
	{
		var i=15;do{
			for(var item in Objs)
			{
				////if(DEBUG_PTR){post(Objs[item], typeof(selected[Objs[item]]), 'retrieving...\n');}
				part[i].obj.get[Objs[item].Name]();
			}
		}while(i--);
	}	
	/*selected.nudge = Math.floor(selected.obj.nudge.getvalueof());
	selected.steps = Math.floor(selected.obj.steps.getvalueof());
	selected.root = Math.floor(selected.obj.noteoffset.getvalueof()%12);
	selected.octave = Math.floor(selected.obj.noteoffset.getvalueof()/12);*/
	//var i=15;do{
		//part[i].active = part[i].obj.active.getvalueof();
		//part[i].quantize = part[i].obj.active.getvalueof();
		
	//	update_speed(part[i]);
	//}while(i--);
	//update_step();
	refresh_keys();
	refresh_grid();
	update_gui();
}

function read()
{
	presets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
	preset = 1;
	storage.message(preset);
}

///this is how we inject the data to the poly~ objects:
function make_funcs(part)
{
	new_part = [];
	new_part.stepLoop = function(In, Out)
	{
		//if(DEBUG_STEP){post('step Loop', In, Out, '\n');}
		selected.nudge = In;
		selected.obj.nudge.message('set', selected.nudge);
		selected.steps = Out - In;
		selected.obj.steps.message('int', selected.steps);
		selected.obj.restart.message('bang');
		refresh_keys();
	}
	new_part.stepDir = function(step, val)
	{
		//if(DEBUG_STEP){post('step Dir', step, val, '\n');}
		part.direction = val;
		part.obj.direction.message('int', val);
	}
	new_part.stepNote = function(step, val)
	{
		/*//if(DEBUG_STEP){post('step note', step, val, '\n');}
		part.note[step] = val;
		part.obj.note.message('list', part.note);*/
	}
	new_part.stepVel = function(step, val)
	{
		//if(DEBUG_STEP){post('step vel', step, val, '\n');}
		part.velocity[step] = val;
		part.obj.velocity.message('list', part.velocity);
	}
	new_part.stepDur = function(step, val)
	{
		//if(DEBUG_STEP){post('step dur', step, val, '\n');}
		part.duration[step] = val;
		part.obj.duration.message('list', part.duration);
	}
	new_part.stepExtra1 = function(step, val)
	{
		//if(DEBUG_STEP){post('step extra1', step, val, '\n');}
		part.pattern[step] = val;
		part.obj.pattern.message('list', part.pattern);
		refresh_keys();
	}
	new_part.stepExtra2 = function(step, val)
	{
		/*//if(DEBUG_STEP){post('step extra2', step, val, '\n');}
		part.rulebends[step] = val;
		part.obj.rulebends.message('list', part.rulebends);*/
	}		 
	return new_part
}

//called to update data in live.step when changes are made to poly
function update_step()
{
	/*step_value = step.getvalueof();
	//if(DEBUG_STEP){post('update step: step_value', step_value.length, '\n', step_value, '\n');}
	selected.nudge = parseInt(selected.obj.nudge.getvalueof());
	selected.steps = parseInt(selected.obj.steps.getvalueof());
	step_value[5] = Math.floor(selected.nudge);
	step_value[6] = Math.floor(selected.nudge) + Math.floor(selected.steps) + 1;
	selected.pattern = selected.obj.pattern.getvalueof();
	selected.velocity = selected.obj.velocity.getvalueof();
	selected.duration = selected.obj.duration.getvalueof();
	//selected.behavior = selected.obj.behavior.getvalueof();
	//selected.rulebends = selected.obj.rulebends.getvalueof();
	//selected.note = selected.obj.note.getvalueof();
	var i=15;do{
		var s = 11 + (i*5);
		step_value[s] = selected.note[i];
		step_value[s + 1] = selected.velocity[i];
		step_value[s + 2] = selected.duration[i];
		step_value[s + 3] = selected.pattern[i];
		//step_value[s + 4] = selected.rulebends[i];
	}while(i--);
	//if(DEBUG_STEP){post('to step', step_value.length, '\n', step_value, '\n');}
	step.setvalueof(step_value);*/
}

//called to update data in poly when changes are made in livestep
function update_poly()
{
	/*var args = arrayfromargs(arguments);
	step_value = step.getvalueof();
	//if(DEBUG_STEP){post('update_poly\n unmatching args', args, '\n');}
	//for(var i in args)
	var i = args.length;do{
		if(args[i]>10)
		{
			var index = args[i]-11;
			//if(DEBUG_STEP){post(args[i], '\n');}
			selected.funcs[Funcs[index%5]](Math.floor(index/5), step_value[index+11]);
		}
		else
		{
			switch(args[i])
			{
				case 5:
					selected.funcs.stepLoop(step_value[args[i]], step_value[args[i]+1]-1);
					break;
				case 6:
					selected.funcs.stepLoop(step_value[args[i]-1], step_value[args[i]]-1);
					break;
			}
		}		 
	}while(i--);*/
}


/*///////////////////////
// internal processes  //
///////////////////////*/


//select the current pattern and load its data to CNTRLR/live.step/gui
function select_pattern(num)
{
	if(!locked)
	{
		storage.message('store', 'poly.'+(selected.num+1), presets[selected.num]);
	}
	var range = num>7;
	selected = part[num];
	_select_chain(num);
	selected_filter.message('offset', num + 1);
	refresh_grid();
	refresh_keys();
	update_gui();
	//presetdisplaygui.message('text', 'Preset', presets[selected.num]);
}	 

//update the current global transposition to all polys
function change_transpose(val)
{
	if(selected.channel==0)
	{
		var indicator;
		if(val < 4)
		{
			indicator = 0;
		}
		else if(val > 103)
		{
			indicator = 8;
		}
		else
		{
			indicator = Math.floor((val-4)/16)+1;
		}
		this.patcher.getnamed('kitindicator').message('set', indicator);
		//if(DEBUG){post('global_offset', val, '\n');}
		global_offset = (Math.max(Math.min(val, 112), 0));
		//transposegui.message('set', global_offset);
		for(var i = 0;i< 16;i++)
		{
			part[i].obj.noteoffset.message('int', global_offset + i);
		}
		_select_chain(selected.num);
	}	
}

//change the function of the keys
function change_key_mode(val)
{
	//if(DEBUG){post('key_mode', val, '\n');}
	key_pressed = -1;
	key_mode = val;
	switch(key_mode)
	{
		default:
			break;
	}
	//keymodegui.message('set', key_mode);
	refresh_keys();
	update_bank();
}

//change the function of the pad
function change_pad_mode(val)
{
	pad_mode = val;
	switch(pad_mode)
	{
		default:
			break;
	}
	padmodegui.message('set', pad_mode);
	refresh_grid();
	update_bank();
}
	
//called from key_in, change the loopOut point and update it to live.step and poly
function change_Out(val)
{
	//if(DEBUG){post('change Out', val, '\n');}
	//selected.steps = val-parseInt(selected.nudge);
	//selected.obj.steps.message('int', selected.steps);
	selected.obj.set.steps(selected.steps);
	update_step();
	refresh_keys();
}

//called from key_in, change the loopIn point and update it to the live.step and poly
function change_In(val)
{
	//if(DEBUG){post('change In', val, '\n');}
	var change = parseInt(selected.nudge) - val;
	selected.nudge = val;
	if(timing_immediate)
	{
		//selected.obj.nudge.message('int', selected.nudge);
		selected.obj.set.nudge(selected.nudge);
		selected.steps += change;
		//selected.obj.steps.message('int', selected.steps);
		selected.obj.set.steps(selected.steps);
	}
	else
	{
		//selected.obj.nudge.message('set', selected.nudge);
		selected.obj.set.nudge(selected.nudge, 0);
		selected.steps += change;
		//selected.obj.steps.message('int', selected.steps);
		selected.obj.set.steps(selected.steps);
		selected.obj.restart.message('bang');
	}
	update_step();
	refresh_keys();
}

//add a note from the pads to the appropriate poly, and trigger a message back from it
function add_note(part)
{
	//if(DEBUG){post('add_note', part.num, '\n');}
	part.obj.addnote.message('bang');
}

//add new notes received from poly to the appropriate place and update display
function _addnote(num, val)
{
	num += -1;
	val += -1;
	//if(DEBUG){post('addnote', num, val, '\n');}
	part[num].pattern[val] = 1;
	//part[num].obj.pattern.message('list', part[num].pattern);
	part[num].obj.set.pattern(part[num].pattern);
	refresh_keys();
	//update_step();
}

//rotate the pattern based on the blocksize defined in the main patch
/*function rotate_pattern(part, len, dir)
{
	//if(DEBUG){post('rotate_pattern', len, dir, '\n');}
	var bits = Math.ceil(16/len);
	var Out;
	var In;
	if(dir < 0)
	{
		for(var i=0;i<bits;i++)
		{
			Out = Math.min(parseInt((len*(i+1))-1), 15);
			In = len*i;
			part.pattern.splice(Out, 0, parseInt(part.pattern.splice(In, 1)));
			part.velocity.splice(Out, 0, parseInt(part.velocity.splice(In, 1)));
			part.duration.splice(Out, 0, parseInt(part.duration.splice(In, 1)));
			//part.note.splice(Out, 0, parseInt(part.note.splice(In, 1)));
		}
	}
	else
	{
		for(var i=0;i<bits;i++)
		{
			Out = len*i;
			In = Math.min(parseInt((len*(i+1))-1), 15);
			part.pattern.splice(Out, 0, parseInt(part.pattern.splice(In, 1)));
			part.velocity.splice(Out, 0, parseInt(part.velocity.splice(In, 1)));
			part.duration.splice(Out, 0, parseInt(part.duration.splice(In, 1)));
			//part.note.splice(Out, 0, parseInt(part.note.splice(In, 1)));
		}
	}
	part.obj.pattern.message('list', part.pattern);
	part.obj.velocity.message('list', part.velocity);
	part.obj.duration.message('list', part.duration);
	//part.obj.note.message('list', part.note);
	update_step();
	refresh_keys();
}
*/

//New way of doing: rotate the pattern based on the blocksize defined in the main patch
function rotate_pattern(part, len, dir)
{
	//post('rotate_pattern', len, dir, '\n');
	var bits = Math.ceil(16/len);
	var Out;
	var In;
	if(dir < 0)
	{
		for(var i=0;i<bits;i++)
		{
			Out = Math.min(parseInt((len*(i+1))-1), 15);
			In = len*i;
			part.pattern.splice(Out, 0, parseInt(part.pattern.splice(In, 1)));
			part.velocity.splice(Out, 0, parseInt(part.velocity.splice(In, 1)));
		}
	}
	else
	{
		for(var i=0;i<bits;i++)
		{
			Out = len*i;
			In = Math.min(parseInt((len*(i+1))-1), 15);
			part.pattern.splice(Out, 0, parseInt(part.pattern.splice(In, 1)));
			part.velocity.splice(Out, 0, parseInt(part.velocity.splice(In, 1)));
		}
	}
	part.obj.set.pattern(part.pattern);
	part.obj.set.velocity(part.velocity);
	refresh_keys();
}

//update the current value reflected on the invisible ui speed controls
function update_speed(part)
{
	if(!part.lock)
	{
		part.ticks = part.obj.ticks.getvalueof();
		//script['Speed'+(part.num+1)].message('set', part.ticks);
	}
	else
	{
		part.notevalues = part.obj.notevalues.getvalueof();
		part.notetype = part.obj.notetype.getvalueof();
		//script['Speed'+(part.num+1)].message('set', TRANS[part.notevalues][part.notetype]);
	}
}

//DISABLED
//change the display on the CNTRLR encoder rings to reflect the current play position when in freewheel mode
function rotate_wheel(num, pos)
{
	//if(DEBUG_FRWL){post('rotate_wheel', num, pos, '\n');}
	/*if((key_mode==5)&&(num==selected.num+1))
	{
		//post('current_step', num, pos, '\n');
		mod.Send( 'mask', 'key', selected.note[current_step], -1);
		current_step = pos;
		mod.Send( 'mask', 'key', selected.note[current_step], 5);
	}
	if(pad_mode==5)
	{
		if((selected.num<8)&&(num<9))
		{
			num-=1;
			mod.Send( 'to_wheel', num%4, Math.floor(num/4), 'value', pos);
		}
		else if((selected.num>7)&&(num>8))
		{
			num-=9;
			mod.Send( 'to_wheel', num%4, Math.floor(num/4), 'value', pos);
		}
	}*/
}

//DISABLED
//synchronize two parts when holding down select while selecting another part
function sync_wheels(master, slave)
{
	/*//if(DEBUG){post('sync_wheels', master.num, slave.num, '\n');}
	if(slave.lock != master.lock)
	{
		//change_lock_status(slave);
		slave.lock = master.lock;
		slave.obj.quantize.message('int', slave.lock);
		mod.Send( 'to_wheel', slave.num%4, Math.floor(slave.num/4)%2, 'green', slave.lock);
	}
	switch(master.lock)
	{
		case 0:
			slave.ticks = master.ticks;
			slave.obj.ticks.message('int', master.obj.ticks.getvalueof());
			break;
		case 1:
			slave.notevalues = master.notevalues;
			slave.notetype = master.notetype;
			slave.obj.notevalues.message('int', master.obj.notevalues.getvalueof());
			slave.obj.notetype.message('int', master.obj.notetype.getvalueof());
			break;
	}
	update_speed(slave);*/
}

//DISABLED
//change the variables necessary to change the quantization status of a part
function change_lock_status(part, dir)
{
	/*//if(DEBUG_LOCK){post('change_lock_status', part.num, '\n');}
	part.lock = Math.abs(part.lock - 1);
	if(dir==undefined){dir = 0;}
	//if(DEBUG_LOCK){post('direction of change', dir, '\n');}
	var new_speed = TRANS[0];
	part.notevalues = part.obj.notevalues.getvalueof();
	part.notetype = part.obj.notetype.getvalueof();
	part.ticks = part.obj.ticks.getvalueof();
	//if(DEBUG_LOCK){post('got old values:', part.notevalues, part.notetype, part.ticks, '\n');}
	switch(part.lock)
	{
		case 0:
			//if(DEBUG_LOCK){post('was quantized\n');}
			new_speed = TRANS[part.notevalues];
			break;
		case 1:
			switch(dir)
			{
				case 0:
					for(var i=0;i<TRANS.length;i++)
					{
						if(TRANS[i][part.notetype]>=part.ticks)
						{
							new_speed = TRANS[i];
							break;
						}
					}
					break;
				case 1:
					var i=TRANS.length-1;do{
						if(TRANS[i][part.notetype]<=part.ticks)
						{
							new_speed = TRANS[i];
							break;
						}
					}while(i--);
					break;
			}			
			break;
	}
	//if(DEBUG_LOCK){post('new_speed', new_speed, '\n');}
	part.obj.quantize.message('int', part.lock);
	part.ticks = new_speed[part.notetype];
	part.notevalues = TRANS.indexOf(new_speed);
	part.obj.ticks.message('int', part.ticks);
	part.obj.notevalues.message('int', part.notevalues);
	if(part==selected)
	{
		update_gui();
	}
	mod.Send( 'to_wheel', part.num%4, Math.floor(part.num/4)%2, 'green', part.lock);
	update_speed(part);*/
}

//DISABLED
//release any polyplay sequences from being held when the hold key is turned off
function release_held_sequences(part)
{
	//if(DEBUG){post('release held seqs', part.held, '\n');}
	/*for(var i in part.held)
	{
		part.obj.polyplay.message('midinote', part.held[i], 0);
		var trig = part.triggered.indexOf(part.held[i]);
		if(trig > -1)
		{
			part.triggered.splice(trig, 1);
		}
	}
	part.held = [];*/
}



/*	  automation	 */

//DISABLED
//enable recording of preset changes and mutes to a live.clip
function record(val)
{
	/*if(val > 0)
	{
		record_enabled = begin_record();
	}
	else
	{
		record_enabled = 0;
	}	 
	//if(DEBUG_REC){post('record_enabled', record_enabled, '\n');}*/
}

//DISABLED
//check api for current clip and return confirmation of recording
function begin_record()
{
	/*finder.goto('this_device');
	finder.goto('canonical_parent');
	var playing_slot_index = parseInt(finder.get('playing_slot_index'));
	//if(DEBUG_REC){post('playing_slot_index:', playing_slot_index, '\n');}
	if(playing_slot_index>=0)
	{
		finder.goto('clip_slots', playing_slot_index, 'clip');
		autoclip.id = parseInt(finder.id);
	}
	return (parseInt(autoclip.id)>0);*/
}

//DISABLED
//add automation steps directly to the attached Live clip
function add_automation(part, type, val)
{
	/*if(record_enabled)
	{
		autoclip.call('select_all_notes');
		var notes = autoclip.call('get_selected_notes');
		var num = parseInt(notes[1]);
		switch(type)
		{
			case 'mute':
				new_notes = notes.slice(2, -1).concat(['note', part.num+111, Math.round(autoclip.get('playing_position')*100)/100, .2, val+1, 0]);
				break;
			case 'preset':
				new_notes = notes.slice(2, -1).concat(['note', part.num+111, Math.round(autoclip.get('playing_position')*100)/100, .2, val+10, 0]);
				break;
		}				 
		//if(DEBUG_REC){post('notes:', new_notes, '\n');}
		finder.call('replace_selected_notes'); 
		finder.call('notes', num+1);
		for(var i = 0;i<new_notes.length;i+=6)
		{
			finder.call('note', new_notes[i+1], new_notes[i+2]+.001, new_notes[i+3]+.001, new_notes[i+4], new_notes[i+5]);
		} 
		finder.call('done');
		////if(DEBUG_REC){post('new_notes:', finder.call('get_selected_notes'), '\n');}
	}*/
}


/*	 settings		*/

//all of these do , pretty much what they say
function randomize_pattern(global)
{
	if(global>0)
	{
		//if(DEBUG){post('global pattern random');}
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random());
				}while(j--);
				part[i].obj.set.pattern(seq, h+1); 
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].pattern[j]=Math.round(Math.random());
			}while(j--);
			part[i].obj.set.pattern(part[i].pattern);
		}while(i--);
	}
	//update_step();
	refresh_keys();
}

function randomize_velocity(global)
{
	if(global)
	{
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random()*127);
				}while(j--);
				part[i].obj.set.velocity(seq, h+1);
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].velocity[j]=Math.floor(Math.random()*127);
			}while(j--);
			part[i].obj.set.velocity(part[i].velocity);
		}while(i--);
	}
	//update_step();
	refresh_keys();
}

function randomize_duration(global)
{
	if(global)
	{
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random()*7);
				}while(j--);
				part[i].obj.set.duration(seq, h+1);
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].duration[j]=Math.floor(Math.random()*7);
			}while(j--);
			part[i].obj.set.duration(part[i].duration);
		}while(i--);
	}
	//update_step();
}

function reset_data(global)
{
	var i=15;do{
		var Part = part[i];
		//var pset = presets[Part.num];
		Part.obj.set.pattern(default_pattern.slice());
		Part.obj.set.velocity(default_velocity.slice());
		Part.obj.set.duration(default_duration.slice());
		Part.obj.set.swing(0);
		Part.obj.set.random(0);
		Part.obj.set.direction(0);
		Part.obj.set.notevalues(3);
		Part.obj.set.notetype(0);
	}while(i--);
	//if(global)
	//{
		var h=15;do{
			storage.message('store', h);
		}while(h--);
	//}
	refresh_keys();
}


/*	 display routines	 */

//update the display on the CNTLRL/padgui to reflect current data
function refresh_grid()
{
	//if(DEBUG){post('refresh_grid\n');}
	switch(pad_mode)
	{
		default:
			var i=3;do{
				var j=3;do{
					var v = SelectColors[Math.floor(partTRANS[i+(j*4)] == selected.num)];
					mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);
					padgui.message(i, j, v);
				}while(j--);
			}while(i--);
			break;
		case 1:
			var i=3;do{
				var j=3;do{
					var v = AddColors[Math.floor(partTRANS[i+(j*4)] == selected.num)];
					mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);
					padgui.message(i, j, v);
				}while(j--);
			}while(i--);
			break;
	}
	mod.Send( 'receive_translation', 'buttons_5', 'value', (pad_mode==1)*2);
}

//update the display on the CNTRLR/keygui to reflect current data
function refresh_keys()
{ 
	var i=15;do{
		mod.Send( 'receive_translation', 'keys2_'+i, 'value', selected.pattern[i] * StepColors[i]);
		keygui2.message(i, 0, (selected.pattern[i] * GUI_StepColors[i]));
	}while(i--);
	switch(key_mode)
	{
		default:
			var i=15;do{
				var v = ACCENTS[Math.floor(selected.velocity[i]/8)];
				//if(DEBUG){post('velocity', v, '\n');}
				mod.Send( 'receive_translation', 'keys_'+i, 'value', v);
				keygui.message(i, 0, v);
			}while(i--);
			break;
		case "old_default":
			var i=15;do{
				var v = part[i].active*2
				mod.Send( 'receive_translation', 'keys_'+i, 'value',  v);
				keygui.message(i, 0, v);
				mod.Send( 'key', i+16, selected.pattern[i] * StepColors[i]);
			}while(i--);
			break;
		case 1:
			var i=15;do{
				mod.Send( 'receive_translation', 'keys_'+i, 'mask', -1);
				var v = (i>=part[selected.num].nudge&&i<=(part[selected.num].nudge+part[selected.num].steps))*5;
				mod.Send( 'receive_translation', 'keys_'+i, 'value',  v);
				keygui.message(i, 0, v);
				mod.Send( 'receive_translation', 'keys2_'+i, 'value',  selected.pattern[i] * StepColors[i]);
			}while(i--);
			break;
		case 2:
			var i=15;do{
				mod.Send( 'receive_translation', 'keys_'+i, 'mask', -1);
				mod.Send( 'receive_translation', 'keys_'+i, 'value',  Colors[part[selected.num].behavior[i]]);
				keygui.message(i, 0, selected.behavior[i]+8);
				mod.Send( 'receive_translation', 'keys2_'+i, 'value',  selected.pattern[i] * StepColors[i]);
			}while(i--);
			break;
		case 3:
			var p = presets[selected.num]-1;
			var i=15;do{
				mod.Send( 'receive_translation', 'keys_'+i, 'mask', -1);
				var v = (i==p)+3;
				mod.Send( 'receive_translation', 'keys_'+i, 'value', v);
				keygui.message(i, 0, v);
				mod.Send( 'receive_translation', 'keys2_'+i,  selected.pattern[i] * StepColors[i]);
			}while(i--);
			break;
		case 4:
			var p = presets[selected.num]-1;
			var i=15;do{
				mod.Send( 'receive_translation', 'keys_'+i, 'mask', -1);
				var v = (i==p)+6;
				mod.Send( 'receive_translation', 'keys_'+i, 'value', v);
				keygui.message(i, 0, v);
				mod.Send( 'receive_translation', 'keys2_'+i,  selected.pattern[i] * StepColors[i]);
			}while(i--);
			break;
	}
	presetdisplaygui.message('text', presets[selected.num]);
	messnamed(unique+'confirm', 'Reset');	 
}


//remove any masked elements on the CNTRLR
function demask()
{
	post('demask\n');
}

//update gui elements to reflect current data
function update_gui()
{
	notevaluesgui.message('set', selected.obj.notevalues.getvalueof());
	notetypegui.message('set', selected.obj.notetype.getvalueof());
	directiongui.message('set', selected.obj.direction.getvalueof());
	Random.message('set', selected.obj.random.getvalueof());
	Groove.message('set', (selected.obj.swing.getvalueof()*100)-50);
	update_time_bg();

}

function update_time_bg()
{
	if(time1 == 8)
	{
		timedngui.activebgcolor(.35, .35, .35);
		mod.Send( 'receive_translation', 'buttons_0', 'value', 0);
	}
	else
	{
		if(selected.notevalues!=time1)
		{
			timedngui.activebgcolor(.35, .35, .35);
			mod.Send( 'receive_translation', 'buttons_0', 'value', 0);
		}
		else
		{
			timedngui.activebgcolor(0, 1, 0);
			mod.Send( 'receive_translation', 'buttons_0', 'value', 6);
		}
	}
	if(time2 == 8)
	{
		timeupgui.activebgcolor(.35, .35, .35);
		mod.Send( 'receive_translation', 'buttons_1', 'value', 0);
	}
	else
	{
		if(selected.notevalues!=time2)
		{
			timeupgui.activebgcolor(.35, .35, .35);
			mod.Send( 'receive_translation', 'buttons_1', 'value', 0);
		}
		else
		{
			timeupgui.activebgcolor(0, 1, 0);
 			mod.Send( 'receive_translation', 'buttons_1', 'value', 6);
		}
	}
}

//DISABLED
//update the current bank assignment in Python
function update_bank()
{
	/*switch(pad_mode)
	{
		default:
			mod.Send( 'set_device_bank', selected.channel>0);
			mod.Send( 'set_local_ring_control', 1);
			var i=7;do{
				params[Encoders[i]].hidden = 0;
				params[Speeds[i]].hidden = 1;
				params[Speeds[i+8]].hidden = 1;
			}while(i--);
			break;
		case 5:
			mod.Send( 'set_device_bank', 2+(selected.num>7));
			mod.Send( 'set_local_ring_control', 0);
			var r = (selected.num>7)*8;
			var i=7;do{
				params[Encoders[i]].hidden = 1;
				params[Speeds[i]].hidden = selected.num>7;
				params[Speeds[i+8]].hidden = selected.num<8;
				var x = i%4;
				var y = Math.floor(i/4);
				mod.Send( 'to_wheel', x, y, 'mode', 4);
				mod.Send( 'to_wheel', x, y, 'custom', 'x'+(part[i+r].pattern.join('')));
				mod.Send( 'to_wheel', x, y, 'green', part[i+r].lock);
			}while(i--);
			var i=3;do{
				mod.Send( 'to_wheel', i, 2, 'mode', 1);
				mod.Send( 'to_wheel', i, 2, 'green', 0);
			}while(i--);
			break;
	}
	rotgate.message('int', ((pad_mode==5)||(key_mode==5))); 
	*/
}


/*///////////////////////////
//	   Device Component	   //
//		  and LCD		   //
///////////////////////////*/


var pns=[];
var mps=[];
var found_device = 0;
var params = [];
var dials = [];

var Encoders = ['Encoder_0', 'Encoder_1', 'Encoder_2', 'Encoder_3', 'Encoder_4', 'Encoder_5', 'Encoder_6', 'Encoder_7', 'Encoder_8', 'Encoder_9', 'Encoder_10', 'Encoder_11'];
var Dials =  ['RepeatLen', 'Groove', 'Random', 'RotSize'];
Warning = ['Missing', 'DrumRack.', 'Please', 'insert', 'and', 'press', 'Detect', 'Rack.', ' ', ' ', ' ', ' '];

//var Warning = ['No device', 'was found.', 'Place a', 'DrumRack', 'next to', 'this mod', 'and press', '\"Detect',	'DrumRack\"', 'get', 'started.', ' '];
//var PolyWarning = ['No device', 'is stored', 'for this', 'PolySeq.', 'Use the', 'selector', 'button in', 'the settings', 'menu to', 'select the', 'target', 'instrument.'];
// called from init
function init_device()
{
	finder = new LiveAPI(callback, 'this_device');
	pns['device_name']=this.patcher.getnamed('device_name');
	for(var i=0;i<8;i++)
	{
		pns[Encoders[i]]=this.patcher.getnamed('pn'+(i+1));
		pns[Encoders[i]].message('text', ' ');
		mps[Encoders[i]]=this.patcher.getnamed('mp'+(i+1));
		mps[Encoders[i]].message('text', ' ');
		params[Encoders[i]]=this.patcher.getnamed(Encoders[i]);
		params[Encoders[i]].message('set', 0);
	}
	for(var i=0;i<4;i++)
	{
		pns[Encoders[i+8]]=this.patcher.getnamed('pn'+(i+9));
		pns[Encoders[i+8]].message('text', ' ');
		mps[Encoders[i+8]]=this.patcher.getnamed('mp'+(i+9));
		mps[Encoders[i+8]].message('text', ' ');
	}
	for(var i=0;i<4;i++)
	{
		dials[Encoders[i+8]]=this.patcher.getnamed(Dials[i]);
		dials[Encoders[i+8]].message('set', 0);
	}
	params[Encoders[11]]=this.patcher.getnamed(Dials[3]);
	params[Encoders[11]].message('set', 0);
	detect_drumrack();
}

function detect_devices()
{
	detect_drumrack();
	if(devices[0]==0)
	{
		this.patcher.getnamed('devices').front();
	}
}

function detect_drumrack()
{
	//setup the initial API path:
	if(devices[0] > 0)
	{
		devices[0] = check_device_id(devices[0]);
	}
	if(devices[0] == 0)
	{
		finder.goto('this_device');
		var this_id = parseInt(finder.id);
		finder.goto('canonical_parent');
		var track_id = parseInt(finder.id);
		var found_devices = finder.getcount('devices');
		for (var i=0;i<found_devices;i++)
		{
			finder.id = track_id;
			finder.goto('devices', i);
			if(finder.get('class_name')=='DrumGroupDevice')
			{
				debug("\nDrumRack found");
				devices[0] = parseInt(finder.id);
				//if(DEBUG){post('DrumRack found', devices[0], '\n');}
				break;
			}
		}
	}
	if(devices[0] == 0)
	{
		showerror();
	}
	else
	{
		hideerror();
		_select_chain(selected.num)
		//report_drumrack_id();
	}
}

//called fram pattr that stores any device id that was selected by the user last session
function set_devices()
{
	var ids = arrayfromargs(arguments);
	//if(DEBUG){post('set_devices', ids, '\n');}
	devices = ids;
}

//find the appointed_device
function detect_device()
{
	//if(DEBUG){post('select_device \n');}
	finder.goto('live_set', 'appointed_device');
	//if(DEBUG){post('device id ==', finder.id, '\n');}
	if(check_device_id(parseInt(finder.id))>0)
	{
		_select_chain(selected.num);
	}
	//this.patcher.getnamed('devices').wclose();
}

//check to make sure previous found_device is valid
function check_device_id(id)
{
	var found = 0;
	//if(DEBUG){post('device_id', id, '\n')};
	if(id>0)
	{
		if(selected.channel == 0)
		{
			finder.id = id;
			if(finder.get('class_name')=='DrumGroupDevice')
			{
				found = parseInt(finder.id);
			}
		}
		else
		{
			finder.goto('canonical_parent');
			finder.goto('canonical_parent');
			if(finder.get('class_name')=='DrumGroupDevice')
			{
				drumgroup_is_present = true;
				found = parseInt(finder.id);
			}
		}
	}
	devices[selected.channel] = found;
	this.patcher.getnamed('devices').subpatcher().getnamed('devices').message('list', devices);
	return found;
}

//send the current chain assignment to mod.js
function _select_chain(chain_num)
{
	//if(DEBUG){post('select_chain', chain_num, selected.channel, devices[selected.channel], '\n');}
	if(selected.channel==0)
	{
		//mod.Send( 'set_device_parent', devices[selected.channel]);
		//mod.Send( 'set_device_chain', Math.max(0, Math.min(chain_num + global_offset, 112)));
		mod.Send( 'send_explicit', 'receive_device', 'set_mod_device_parent', 'id', devices[selected.channel]);
		mod.Send( 'receive_device', 'set_mod_drum_pad', Math.max(0, Math.min(chain_num + global_offset, 112)));

	}
	else
	{
		//mod.Send( 'set_device_single', devices[selected.channel]);
		mod.Send( 'send_explicit', 'receive_device', 'mod_set_device_parent', 'id', devices[selected.channel], 1);

	}
	if(devices[selected.channel]==0)
	{
		showerror();
	}
	update_bank();
}

//sort calls to the internal LCD
function _lcd(obj, type, val)
{
	debuglcd('lcd', obj, type, val);
	if(val==undefined)
	{
		val = '_';
	}
	if((type=='lcd_name'))
	{
		if(pns[obj])
		{
			pns[obj].message('text', val.replace(/_/g, ' '));
		}
	}
	else if((type == 'lcd_value'))
	{
		if(mps[obj])
		{
			mps[obj].message('text', val.replace(/_/g, ' '));
		}
	}
	else if(type == 'encoder_value')
	{
		if(params[obj]!=undefined)
		{
			params[obj].message('set', val);
		}
	}
}

//distribute gui knobs to their destinations
function _encoder(num, val)
{
	//if(DEBUG){post('encoder in', num, val, '\n');}
	if(num<8)
	{				
		mod.Send( 'receive_device', 'set_mod_parameter_value', num, val);
	}
	else
	{
		switch(num)
		{
			case 8:
				//selected.repeat = val;
				//selected.obj.repeat.message('int', selected.repeat);
				selected.obj.set.repeat(val);
				break;
			case 9:
				//selected.swing = (val+50)/100;
				//selected.obj.swing.message('float', selected.swing);
				selected.obj.set.swing((val+50)/100);
				break;
			case 10:
				//selected.random = val;
				//selected.obj.random.message('float', selected.random);
				selected.obj.set.random(val);
				break;
			case 11:
				mod.Send( 'receive_device', 'set_mod_parameter_value', num, val);
				break;
		}
	}	 
}

//Used for UI warning. Uses the lcd objects to display an error message.
function showerror()
{
	pns.device_name.message('text', 'Detect Rack');
	pns.device_name.message('activebgcolor', 0.92, 0.95, 0.05, 0.73);
	for(var i=0;i<8;i++)
	{
		pns[Encoders[i]].message('text', Warning[i]);
		mps[Encoders[i]].message('text', ' ');
	}
}

//Used for UI warning.	Uses the lcd objects to display an error message.
function hideerror()
{
	pns.device_name.message('text', 'Drumrack Found');
	pns.device_name.message('activebgcolor', 0.92, 0.95, 0.05, 0.);
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]].message('text', ' ');
	}
}

forceload(this);
