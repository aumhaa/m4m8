/*
	translates messages from pattrstorage into values that the control surface JS will understand
	translates control surface messages into thing pattrstorage will understand.
*/

autowatch = 1;
outlets = 2;
setoutletassist(0,"latch messages, msgs from pattrstorage, etc.");
setoutletassist(1,"to mods");
setinletassist(0,"to pattrstorage");


var script = this;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);

var DEBUG_UPDT = false;
var DEBUG_LCD = false;
var DEBUG_NEW = false;

var unique = jsarguments[1];

var SYNTH = (jsarguments[2]=='synth');
var type = jsarguments[2] == 'synth' ? 'SynthSteppr' : 'DrumSteppr';

var Translations = require(type+"Translations");
var Colors = require(type+"Colors");
include(type+'Functions', this);

var finder;
var mod;
var found_mod;
var mod_finder;
var Mod = ModComponent.bind(script);
var ModProxy = ModProxyComponent.bind(script);

var gridbuf=new Array();
var gridunique = 1;


var done_count = 0;

var selected_sequence_number = 0;
var keys_to_mutes = false;
var mgate = 0;
var live = 0;
var shifted = false;

var BUTTON_COLORS = [1, 1, 2, 2, 3, 4, 5, 5];

var ctlr = new Object;
ctlr.ctls = new Object; //the control names, like "key 0" or "ring 2 2 0"
ctlr.msgs = new Object; //messages 

var GRIDMAP =[	[undefined, undefined, undefined, undefined, 'pads_0', 'pads_1', 'pads_2', 'pads_3'],
				['buttons_0', 'buttons_1', 'buttons_2', 'buttons_3', 'pads_4', 'pads_5', 'pads_6', 'pads_7'],
				['buttons_4', 'buttons_5', 'buttons_6', 'buttons_7', 'pads_8', 'pads_9', 'pads_10', 'pads_11'],
				[undefined, undefined, undefined, undefined, 'pads_12', 'pads_13', 'pads_14', 'pads_15'],
				['keys_0', 'keys_1', 'keys_2', 'keys_3', 'keys_4', 'keys_5', 'keys_6', 'keys_7'],
				['keys2_0', 'keys2_1', 'keys2_2', 'keys2_3', 'keys2_4', 'keys2_5', 'keys2_6', 'keys2_7'],
				['keys_8', 'keys_9', 'keys_10', 'keys_11', 'keys_12', 'keys_13', 'keys_14', 'keys_15'],
				['keys2_8', 'keys2_9', 'keys2_10', 'keys2_11', 'keys2_12', 'keys2_13', 'keys2_14', 'keys2_15']]

var Ctl_to_Trans= {};

var Mod = ModComponent.bind(script);

function init()
{
	mod = new ModProxy(script, ['Send', 'SendDirect', 'restart']);
	found_mod = new Mod(script, (SYNTH ? 'synth' : 'drum') + 'steppr', unique, false);
	//mod.debug = debug;
	mod_finder = new LiveAPI(mod_callback, 'this_device');
	found_mod.assign_api(mod_finder);


	deprivatize_script_functions(script);
	setup_translations();
	setup_modtranslations();
	setup_mutes();
	init_device();
	update_all();
	messnamed(unique+'loadbang', 'bang');
	if(!SYNTH){ctl('pads_12', 1);}
	mod.Send('receive_translation', 'keys2_8', 'value', 1);
}

function mod_callback(args)
{
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		//debug('mod callback:', args);
		if(args[1] in script)
		{
			//debug(script[args[1]]);
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
	if(val)
	{
		Alive = 1;
	}
}

function initialize(val)
{
	mod = found_mod;
}

function setup_translations()
{
	/*Here we set up some translation assignments and send them to the Python ModClient.
	Each translation add_translation assignment has a name, a target, a group, and possibly some arguments.
	Translations can be enabled individually using their name/target combinations, or an entire group can be enabled en masse.
	There are not currently provisions to dynamically change translations or group assignments once they are made.*/

	//Base stuff:
	if(SYNTH)
	{
		for(var i = 0;i < 16;i++)
		{
			mod.Send('add_translation', 'pads_'+i, 'base_grid', 'base_pads', i%8, Math.floor(i/8));
			mod.Send('add_translation', 'keys2_'+i, 'base_grid', 'base_keys', i%8, Math.floor(i/8));
			mod.Send('add_translation', 'keys_'+i, 'base_grid', 'base_keys2', i%8, Math.floor(i/8)+2);
		}
		for(var i=0;i<8;i++)
		{
			mod.Send('add_translation', 'buttons_'+i, 'key', 'base_buttons', i);
		}
	}
	else
	{
		for(var i = 0;i < 16;i++)
		{
			mod.Send('add_translation', 'pads_'+i, 'base_grid', 'base_pads', i%4, Math.floor(i/4));
			mod.Send('add_translation', 'keys_'+i, 'base_grid', 'base_keys', (i%4)+(4*(!SYNTH)), Math.floor(i/4));
			mod.Send('add_translation', 'keys2_'+i, 'base_grid', 'base_keys2', (i%4)+4, Math.floor(i/4));
		}
		mod.Send('add_translation', 'pads_batch_fold', 'base_grid', 'base_pads', 0, 4);
		mod.Send('add_translation', 'keys_batch_fold', 'base_grid', 'base_keys', 0, 4);
		mod.Send('add_translation', 'keys2_batch_fold', 'base_grid', 'base_keys2', 0, 8, 4);
		for(var i=0;i<8;i++)
		{
			mod.Send('add_translation', 'buttons_'+i, 'key', 'base_buttons', i);
		}
	}
	mod.Send('enable_translation_group', SYNTH ? 'base_pads' : 'base_keys', 0);

	//CNTRLR stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send('add_translation', 'pads_'+i, 'cntrlr_grid', 'cntrlr_pads', i%4, Math.floor(i/4));
		mod.Send('add_translation', 'keys_'+i, 'cntrlr_key', 'cntrlr_keys', i, 0);
		mod.Send('add_translation', 'keys2_'+i, 'cntrlr_key', 'cntrlr_keys2', i, 1);
	}
	mod.Send('add_translation', 'pads_batch', 'cntrlr_grid', 'cntrlr_pads', 0);
	mod.Send('add_translation', 'keys_batch', 'cntrlr_key', 'cntrlr_keys', 0);
	mod.Send('add_translation', 'keys2_batch', 'cntrlr_key', 'cntrlr_keys2', 1); 
	for(var i=0;i<8;i++)
	{
		mod.Send('add_translation', 'buttons_'+i, 'cntrlr_encoder_button_grid', 'cntrlr_buttons', i);
		mod.Send('add_translation', 'extras_'+i, 'cntrlr_encoder_button_grid', 'cntrlr_extras', i);
	}
	mod.Send('add_translation', 'buttons_batch', 'cntrlr_encoder_button_grid', 'cntrlr_buttons');
	mod.Send('add_translation', 'extras_batch', 'cntrlr_encoder_button_grid', 'cntrlr_extras');

	//Ohm stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send('add_translation', 'pads_'+i, 'grid', 'ohm_pads', (i%4)+4, Math.floor(i/4));
		mod.Send('add_translation', 'keys_'+i, 'grid', 'ohm_keys', i%8, (i < 8 ? 4 : 6));
		mod.Send('add_translation', 'keys2_'+i, 'grid', 'ohm_keys2', i%8, (i < 8 ? 5 : 7));
	}
	//mod.Send('add_translation', 'pads_batch', 'grid', 'ohm_pads', 0);
	//mod.Send('add_translation', 'keys_batch', 'grid', 'ohm_keys', 2);
	//mod.Send('add_translation', 'keys2_batch', 'grid', 'ohm_keys2', 4); 
	for(var i=0;i<8;i++)
	{
		mod.Send('add_translation', 'buttons_'+i, 'grid', 'ohm_buttons', i%4, Math.floor(i/4)+1);
		//mod.Send('add_translation', 'extras_'+i, 'grid', 'ohm_extras', i, 7);
	}
	//mod.Send('add_translation', 'buttons_batch', 'grid', 'ohm_buttons', 6);
	//mod.Send('add_translation', 'extras_batch', 'grid', 'ohm_extras', 7);

}

function setup_modtranslations()
{
	/*This function replaces the latchControls patcher */

	if(!SYNTH)
	{
		latch('8vaDn', 'buttons_0', 'button', 0, 1, 0, 1);
		latch('8vaUp', 'buttons_1', 'button', 0, 1, 0, 1);
		latch('PitchDn', 'buttons_2', 'button', 0, 1, 0, 1);
		latch('PitchUp', 'buttons_3', 'button', 0, 1, 0, 1);
		latch('sequence['+selected_sequence_number+']::repeat_enable', 'buttons_4', 'button', 0, 1, 0, 1);
		latch('addmode', 'buttons_5', 'cycle', 0, 3, 0, 6);
		latch('RotL', 'buttons_6', 'button', 0, 1, 0, 1);
		latch('RotR', 'buttons_7', 'button', 0, 1, 0, 1);
		var COLORS = [3, 127, 127, 127];
		for(var i=0;i<16;i++)
		{
			latch('seqselect', 'pads_'+i, 'matrix', i%4, Math.floor(i/4), 1, 6);
			latch('enable['+i+']', 'keys2_'+i, 'toggle', 0, 1, 0, COLORS[i%4]);
			latch('chainmute['+i+']', 'keys_'+i, 'toggle', 0, 1, 2, 0);
		}
	}
	else
	{
		latch('8vaDn', 'buttons_0', 'button', 0, 1, 0, 1);
		latch('8vaUp', 'buttons_1', 'button', 0, 1, 0, 1);
		latch('PitchDn', 'buttons_2', 'button', 0, 1, 0, 1);
		latch('PitchUp', 'buttons_3', 'button', 0, 1, 0, 1);
		latch('sequence['+selected_sequence_number+']::repeat_enable', 'buttons_4', 'button', 0, 1, 0, 1);
		latch('AutomatorStart', 'buttons_5', 'button', 0, 3, 0, 6);
		latch('RotL', 'buttons_6', 'button', 0, 1, 0, 1);
		latch('RotR', 'buttons_7', 'button', 0, 1, 0, 1);
		var COLORS = [3, 127, 127, 127];
		for(var i=0;i<16;i++)
		{
			latch('sequence[0]::preset', 'pads_'+i, 'matrix', i, 0, 1, 5);
			latch('enable['+i+']', 'keys2_'+i, 'toggle', 0, 1, 0, COLORS[i%4]);
			latch('add', 'keys_'+i, 'matrix', i, 0, 0, 4);
		}
		outlet(1, 'sequence[0]::seqactive', 1);
	}		
}

function key(x, val)
{
	ctl('buttons_'+x, val ? 127 : 0);
}

function base_grid(x, y, val)
{
	//debug('base_grid', x, y, val);
	{
		if(SYNTH)
		{
			if(!shifted)
			{
				if(y<2)
				{
					ctl('keys2_'+(x + (y*8)), val ? 127 : 0);
				}
				else
				{
					ctl('keys_'+(x + ((y-2)*8)), val ? 127 : 0);
				}
			}
			else
			{
				if(y<2)
				{
					ctl('pads_'+(x + (y*8)), val ? 127 : 0);
				}
				else
				{
					ctl('buttons_'+(x + ((y-2)*8)), val ? 127 : 0);
				}
			}
		}
		else
		{
			if(!shifted)
			{
				if(x < 4)
				{
					ctl('pads_'+(x + (y*4)), val ? 127 : 0);
				}
				else
				{
					ctl('keys2_'+((x-4) + (y*4)), val ? 127 : 0);
				}
			}
			else
			{
				if(x < 4)
				{
					ctl('keys_'+(x + (y*4)), val ? 127 : 0);
				}
				else if(y<2)
				{
					ctl('buttons_'+((x-4) + (y*4)), val ? 127 : 0);
				}
			}
		}
	}	
}

function cntrlr_grid(x, y, val)
{
	ctl('pads_'+(x + (y*4)), val);
}

function cntrlr_key(x, y, val)
{
	switch(y)
	{
		case 0:
			ctl('keys_'+x, val);
			break;
		case 1:
			ctl('keys2_'+x, val);
			break;
	}
}

function cntrlr_encoder_button_grid(x, y, val)
{
	ctl('buttons_'+(x + (Math.abs(y-1)*4)), val);
}

function grid(x, y, val)
{
	debug('grid', x, y, val);
	{
		var msg = GRIDMAP[y][x];
		if(msg)
		{
			ctl(msg, val);
		}
	}
}

function shift(val)
{
	debug('shift:', val);
	if(val!=shifted)
	{
		shifted = val;
		if(SYNTH)
		{
			mod.Send('enable_translation_group', 'base_keys', Math.floor(!shifted));
			mod.Send('enable_translation_group', 'base_pads', Math.floor(shifted));
			mod.Send('enable_translation_group', 'base_keys2', Math.floor(!shifted));
		}
		else
		{
			mod.Send('enable_translation_group', 'base_pads', Math.floor(!shifted));
			mod.Send('enable_translation_group', 'base_keys', Math.floor(shifted));
			mod.Send('enable_translation_group', 'base_keys2', Math.floor(!shifted));
		}
		//mod.Send('enable_translation_group', 'base_buttons',  Math.floor(shifted));
		//mod.Send('enable_translation_group', 'base_extras',  Math.floor(shifted));
		update_all();
	}
}

function update_all()
{
	if(SYNTH)
	{
		var i=15;do{
			mod.Send('receive_translation', 'pads_'+i, 'value', 1);
			mod.Send('receive_translation', 'keys_'+i, 'value', 0);
		}while(i--);
		outlet(1, 'getsequence[0]::preset');
	}
	else
	{
		var i=15;do{
			mod.Send('receive_translation', 'pads_'+i, 'value', padsToChain[i]==selected_sequence_number ? 6 : 1);
			outlet(1, 'getchainmute['+i+']');
		}while(i--);
	}
	for(var i=0;i<8;i++)
	{
		mod.Send('receive_translation', 'buttons_'+i, 'value', BUTTON_COLORS[i]);
		//mod.Send('receive_translation', 'extras_'+i, 'value', 0);
	}
	for(var i=0;i<16;i++)
	{
		outlet(1, 'getbehav['+i+']');
		outlet(1, 'getenable['+i+']');
	}
}

//function update_all(){}
	
function set_selected_seq(chain, num) 
{
	var COLORS = [3, 127, 127, 127];
	selected_sequence_number = num;
	for(var i=0;i<16;i++)
	{
		latch('enable['+i+']', 'keys2_'+i, 'toggle', 0, 1, 0, COLORS[i%4]);
		outlet(1, 'getenable['+i+']');
	}
	//if(!SYNTH)
	//{
		latch('sequence['+selected_sequence_number+']::repeat_enable', 'buttons_4', 'button', 0, 1, 0, 1);
		api_links(chain);
	//}
}

function set_keys_to_mutes(val)
{
	if(val != keys_to_mutes)
	{
		keys_to_mutes = val>0;
		switch(val)
		{
			case 0:
				if(!SYNTH)
				{
					for(var i=0;i<16;i++)
					{
						latch('chainmute['+i+']', 'keys_'+i, 'toggle', 0, 1, 2, 0);
					}
				}
				else
				{
					for(var i=0;i<16;i++)
					{
						latch('add', 'keys_'+i, 'matrix', i, 0, 0, 4);
					}
				}
				break;
			case 1:
				for(var i=0;i<16;i++)
				{
					latch('behav['+i+']', 'keys_'+i, 'cycle', 0, 8, 0, 1);
				}
				break;
		}
	}
	update_all();
}

function anything(){}

function clear(){
	ctlr.ctls = new Object; //the control names, like "key 0" or "ring 2 2 0"
	ctlr.msgs = new Object; //messages 
}

//turn mod message input into a pattrstorage message output
function ctl(){
	var a = arrayfromargs(arguments);
	var val = a.pop(); //the last element in the array is removed and assigned to val. I'm assuming it is range 0-127 always.
	var bval = val>0; //"bit" value - convert to 0/1
	//var key = a.join(" "); //e.g., "key 1"
	var key = a[0];
	//debug("\nCT->>key",key,val); 
	if(ctlr.ctls[key]){	   
		var msgout = ctlr.ctls[key].message;
		var min = parseInt(ctlr.ctls[key].rangelo);
		var max = parseInt(ctlr.ctls[key].rangehi);
		var range = Math.abs(max-min);
		var on = ctlr.ctls[key].vel_on;
		var off = ctlr.ctls[key].vel_off;
		var sval = parseInt(ctlr.ctls[key].value); //storedvalue
		//debug("\nCT->>msgout",msgout,ctlr.ctls[key].type,"v",sval);
		switch(ctlr.ctls[key].type){
			case 'toggle':
			//don't care about button release:
			if(bval){
				sval=1-sval; //invert the toggle
				ctlr.ctls[key].value=sval; //update the object's stored value
				val = sval; 
				outlet(1,msgout,val);
			}
			break;
			
			case 'button':
			//scale the values if needed:
			val = (1-bval)*min + (bval*max);
			outlet(1,msgout,val);
			break;
			
			case 'matrix':
			if(bval){
				var x = ctlr.ctls[key].matrix_x;
				var y = ctlr.ctls[key].matrix_y;
				outlet(1,msgout,x,y,bval);
				//debug("\nCT-matrix--",x,y,bval);
			}
			break;
			
			case 'pot':
			val = (range*val/127)+min;
			outlet(1,msgout,val);
			break;
			
			case 'cycle':
			//don't want button release:
			if(bval){
				//debug("cycle",sval,min,max);
				sval = ((1+sval)+min)%max;
				//debug("...after",sval);
				ctlr.ctls[key].value=sval;
				outlet(1,msgout,sval);
			}
			break;
			
			case 'encoder':
			ctlr.ctls[key].value = val; //update the object's stored value
			val = (range*val/127)+min;
			outlet(1,msgout,val);
			break;
		}
	}else{
		//debug("CT-unassigned ctl");
	}
}

//turn a pattrstorage message into a MIDI message
function update(){
	var key,min,max,range,mval;
	var a = arrayfromargs(arguments);
	var themess = a[0];
	var theval = a.slice(1);
	//debug("CT-<<update",themess,"-",theval);
	//if there's something latched to this message, let's update the controller's LEDs:
	if(ctlr.msgs[themess]){
		//is this a matrix type? key is stored a bit differently with a matrix type:
		if(ctlr.msgs[themess].matrix){
			//debug("CT-isMATRIX",themess,theval.length);
			if(theval.length==1){
				theval = Math.max(theval, 0);
				theval = [theval,0,1];
			}
			//turn off the previous matrix button:
			if(ctlr.msgs[themess].pvsmtx.length){
				var pvs = ctlr.msgs[themess].pvsmtx.slice(0);
				var keypvs = ctlr.msgs[themess][pvs[0]][pvs[1]];
				ctlout(keypvs, ctlr.ctls[keypvs].vel_off);
			}
			//assuming (dangerously?) that 'theval' is a 3 item array of x,y,theval
			//if(ctlr.msgs[themess]&&ctlr.msgs[themess][theval[0]]&&ctlr.msgs[themess][theval[0]][theval[1]]){
			key=ctlr.msgs[themess][theval[0]][theval[1]];
			//store the value from the update:
			ctlr.ctls[key].value = theval;
			//debug("CT-mtx key",key);
			if(theval[2]>0){
				mval = ctlr.ctls[key].vel_on;
			}else{
				mval = ctlr.ctls[key].vel_off;
			}
			//store these mtx coords in pvsmtx so we can turn it off on the next one:
			ctlr.msgs[themess].pvsmtx = [ theval[0], theval[1] ];		 
			ctlout(key, mval);
		}else{ //pots, buttons, toggles, encoders, cycle
		
			key = ctlr.msgs[themess].control;
			if(key&&ctlr.ctls[key]){
				//debug("CT-<<key",key,themess);
				//store the value from the update:
				ctlr.ctls[key].value = theval;
				min = ctlr.ctls[key].rangelo;
				max = ctlr.ctls[key].rangehi;
				range = Math.abs(max-min);
				//no need to update pots, so filter those out:
				if(ctlr.ctls[key].type!='pot'){
					switch(ctlr.ctls[key].type){
					case 'encoder':
					//encoder just gets sent the value for an update:
					mval = Math.floor(127*(theval-min)/range);
					//debug("CT-mval",mval,theval,min,"....",theval-min,range);
					break;
				
					case 'button':
					//buttons get their value changed based on color:
					if(theval>0){
						mval = ctlr.ctls[key].vel_on;
					}else{
						mval = ctlr.ctls[key].vel_off;
					}
					//debug("CT-btns",themess,theval,"--",mval);
					break;
				
					case 'toggle':
					//toggles get their value changed based on color:
					if(theval>0){
						mval = ctlr.ctls[key].vel_on;
					}else{
						mval = ctlr.ctls[key].vel_off;
					}
					//debug("CT-togs",themess,theval,"--",mval);
					break;
				
					//with cycle we make a concession that it could cycle a range of, say, 2-9, so we want to  
					case 'cycle':
					var colorsout = [0,1,3,4,5,127,2,6]; //turn values 0-7 into color values for modjs. off, white, cyan,magenta,red,blue,yellow,green
					var min = ctlr.ctls[key].rangelo;
					//for use with mods.js in Live, non-blinking colors
					mval = colorsout[theval-min];
					//debug("CT-cycle",themess,theval,"--",mval);
					break;
				
					}
					ctlout(key, mval);
				}
			}
		}
		//if(themess == 
	}
}

//NOT USED: used to create a unique ID for a matrix cell. can be used for matrix of up to 256x256:
function mtxid(x,y){
	key = x | (y << 8);
	return key;
}

//arguments for non-matrix are: 
//	  message, ctl #, type ,range lo, range hi, vel (color) on, vel (color) off
//and for a 'matrix'
//	  message, ctl #, type, matrix_x, matrix_y, vel on,vel off
function latch(){
	var a=arrayfromargs(arguments);
	var pnames= ['message','control','type','rangelo','rangehi','vel_off','vel_on','value'];
	//first setup default values
	var args = new Object;
	if(a[2]!=='matrix'){
		//non-matrix:
		args.message = 'parameter';
		args.control = 0;
		args.type = 'button';
		args.rangelo = 0;
		args.rangehi = 127;
		args.vel_off = 0;
		args.vel_on = 127;
		args.value = 0; //used for storing current value
	}else{
		//matrix types:
		pnames= ['message','control','type','matrix_x','matrix_y','vel_off','vel_on','value'];
		args.message = 'parameter';
		args.control = 0;
		args.type = 'matrix';
		args.matrix_x = 0;
		args.matrix_y = 0;
		args.vel_off = 0;
		args.vel_on = 127;
		args.value = 0; //used for storing current value
	}
	//then overwrite them with the arguments that are actually provided. (this way we don't have to code different cases for different lengths):
	for(var i=0;i<a.length;i++){
		args[pnames[i]]=a[i];
		//debug("CT-define",i,args[pnames[i]])
	}
	
	//setup the ctlr.ctls object which is used to extract a pattr message from a given mod message
	var key = args.control;
	var mess = args.message;
	//make the ctls object for this key:
	if(!ctlr.ctls[key]){
		ctlr.ctls[key] = new Object;
	}else{
		//if this key is already assigned to a message, lets remove it:
		if(args.type!='matrix'){
			var remove = ctlr.ctls[key].message;
			//debug("CT-removing",remove,"from ctrlr.msgs",key);
			ctlr.msgs[remove]=new Object;
		}
	}
	//now make all the assignments:
	for(p in args){
		ctlr.ctls[key][p] = args[p];
		//debug("CT-latched",p,"-",ctlr.ctls[key][p]);
	}
	//now we set up the companion ctntrl.msgs object which is used to extract a mod message from a pattr message
	if(!ctlr.msgs[mess]){
		ctlr.msgs[mess]=new Object;
	}
	
	//with matrix types, we need to fetch the key from the message using coordinates (i.e., "mtx 2 3 <val>" comes in, rather than "tog 5 <val>"), rather than ints, so we setup ctlr.msgs accordingly:
	if(args.type=='matrix'){
		ctlr.msgs[mess].matrix = true;
		if(!ctlr.msgs[mess][args.matrix_x]){
			ctlr.msgs[mess][args.matrix_x] = new Object();
		}
		ctlr.msgs[mess][args.matrix_x][args.matrix_y]=key;
		ctlr.msgs[mess].pvsmtx = new Array(); //a place to store previous matrix button to turn it off
	}else{
		ctlr.msgs[mess].control=key;
		ctlr.msgs[mess].matrix = false;
	}
	
	//ctlr.msgs[themess].control
}

function ctlout(){
	var a = arrayfromargs(arguments);
	if(a.length==1){
		a=a[0];
	}
	var keyout = a[0];
	var valout = a[1];
	//debug('ctlout', keyout, valout);
	mod.Send('receive_translation', keyout, 'value', valout);
	
}


//MIDI handling:
//*******************************************************************************************
// parse midi data direct from "midiin" object:
var issysex = 0;
//if cc data is coming in from the controller, 
//we don't want to mirror it back to the controller - 
//it's redundant and possibly causes action problems on encoders
var midigate = 1; 

function msg_int(v){
	if(issysex==0){
		midigate = 1; //is closed only by cc messages
		if(v>=128 && v<=143){ 
			miditype = 7; //notes off <noteID&ch,note#,vel>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=144 && v<=159){ 
			miditype = 1; //notes <noteID&ch,note#,vel>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=160 && v<=175){
			miditype = 2; //after(poly)touch <polyID&ch,note#,val>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=176 && v<=191){
			miditype = 3; //ctlr <ctlID&ch, cc#, val>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=192 && v<=207){ 
			miditype = 4; //pgm ch <pgmID&ch,val>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=208 && v<=223){
			miditype = 5; //ch. pressure <chprID&ch, val>
			counter = 0;
			midichunk = new Array();
		}
		if(v>=224 && v<=239){
			miditype = 6; //pitch bend <pbID&ch, msb, lsb>
			counter = 0;
			midichunk = new Array();
		}
	}
	if(v==240){
		issysex = 1;
	}
	if(v==247){
		issysex = 0;
	}

	switch(miditype){
		case 1: //note ON
			midichunk[counter] = v;
			if (counter==2) toctl(midichunk[0],midichunk[1],midichunk[2]);
			counter++;
		break;
		
		case 2: //after(poly)touch
			 midichunk[counter] = v;
			if (counter==2) toctl(midichunk[0],midichunk[1],midichunk[2]);
			counter++;
		break;
		
		case 3: //cc
			midigate = mgate; //close the gate so cc data isn't mirrored back. 
			midichunk[counter] = v;
			if (counter==2) {
				toctl(midichunk[0],midichunk[1],midichunk[2]);
				//all notes off m.messages use CC# 123
				midigate = 1; //open it back up now that we are done processing this cc.
				if(midichunk[1]==123 && midichunk[2]==0) allnotesoff();
			}
			counter++;
		break;
		
		case 4: //pgm changes
			 midichunk[counter] = v;
			if (counter==1) toctl(midichunk[0],midichunk[1]);
			counter++;
		break;
		
		case 5: //ch. pressure
			 midichunk[counter] = v;
			if (counter==1) toctl(midichunk[0],midichunk[1]);
			counter++;
		break;
		
		case 6://pitch bend
			midichunk[counter] = v;
			if (counter==2) toctl(midichunk[0],midichunk[1],midichunk[2]);
			counter++;
		break;
		
		case 7: //note OFF - converted to noteon, vel=0 with the "+16" for matching purposes
			midichunk[counter] = v;
			if (counter==2)
				toctl(midichunk[0]+16,midichunk[1],0);
			counter++;
		break;

	}
}

//turn midi into key/value pair
function toctl(){
	var key,value;
	var a = arrayfromargs(arguments);
	if(a.length == 3){
		key = a[0] | (a[1] << 8);
		value = a[2];
	}else{
		key = a[0];
		value = a[1];
	} 
	ctl(key,value);
}


////////////////////////////////////////////
//chainmutes


//provides chain mute controls for the drum rack by linking to the chain active in the API
//assumes we are communicating with pattr objects called "chainmute[<n>]"

var mutes = new Array();
mutes.length = 16;
var pnames = new Object();
var values = new Array();
var initpath = 'this_device canonical_parent devices 1 chains 0'; //first drum pad
var padsToChain = [12,13,14,15,8,9,10,11,4,5,6,7,0,1,2,3]; //we need to map the pad#s to chain number in a weird way
//path live_set tracks 0 devices 1 chains <pad#>

function setup_mutes(){
	//debug("linking to chain mutes");
	if(!SYNTH)
	{
		for(var i=0;i<mutes.length;i++)
		{
			mutes[i]=new LiveAPI(mutes_callback);
			initpath = 'this_device canonical_parent devices 1 chains '+padsToChain[i];
			mutes[i].path = initpath;
			var thename = "chainmute["+i+"]";
			mutes[i].name = thename;
			pnames[thename]=i; //associate the index from name;
			//watch:
			mutes[i].property = "mute";
		}
	}
}

function update_mute(p,v){
	//get the index that the parameter name corresponds to:
	var i = pnames[p];
	if(i>=0){
		if(mutes[i].id==0)
		{
			mutes[i].goto('this_device', 'canonical_parent', 'devices', 1, 'chains', padsToChain[i]);
			mutes[i].property = 'mute';
		}
		mutes[i].set("mute",v);
	}
}

function mutes_callback(args){
	//debug("callback arrived from", this, ":", args);
	if (this.name && args[0]=="mute"){
		var sendto = this.patcher.getnamed(this.name);
		sendto.message(args[1]);
	}
}

function gitprop(prop){
	for(var i=0;i<mutes.length;i++){
		var got=mutes[i].get(prop);
	}
}


///////////////////////////////////////////
//lividsteppr_lcd

var LiveClassNames = [
'InstrumentGroupDevice', 'DrumGroupDevice', 'Operator', 
'UltraAnalog', 'OriginalSimpler', 'MultiSampler', 'LoungeLizard', 'StringStudio', 
'Collision', 'InstrumentImpulse'
];

/*///////////////////////////
//	   Device Component	   //
//		  and LCD		   //
///////////////////////////*/


var finder;
var pns=[];
var mps=[];
var found_device = 0;
var params = [];
var dials = [];
var global_offset = 36
var stepseq;
var chain = -1;
var seq = 0;
var repeats = [];
var grooves = [];
var randoms = [];

var Encoders = ['Encoder_0', 'Encoder_1', 'Encoder_2', 'Encoder_3', 'Encoder_4', 'Encoder_5', 'Encoder_6', 'Encoder_7', 'Encoder_8', 'Encoder_9', 'Encoder_10', 'Encoder_11'];

var Warning = ['No device', 'was found.', 'Place a', 'DrumRack', 'next to', 'this mod', 'and press', '\"Detect',	'DrumRack\"', 'to', 'get', 'started.', ' '];
var ChainNumbers = {0:12, 1:13, 2:14, 3:15, 4:8, 5:9, 6:10, 7:11, 8:4, 9:5, 10:6, 11:7, 12:0, 13:1, 14:2, 15:3}; 
// called from init

function callback(){};

function init_device()
{
	mod.Send('receive_device', 'set_mod_device_type', type);
	mod.Send('receive_device', 'set_number_params', 12);
	for(var dev_type in DEVICE_BANKS)
	{
		for(var bank_num in DEVICE_BANKS[dev_type])
		{
			mod.SendDirect('receive_device_proxy', 'set_bank_dict_entry', dev_type, bank_num, DEVICE_BANKS[dev_type][bank_num]);
		}
		//mod.Send('receive_device_proxy', 'update_parameters');
	}
	found_device = 0;
	stepseq = this.patcher.getnamed('stepseq');
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
		dials[Encoders[i+8]]=this.patcher.getnamed(Dials[i]);
		debug('setting dial:', Encoders[i+8], this.patcher.getnamed(Dials[i]), Dials[i]);
		dials[Encoders[i+8]].message('set', 0);
	}
	if(SYNTH)
	{
		for(var i=0;i<16;i++)
		{
			repeats[ChainNumbers[i]] = this.patcher.getnamed('sequence[0]').subpatcher().getnamed('RepeatRate');
			grooves[ChainNumbers[i]] = this.patcher.getnamed('sequence[0]').subpatcher().getnamed('groove');
			randoms[ChainNumbers[i]] = this.patcher.getnamed('sequence[0]').subpatcher().getnamed('RandomWeight');
		}
	}	
	else
	{
		for(var i=0;i<16;i++)
		{
			repeats[ChainNumbers[i]] = this.patcher.getnamed('sequence['+i+']').subpatcher().getnamed('RepeatRate');
			grooves[ChainNumbers[i]] = this.patcher.getnamed('sequence['+i+']').subpatcher().getnamed('groove');
			randoms[ChainNumbers[i]] = this.patcher.getnamed('sequence['+i+']').subpatcher().getnamed('RandomWeight');
		}
	}
	live = 1;
	/*if(!SYNTH)
	{
		detect_devices();
	}
	else
	{
		_detect_devices();
	}*/
	detect_devices();
}

/*
//find the drumrack
function detect_devices()
{
	//setup the initial API path:
	found_device = 0;
	finder.goto('this_device');
	var this_id = parseInt(finder.id);
	finder.goto('canonical_parent');
	var track_id = parseInt(finder.id);
	var devices = finder.getcount('devices');
	for (var i=0;i<devices;i++)
	{
		finder.id = track_id;
		finder.goto('devices', i);
		if(finder.get('class_name')=='DrumGroupDevice')
		{
			debug("DrumRack found", finder.get('name'));
			found_device = parseInt(finder.id);
			break;
		}
	}
	if(found_device == 0)
	{
		showerror();
	}
	else
	{
		finder.id = found_device;
		debug('chains:', finder.getcount('chains'));
		if(finder.getcount('chains')<16)
		{
			showCountError();
		}
		else
		{
			hideerror();
		}
		report_drumrack_id();
	}
}

//find the synth
function _detect_devices()
{
	//setup the initial API path:
	found_device = 0;
	finder.goto('this_device');
	var this_id = parseInt(finder.id);
	finder.goto('canonical_parent');
	var track_id = parseInt(finder.id);
	var devices = finder.getcount('devices');
	for (var i=0;i<devices;i++)
	{
		finder.id = track_id;
		finder.goto('devices', i);
		if(parseInt(finder.id)!=this_id)
		{
			var found = 0;
			for(var j in LiveClassNames)
			{
				if(finder.get('class_name')==LiveClassNames[j])
				{
					found = 1;
					break;
				}
			}
			if(found>0)
			{
				debug("Synth found");
				found_device = parseInt(finder.id);
			}
		}
	}
	if(found_device == 0)
	{
		showerror();
	}
	else
	{
		hideerror();
		report_drumrack_id();
	}
}
*/

//sort calls to the internal LCD
function lcd(obj, type, val)
{
	if(live > 0)
	{
		//debuglcd('lcd', obj, type, val, '\n');}
		if(val==undefined)
		{
			val = '_';
		}
		switch(type)
		{
			case 'lcd_name':
				pns[obj].message('text', val.replace(/_/g, ' '));
				break;
			case 'lcd_value':
				mps[obj].message('text', val.replace(/_/g, ' '));
				break;
			case 'encoder_value':
				if(params[obj]!=undefined)
				{
					params[obj].message('set', val);
				}
				break;
			case 'check':
				detect_devices();
				break;
		}
	}
}

//distribute gui knobs to their destinations
function encoder(num, val)
{
	debug('encoder in', num, val, '\n');
	var seq = ChainNumbers[selected_sequence_number];
	if(live>0)
	{
		if(num<8)
		{
			mod.Send('receive_device', 'set_mod_parameter_value', num, val);
		}				 
		else
		{
			switch(num)
			{
				case 8:
					repeats[seq].message('int', val);
					break;
				case 9:
					grooves[seq].message('float', val);
					break;
				case 10:
					randoms[seq].message('float', val);
					break;
				case 11:
					break;
			}
		}
	}			 
}

//send the drumrack id to mod.js
/*
function report_drumrack_id()
{
	if(SYNTH==0)
	{
		//mod.Send('set_device_parent', found_device);
		mod.Send('send_explicit', 'receive_device', 'set_mod_device_parent', 'id', found_device);
		select_chain(chain);
	}
	else
	{
		mod.Send('send_explicit', 'receive_device', 'set_mod_device', 'id', found_device);
		//mod.Send('set_device', found_device);
	}
}
*/

//send the current chain assignment to mod.js
function select_chain(chain_num)
{
	debug('select_chain', chain_num);
	var a = this.patcher.getnamed('GRID').getvalueof();
	seq = ChainNumbers[a[0] + (a[1]*4)];
	debug('new seq =', seq);
	if(live>0)
	{
		//mod.Send('set_device_chain', Math.max(0, Math.min(chain_num + global_offset, 127)));
		//mod.Send('send_explicit', 'receive_device', 'set_mod_device_parent', 'id', devices[selected.channel]);
		if(!SYNTH){
			mod.Send('receive_device', 'set_mod_drum_pad', chain_num + 36);
			//mod.Send('receive_device', 'set_mod_device_chain', Math.max(0, Math.min(chain_num + global_offset, 127)));
		}
		dials.Encoder_8.message('set', repeats[seq].getvalueof());
		dials.Encoder_9.message('set', grooves[seq].getvalueof());
		dials.Encoder_10.message('set', randoms[seq].getvalueof());
	}
}

//Used for UI warning. Assumes you have something with a scripting name "errorui"
function showerror()
{
	error_button = this.patcher.getnamed('errorui');
	pns.device_name.message('text', ' ');
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]].message('text', ' ');
	}
	error_button.message("text",error_text);
	error_button.message('presentation', 1);
	error_button.message('presentation_rect',error_rect);
	post("\ne2API: Step\:r - Instrument not properly configured by user.");
}

function showCountError()
{
	error_button = this.patcher.getnamed('errorui');
	pns.device_name.message('text', ' ');
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]].message('text', ' ');
	}
	error_button.message("text",count_error_text);
	error_button.message('presentation', 1);
	error_button.message('presentation_rect',error_rect);
	post("\ne2API: Step\:r - Instrument not properly configured by user.");
}
	
function hideerror()
{
	error_button = this.patcher.getnamed('errorui');
	pns.device_name.message('text', ' ');
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]].message('text', ' ');
	}
	error_button.message('presentation', 0);
}

function anything(){}

function api_links(num)
{
	debug('chain num', num);
	if(num != chain){
		chain = num;
		select_chain(num);
	}
}

function update_lcd()
{
	var args = arrayfromargs(arguments);
	debug('update', args);
	api_links(chain);
}

//if(SYNTH){script.detect_devices = script._detect_devices;}

function mask()
{
	var args = arrayfromargs(arguments);
	debug('mask', args);
	switch(args[0])
	{
		case 'key':
			mod.Send('receive_translation', args[1]<16 ? 'keys_'+(args[1]%16) : 'keys2_'+(args[1]%16), 'mask', args[2]);
			break;
		case 'grid':
			mod.Send('receive_translation', 'pads_'+(args[1] + (args[2]*4)), args[3]);
			break;
	}
}

forceload(this);


//notelock

