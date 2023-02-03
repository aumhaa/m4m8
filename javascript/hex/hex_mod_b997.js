//Hexadecimal
//by amounra
//aumhaa@gmail.com --- http://www.aumhaa.com


/*This patch is the evolution of the binary mod;  The majority of the functionality for the entire patch
can be modified in this js or the accompanying poly~ object, "steppr_wheel", without ever opening
the actual containing patch in the m4l editor (this was crucial for speeding up the development process).
Because of this, the functionality of the patch can be radically altered merely by modifying the
poly~ or adding some lines of code in to this js.  As an example, the poly~ used as the base for
this patch is only a slightly modified version of the "binary" mod (from Monomodular), and the
majority of processes in this script are maintained between both versions.*/

/*It should be noted that many of the processes used in "binary" are still available yet unused
in this script, offering some excellent prospects for the future development of this mod.*/

autowatch = 1;

outlets = 4;
inlets = 5;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);

var NEW_DEBUG = false;
var DEBUG_LCD = false;
var DEBUG_PTR = false;
var DEBUG_STEP = false;
var DEBUG_BLINK = false;
var DEBUG_REC = false;
var DEBUG_LOCK = false;
var DEBUGANYTHING = false;
var SHOW_POLYSELECTOR = false;
var SHOW_STORAGE = false;


var newdebug = (NEW_DEBUG&&Debug) ? Debug : function(){};
var debuglcd = (DEBUG_LCD&&Debug) ? Debug : function(){};
var debugptr = (DEBUG_PTR&&Debug) ? Debug :function(){};
var debugstep = (DEBUG_STEP&&Debug) ? Debug : function(){};
var debugblink = (DEBUG_BLINK&&Debug) ? Debug : function(){};
var debugrec = (DEBUG_REC&&Debug) ? Debug : function(){};
var debuganything = (DEBUGANYTHING&&Debug) ? Debug : function(){};

var forceload = (FORCELOAD&&Forceload) ? Forceload : function(){};

var finder;
var mod;
var mod_finder;

var unique = jsarguments[1];

//this array contains the scripting names of objects in the top level patcher.	To include an new object to be addressed
//in this script, it's only necessary to add its name to this array.  It can then be addressed as a direct variable
var Vars = ['poly', 'pipe', 'selected_filter', 'step', 'storepattr', 'storage', 'preset_selector', 'padgui', 'padmodegui', 'keygui', 'keymodegui', 'repeatgui',
			'rotleftgui', 'rotrightgui', 'notevaluesgui', 'notetypegui', 'stepmodegui', 'keymodeadv', 'Groove', 'Random', 'Channel', 'Mode', 'PolyOffset', 'BaseTime',
			'timeupgui', 'timedngui', 'pitchupgui', 'pitchdngui', 'transposegui', 'playgui', 'recgui', 'directiongui', 'lockgui','lockgui', 'Speed',
			'Speed1', 'Speed2', 'Speed3', 'Speed4', 'Speed5', 'Speed6', 'Speed7', 'Speed8', 'Speed9', 'Speed10', 'Speed11', 'Speed12', 'Speed13', 'Speed14', 'Speed15', 'Speed16',
			'Adjust1', 'Adjust2', 'Adjust3', 'Adjust4', 'Adjust5', 'Adjust6', 'Adjust7', 'Adjust8', 'Adjust9', 'Adjust10', 'Adjust11', 'Adjust12', 'Adjust13', 'Adjust14', 'Adjust15', 'Adjust16',
			'rotgate', 'transport_change', 'midiout'];

//this array contains the scripting names of pattr-linked objects in each of the polys. To include an new object to be addressed
//in the poly, it's only necessary to add its name to this array.  It can then be addressed as part[poly number].obj[its scripting name]
var Objs = {'pattern':{'Name':'pattern', 'Type':'list', 'pattr':'pattern'},
			'duration':{'Name':'duration', 'Type':'list', 'pattr':'duration'},
			'velocity':{'Name':'velocity', 'Type':'list', 'pattr':'velocity'},
			'note':{'Name':'note', 'Type':'list', 'pattr':'note'},
			'behavior':{'Name':'behavior', 'Type':'list', 'pattr':'behavior'},
			'rulebends':{'Name':'rulebends', 'Type':'list', 'pattr':'rulebends'},
			'mode':{'Name':'mode', 'Type':'int', 'pattr':'mode'},
			'polyenable':{'Name':'polyenable', 'Type':'int', 'pattr':'polyenable'},
			'swing':{'Name':'swing', 'Type':'float', 'pattr':'swingpattr'},
			'steps':{'Name':'steps', 'Type':'int', 'pattr':'stepspattr'},
			'channel':{'Name':'channel', 'Type':'int', 'pattr':'hidden'},
			'direction':{'Name':'direction', 'Type':'int', 'pattr':'directionpattr'},
			'nudge':{'Name':'nudge', 'Type':'int', 'pattr':'nudgepattr'},
			'noteoffset':{'Name':'noteoffset', 'Type':'int', 'pattr':'hidden'},
			'random':{'Name':'random', 'Type':'float', 'pattr':'randompattr'},
			'polyoffset':{'Name':'polyoffset', 'Type':'int', 'pattr':'polyoffsetpattr'},
			'repeatenable':{'Name':'repeatenable', 'Type':'int', 'pattr':'object'},
			'polyplay':{'Name':'polyplay', 'Type':'int', 'pattr':'object'},
			'notevalues':{'Name':'notevalues', 'Type':'int', 'pattr':'notevaluepattr'},
			'notetype':{'Name':'notetype', 'Type':'int', 'pattr':'notetypepattr'},
			'quantize':{'Name':'quantize', 'Type':'int', 'pattr':'hidden'},
			'active':{'Name':'active', 'Type':'int', 'pattr':'active'},
			'offset':{'Name':'offset', 'Type':'int', 'pattr':'hidden'},
			'addnote':{'Name':'addnote', 'Type':'int', 'pattr':'object'},
			'patterncoll':{'Name':'patterncoll', 'Type':'list', 'pattr':'object'},
			'last_trigger':{'Name':'last_trigger', 'Type':'bang', 'pattr':'object'},
			'clutch':{'Name':'clutch', 'Type':'int', 'pattr':'object'},
			'restart':{'Name':'restart', 'Type':'bang', 'pattr':'object'},
			'repeat':{'Name':'repeat', 'Type':'int', 'pattr':'hidden'},
			'restartcount':{'Name':'restartcount', 'Type':'int', 'pattr':'object'},
			'basetime':{'Name':'basetime', 'Type':'int', 'pattr':'basetimepattr'},
			'timedivisor':{'Name':'timedivisor', 'Type':'int', 'pattr':'timedivisorpattr'},
			'nexttime':{'Name':'nexttime', 'Type':'set', 'pattr':'object'},
			'behavior_enable':{'Name':'behavior_enable', 'Type':'int', 'pattr':'hidden'},
			'resync':{'Name':'resync', 'Type':'bang', 'pattr':'object'},
			};

/*			'phasor':{'Name':'phasor', 'Type':'float', 'pattr':'object'},
			'phasor_free':{'Name':'phasor_free', 'Type':'float', 'pattr':'object'},
			'ticks':{'Name':'ticks', 'Type':'float', 'pattr':'hidden'},
*/


var HEX_SPEED_1 = ['ModDevice_Speed1', 'ModDevice_Speed2', 'ModDevice_Speed3', 'ModDevice_Speed4', 'ModDevice_Speed5', 'ModDevice_Speed6', 'ModDevice_Speed7', 'ModDevice_Speed8', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3']
var HEX_SPEED_2 = ['ModDevice_Speed9', 'ModDevice_Speed10', 'ModDevice_Speed11', 'ModDevice_Speed12', 'ModDevice_Speed13', 'ModDevice_Speed14', 'ModDevice_Speed15', 'ModDevice_Speed16', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3']
var HEX_BANKS = {'InstrumentGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'DrumGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'MidiEffectGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'Other':[['None', 'None', 'None', 'None', 'None', 'None', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['None', 'None', 'None', 'None', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'Operator':[['Osc-A Level', 'Osc-B Level', 'Osc-C Level', 'Osc-D Level', 'Transpose', 'Filter Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime','Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Osc-A Level', 'Osc-B Level', 'Osc-C Level', 'Osc-D Level', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'UltraAnalog':[['AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'OSC1 Semi', 'F1 Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'OriginalSimpler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'MultiSampler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'LoungeLizard':[['M Force', 'F Release', 'F Tone Decay', 'F Tone Vol', 'Semitone', 'P Distance', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['M Force', 'F Release', 'F Tone Decay', 'F Tone Vol', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'StringStudio':[['E Pos', 'Exc ForceMassProt', 'Exc FricStiff', 'Exc Velocity', 'Semitone', 'Filter Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['E Pos', 'Exc ForceMassProt', 'Exc FricStiff', 'Exc Velocity', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'Collision':[['Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release', 'Res 1 Tune', 'Res 1 Brightness', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'InstrumentImpulse':[['1 Start', '1 Envelope Decay', '1 Stretch Factor', 'Global Time', 'Global Transpose', '1 Filter Freq', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime','Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['1 Start', '1 Envelope Decay', '1 Stretch Factor', 'Global Time', 'ModDevice_PolyOffset', 'ModDevice_Mode', 'ModDevice_Speed', 'Mod_Chain_Vol', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2],
			'NoDevice':[['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTimev','Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'ModDevice_Channel', 'ModDevice_Groove', 'ModDevice_Random', 'ModDevice_BaseTime', 'Mod_Chain_Send_0', 'Mod_Chain_Send_1', 'Mod_Chain_Send_2', 'Mod_Chain_Send_3'], HEX_SPEED_1, HEX_SPEED_2]}

var CODEC_HEX_SPEED = ['ModDevice_Speed1', 'ModDevice_Speed2', 'ModDevice_Speed3', 'ModDevice_Speed4', 'ModDevice_Speed5', 'ModDevice_Speed6', 'ModDevice_Speed7', 'ModDevice_Speed8', 'ModDevice_Speed9', 'ModDevice_Speed10', 'ModDevice_Speed11', 'ModDevice_Speed12', 'ModDevice_Speed13', 'ModDevice_Speed14', 'ModDevice_Speed15', 'ModDevice_Speed16', 'ModDevice_Adjust1', 'ModDevice_Adjust2', 'ModDevice_Adjust3', 'ModDevice_Adjust4', 'ModDevice_Adjust5', 'ModDevice_Adjust6', 'ModDevice_Adjust7', 'ModDevice_Adjust8', 'ModDevice_Adjust9', 'ModDevice_Adjust10', 'ModDevice_Adjust11', 'ModDevice_Adjust12', 'ModDevice_Adjust13', 'ModDevice_Adjust14', 'ModDevice_Adjust15', 'ModDevice_Adjust16'];
var CODEC_HEX_BANKS = {'NoDevice':[CODEC_HEX_SPEED, CODEC_HEX_SPEED],
						'Other':[CODEC_HEX_SPEED, CODEC_HEX_SPEED]};

var Modes=[4, 2, 3, 5, 1];
var RemotePModes=[0, 1, 4];
var Funcs = ['stepNote', 'stepVel', 'stepDur', 'stepExtra1', 'stepExtra2'];
var default_pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var default_step_pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var default_duration = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var default_note = [[1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]];
var default_velocity = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100];
var empty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var modes = [[0, 2, 4, 5, 7, 9, 11, 12], [0, 2, 3, 5, 7, 9, 10, 12], [0, 1, 3, 5, 7, 8, 10, 12], [0, 2, 4, 6, 7, 9, 11, 12], [0, 2, 4, 5, 7, 9, 10, 12], [0, 2, 3, 5, 7, 8, 10, 12], [0, 1, 3, 5, 6, 8, 10, 12]];
var Colors = [0, 1, 2, 3, 4, 5, 6, 127];
var StepColors = [127, 3, 3, 3, 127, 3, 3, 3, 127, 3, 3, 3, 127, 3, 3, 3 ];
var SelectColors = [1, 5, 4, 6];
var AddColors = [5, 6];
var Blinks=[-1, 2];
var modColor = 5;
var TVEL_COLORS = [1,2,3,4];
var BEHAVE_COLORS = [0, 1, 2, 3, 4, 5, 6, 127];
var TIMES = {'1':0, '2':1, '4':2, '8':3, '16':4, '32':5, '64':6, '128':7};
var ACCENTS = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4];
var ACCENT_VALS = [63, 87, 111, 127];
var TRANS = {0:[[1, 1], [1, 2], [1, 4], [1, 8], [1, 16], [1, 32], [1, 64], [1, 128]],
				1:[[3, 2], [3, 4], [3, 8], [3, 16], [3, 32], [3, 64], [3, 128], [1, 128]],
				2:[[2, 3], [1, 3], [1, 6], [1, 12], [1, 24], [1, 48], [1, 96], [1, 128]]};
var ENC_COLORS = [5, 5, 127, 127, 6, 1, 2, 2];
var MODE_COLORS = [2, 5, 1, 3, 6, 4, 7, 2];

/*Naming the js instance as script allows us to create scoped variables
(properties of js.this) without specifically declaring them with var
during the course of the session. This allows dynamic creation of
objects without worrying about declaring them beforehand as globals
presumably gc() should be able to do its job when the patch closes, or
if the variables are redclared.	 I'd love to know if this works the
way I think it does.*/

var script = this;
var autoclip;

var part =[];

//var live_set;
//var song_tempo = 120;

var KEYMODES = ['mute', 'length', 'behaviour', 'single preset', 'global preset', 'polyrec', 'polyplay', 'accent'];
var PADMODES = ['select', 'add', 'mute', 'preset', 'global', 'freewheel', 'play'];
var STEPMODES = ['active', 'velocity', 'duration', 'rulebends', 'pitch'];
var GRIDMODES = ['hex', 'tr256', 'polygome', 'cafe', 'boinngg', 'none', 'none', 'behaviour'];
var CODECMODES = ['velocity', 'duration', 'behaviour', 'pitch'];

var Alive=0;
var step_mode = 0;
var pad_mode = 0;
var key_mode = 0;
var grid_mode = 0;
var codec_mode = 0;
var solo_mode = 0;
var last_mode = 1;
var last_key_mode = 0;
var last_pad_mode = 0;
var locked = 0;
var shifted = false;
//var play_mode = 0;

var selected;
var presets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
var devices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var drumgroup_is_present = false;
var preset = 1;
var last_mask = 0;
var global_offset = 0;
var global_chain_offset = 0;
var pad_invoked_key_mode = 3;
var timing_immediate = 0;
var transpose_steps = 1;
var record_enabled = 0;
var play_enabled = 0;
var randomize_global = 0;
var last_blink = 0;
var rot_length = 4;
var step_value = [];
var key_pressed = -1;
var pad_pressed = -1;
var grid_pressed = -1;
var current_step = 0;
var autoclip;
var dirty = 0;
var keymodeenables = [0, 1, 2, 3, 4, 5, 6, 7];
var padmodeenables = [0, 1, 2, 3, 4, 5];

//new props
var sel_vel = 0;
var altVal = 0;
var ColNOTE = 1;
var RowNOTE = 2;
var curSteps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var edit_preset = 1;
var btn_press1 = 0;
var btn_press2 = 0;
var last_mutes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
var boing_pattern = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var Tvel = 2;
var rec_enabled = 0;
var behavegraph = [];
for(var i=0;i<7;i++){
	behavegraph[i]=[];
	for(var j=0;j<8;j++){
		behavegraph[i][j]=0;
	}
}

var current_rule = 0;
var handlers = [];
var codec_handler = false;

// var Protos = require('_deprecated_protos');
//var ButtonClass = require('ButtonClass');
//include('protos');

var controlRegistry = new ControlRegistry();
debug('controlRegistry is:', controlRegistry);
var buttonControls = [];
for(var x=0;x<16;x++)
{
	buttonControls[x] = [];
	for(var y=0;y<16;y++)
	{
		var id = x+(y*16);
		buttonControls[x][y] = new ButtonClass(id, 'Button_'+id);
		controlRegistry.register_control(id, buttonControls[x][y]);
	}
}

/*/////////////////////////////////////////
///// script initialization routines //////
/////////////////////////////////////////*/


/*	VERY IMPORTANT!! : This code utilizes a naming convention for private functions:  any function
preceeded by an underscore is considered private, but will have a public function reference
assigned to it AFTER the script has received an initiallization call from mod.js.  That means that any
function that shouldn't be accessed before initialization can be created as a private function without
the need to use an internal testing routine to find out whether the script has init()ed.

Example:

If we create _private_function(), and before init a call from max comes in to private_function(), that call
will be funneled to anything().	 After init(), however, all calls to private_function() will be forwarded to
_private_function().

Note:  It is best to only address these private functions by their actual names in the script, since calling aliased
names will not be routed to anything().*/

var Mod = ModComponent.bind(script);

function init()
{
	mod = new Mod(script, 'hex', unique, false);
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
			//debug(script[args[1]]);
			script[args[1]].apply(script, args.slice(2));
		}
		if(args[1]=='disconnect')
		{
			mod.restart.schedule(3000);
		}
	}
}

function active_handlers()
{
	handlers = arrayfromargs(arguments);
	codec_handler = false;
	for(var i in handlers)
	{
		if(handlers[i]=='CodecModHandler')
		{
			codec_handler = true;
		}
	}
}

function alive(val)
{
	initialize(val);
}


//called when mod.js is finished loading for the first time
function initialize(val)
{
	if(val>0)
	{
		debug('hex init\n');
		setup_translations();
		setup_colors();
		for(var i in Vars)
		{
			script[Vars[i]] = this.patcher.getnamed(Vars[i]);
		}
		var y=15;do{
			script['poly.'+(y+1)+'::pattern'] = make_pset_edit_input(y);
			script['poly.'+(y+1)+'::velocity'] = make_tvel_edit_input(y);
		}while(y--);
		for(var i = 0; i < 16; i++)
		{
			var poly_num = i;
			storage.message('priorty', 'poly.'+(poly_num+1), 'tickspattr', 10);
			storage.message('priorty', 'poly.'+(poly_num+1),  'notetypepattr', 11);
			storage.message('priorty', 'poly.'+(poly_num+1),  'notevaluepattr', 12);
			part[i] = {'n': 'part', 'num':i, 'nudge':0, 'offset':0, 'channel':0, 'len':16, 'start':0,
						'jitter':0, 'active':1, 'swing':.5, 'lock':1, 'ticks':480, 'notevalues':3, 'notetype':0,
						'pushed':0, 'direction':0, 'noteoffset':i, 'root':i, 'octave':0, 'add':0, 'quantize':1, 'repeat':6, 'clutch':1,
						'random':0, 'note':i, 'steps':15, 'mode':0, 'polyenable':0, 'polyoffset':36, 'mode':0,
						'hold':0, 'held':[], 'triggered':[], 'recdirty':0, 'timedivisor':16, 'basetime':1, 'behavior_enable':1};//'speed':480,'notevalue':'4n'
			part[i].num = parseInt(i);
			part[i].pattern = default_pattern.slice();
			part[i].edit_buffer = default_pattern.slice();
			part[i].edit_velocity = default_velocity.slice();
			part[i].step_pattern = default_step_pattern.slice();
			part[i].duration = default_duration.slice();
			part[i].velocity = default_velocity.slice();
			part[i].behavior = default_pattern.slice();
			part[i].rulebends = default_pattern.slice();
			part[i].note = default_pattern.slice();
			part[i].obj = [];
			part[i].obj.set = [];
			part[i].obj.get = [];
			for(var j in Objs)
			{
				//debug(Objs[j].Name, '\n');
				part[i].obj[Objs[j].Name] = this.patcher.getnamed('poly').subpatcher(poly_num).getnamed(Objs[j].Name);
				part[i].obj.set[Objs[j].Name] = make_obj_setter(part[i], Objs[j]);
				part[i].obj.get[Objs[j].Name] = make_obj_getter(part[i], Objs[j]);
			}
			part[i].funcs = make_funcs(part[i]);
			script['Speed'+(i+1)].message('set', part[i].obj.timedivisor.getvalueof());
			//part[i].notes_assignment = part[i].obj.notes.getvalueof();
			//part[i].note = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
			//part[i].note = default_note.slice();
			//part[i].note = i;
		}
		script.rulemap = this.patcher.getnamed('settings').subpatcher().getnamed('rulemap');
		this.patcher.getnamed('poly').message('target', 0);
		selected_filter.message('offset', 1);
		autoclip = new LiveAPI(callback, 'live_set');
		step.message('int', 1);
		messnamed(unique+'restart', 1);
		transport_change.message('set', -1);
		selected = part[0];
		init_device();
		deprivatize_script_functions(this);
		//for(var i in script)
		//{
		//	if((/^_/).test(i))
		//	{
		//		debug('replacing', i, '\n');
		//		script[i.replace('_', "")] = script[i];
		//	}
		//}
		Alive = 1;
		clear_surface();

		storage.message('recall', 1);

		select_pattern(0);
		refresh_extras();

		rotgate.message('int', 1);
		messnamed(unique+'ColNOTE', ColNOTE);
		messnamed(unique+'RowNOTE', RowNOTE);
		this.patcher.getnamed('polyselector').hidden = Math.abs(SHOW_POLYSELECTOR-1);
		if(SHOW_STORAGE)
		{
			this.patcher.getnamed('storage').message('clientwindow');
			this.patcher.getnamed('storage').message('storagewindow');
		}
		change_transpose(transposegui.getvalueof());
		post("Hex initialized.\n");
		//mod.Send( 'set_mod_color', modColor);
		//mod.Send( 'set_color_map', 'Monochrome', 127, 127, 127, 15, 22, 29, 36, 43);
		//mod.Send( 'set_report_offset', 1);
		/*var i=7;do{
			mod.Send( 'key', i, (i==grid_mode)*8);
			mod.Send( 'grid', i, 6, ENC_COLORS[i]);
		}while(i--);*/
		var i=3;do{
			mod.Send( 'cntrlr_encoder_grid', 'mode', i, 2, 0);
		}while(i--);
		var i=7;do{
			mod.Send( 'code_encoder_grid', 'mode', i, 0, 4);
			mod.Send( 'code_encoder_grid', 'mode', i, 1, 4);
			mod.Send( 'code_encoder_grid', 'mode', i, 2, 5);
			mod.Send( 'code_encoder_grid', 'mode', i, 3, 5);
		}while(i--);
		//this is here because it wasn't getting called at init() with refresh_grid()
		var i=7;do{
			mod.Send( 'receive_translation', 'buttons_'+i, 'value', ENC_COLORS[i]);
		}while(i--);
	}
	else
	{
		_dissolve();
	}
	//test_things();
}

function test_cb(args){
	debug('test_cb:', args);
}

//test function used in Mod Restart Test to try and establish a listener for Modrouter's @connected property
//property is available to [live.observer], but doesn't seem to come through js for some reason.
//testpatch is modrestarttest.amxd.  040919
function test_things(){
	var finder2 = new LiveAPI(test_cb, 'live_set');
	debug('monomodular id:', mod.monomodular_id);
	finder2.id = mod.monomodular_id;
	var mods = finder2.info;
	//debug('mods:', mods);
	finder2.property = 'connected';
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
				debugptr('setter hidden', obj.Name, val, '\n');
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
					debugptr('setter bang\n');
					part[obj.Name].message('bang');
				}
			}
		}
		else
		{
			var setter = function(val)
			{
				debugptr('setter object\n');
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
				debugptr('setter pattr\n');
				var num = part.num;
				if(!pset){
					var pset = presets[num];
					part[obj.Name] = val;
					part.obj[obj.Name].message(obj.Type, val);
				}
				debug('storing', obj.Name, 'in', obj.pattr, 'at', pset, 'with', val, '\n');
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

//make a closure to hold a callback from pattrstorage to use when requesting unloaded preset data for editing in TR256
//since this is the only place we use this call, we can directly forward the data to the grid
function make_pset_edit_input(num)
{
	var pset_edit_input = function()
	{
		var args = arrayfromargs(arguments);
		part[num].edit_buffer = args;
		//post('received input', num, args, '\n');
		//var x=(args.length-1);do{
		//	mod.Send( 'grid', x, num+2, args[x]);
		//}while(x--);
	}
	return pset_edit_input
}

//make a closure to hold a callback from pattrstorage to use when requesting unloaded preset data for editing in TR256
//since this is the only place we use this call, we can directly forward the data to the grid
function make_tvel_edit_input(num)
{
	var pset_tvel_input = function()
	{
		var args = arrayfromargs(arguments);
		//post('received velocities', num, args, '\n');
		var x=(args.length-1);do{
			mod.Send( 'grid', 'value', x, num+2, part[num].edit_buffer[x]*ACCENTS[Math.floor(args[x]/8)]);
		}while(x--);
	}
	return pset_tvel_input
}

//dummy callback to compensate for api bug in Max6
function callback(){}

//called by init to initialize state of polys
function init_poly()
{
	//poly.message('target', 0);
	mod.Send( 'batch', 'c_grid', 0);
	grid_out('batch', 'grid', 0);
	for(var i=0;i<16;i++)
	{
		part[i].obj.quantize.message('int', part[i].quantize);
		part[i].obj.active.message('int', part[i].active);
		part[i].obj.swing.message('float', part[i].swing);
		part[i].obj.ticks.message(part[i].ticks);
		//part[i].obj.phasor.lock = 1;
		part[i].obj.polyenable.message('int', part[i].polyenable);
		//part[i].obj.phasor.message('float', 0);
		part[i].obj.noteoffset.message('int', (part[i].octave *12) + part[i].root);
		part[i].obj.pattern.message('list', part[i].pattern);
		part[i].obj.note.message('list', part[i].note);
		part[i].obj.velocity.message('list', part[i].velocity);
		part[i].obj.duration.message('list', part[i].duration);
		part[i].obj.notetype.message('int', part[i].notetype);
		part[i].obj.notevalues.message('int', part[i].notevalues);
		part[i].obj.channel.message('int', part[i].channel);
		part[i].obj.behavior_enable.message('int', part[i].behavior_enable);
		//update_note_pattr(part[i]);

	}
}

//called by init to initialize state of gui objects
function _clear_surface()
{
	debug('clear_surface\n');
	stepmodegui.message('int', 0);
}

//should be called on freebang, currently not implemented
function _dissolve()
{
	for(var i in script)
	{
		if((/^_/).test(i))
		{
			post('replacing', i);
			script[i.replace('_', "")] = script['anything'];
		}
	}
	Alive=0;
	post('Hex dissolved.\n');
}

///////////////////////////
/*	 display routines	 */
///////////////////////////

function setup_translations()
{
	//Notes
	/*Here we set up some translation assignments and send them to the Python ModClient.
	Each translation add_translation assignment has a name, a target, a group, and possibly some arguments.
	Translations can be enabled individually using their name/target combinations, or an entire group can be enabled en masse.
	There are not currently provisions to dynamically change translations or group assignments once they are made.*/

	/*Batch translations can be handled by creating alias controls with initial arguments so that when the batch command is sent
	the argument(s) precede the values being sent.	They are treated the same as the rest of the group regarding their
	enabled state, and calls will be ignored to them when they are disabled.  Thus, to send a column command to an address:
	'add_translation', 'alias_name', 'address', 'target_group', n.
	Then, to invoke this translation, we'd call:
	'receive_translation', 'alias_name', 'column', nn.
	This would cause all leds on the column[n] to be lit with color[nn].

	It's important to note that using batch_row/column calls will wrap to the next column/row, whereas column/row commands will
	only effect their actual physical row on the controller.*/

	//Ohm stuff:
	for(var i = 0;i < 16; i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'grid', 'ohm_pads', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys_'+i, 'grid', 'ohm_keys', i%8, (i < 8 ? 2 : 3));
		mod.Send( 'add_translation', 'keys2_'+i, 'grid', 'ohm_keys2', i%8, (i < 8 ? 4 : 5));
	}
	mod.Send( 'add_translation', 'pads_batch', 'grid', 'ohm_pads', 0);
	mod.Send( 'add_translation', 'keys_batch', 'grid', 'ohm_keys', 2);
	mod.Send( 'add_translation', 'keys_batch_fold', 'grid', 'ohm_keys', 2, 8);
	mod.Send( 'add_translation', 'keys2_batch', 'grid', 'ohm_keys2', 4);
	mod.Send( 'add_translation', 'keys2_batch_fold', 'grid', 'ohm_keys2', 4, 8);
	for(var i=0;i<8;i++)
	{
		mod.Send( 'add_translation', 'buttons_'+i, 'grid', 'ohm_buttons', i, 6);
		mod.Send( 'add_translation', 'extras_'+i, 'grid', 'ohm_extras', i, 7);
	}
	mod.Send( 'add_translation', 'buttons_batch', 'grid', 'ohm_buttons', 6);
	mod.Send( 'add_translation', 'extras_batch', 'grid', 'ohm_extras', 7);

	//Base stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'base_grid', 'base_pads', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys_'+i, 'base_grid', 'base_keys', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys2_'+i, 'base_grid', 'base_keys2', i%8, Math.floor(i/8)+2);
	}
	mod.Send( 'add_translation', 'pads_batch', 'base_grid', 'base_pads', 0);
	mod.Send( 'add_translation', 'keys_batch', 'base_grid', 'base_keys', 0);
	mod.Send( 'add_translation', 'keys_batch_fold', 'base_grid', 'base_keys', 0, 8);
	mod.Send( 'add_translation', 'keys2_batch', 'base_grid', 'base_keys2', 2);
	mod.Send( 'add_translation', 'keys2_batch_fold', 'base_grid', 'base_keys2', 2, 8);
	mod.Send( 'enable_translation_group', 'base_keys', 0);

	for(var i=0;i<8;i++)
	{
		mod.Send( 'add_translation', 'buttons_'+i, 'base_grid', 'base_buttons', i, 2);
		mod.Send( 'add_translation', 'extras_'+i, 'base_grid', 'base_extras', i, 3);
	}
	mod.Send( 'add_translation', 'buttons_batch', 'base_grid', 'base_buttons', 2);
	mod.Send( 'add_translation', 'extras_batch', 'base_grid', 'base_extras', 3);
	mod.Send( 'enable_translation_group', 'base_buttons', 0);
	mod.Send( 'enable_translation_group', 'base_extras',  0);

	//Code stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'code_grid', 'code_pads', i%8, Math.floor(i/8));
		//mod.Send( 'add_translation', 'keys_'+i, 'code_grid', 'code_keys', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys2_'+i, 'code_grid', 'code_keys2', i%8, Math.floor(i/8)+2);
	}
	mod.Send( 'add_translation', 'pads_batch', 'code_grid', 'code_pads', 0);
	//mod.Send( 'add_translation', 'keys_batch', 'code_grid', 'code_keys', 0);
	//mod.Send( 'add_translation', 'keys_batch_fold', 'code_grid', 'code_keys', 0, 8);
	mod.Send( 'add_translation', 'keys2_batch', 'code_grid', 'code_keys2', 2);
	mod.Send( 'add_translation', 'keys2_batch_fold', 'code_grid', 'code_keys', 2, 8);
	mod.Send( 'enable_translation_group', 'code_keys', 0);

	for(var i=0;i<8;i++)
	{
		mod.Send( 'add_translation', 'buttons_'+i, 'code_grid', 'code_buttons', i, 2);
		mod.Send( 'add_translation', 'extras_'+i, 'code_grid', 'code_extras', i, 3);
	}
	mod.Send( 'add_translation', 'buttons_batch', 'code_grid', 'code_buttons', 2);
	mod.Send( 'add_translation', 'extras_batch', 'code_grid', 'code_extras', 3);
	mod.Send( 'enable_translation_group', 'code_buttons', 0);
	mod.Send( 'enable_translation_group', 'code_extras',  0);

	//CNTRLR stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'cntrlr_grid', 'cntrlr_pads', i%4, Math.floor(i/4));
		mod.Send( 'add_translation', 'keys_'+i, 'cntrlr_key', 'cntrlr_keys', i, 0);
		mod.Send( 'add_translation', 'keys2_'+i, 'cntrlr_key', 'cntrlr_keys2', i, 1);
	}
	mod.Send( 'add_translation', 'pads_batch', 'cntrlr_grid', 'cntrlr_pads', 0);
	mod.Send( 'add_translation', 'keys_batch', 'cntrlr_key', 'cntrlr_keys', 0);
	mod.Send( 'add_translation', 'keys_batch_fold', 'cntrlr_key', 'cntrlr_keys', 0, 16);
	mod.Send( 'add_translation', 'keys2_batch', 'cntrlr_key', 'cntrlr_keys2', 1);
	mod.Send( 'add_translation', 'keys2_batch_fold', 'cntrlr_key', 'cntrlr_keys', 1, 16);
	for(var i=0;i<8;i++)
	{
		mod.Send( 'add_translation', 'buttons_'+i, 'cntrlr_encoder_button_grid', 'cntrlr_buttons', i);
		mod.Send( 'add_translation', 'extras_'+i, 'cntrlr_encoder_button_grid', 'cntrlr_extras', i);
	}
	mod.Send( 'add_translation', 'buttons_batch', 'cntrlr_encoder_button_grid', 'cntrlr_buttons');
	mod.Send( 'add_translation', 'extras_batch', 'cntrlr_encoder_button_grid', 'cntrlr_extras');

}

function setup_colors()
{
	mod.Send( 'fill_color_map', 'Monochrome', 0, 1, 1, 1, 8, 1);
}

function refresh_pads()
{
	debug('refresh_pads:', pad_mode, ',', PADMODES[pad_mode]);
	switch(PADMODES[pad_mode])
	{
		case 'select':
			var i=3;do{
				var j=3;do{
					var v = SelectColors[Math.floor(i+(j*4) == selected.num)];
					if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);}
					padgui.message(i, j, v);
				}while(j--);
			}while(i--);
			break;
		case 'add':
			var i=3;do{
				var j=3;do{
					var v = AddColors[Math.floor(i+(j*4) == selected.num)];
					if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);}
					padgui.message(i, j, v);
				}while(j--);
			}while(i--);
			break;
		case 'mute':
			var i=15;do{
				var v = part[i].active*2;
				if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+i, 'value', v);}
				padgui.message(i%4, Math.floor(i/4), v);
			}while(i--);
			break;
		case 'preset':
			var p = presets[selected.num]-1;
			var i=15;do{
				var v = (i==p)+3;
				if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+i, 'value', v);}
				//mod.Send( 'receive_translation', 'pads_'+i, 'value', v);
				padgui.message(i%4, Math.floor(i/4), v);
			}while(i--);
			break;
		case 'global':
			var p = presets[selected.num]-1;
			var i=15;do{
				var v = (i==p)+6;
				if(grid_mode == 0){
					mod.Send( 'receive_translation', 'pads_'+i, 'value', -1);
					mod.Send( 'receive_translation', 'pads_'+i, 'value', v);
				}
				padgui.message(i%4, Math.floor(i/4), v);
			}while(i--);
			break;
		case 'play':
			var i=15;do{
				var v=(selected.triggered.indexOf(i)>-1) + 7;
				if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+i, 'value', v);}
				padgui.message(i%4, Math.floor(i/4), v);
			}while(i--);
			break;
		case 'extra':
			var i=15;do{
				var v=(selected.triggered.indexOf(i)>-1) + 7;
				if(grid_mode == 0){ mod.Send( 'receive_tranlsation', 'pads_'+i, 'value', v);}
				padgui.message(i%4, Math.floor(i/4), v);
			}while(i--);
			break;
		case 'freewheel':
			if(selected.num<8)
			{
				var i=3;do{
					var j=3;do{
						var v = SelectColors[Math.floor(i+(j*4) == selected.num)+((j<2)*2)];
						if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);}
						padgui.message(i, j, v);
					}while(j--);
				}while(i--);
			}
			else
			{
				var i=3;do{
					var j=3;do{
						var v = SelectColors[Math.floor(i+(j*4) == selected.num)+((j>1)*2)];
						if(grid_mode == 0){ mod.Send( 'receive_translation', 'pads_'+(i+(j*4)), 'value', v);}
						padgui.message(i, j, v);
					}while(j--);
				}while(i--);
			}
			break;
	}
}

function refresh_c_keys()
{
	var pattern = [];
	var i = 15;do{
		pattern.unshift(selected.pattern[i] * StepColors[i]);
	}while(i--);
	if(grid_mode == 0){ mod.Send( 'receive_translation', 'keys2_batch_fold', 'batch_row_fold', pattern);}
	var batch = [];
	switch(KEYMODES[key_mode])
	{
		case 'length':
			var i=15;do{
				var v = (i>=part[selected.num].nudge&&i<=(part[selected.num].nudge+part[selected.num].steps))*5;
				keygui.message(i, 0, v);
				batch.unshift(v);
			}while(i--);
			if(grid_mode == 0){
				mod.Send( 'receive_translation', 'keys_batch', 'batch_mask_row', -1);
				mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);
			}
			break;
		case 'behaviour':
			var i=15;do{
				batch.unshift(Colors[part[selected.num].behavior[i]]);
				keygui.message(i, 0, selected.behavior[i]+8);
			}while(i--);
			if(grid_mode == 0){
				mod.Send( 'receive_translation', 'keys_batch', 'batch_mask_row', -1);
				mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);
			}
			break;
		case 'single preset':
			var p = presets[selected.num]-1;
			var i=15;do{
				var v = (i==p)+3;
				batch.unshift(v);
				keygui.message(i, 0, v);
			}while(i--);
			if(grid_mode == 0){
				mod.Send( 'receive_translation', 'keys_batch', 'batch_mask_row', -1);
				mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);
			}
			break;
		case 'global preset':
			var p = presets[selected.num]-1;
			var i=15;do{
				var v = (i==p)+6;
				batch.unshift(v);
				keygui.message(i, 0, v);
			}while(i--);
			if(grid_mode == 0){
				mod.Send( 'receive_translation', 'keys_batch', 'batch_mask_row', -1);
				mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);
			}
			break;
		case 'polyrec':
			var i=15;do{
				batch.unshift(4);
				keygui.message(i, 0, 4);
			}while(i--);
			if(grid_mode == 0){
				mod.Send( 'receive_translation', 'keys_batch', 'batch_mask_row', -1);
				mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);
				mod.Send( 'receive_translation', 'keys_'+i, 'mask', selected.note[current_step], 5);
			}
			break;
		case 'polyplay':
			var i=15;do{
				var v=(selected.triggered.indexOf(i)>-1) + 7;
				batch.unshift(v);
				keygui.message(i, 0, v);
			}while(i--);
			if(grid_mode == 0){ mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);}
			break;
		case 'accent':
			var i=15;do{
				var v = ACCENTS[Math.floor(selected.velocity[i]/8)];
				batch.unshift(v);
				keygui.message(i, 0, v);
			}while(i--);
			if(grid_mode == 0){ mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);}
			break;
		default:
			var i=15;do{
				var v = part[i].active*2;
				batch.unshift(v);
				keygui.message(i, 0, v);
				pattern.push(selected.pattern[i] * StepColors[i]);
			}while(i--);
			if(grid_mode == 0){ mod.Send( 'receive_translation', 'keys_batch_fold', 'batch_row_fold', batch);}
			if(codec_handler){mod.Send( 'code_encoder_grid', 'custom', selected.num%8, Math.floor(selected.num/8), selected.pattern);}
			break;
	}
}

function refresh_grid()
{
	//debug('refresh_grid\n');
	switch(GRIDMODES[grid_mode])
	{
		case 'hex':
			refresh_pads();
			refresh_c_keys();
			var i=7;do{
				mod.Send( 'receive_translation', 'buttons_'+i, 'value', ENC_COLORS[i]);
			}while(i--);
			refresh_extras();
			break;
		case 'tr256':
			var i=15;do{
				mod.Send( 'grid', 'value', i, 0, ((preset-1)==i)*((4*rec_enabled)+1));
				mod.Send( 'grid', 'value', i, 1, ((edit_preset-1)==i)*((4*rec_enabled)+1));
			}while(i--);
			break;
		case 'polygome':
			mod.Send( 'grid', 'value', 0, 0, selected.hold*7);
			//mod.Send( 'grid', 'value',0, 15, selected.hold*7);
			//mod.Send( 'grid', 'value',15, 0, selected.hold*7);
			//mod.Send( 'grid', 'value',15, 15, selected.hold*7);
			var i=7;do{
				mod.Send( 'grid', 'value', i+1, 0, presets[selected.num] == i+1 ? 1 : 0);
			}while(i--);

			break;
		case 'cafe':
			break;
		case 'boinngg':
			break;
		case 'behaviour':
			var i=7;do{
				var j=6;do{
					mod.Send( 'grid', 'value', j, i, BEHAVE_COLORS[behavegraph[j][i]]);
				}while(j--);
			}while(i--);
			var i=6;do{
					mod.Send( 'grid', 'value', 7, i, BEHAVE_COLORS[i] * Math.floor(i==current_rule));
			}while(i--);
			break;
	}
}

function refresh_keys()
{
	if(!alt)
	{
		var x=7;do{
			mod.Send( 'key', 'value', x, (x==grid_mode)*8);
		}while(x--);
	}
	else
	{
		var i=3;do{
			mod.Send( 'key', 'value', i, (i==(Tvel))*(TVEL_COLORS[i]));
		}while(i--);
	}
}

function refresh_extras()
{
	if(grid_mode == 0){
		var i=7;do{
			mod.Send( 'receive_translation', 'extras_'+i, 'value', MODE_COLORS[i]+(7*(i==key_mode)));
		}while(i--);
	}
}

function refresh_adjusters()
{
	switch(STEPMODES[step_mode])
	{
		case 'rulebends':
			var i=15;do{
				script['Adjust'+(i+1)].message('set', selected.rulebends[i]*8);
			}while(i--);
			break;
		case 'duration':
			var i=15;do{
				script['Adjust'+(i+1)].message('set', selected.duration[i]*16);
			}while(i--);
			break;
		case 'velocity':
			var i=15;do{
				script['Adjust'+(i+1)].message('set', selected.velocity[i]);
			}while(i--);
			break;
	}
}

function refresh_code_buttons()
{
	var i=2;do{
		mod.Send('code_button', 'value', i+1, ((i+1)==step_mode) * 64);
	}while(i--);
}

function grid_out(){}

function base_grid_out(){}

/*/////////////////////////////////
///// api callbacks and input /////
/////////////////////////////////*/

//catch old calls that should be changed
function grid_in(x, y, val)
{
	debug('grid in: shouldnt happen::', x, y, val);
}

function key_in(num, val)
{
	debug('key in: shouldnt happen::', num, val);
}

function button_in(x, y, val)
{
	debug('button in: shouldnt happen::', x, y, val);
}

//main input sorter for calls from mod.js
function anything()
{
	var args = arrayfromargs(arguments);
	if(DEBUGANYTHING){post('anything', messagename, arguments, '\n');}
	switch(messagename)
	{
		case 'settingsgui':
			switch(args[0])
			{
				case 0:
					pad_invoked_key_mode = args[1];
					break;
				case 1:
					timing_immediate = args[1];
					break;
				case 2:
					global_chain_offset = args[1];
					break;
				case 4:
					transpose_steps = args[1];
					break;
				case 14:
					vals = args.slice(1, 9);
					keymodeenables = [];
					for(var i=0;i<8;i++)
					{
						if(vals[i])
						{
							keymodeenables.push(i);
						}
					}
					debug('keymodeenables', keymodeenables, '\n');
					break;
				case 15:
					vals = args.slice(1, 8);
					padmodeenables = args.slice(1, 8);
					padmodeenables = [];
					for(var i=0;i<7;i++)
					{
						if(vals[i])
						{
							padmodeenables.push(i);
						}
					}
					debug('padmodeenables', padmodeenables, '\n');
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
					global_offset = (Math.max(Math.min(args[1], 96), 0));
					break;
				case 14:
					locked = args[1];
					break;
			}
			break;
		default:
			debug('anything', messagename, args, '\n');
			break;
	}
}

var _cntrlr_encoder_button_grid = _c_button;
function _c_button(x, y, val)
{
	debug('button_in', x, y, val, '\n');
	switch(y)
	{
		//top row
		case 0:
			switch(x)
			{
				//time slower, change note type
				case 0:
					if(pad_pressed<0){
						if(selected.lock==0){
							change_lock_status(selected, 0);
						}
						else{
							timedngui.message('int', val);
						}
					}
					else if(val>0){
						notetypegui.message('int', Math.max(0, Math.min(selected.notetype+1, 3)));
					}
					break;
				//time faster, change note type
				case 1:
					if(pad_pressed<0){
						if(selected.lock==0){
							change_lock_status(selected, 1);
						}
						else{
							timeupgui.message('int', val);
						}
					}
					else if(val>0){
						notetypegui.message('int', Math.max(0, Math.min(selected.notetype-1, 3)));
					}
					break;
				//pitch down, resync_single
				case 2:
					if(pad_pressed<0){
						pitchdngui.message('int', val);
					}
					else if(val>0){
						//recgui.message('bang');
						resync_single(selected);
					}
					break;
				//pitch up, resync
				case 3:
					if(pad_pressed<0){
					pitchupgui.message('int', val);
					}
					else if(val>0){
						//playgui.message('bang');
						resync();
					}
					break;
			}
			break;
		//second row
		case 1:
			switch(x)
			{
				//pad cycle
				case 0:
					/*if((pad_mode!=6)&&(key_mode!=6))
					{
						if(pad_pressed<0){
							repeatgui.message('int', val);
						}
						else if(val>0){
							directiongui.message('int', (selected.direction+1)%3);
						}
					}
					else
					{
						//post('pad mode is 6\n');
						if(val>0)
						{
							selected.hold = Math.abs(selected.hold-1);
							//post('val is > 0, selected.hold ==', selected.hold, '\n');
							mod.Send( 'button', 0, 2, selected.hold);
							if(selected.hold<1)
							{
								release_held_sequences(selected);
							}
						}
						if(pad_mode == 6)
						{
							refresh_pads();
						}
						if(key_mode == 6)
						{
							refresh_c_keys();
						}
					}*/
					btn_press1 = val;
					if(btn_press1+btn_press2==2)
					{
						padmodegui.message('int', (pad_mode!=5)*5);
					}
					else
					{
						repeatgui.message('int', val);
					}
					break;
				//key cycle
				case 1:
					btn_press2 = val;
					if(btn_press1+btn_press2==2)
					{
						padmodegui.message('int', (pad_mode!=5)*5);
					}
					else
					{
						keymodeadv.message('int', val);
					}
					break;
				//rotate, *change slider view
				case 2:
					if(pad_pressed<0){
						rotleftgui.message('int', val);
					}
					else if(val>0){
						stepmodegui.message('int', Math.max(0, Math.min(3, step_mode-1)));
					}
					break;
				//rotate, *change slider view
				case 3:
					if((pad_mode!=6)&&(key_mode!=6))
					{
						if(pad_pressed<0){
							rotrightgui.message('int', val);
						}
						else if(val>0){
							stepmodegui.message('int', Math.max(0, Math.min(3, step_mode+1)));
						}
					}
					else
					{
						//post('pad mode is 6\n');
						if(val>0)
						{
							poly_hold_toggle();
						}
						if(pad_mode == 6)
						{
							refresh_pads();
						}
						if(key_mode == 6)
						{
							refresh_c_keys();
						}
					}
					break;
			}
			break;
	}
}

var _cntrlr_key = _c_key;
function _c_key(x, y, val)
{
	debug('c key in', x, y, val, '\n');
	num = (x + (y*16));
	if((y==1)&&(val>0))
	{
		num -= 16;;
		debug('pattern is:', selected.pattern, 'num is:', num);
		selected.pattern[num] = Math.abs(selected.pattern[num]-1);
		//debug('pattern is:', selected.pattern);
		selected.obj.set.pattern(selected.pattern);
		if((edit_preset == presets[selected.num])&&(grid_mode==1))
		{
			storage.getstoredvalue('poly.'+(selected.num+1)+'::pattern', edit_preset);
		}
		step.message('extra1', 1, selected.pattern);
		step.message('zoom', 1, 1);
		refresh_c_keys();
		refresh_grid();
		mod.Send( 'cntrlr_encoder_grid', 'custom', selected.num%4, Math.floor(selected.num/4)%2, selected.pattern);
		mod.Send( 'code_encoder_grid', 'custom', selected.num%8, Math.floor(selected.num/8), selected.pattern);
	}
	else
	{
		switch(key_mode)
		{
			//mute mode
			default:
				if(val>0)
				{
					var Part = part[num];
					//part[num].active = Math.abs(part[num].active-1);
					Part.obj.set.active(Math.abs(Part.active-1));
					refresh_c_keys();
					if(pad_mode==2){refresh_pads();}
					refresh_grid();
					add_automation(Part, 'mute', Part.active);
				}
				break;
			//loop mode
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
				refresh_c_keys();
				break;
			//behavior mode
			case 2:
				if(val>0)
				{
					selected.behavior[num] = (selected.behavior[num]+1)%8;
					part[selected.num].obj.set.behavior(selected.behavior);
					update_step();
					refresh_c_keys();
					break;
				}
			//preset mode
			case 3:
				if((val>0)&&(key_pressed<0))
				{
					key_pressed = num;
					if(val>0)
					{
						presets[selected.num] = num+1;
						storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
						add_automation(selected, 'preset', presets[selected.num]);
					}
				}
				else if(val>0)
				{
					key_pressed = -1;
					copy_preset(selected, num+1);
				}
				else
				{
					key_pressed = -1;
				}
				break;
			//global mode
			case 4:
				if((val>0)&&(key_pressed<0))
				{
					key_pressed = num;
					if(val>0)
					{
						for(var i=0;i<16;i++)
						{
							presets[i] = num+1;
						}
						preset = num+1;
						storage.message(presets[selected.num]);
					}
				}
				else if(val>0)
				{
					key_pressed = -1;
					copy_global_preset(preset, num+1);
				}
				else
				{
					key_pressed = -1;
				}
				break;
			//polyrec mode
			case 5:
				if(val>0)
				{
					selected.note[current_step] = num;
					selected.obj.set.note(selected.note);
					step.message('pitch', 1, selected.note);
					selected.pattern[current_step] = 1;
					selected.obj.set.pattern(selected.pattern);
					selected.obj.last_trigger.message('bang');
					step.message('extra1', 1, selected.pattern);
					step.message('zoom', 0, 16);
					refresh_c_keys();
				}
				break;
			//polyplay mode
			case 6:
				play_sequence(selected, num, val);
				refresh_c_keys();
				break;
			//accent mode
			case 7:
				if(val>0)
				{
					selected.velocity[num] = ACCENT_VALS[(ACCENTS[Math.floor(selected.velocity[num]/8)])%4];
					//post('vel:', selected.velocity[num], 'calc:', (Math.floor(selected.velocity[num]/8)), '\n');
					selected.obj.set.velocity(selected.velocity);
					refresh_c_keys();
				}
				break;
		}
	}
}

var _cntrlr_grid = _c_grid;
function _c_grid(x, y, val)
{
	debug('_c_grid', x, y, val);
	switch(pad_mode)
	{
		//select mode
		default:
			if((val>0)&&(pad_pressed<0))
			{
				pad_pressed = x + (y*4);
				select_pattern(pad_pressed);
				last_key_mode = key_mode;
				pipe.message('int', pad_pressed);
			}
			else if((x + (y*4) == pad_pressed)&&(val<1))
			{
				pad_pressed = -1;
				change_key_mode(last_key_mode);
			}
			else
			{
				copy_pattern(selected, part[x + (y*4)]);
			}
			break;
		//add mode
		case 1:
			if(val>0)
			{
				var p = x+(y*4);
				add_note(part[p]);
				/*if(p != selected.num)
				{
					select_pattern(p);
				}
			}
			else if((x + (y*4) == pad_pressed)&&(val<1))
			{
				pad_pressed = -1;
				change_key_mode(last_key_mode);*/
			}
			break;
		//mute mode
		case 2:
			if(val>0)
			{
				var Part = part[x + (y*4)];
				Part.obj.set.active(Math.abs(Part.active-1));
				refresh_pads();
				if(key_mode==0){refresh_c_keys();}
				add_automation(Part, 'mute', Part.active);
			}
			break;
		//preset mode
		case 3:
			debug('pad_pressed', pad_pressed, '\n');
			if((val>0)&&(pad_pressed<0))
			{
				pad_pressed = x + (y*4);
				var num = x + (y*4);
				if(val>0)
				{
					presets[selected.num] = num+1;
					storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
					add_automation(selected, 'preset', presets[selected.num]);
				}
			}
			else if(val>0)
			{
				pad_pressed = -1;
				copy_preset(selected, x+(y*4)+1);
			}
			else
			{
				pad_pressed = -1;
			}
			break;
		//global mode
		case 4:
			if((val>0)&&(pad_pressed<0))
			{
				pad_pressed = x + (y*4);
				var num = x + (y*4);
				if(val>0)
				{
					for(var i=0;i<16;i++)
					{
						presets[i] = num+1;
					}
					preset = num+1;
					storage.message(presets[selected.num]);
				}
			}
			else if(val > 0)
			{
				pad_pressed = -1;
				copy_global_preset(preset, x+(y*4)+1);
			}
			else
			{
				pad_pressed = -1;
			}
			break;
		//freewheel mode
		case 5:
			if((val>0)&&(pad_pressed<0))
			{
				pad_pressed = x + (y*4);
				select_pattern(pad_pressed);
				last_key_mode = key_mode;
				pipe.message('int', pad_pressed);
			}
			else if((x + (y*4) == pad_pressed)&&(val<1))
			{
				pad_pressed = -1;
				change_key_mode(last_key_mode);
			}
			else
			{
				sync_wheels(selected, part[x + (y*4)]);
			}
			break;
		//play mode
		case 6:
			if(val>0)
			{
				var p = x+(y*4);
				play_note(part[p]);

			}
			break;
		//polyplay mode
		case 7:
			//post('pad_play', x, y, val);
			var num = x + (y*4);
			if(val>0)
			{
				var trig = selected.triggered.indexOf(num);
				if(trig == -1)
				{
					selected.triggered.push(num);
					selected.obj.polyplay.message('midinote', num, val);
				}
				else
				{
					var held = selected.held.indexOf(num);
					if(held > -1)
					{
						//remove from the held array since a new sequence has been triggered
						selected.held.splice(held, 1);
					}
				}
			}
			else
			{
				if(selected.hold == 0)
				{
					var trig = selected.triggered.indexOf(num);
					if(trig > -1)
					{
						selected.triggered.splice(trig, 1);
					}
					selected.obj.polyplay.message('midinote', num, val);
				}
				else
				{
					//add to the held array, so that when hold for part is turned off the note can be flushed
					selected.held.push(num);
				}
			}
			//part[num].obj.polyenable.message('int', part[num].polyenable);
			refresh_pads();
			break;
	}
}

function _grid(x, y, val)
{
	debug('_grid', x, y, val, '\n');
	controlRegistry.receive(x+(y*16), val);
	switch(GRIDMODES[grid_mode])
	{
		//cntrlr mode
		case 'hex':
			if(y<2)
			{
				_c_grid(x%4, Math.floor(x/4)+(y*2), val);
			}
			else if (y<4)
			{
				_c_key(x + 8*(y-2), 0, val);
			}
			else if (y<6)
			{
				_c_key(x + 8*(y-4), 1, val);
			}
			else if (y==6)
			{
				_c_button(x%4, Math.floor(x/4), val);
			}
			else if ((y==7)&&(val))
			{
				keymodegui.message('int', x);
			}
			break;
		//tr256 mode
		case 'tr256':
			if(val>0)
			{
				switch(y)
				{
					case 0:
						if(grid_pressed<0)
						{
							if(rec_enabled)
							{
								set_record(0);
							}
							else
							{
								grid_pressed = x + (y*16);
								preset = x+1;
								var i=15;do{
									presets[i] = x+1;
								}while(i--);
								storage.message(preset);
								refresh_grid();
							}
							break;
						}
						else
						{
							copy_global_preset(x+(y*16)+1);
							grid_pressed = -1;
						}
						break;
					case 1:
						if(rec_enabled)
						{
							set_record(0);
						}
						if(grid_pressed<0)
						{
							edit_preset = x+1;
							var y=13;do{
								storage.getstoredvalue('poly.'+y+'::pattern', edit_preset);
								storage.getstoredvalue('poly.'+y+'::velocity', edit_preset);
							}while(y--);
						}
						else if(grid_pressed==x)
						{
							set_record(1);
						}
						refresh_grid();
						break;
					default:
						var Part = part[y-2], cur_step = Part.edit_buffer[x],
							cur_vel = Part.edit_velocity[x], new_vel = ACCENT_VALS[Tvel];
						if((cur_step)&&(cur_vel!=new_vel))
						{
							cur_vel=new_vel;
						}
						else if(cur_step)
						{
							cur_step = 0;
						}
						else
						{
							cur_step = 1;
							cur_vel = new_vel;
						}
						Part.edit_buffer[x]=cur_step;
						Part.edit_velocity[x]=cur_vel;
						if(altVal)
						{
							var quad = (x+8)%16;
							Part.edit_buffer[quad] = cur_step;
							Part.edit_velocity[quad] = ACCENT_VALS[Tvel];
						}
						if(edit_preset!=preset)
						{
							//don't send to objects since this is for a non-loaded preset
							Part.obj.set.pattern(Part.edit_buffer, edit_preset);
							if(cur_step>0)
							{
								Part.obj.set.velocity(Part.edit_velocity, edit_preset);
							}
						}
						else
						{
							Part.obj.set.pattern(Part.edit_buffer);
							Part.obj.set.velocity(Part.edit_velocity);
							if(Part == selected)
							{
								step.message('velocity', 1, selected.velocity);
								step.message('extra1', 1, selected.pattern);
								step.message('zoom', 1, 1);
								refresh_c_keys();
								mod.Send( 'cntrlr_encoder_grid', 'custom', Part.num%4, Math.floor(Part.num/4)%2, Part.pattern);
								mod.Send( 'code_encoder_grid', 'custom', Part.num%8, Math.floor(Part.num/8), Part.pattern);
							}
						}
						mod.Send( 'grid', 'value', x, y, Part.edit_buffer[x]*(ACCENTS[Math.floor(Part.edit_velocity[x]/8)]));
						//refresh_grid();
						break;
				}
			}
			else if((x + (y*16) == grid_pressed)&&(val<1))
			{
				grid_pressed = -1;
			}
			break;
		//gome mode
		case 'polygome':
			if(altVal>0)
			{
				//Poly_Record_mode
				if(((x==0)&&(y==0))||((x==15)&&(y==0))||((x==15)&&(y==15))||((x==0)&&(y==15)))
				{
					if(val>0)
					{
						poly_hold_toggle();
						refresh_grid();
					}
				}
				else if((y==0)&&(val>0))
				{
					presets[selected.num] = x;
					storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
					refresh_grid();
				}
				else if(val>0)
				{
					y -= 1;
					var note = (x<<6) + (y<<10) + 32;
					debug('new note', current_step, x, y, note);
					debug('decoded:', (note>>6)%16, note>>10);
					if(selected.note[0]<32)
					{
						selected.obj.offset.message('int', 0);
						curSteps[selected.num]=0;
					}
					selected.note[curSteps[selected.num]] = note;
					selected.obj.set.note(selected.note);
					debug('new notes:', selected.obj.note.getvalueof());
					step.message('pitch', 1, selected.note);
					selected.pattern[curSteps[selected.num]] = 1;
					selected.obj.set.pattern(selected.pattern);
					selected.obj.last_trigger.message('bang');
					step.message('extra1', 1, selected.pattern);
					step.message('zoom', 0, 16);
					refresh_c_keys();
				}
			}
			else
			{
				//Poly_Play_mode
				if(((x==0)&&(y==0))||((x==15)&&(y==0))||((x==15)&&(y==15))||((x==0)&&(y==15)))
				{
					if(val>0)
					{
						poly_hold_toggle();
						refresh_grid();
					}
				}
				else if((y==0)&&(val>0))
				{
					presets[selected.num] = x;
					storage.message('recall', 'poly.'+(selected.num+1), presets[selected.num]);
					refresh_grid();
				}
				else
				{
					y -= 1;
					var root = selected.obj.note.getvalueof()[0];
					//play_sequence(selected, ((x-(root>>6)%16)<<6) + (y-(root>>10)<<10) + 32, val);
					play_sequence(selected, (x<<6) + (y<<10) + 32, val);
					refresh_c_keys();
					refresh_grid();
				}
			}
			break;
		//cafe mode
		case 'cafe':
			//Cafe_Play_mode
			debug('cafe play', presets[x]);
			var Part = part[y];
			if(((x+1)==presets[y])&&(val==0)&&(altVal==0))
			{
				Part.obj.set.clutch(0);
				var i=15;do{
					mod.Send( 'grid', 'value', i, y, 0);
				}while(i--);
			}
			else if(val>0)
			{
				if((x+1)!=presets[y])
				{
					presets[y] = x+1;
					storage.message('recall', 'poly.'+(y+1), presets[y]);
					Part.pattern = Part.obj.pattern.getvalueof();
				}
				Part.obj.restartcount.message(0);
				Part.obj.set.clutch(1);
			}
			break;
		//boinngg mode
		case 'boinngg':
			//Boiingg_Play_mode
			debug('boiingg input:', x, y, val, altVal);
			if(val>0)
			{
				if(altVal>0)
				{
					switch(y)
					{
						case 0:
							timeupgui.message('int', val);
							break;
						case 1:
							timedngui.message('int', val);
							break;
					}
				}
				else
				{
					if(y>0)
					{
						var pset = presets[x];
						var Part = part[x];
						if(Part.direction!=2){
							Part.obj.set.direction(2);
						}
						if(Part.nudge!=0){
							Part.obj.set.nudge(0);
						}
						if(Part.pattern.join('')!='1000000000000000'){
							Part.obj.set.pattern([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
						}
						Part.obj.restartcount.message(0);
						Part.obj.set.steps(y);
					}
					else
					{
						mod.Send( 'grid', 'mask_column', x, -1);
					}
					if(part[x].active!=(y>0)){
						part[x].obj.set.active(y>0);
					}
					if(part[x]==selected)
					{
						refresh_c_keys();
						if(pad_mode==2){refresh_pads();}
						update_gui();
					}
				}
			}
			break;
		//slider mode
		case 'skin':
			//Slider Mode
			break;
		//preset mode
		case 'none':
			//Preset_Mode
			break;
		//behavior mode
		case 'behaviour':
			//Behavior_Grid_mode
			if((val>0)&&(x<7))
			{
				if(current_rule == 0)
				{
					rulemap.message('list', x, y, (behavegraph[x][y]+1)%7);
				}
				else
				{
					rulemap.message('list', x, y, current_rule);
				}
			}
			else if((val>0)&&(x==7))
			{
				current_rule = y;
				refresh_grid();
			}
			break;
	}
}

function _base_grid(x, y, val)
{
	debug('_base_grid', x, y, val, '\n');
	if(shifted)
	{
		if(y<2)
		{
			_c_key(x + 8*(y), 0, val);
		}
		else if(y<3)
		{
			_c_button(x%4, Math.floor(x/4), val);
		}
		else if((y==3)&&(val>0))
		{
			keymodegui.message('int', x);
		}
	}
	else if (y<2)
	{
		_c_grid(x%4, Math.floor(x/4)+(y*2), val);
	}
	else if (y<4)
	{
		_c_key(x + 8*(y-2), 1, val);
	}
}

function _code_button(num, val)
{
	if(val)
	{
		if(num==0){num=1;}
		stepmodegui.message('int', num);
	}
}

function _code_grid(x, y, val)
{
	if(y<2)
	{
		if(shifted)
		{

		}
		else
		{
			_c_grid(x%4, Math.floor(x/4)+(y*2), val);
		}
	}
	else if (y<4)
	{
		_c_key(x + 8*(y-2), 1, val);
	}
}

function _push_grid(x, y, val)
{
	debug('push_grid', x, y, val, '\n');
	_grid(x, y, val);
}

function _shift(val)
{
	debug('shift:', val, '\n');
	if(val!=shifted)
	{
		shifted = val;
		mod.Send( 'enable_translation_group', 'base_keys', Math.floor(shifted));
		mod.Send( 'enable_translation_group', 'base_pads', Math.floor(!shifted));
		mod.Send( 'enable_translation_group', 'base_keys2', Math.floor(!shifted));
		mod.Send( 'enable_translation_group', 'base_buttons',  Math.floor(shifted));
		mod.Send( 'enable_translation_group', 'base_extras',  Math.floor(shifted));

		mod.Send( 'enable_translation_group', 'code_keys', Math.floor(shifted));
		mod.Send( 'enable_translation_group', 'code_pads', Math.floor(!shifted));
		mod.Send( 'enable_translation_group', 'code_keys2', Math.floor(!shifted));
		mod.Send( 'enable_translation_group', 'code_buttons',  Math.floor(shifted));
		mod.Send( 'enable_translation_group', 'code_extras',  Math.floor(shifted));

		refresh_grid();
		refresh_keys();
	}
	refresh_code_buttons();
}

function _key(num, val)
{
	debug('_key', num, val, '\n');
	switch(altVal)
	{
		default:
			if(val>0)
			{
				change_grid_mode(num);
			}
			break;
		case 1:
			if(val>0)
			{
				Tvel=num;
				var i=3;do{
					mod.Send( 'key', 'value', i, (i==(Tvel))*(TVEL_COLORS[i]));
				}while(i--);
			}
			break;
	}
}

function surface_offset(val)
{
	grid_offset = val;
}

//this is mainly for the select-hold
function _msg_int(val)
{
	debug('msg_int', val, '\n');
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
			_grid(args[0], args[1], args[2]);
			break;
		case 1:
			_key(args[0], args[1]);
			break;
	}
}

function _alt(val)
{
	//because of changes in b996, alt now comes in as "alt" instead of "alt_in"
	_alt_in(val);
}

function _alt_in(val)
{
	debug('alt_in', val, '\n');
	altVal = Math.floor(val>0);
	switch(altVal)
	{
		default:
			var i=7;do{
				mod.Send( 'key', 'value', i, (i==grid_mode)*8);
			}while(i--);
			break;
		case 1:
			var i=3;do{
				mod.Send( 'key', 'value', i, (i==(Tvel))*(TVEL_COLORS[i]));
			}while(i--);
			break;
	}
	switch(grid_mode)
	{
		default:
			break;
		case 2:
			mod.Send( 'grid', 'batch', 0);
			refresh_grid();
			break;
	}
}


//input sorter for patcher calls

//called by gui object, sets visible portion of live.step
function _mode(val)
{
	debug('mode', val, '\n');
	step_mode = val;
	step.message('mode', Modes[step_mode]);
	switch(step_mode)
	{
		default:
			mod.Send( 'code_encoder_grid', 'local', 0);
	}
	refresh_code_buttons();
	refresh_adjusters();
}

//from live.step
function _step_in()
{
	var args = arrayfromargs(arguments);
	debugstep('step_in', args);
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
					debugstep('old', step_value);
					outlet(2, new_value);
					break;
			}
		case 3:
			break;
	}
}

//distributes input from gui button and menu elements
function _guibuttons(num, val)
{
	debug('gui_buttons', num, val, '\n');
	switch(num)
	{
		//pad cycle
		case 0:
			//padmodegui.message('int', RemotePModes[Math.max((RemotePModes.indexOf(pad_mode)+1)%3, 0)]);
			if(padmodeenables.length)
			{
				while(padmodeenables.indexOf(pad_mode)==-1)
				{
					pad_mode = (pad_mode+1)%7;
				}
				padmodegui.message('int', padmodeenables[(padmodeenables.indexOf(pad_mode)+1)%padmodeenables.length]);
			}
			break;
		//key cycle
		case 1:
			//keymodegui.message('int', (key_mode+1)%8);
			if(keymodeenables.length)
			{
				while(keymodeenables.indexOf(key_mode)==-1)
				{
					key_mode = (key_mode+1)%8;
				}
				keymodegui.message('int', keymodeenables[(keymodeenables.indexOf(key_mode)+1)%keymodeenables.length]);
			}
			break;
		//rotate
		case 2:
			rotate_pattern(selected, rot_length, -1);
			break;
		//rotate
		case 3:
			rotate_pattern(selected, rot_length, 1);
			break;
		//time value
		case 4:
			selected.obj.set.notevalues(val);
			{
				selected.obj.set.basetime(TRANS[selected.notetype][val][0]);
				selected.obj.set.timedivisor(TRANS[selected.notetype][val][1]);
				if(timing_immediate)
				{
					selected.obj.nexttime.message('bang');
				}
				BaseTime.message('set', TRANS[selected.notetype][val][0]);
				script['Speed'+(selected.num+1)].message('set', TRANS[selected.notetype][val][1]);
			}
			break;
		//note type
		case 5:
			selected.obj.set.notetype(val);
			var notevalues = selected.notevalues;
			if(notevalues < 8)
			{
				selected.obj.set.basetime(TRANS[val][notevalues][0], presets[selected.num]);
				selected.obj.set.timedivisor(TRANS[val][notevalues][1], presets[selected.num]);
				if(timing_immediate)
				{
					selected.obj.nexttime.message('bang');
				}
				BaseTime.message('set', TRANS[val][notevalues][0]);
			}
			break;
		//time up
		case 6:
			if(selected.notevalues<8)
			{
				notevaluesgui.message('int', Math.max(Math.min(7, parseInt(selected.notevalues)-1), 0));
			}
			else
			{
				notevaluesgui.message('int', Math.floor(selected.timedivisor / selected.basetime).toString(2).length-1);
				notetypegui.message('set', 0);
			}
			break;
		//time down
		case 7:
			if(selected.notevalues<8)
			{
				notevaluesgui.message('int', Math.max(Math.min(7, parseInt(selected.notevalues)+1), 0));
			}
			else
			{
				notevaluesgui.message('int', Math.ceil(selected.timedivisor / selected.basetime).toString(2).length);
				notetypegui.message('set', 0);
			}
			break;
		//transpose up
		case 8:
			change_transpose(Math.max(Math.min(global_offset - transpose_steps, 96), 0));
			break;
		//transpose down
		case 9:
			change_transpose(Math.max(Math.min(global_offset + transpose_steps, 96), 0));
			break;
		//pad mode menu
		case 10:
			change_pad_mode(val);
			break;
		//key mode menu
		case 11:
			change_key_mode(val);
			break;
		//transpose menu
		case 12:
			change_transpose(val);
			break;
		//direction menu
		case 13:
			//selected.direction = val;
			//selected.obj.direction.message('int', val);
			selected.obj.set.direction(val);
			break;
		//lock
		case 14:
			debug('lock', val, '\n');
			locked = val;
			break;
		//detect device
		case 15:
			detect_devices();
			break;
		//record
		case 16:
			record(val);
			break;
		//play
		case 17:
			play_enabled = val;
			locked = 1;
			break;
	}
}

//distributes input from gui grid element
function _padgui_in(val)
{
	debug('padguiin', val, '\n');
	_c_grid(val%4, Math.floor(val/4), 1);
	_c_grid(val%4, Math.floor(val/4), 0);
}

//distributes input from gui key element
function _keygui_in(val)
{
	debug('keyguiin', val, '\n');
	_c_key(val%16, Math.floor(val/16), 1);
	_c_key(val%16, Math.floor(val/16), 0);

}

//displays played notes on grid
function _blink(val)
{
	//if(DEBUG_BLINK){post('blink', val, '\n');}
	if(grid_mode == 0)
	{
		mod.Send( 'receive_translation', 'keys2_'+last_mask, 'mask', -1);
		mod.Send( 'receive_translation', 'keys2_'+val, 'mask', 5);
	}
	last_mask = val;
}

//displays played notes on keys
function _vblink(num, val)
{
	debugblink('vblink', val, '\n');
	if(grid_mode == 0)
	{
		if(key_mode==0)
		{
			//mod.Send( 'mask', 'c_key', num, val);
			//grid_out('mask', 'key', num, val);
			mod.Send( 'receive_translation', 'keys_'+num, val);
		}
		//mod.Send( 'mask', 'c_grid', num%4, Math.floor(num/4), Blinks[Math.floor(val>0)]);
		//grid_out('mask', 'grid', num, val);
		mod.Send( 'receive_translation', 'pads_'+num, Blinks[Math.floor(val>0)]);
	}
}

//evaluate and distribute data recieved from the settings menu
function _settingsgui(num, val)
{
	args = arrayfromargs(arguments);
	num = args[0];
	val = args[1];
	switch(num)
	{
		//select+hold option
		case 0:
			pad_invoked_key_mode = val;
			break;
		//immediate timing option
		case 1:
			timing_immediate = val;
			break;
		//global offset
		case 2:
			global_chain_offset = val;
			_select_chain(selected.num);
			break;
		//empty
		case 3:
			break;
		//transpose steps
		case 4:
			transpose_steps = val;
			break;
		//randomize pattern
		case 5:
			randomize_pattern(randomize_global);
			break;
		//randomize velocity
		case 6:
			randomize_velocity(randomize_global);
			break;
		//randomize duration
		case 7:
			randomize_duration(randomize_global);
			break;
		//randomize behavior
		case 8:
			randomize_behavior(randomize_global);
			break;
		//randomize rulebends
		case 9:
			randomize_rulebends(randomize_global);
			break;
		//full reset
		case 10:
			reset_data(randomize_global);
			break;
		//randomize global
		case 12:
			randomize_global = val;
			break;
		//randomize all
		case 11:
			randomize_pattern(randomize_global);
			randomize_velocity(randomize_global);
			randomize_duration(randomize_global);
			randomize_behavior(randomize_global);
			randomize_rulebends(randomize_global);
			break;
		//randomize rules
		case 13:
			randomize_rules();
			break;
		//keymode enables
		case 14:
			vals = args.slice(1, 9);
			keymodeenables = [];
			for(var i=0;i<8;i++)
			{
				if(vals[i])
				{
					keymodeenables.push(i);
				}
			}
			debug('keymodeenables', keymodeenables, '\n');
			break;
		//padmode enables
		case 15:
			vals = args.slice(1, 8);
			padmodeenables = args.slice(1, 8);
			padmodeenables = [];
			for(var i=0;i<7;i++)
			{
				if(vals[i])
				{
					padmodeenables.push(i);
				}
			}
			debug('padmodeenables', padmodeenables, '\n');
			break;
		//behavior enables
		case 16:
			vals = args.slice(1, 17);
			debug('behavior enables:', vals, '\n');
			for(var i=0;i<16;i++)
			{
				if(vals[i+1]!=part[i].behavior_enable)
				{
					debug('part', i, 'behavior enable, was', part[i].behavior_enable, ', setting:', vals[i+1], '\n');
					part[i].behavior_enable = vals[i+1];
					part[i].obj.set.behavior(vals[i+1]);
				}
			}
			break;
		case 17:
			debug('reset_data', val);
			reset_data(true);
			break;
	}
}

//evaluate and distribute data recieved from the behavior graph in the settings menu
function behavegraph_in(behave, bar, val)
{
	behavegraph[behave][bar] = val;
	if(grid_mode==7)
	{
		mod.Send( 'grid', 'value', behave, bar, BEHAVE_COLORS[val]);
	}
}

//distribute MIDI remote control assignments to their destination
function _remote(num, val)
{
	switch(num<16)
	{
		case 0:
			_c_grid(num%4, Math.floor(num/4), 1);
			break;
		case 1:
			_c_key(num-16, val);
			break;
	}
}

//distribute
function _receive_automation(num, val)
{
	if((play_enabled>0)&&(num>110)&&(val!==0))
	{
		num-=111;
		if(DEBUG_REC){post('receive auto:', num, val, '\n');}
		if(val>9)
		{
			presets[part[num].num] = val-10;
			if(DEBUG_REC){post('preset change:', part[num].num+1, presets[part[num].num], '\n');}
			storage.message('recall', 'poly.'+(part[num].num+1), presets[part[num].num]);
		}
		else if(val>0)
		{
			part[num].active = val-1;
			part[num].obj.active.message('int', part[num].active);
			if(pad_mode==2)
			{
				refresh_pads();
			}
			if(key_mode==0)
			{
				refresh_c_keys();
			}
		}
	}
}

function _grid_play(x, y, voice, val, poly)
{
	//var args = arrayfromargs(arguments);
	debug('_grid_play', x, y, voice, val, poly, '\n');
	switch(grid_mode)
	{
		case 2:
			debug('sel:', selected.num, poly, '\n');
			if(altVal>0)
			{
				if((voice==0)&&((poly-1)==selected.num))
				{
					mod.Send( 'grid', 'mask', Math.max(Math.min(x, 15), 0), Math.max(Math.min(y, 15), 0) + 1, val);
				}
			}
			else
			{
				if((voice>0)&&((poly-1)==selected.num))
				{
					mod.Send( 'grid', 'mask', Math.max(Math.min(x, 15), 0), Math.max(Math.min(y, 15), 0) + 1, val*voice);
				}
			}
			break;
	}
}


/*/////////////////////////////
///// data syncronization /////
/////////////////////////////*/


//called by pattr when it recalls a preset
////need to figure out how to deal with global preset loading....there's missing data doing things this way.
function _recall()
{
		if(DEBUG_PTR){post('recall\n');}
		for(var item in Objs)
		{
			//post(Objs[item], typeof(selected[Objs[item]]), 'retrieving...\n');
			selected.obj.get[Objs[item].Name]();
		}
		selected.nudge = Math.floor(selected.obj.nudge.getvalueof());
		selected.steps = Math.floor(selected.obj.steps.getvalueof());
		selected.root = Math.floor(selected.obj.noteoffset.getvalueof()%12);
		selected.octave = Math.floor(selected.obj.noteoffset.getvalueof()/12);
		var i=15;do{
			part[i].active = part[i].obj.active.getvalueof();
			part[i].quantize = part[i].obj.quantize.getvalueof();
			part[i].pattern = part[i].obj.pattern.getvalueof();
			//script['Speed'+(i+1)].message('set', part[i].ticks);
			update_speed(part[i]);
		}while(i--);
		update_step();
		refresh_c_keys();
		refresh_pads();
		update_gui();
		if(key_mode>4)
		{
			var i=7;do{
				mod.Send( 'cntrlr_encoder_grid', 'custom', i%4, Math.floor(i/4),  part[i+(8*(selected.num>7))].pattern);
			}while(i--);
			var i=15;do{
				mod.Send( 'code_encoder_grid', 'custom', i%8, Math.floor(i/8),  part[i].pattern);
			}while(i--);
		}
		//select_pattern(selected.num);
		//refresh_edit_view();
		//refresh_dials();
		//refresh_lcd();
}

//called by pattr when loading a xml preset file
function read()
{
	presets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
	preset = 1;
	storage.message(preset);
}

///this is how we inject the data to the poly~ objects:
function make_funcs(part)
{
	var new_part = [];
	new_part.stepLoop = function(In, Out)
	{
		debugstep('step Loop', In, Out);
		selected.nudge = In;
		selected.obj.nudge.message('set', selected.nudge);
		selected.obj.set.nudge(selected.nudge, presets[selected.num]);
		//selected.steps = Out - In;
		//selected.obj.steps.message('int', selected.steps);
		selected.obj.set.steps(Out - In);
		selected.obj.restart.message('bang');
		refresh_c_keys();
	}
	new_part.stepDir = function(step, val)
	{
		debugstep('step Dir', step, val);
		//part.direction = val;
		//part.obj.direction.message('int', val);
		part.obj.set.direction(val);
	}
	new_part.stepNote = function(step, val)
	{
		debugstep('step note', step, val);
		part.note[step] = val;
		part.obj.set.note(part.note);
	}
	new_part.stepVel = function(step, val)
	{
		debugstep('step vel', step, val);
		part.velocity[step] = val;
		part.obj.set.velocity(part.velocity);
	}
	new_part.stepDur = function(step, val)
	{
		debugstep('step dur', step, val);
		part.duration[step] = val;
		part.obj.set.duration(part.duration);
	}
	new_part.stepExtra1 = function(step, val)
	{
		debugstep('step extra1', step, val);
		part.pattern[step] = val;
		part.obj.set.pattern(part.pattern);
		refresh_c_keys();
	}
	new_part.stepExtra2 = function(step, val)
	{
		debugstep('step extra2', step, val);
		part.rulebends[step] = val;
		part.obj.set.rulebends(part.rulebends);
	}
	return new_part
}

//called to update data in live.step when changes are made to poly
function update_step()
{
	//set_dirty(1);
	step_value = step.getvalueof();
	debugstep('update step: step_value', step_value.length, '\n', step_value);
	selected.nudge = parseInt(selected.obj.nudge.getvalueof());
	selected.steps = parseInt(selected.obj.steps.getvalueof());
	step_value[5] = Math.floor(selected.nudge);
	step_value[6] = Math.floor(selected.nudge) + Math.floor(selected.steps) + 1;
	selected.pattern = selected.obj.pattern.getvalueof();
	selected.velocity = selected.obj.velocity.getvalueof();
	selected.duration = selected.obj.duration.getvalueof();
	selected.behavior = selected.obj.behavior.getvalueof();
	selected.rulebends = selected.obj.rulebends.getvalueof();
	selected.note = selected.obj.note.getvalueof();
	var i=15;do{
		var s = 11 + (i*5);
		step_value[s] = selected.note[i];
		step_value[s + 1] = selected.velocity[i];
		step_value[s + 2] = selected.duration[i];
		step_value[s + 3] = selected.pattern[i];
		step_value[s + 4] = selected.rulebends[i];
	}while(i--);
	debugstep('to step', step_value.length, '\n', step_value);
	step.setvalueof(step_value);
}

//called to update data in poly when changes are made in livestep
function update_poly()
{
	//set_dirty(1);
	var args = arrayfromargs(arguments);
	step_value = step.getvalueof();
	debugstep('update_poly\n unmatching args', args);
	var i = args.length;do{
		if(args[i]>10)
		{
			var index = args[i]-11;
			debugstep(args[i]);
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
	}while(i--);
}


/*///////////////////////
// internal processes  //
///////////////////////*/

//change the function of the keys
function change_key_mode(val)
{
	debug('key_mode', val, '\n');
	key_pressed = -1;
	key_mode = val;
	switch(key_mode)
	{
		default:
			break;
		case 5:
			//stepmodegui.message('int', 5);
			break;
	}
	keymodegui.message('set', key_mode);
	refresh_c_keys();
	refresh_extras();
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
	//pad_pressed = -1;
	//change_key_mode(last_key_mode);
	padmodegui.message('set', pad_mode);
	refresh_pads();
	update_bank();
}

//change the function of the grid
function change_grid_mode(val)
{
	//mod.Send( 'set_legacy', val ? 1 : 0);
	mod.Send( 'set_legacy', 0);
	if((grid_mode==3)&&(val!=3))
	{
		var i=15;do{
			part[i].clutch = 1;
			part[i].obj.clutch.message('int', 1);
		}while(i--);
	}
	grid_mode = val;
	var i=15;do{
		mod.Send( 'enable_translation', 'keys_'+i, 'push_grid', (!val));
		mod.Send( 'enable_translation', 'keys2_'+i, 'push_grid', (!val));
		mod.Send( 'enable_translation', 'pads_'+i, 'push_grid', (!val));
	}while(i--);
	var i=7;do{
		mod.Send( 'enable_translation', 'extras_'+i, 'push_grid', (!val));
		mod.Send( 'enable_translation', 'buttons_'+i, 'push_grid', (!val));
	}while(i--);
	mod.Send( 'grid', 'all', 0);

	if(grid_mode == 1)
	{
			edit_preset = preset;
			var y=13;do{
				storage.getstoredvalue('poly.'+y+'::pattern', edit_preset);
				storage.getstoredvalue('poly.'+y+'::velocity', edit_preset);
			}while(y--);
	}

	refresh_grid();
	update_bank();
	var i=7;do{
		mod.Send( 'key', 'value', i, (i==grid_mode)*8);
	}while(i--);
}

function change_step_mode(val)
{
	//this is in _mode....needs to move here but must change patcher first.
	mod.Send( 'code_encoder_grid', 'local', 0);
}

//select the current pattern and load its data to CNTRLR/live.step/gui
function select_pattern(num)
{
	if(codec_handler)
	{
		var i=15;do{
			mod.Send( 'code_encoder_grid', 'custom', i%8, Math.floor(i/8), part[i].pattern);
			mod.Send( 'code_encoder_grid', 'green', i%8, Math.floor(i/8), part[i].notevalues<8);
		}while(i--);
	}
	var range = num>7;
	if(Math.floor(selected.num/8)!=Math.floor(num/8))
	{
		var i=7;do{
			mod.Send( 'cntrlr_encoder_grid', 'custom', i%4, Math.floor(i/4),  part[i+(8*(range))].pattern);
			mod.Send( 'cntrlr_encoder_grid', 'green', i%4, Math.floor(i/4), part[i+(8*(range))].notevalues<8);
		}while(i--);
	}
	selected = part[num];
	_select_chain(num);
	update_step();
	selected_filter.message('offset', num + 1);
	refresh_pads();
	refresh_c_keys();
	update_gui();
	if(pad_mode == 5)
	{
		update_bank();
	}
	refresh_adjusters();
}

function copy_pattern(src, dest)
{
	debug('copy pattern', src.num, dest.num, '\n');
	dest.obj.set.pattern(src.pattern);
}

function copy_preset(part, dest)
{
	//debug('preset: copy', 'poly.'+(part.num+1), presets[part.num], dest, '\n');
	for(var index in Objs)
	{
		debug('copy', 'poly.'+(part.num+1)+'::'+Objs[index].pattr, presets[part.num], dest, '\n');
		var type = Objs[index].pattr;
		var types = {'object':0, 'hidden':0};
		if(!(type in types))
		{
			part.obj.set[index](part[index], dest);
		}
	}
	//storage.copy('poly.'+(part.num+1), presets[part.num], dest);
	//storage.recall('poly.'+(part.num+1), dest);
}

function copy_global_preset(src, dest)
{
	debug('copy global preset', 'copy', src, dest, '\n');
	storage.copy(src, dest);
	storage.recall(dest);
}

function clear_pattern(dest)
{
	/*for(var index in Objs)
	{
		//debug('clear', 'poly.'+(part.num+1)+'::'+Objs[index].pattr, dest, '\n');
		var type = Objs[index].pattr;
		var types = {'object':0, 'hidden':0};
		if(!(type in types))
		{
			part.obj.set[index](part[index], dest);
		}
	}*/
	var Part = dest;
	var pset = presets[Part.num];
	Part.obj.set.rulebends(default_pattern.slice());
	Part.obj.set.pattern(default_pattern.slice());
	Part.obj.set.behavior(default_pattern.slice());
	Part.obj.set.velocity(default_velocity.slice());
	Part.obj.set.duration(default_duration.slice());
	Part.obj.set.note(default_pattern.slice());
	Part.obj.set.basetime(1);
	Part.obj.set.timedivisor(4);
	Part.obj.set.notetype(0);
	Part.obj.set.notevalues(2);
	Part.obj.set.active(1);
	debug('clear_pattern', dest.num);
	//storage.copy('poly.'+(part.num+1), 16, dest.num+1);
	//storage.recall('poly.'+(part.num+1), dest.num+1);
}

function clear_global(dest)
{
	debug('clear_global', dest.num);
	storage.copy(16, dest.num+1);
	storage.recall(dest.num+1);
}

//reset all parts to play from top...quantized
function resync()
{
	/*var i=15;do{
		part[i].obj.offset.message('int', 0);
	}while(i--);*/
	messnamed(unique+'resync', 'bang');
}

//reset all parts to play from top...quantized
function resync_single(selected)
{
	selected.obj.resync.message('bang');
}

//begin or end sequence play from poly_play poly~
function play_sequence(part, note, press)
{
	if(press>0)
	{
		debug('play sequence', note);
		var trig = part.triggered.indexOf(note);
		//if the num wasn't already being held
		if(trig == -1)
		{
			debug('decoded:', (note>>6)%16, note>>10, '\n');
			part.triggered.push(note);
			part.obj.polyplay.message('midinote', note, 1);
		}
		else
		{
			//find out if num has already been played
			var held = part.held.indexOf(note);
			if(held > -1)
			{
				//remove from the held array since a new sequence has been triggered
				part.held.splice(held, 1);
				part.obj.polyplay.message('midinote', note, 0);
				var trig = part.triggered.indexOf(note);
				if(trig > -1)
				{
					part.triggered.splice(trig, 1);
				}
			}
		}
	}
	else
	{
		if(part.hold == 0)
		{
			var trig = part.triggered.indexOf(note);
			if(trig > -1)
			{
				part.triggered.splice(trig, 1);
			}
			part.obj.polyplay.message('midinote', note, 0);
		}
		else
		{
			//add to the held array, so that when hold for part is turned off the note can be flushed
			part.held.push(note);
		}
		refresh_c_keys();
	}
}

//update the current global transposition to all polys
function change_transpose(val)
{
	if(selected.channel==0)
	{
		debug('global_offset', val, '\n');
		global_offset = (Math.max(Math.min(val, 96), 0));
		transposegui.message('set', global_offset);
		for(var i = 0;i< 16;i++)
		{
			//this isn't stored with a preset
			//part[i].obj.noteoffset.message('int', global_offset + i);
			part[i].obj.set.noteoffset(global_offset+i);
		}
		_select_chain(selected.num);
	}
}

//called from key_in, change the loopOut point and update it to live.step and poly
function change_Out(val)
{
	debug('change Out', val, '\n');
	selected.obj.set.steps(val-parseInt(selected.nudge));
	update_step();
	refresh_c_keys();
}

//called from key_in, change the loopIn point and update it to the live.step and poly
function change_In(val)
{
	debug('change In', val, '\n');
	var change = parseInt(selected.nudge) - val;
	selected.nudge = val;
	if(timing_immediate)
	{
		selected.obj.set.nudge(selected.nudge);
		selected.steps += change;
		selected.obj.set.steps(selected.steps);
	}
	else
	{
		selected.obj.nudge.message('set', selected.nudge);
		selected.obj.set.nudge(selected.nudge, 0);
		//storage.setstoredvalue('poly.'+(selected.num+1)+'::nudgepattr', presets[selected.num], selected.nudge);
		selected.steps += change;
		selected.obj.set.steps(selected.steps);
		selected.obj.restart.message('bang');
	}
	update_step();
	refresh_c_keys();
}

//add a note from the pads to the appropriate poly, and trigger a message back from it
function add_note(part)
{
	debug('add_note', part.num, '\n');
	part.obj.addnote.message('bang');
	part.pattern[curSteps[part.num]]=1;
	part.obj.set.pattern(part.pattern);
	if((edit_preset == presets[part.num])&&(grid_mode==1))
	{
		storage.getstoredvalue('poly.'+(part.num+1)+'::pattern', edit_preset);
	}
	if(part==selected)
	{
		step.message('extra1', 1, selected.pattern);
		step.message('zoom', 1, 1);
		refresh_c_keys();
		mod.Send( 'cntrlr_encoder_grid', 'custom', selected.num%4, Math.floor(selected.num/4)%2,  selected.pattern);
		mod.Send( 'code_encoder_grid', 'custom', selected.num%8, Math.floor(selected.num/8),  selected.pattern);
	}
}

function play_note(part)
{
	debug('play_note', part.num, '\n');
	part.obj.addnote.message('bang');
}

/*//add new notes received from poly to the appropriate place and update display
function _addnote(num, val)
{
	num += -1;
	val += -1;
	debug('addnote', num, val, '\n');
	part[num].pattern[val] = 1;
	part[num].obj.set.pattern(part[num].pattern);
	refresh_c_keys();
	update_step();
}*/

//rotate the pattern based on the blocksize defined in the main patch
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
			part.duration.splice(Out, 0, parseInt(part.duration.splice(In, 1)));
			part.note.splice(Out, 0, parseInt(part.note.splice(In, 1)));
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
			part.note.splice(Out, 0, parseInt(part.note.splice(In, 1)));
		}
	}
	var pset = presets[part.num];
	part.obj.set.pattern(part.pattern);
	part.obj.set.velocity(part.velocity);
	part.obj.set.duration(part.duration);
	part.obj.set.note(part.note);
	update_step();
	refresh_c_keys();
}

//change the display on the CNTRLR encoder rings to reflect the current play position when in freewheel mode
function rotate_wheel(num, pos)
{
	if(codec_handler)
	{
		var _num = num-1;
		mod.Send( 'code_encoder_grid', 'value', _num%8, Math.floor(_num/8), pos);
	}
	if(pad_mode==5)
	{
		if((selected.num<8)&&(num<9))
		{
			var _num = num-1;
			if(grid_mode == 0){mod.Send( 'cntrlr_encoder_grid', 'value', _num%4, Math.floor(_num/4), pos);}
		}
		else if((selected.num>7)&&(num>8))
		{
			var _num = num-9;
			if(grid_mode == 0){mod.Send( 'cntrlr_encoder_grid', 'value', _num%4, Math.floor(_num/4), pos);}
		}
	}
	switch(grid_mode)
	{
		case 0:
			//debug('rotate_wheel', num, pos, '\n');
			if((key_mode==5)&&(num==selected.num+1))
			{
				//post('current_step', num, pos, '\n');
				mod.Send( 'receive_translation', 'keys2_'+(selected.note[current_step]), 'mask', -1);
				mod.Send( 'receive_translation', 'keys2_'+(selected.note[pos]), 'mask', 5);
			}
			break;
		case 1:
			//tr256 mode
			var _num = num-1;
			if((_num<14)&&(preset==edit_preset))
			{
				mod.Send( 'grid', 'mask', curSteps[_num], _num+2, -1);
				mod.Send( 'grid', 'mask', pos, _num+2, 5+(_num==selected.num));
			}
			break;
		case 2:
			if(altVal>0)
			{
			}
			break;
		case 3:
			//cafe mode
			//var pat = part[num-1].pattern.slice();
			var _num=num-1, Part = part[_num];
			//debug('cafe_pos', _num, Part.clutch)
			if(Part.clutch > 0)
			{
				var i=15;do{
						mod.Send( 'grid', 'value', i, _num, Part.pattern[(pos+i)%16]);
				}while(i--);
			}
			break;
		case 4:
			//boingg mode
			var _num=num-1;
			if(part[_num].active>0)
			{
				mod.Send( 'grid', 'mask', _num, curSteps[_num], -1);
				mod.Send( 'grid', 'mask', _num, pos, 1);
			}
			break;
		default:
			break;
	}
	current_step = pos;
	curSteps[num-1] = pos;
}

//synchronize two parts when holding down select while selecting another part
function sync_wheels(master, slave)
{
	debug('sync_wheels', master.num, slave.num, '\n');
	if(slave.lock != master.lock)
	{
		slave.lock = master.lock;
		slave.obj.set.quantize(slave.lock);
		mod.Send( 'cntrlr_encoder_grid', 'green', slave.num%4, Math.floor(slave.num/4)%2,  slave.lock);
		if(codec_handler){mod.Send( 'code_encoder_grid', 'green', slave.num%8, Math.floor(slave.num/8),  slave.lock);}
	}
	/*switch(master.lock)
	{
		case 0:
			//slave.obj.set.ticks(master.ticks);
			break;
		case 1:
			slave.obj.set.notevalues(master.notevalues);
			slave.obj.set.notetype(master.notetype);
			break;
	}*/
	slave.obj.set.timedivisor(master.obj.timedivisor.getvalueof());
	slave.obj.set.basetime(master.obj.basetime.getvalueof());
	update_speed(slave);
}

//change the variables necessary to change the quantization status of a part
function change_lock_status(part, dir)
{
	if(DEBUG_LOCK){post('change_lock_status', part.num, '\n');}
	if(dir==undefined){dir = 0;}
	if(part==selected)
	{
		update_gui();
	}
	mod.Send( 'cntrlr_encoder_grid', 'green', part.num%4, Math.floor(part.num/4)%2,	 part.notevalues<8);
	mod.Send( 'code_encoder_grid', 'green', part.num%8, Math.floor(part.num/8), part.notevalues<8);
	update_speed(part);
}

//update the current value reflected on the invisible ui speed controls
function update_speed(part)
{
	part.notevalues = part.obj.notevalues.getvalueof();
	part.notetype = part.obj.notetype.getvalueof();
	script['Speed'+(part.num+1)].message('set', part.obj.timedivisor.getvalueof());
}

//release any polyplay sequences from being held when the hold key is turned off
function release_held_sequences(part)
{
	//post('release held seqs', part.held, '\n');
	for(var i in part.held)
	{
		part.obj.polyplay.message('midinote', part.held[i], 0);
		var trig = part.triggered.indexOf(part.held[i]);
		if(trig > -1)
		{
			part.triggered.splice(trig, 1);
		}
	}
	part.held = [];
}

//change the hold state of the selected polyplay object
function poly_hold_toggle()
{
	selected.hold = Math.abs(selected.hold-1);
	//mod.Send( 'c_button', 3, 2, selected.hold);
	//grid_out('default', 'button', 3, 2, selected.hold);
	if(grid_mode==0){mod.Send( 'receive_translation', 'buttons_'+6, 'value', selected.hold);}
	if(grid_mode==3)
	{
		refresh_grid();
	}
	if(selected.hold<1)
	{
		release_held_sequences(selected);
	}
}

//set the dirty flag so that parts sequence is saved when selecting a new part or preset
function set_dirty(val)
{
	dirty=val;
	post('dirty:', val, '\n');
}


/*	  automation	 */


//enable recording of preset changes and mutes to a live.clip
function record(val)
{
	if(val > 0)
	{
		record_enabled = begin_record();
	}
	else
	{
		record_enabled = 0;
	}
	if(DEBUG_REC){post('record_enabled', record_enabled, '\n');}
}

//check api for current clip and return confirmation of recording
function begin_record()
{
	finder.goto('this_device');
	finder.goto('canonical_parent');
	var playing_slot_index = parseInt(finder.get('playing_slot_index'));
	if(DEBUG_REC){post('playing_slot_index:', playing_slot_index, '\n');}
	if(playing_slot_index>=0)
	{
		finder.goto('clip_slots', playing_slot_index, 'clip');
		autoclip.id = parseInt(finder.id);
	}
	return (parseInt(autoclip.id)>0);
}

//add automation steps directly to the attached Live clip
function add_automation(part, type, val)
{
	if(record_enabled)
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
		if(DEBUG_REC){post('notes:', new_notes, '\n');}
		finder.call('replace_selected_notes');
		finder.call('notes', num+1);
		for(var i = 0;i<new_notes.length;i+=6)
		{
			finder.call('note', new_notes[i+1], new_notes[i+2]+.001, new_notes[i+3]+.001, new_notes[i+4], new_notes[i+5]);
		}
		finder.call('done');
		//if(DEBUG_REC){post('new_notes:', finder.call('get_selected_notes'), '\n');}
	}
}

function receive_record(note, val)
{
	if(grid_mode==1)
	{
		if(val>0)
		{
			var i=15;do{
				if(note==part[i].noteoffset)
				{
					var Part=part[i], pat= Part.edit_buffer, cur_step=curSteps[i];
					Part.edit_buffer[cur_step] = 1;
					Part.pattern = Part.edit_buffer;
					Part.obj.pattern.message('list', Part.edit_buffer);
					Part.edit_velocity[cur_step] = val;
					Part.velocity = Part.edit_velocity;
					Part.obj.velocity.message('list', Part.edit_velocity);
					Part.recdirty=1;
					if(i<14)
					{
						mod.Send( 'grid', 'value',	cur_step, i+2, ACCENTS[Math.floor(val/8)]);
					}
					if(i==selected.num)
					{
						refresh_c_keys();
						step.message('velocity', 1, selected.velocity);
						step.message('extra1', 1, selected.pattern);
						step.message('zoom', 1, 1);
					}
				}
			}while(i--);
		}
	}
}

function set_record(val)
{
	rec_enabled=val;
	if(!rec_enabled)
	{
		storage.message('store', preset);
	}
	this.patcher.getnamed('midiout').subpatcher().getnamed('recgate').message(rec_enabled);
}


/*	 settings		*/


//all of these do , pretty much what they say
function randomize_pattern(global)
{
	if(global>0)
	{
		debug('global pattern random');
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
	update_step();
	refresh_c_keys();
}

function randomize_notes(global)
{
	if(global>0)
	{
		debug('global pattern random');
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random()*16);
				}while(j--);
				part[i].obj.set.note(seq, h+1);
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].note[j]=Math.round(Math.random()*16);
			}while(j--);
			part[i].obj.set.note(part[i].note);
		}while(i--);
	}
	update_step();
	refresh_c_keys();
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
	update_step();
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
	update_step();
}

function randomize_rulebends(global)
{
	if(global)
	{
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random()*15);
				}while(j--);
				part[i].obj.set.rulebends(seq, h+1);
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].rulebends[j]=Math.floor(Math.random()*15);
			}while(j--);
			part[i].obj.set.rulebends(part[i].rulebends);
		}while(i--);
	}
	update_step();
}

function randomize_behavior(global)
{
	if(global)
	{
		var h=15;do{
			var i=15;do{
				var seq = [];
				var j=15;do{
					seq[j]=Math.round(Math.random()*7);
				}while(j--);;
				part[i].obj.set.behavior(seq, h+1);
			}while(i--);
		}while(h--);
	}
	else
	{
		var i=15;do{
			var j=15;do{
				part[i].behavior[j]=Math.round(Math.random()*7);
			}while(j--);
			part[i].obj.set.behavior(part[i].behavior);
		}while(i--);
	}
	if(key_mode == 2)
	{
		refresh_c_keys();
	}
}

function randomize_rules()
{
	var i=6;do{
		var j=7;do{
			rulemap.message(i, j, Math.round(Math.random()*7));
		}while(j--);
	}while(i--);
}

function reset_data(global)
{
	var i=15;do{
		var Part = part[i];
		var pset = presets[Part.num];
		Part.obj.set.rulebends(default_pattern.slice());
		Part.obj.set.pattern(default_pattern.slice());
		Part.obj.set.behavior(default_pattern.slice());
		Part.obj.set.velocity(default_velocity.slice());
		Part.obj.set.duration(default_duration.slice());
		Part.obj.set.note(default_pattern.slice());
		Part.obj.set.basetime(1);
		Part.obj.set.timedivisor(4);
		Part.obj.set.notetype(0);
		Part.obj.set.notevalues(2);
		Part.obj.set.active(1);
	}while(i--);
	if(global)
	{
		var h=16;do{
			storage.message('store', h);
		}while(h--);
	}
	update_step();
	refresh_c_keys();
}

function init_storage()
{
	post('init_storage');
	var storage = this.patcher.getnamed('storage');
	var i=15;do{
		storage.setstoredvalue('poly.'+(i+1)+'::swingpattr', 1, .5);
		storage.setstoredvalue('poly.'+(i+1)+'::stepspattr', 1, 15);
		storage.setstoredvalue('poly.'+(i+1)+'::directionpattr', 1, 0);
		storage.setstoredvalue('poly.'+(i+1)+'::randompattr', 1, 0);
		storage.setstoredvalue('poly.'+(i+1)+'::nudgepattr', 1, 0);
		storage.setstoredvalue('poly.'+(i+1)+'::rulebends', 1, default_pattern.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::pattern', 1, default_pattern.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::behavior', 1, default_pattern.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::velocity', 1, default_velocity.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::duration', 1, default_duration.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::note', 1, default_pattern.slice());
		storage.setstoredvalue('poly.'+(i+1)+'::basetimepattr', 1, 1);
		storage.setstoredvalue('poly.'+(i+1)+'::timedivisorpattr', 1, 4);
		storage.setstoredvalue('poly.'+(i+1)+'::notetypepattr', 1, 0);
		storage.setstoredvalue('poly.'+(i+1)+'::notevaluepattr', 1, 2);
		storage.setstoredvalue('poly.'+(i+1)+'::active', 1, 1)
		storage.setstoredvalue('poly.'+(i+1)+'::behavior_enable', 1, 1);
	}while(i--);
	storage.message(1);
	var h=16;do{
		storage.message('store', h);
	}while(h--);
	post('done!\n');
}

//remove any masked elements on the CNTRLR
function demask()
{
	post('demask\n');
}

//update gui elements to reflect current data
function update_gui()
{
	directiongui.message('set', selected.obj.direction.getvalueof());
	notevaluesgui.message('set', selected.obj.notevalues.getvalueof());
	notetypegui.message('set', selected.obj.notetype.getvalueof());
	Random.message('set', selected.obj.random.getvalueof());
	Groove.message('set', (selected.obj.swing.getvalueof()*100)-50);
	Channel.message('set', selected.obj.channel.getvalueof());
	Mode.message('set', selected.obj.mode.getvalueof());
	BaseTime.message('set', selected.obj.basetime.getvalueof());
	PolyOffset.message('set', selected.obj.polyoffset.getvalueof());
	Speed.message('set', script['Speed'+(selected.num+1)].getvalueof());
	if((pad_mode == 6)||(key_mode == 6))
	{
		//mod.Send( 'c_button', 3, 2, selected.hold);
		//grid_out('default', 'button', 3, 2, selected.hold);
		outlet('receive_translation', 'buttons_'+6, selected.hold);
	}
}

//update the current bank assignment in Python
function update_bank()
{
	if(codec_handler)
	{
		mod.Send( 'code_encoder_grid', 'local', 0);
		var i=15;do{
			var x = i%8;
			var y = Math.floor(i/8);
			mod.Send( 'code_encoder_grid', 'mode', x, y, 4);
			mod.Send( 'code_encoder_grid', 'mode', x, y+2, 5);
			mod.Send( 'code_encoder_grid', 'custom', x, y, part[i].pattern);
			mod.Send( 'code_encoder_grid', 'green', x, y,	 part[i].lock);
		}while(i--);
	}
	switch(pad_mode)
	{
		default:
			//mod.Send( 'receive_device', 'set_mod_device_bank', selected.channel>0);
			//mod.Send( 'set_device_bank', selected.channel>0);
			mod.Send( 'receive_device', 'set_mod_device_bank', selected.channel>0 ? 1 : drumgroup_is_present ? 0 : 1);
			mod.Send( 'cntrlr_encoder_grid', 'local', 1);

			/*var i=7;do{
				params[Encoders[i]].hidden = 0;
				params[Speeds[i]].hidden = 1;
				params[Speeds[i+8]].hidden = 1;
			}while(i--);*/
			break;
		case 5:
			mod.Send( 'receive_device', 'set_mod_device_bank', 2+(selected.num>7));
			mod.Send( 'cntrlr_encoder_grid', 'local', 0);
			var r = (selected.num>7)*8;
			var i=7;do{
				/*params[Encoders[i]].hidden = 1;
				params[Speeds[i]].hidden = selected.num>7;
				params[Speeds[i+8]].hidden = selected.num<8;*/
				var x = i%4;
				var y = Math.floor(i/4);
				mod.Send( 'cntrlr_encoder_grid', 'mode', x, y, 4);
				mod.Send( 'cntrlr_encoder_grid', 'custom', x, y, part[i+r].pattern);
				mod.Send( 'cntrlr_encoder_grid', 'green', x, y,	 part[i+r].lock);
			}while(i--);
			var i=3;do{
				mod.Send( 'cntrlr_encoder_grid', 'mode', i, 2,	5);
				mod.Send( 'cntrlr_encoder_grid', 'green', i, 2, 0);
			}while(i--);
			break;
	}
	rotgate.message('int', codec_handler||((pad_mode==5)||(key_mode==5)||(grid_mode==1)||(grid_mode==2)||(grid_mode==3)||(grid_mode==4)));
}

//open the floating editor, called from MonomodComponent
function pop(val)
{
	post('pop', val, '\n');
	switch(val)
	{
		case 0:
			///this.patcher.parentpatcher.wind.sendtoback();
			messnamed(unique+'pop', 'close');
			break;
		case 1:
			//this.patcher.parentpatcher.front();
			messnamed(unique+'pop', 'open');
			var parent = this.patcher.parentpatcher.getnamed('hex_mod');
			parent.window('flags', 'nozoom');
			parent.window('flags', 'nogrow');
			parent.window('flags', 'float');
			parent.window('exec');
			break;
	}
}

function pop(){}

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
var Speeds = ['Speed1', 'Speed2', 'Speed3', 'Speed4', 'Speed5', 'Speed6', 'Speed7', 'Speed8', 'Speed9', 'Speed10', 'Speed11', 'Speed12', 'Speed13', 'Speed14', 'Speed15', 'Speed16'];
var Dials =	 ['Channel', 'Groove', 'Random', 'BaseTime', 'GlobSpeed', 'PolyOffset', 'Mode', 'RotSize', 'Speed'];
var Dial_Mappings = ['Encoder_8', 'Encoder_9', 'Encoder_10', 'Encoder_11', 'Encoder_11', 'Encoder_4', 'Encoder_5', 'Encoder_10', 'Encoder_6'];
Warning = ['missing', 'device', 'assignment', 'for', 'the', 'currently', 'selected', 'channel', ' ', ' ', ' ', ' '];

// called from init
function init_device()
{
	mod.Send('receive_device', 'set_mod_device_type', 'Hex');
	mod.Send( 'receive_device', 'set_number_params', 16);
	for(var dev_type in HEX_BANKS)
	{
		for(var bank_num in HEX_BANKS[dev_type])
		{
			mod.SendDirect('receive_device_proxy', 'set_bank_dict_entry', dev_type, bank_num, HEX_BANKS[dev_type][bank_num]);
		}
		//mod.Send('receive_device_proxy', 'update_parameters');
	}
	//debug('current parameters:', mod.Send('receive_device_proxy', 'current_parameters'));
	mod.Send('code_encoders_to_device', 'value', 1);
	mod.Send('create_alt_device_proxy', '_codec_device_proxy');
	for(var dev_type in CODEC_HEX_BANKS)
	{
		for(var bank_num in CODEC_HEX_BANKS[dev_type])
		{
			mod.SendDirect('receive_alt_device_proxy', '_codec_device_proxy', 'set_bank_dict_entry', dev_type, bank_num, CODEC_HEX_BANKS[dev_type][bank_num]);
		}
	}
	mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'set_number_params', 32);
	mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'set_mod_device_bank', 0);
	mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'fill_parameters_from_device');
	mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'set_params_report_change', 0);
	mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'set_params_control_prefix', 'CodecEncoder');
	//mod.Send( 'receive_alt_device_proxy', '_codec_device_proxy', 'set_mod_device', 'id', );
	//debug('parameters from client property:', mod.finder.get('parameters'));
	finder = new LiveAPI(callback, 'this_device');
	pns['device_name']=this.patcher.getnamed('device_name');
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]]=this.patcher.getnamed('pn'+(i+1));
		pns[Encoders[i]].message('text', ' ');
		mps[Encoders[i]]=this.patcher.getnamed('mp'+(i+1));
		mps[Encoders[i]].message('text', ' ');
		params[Encoders[i]]=this.patcher.getnamed(Encoders[i]);
		params[Encoders[i]].message('set', 0);
	}
	for(var i=0;i<8;i++)
	{
		params[Speeds[i]] = this.patcher.getnamed(Speeds[i]);
		params[Speeds[i+8]] = this.patcher.getnamed(Speeds[i+8]);
	}
	for(var i=0;i<9;i++)
	{
		params[Dials[i]]=this.patcher.getnamed(Dial_Mappings[i]);
		params[Dials[i]].message('set', 0);
	}
	detect_drumrack();
}

function detect_devices()
{
	this.patcher.getnamed('devices').front();
}

function detect_drumrack()
{
	//setup the initial API path:
	if(devices[0] > 0)
	{
		devices[0] = check_device_id(devices[0], selected.channel);
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
				drumgroup_is_present = true;
				debug("DrumRack found");
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
	debug('set_devices', ids, '\n');
	devices = ids;
}

//find the appointed_device
function detect_device(channel)
{
	debug('select_device \n');
	finder.goto('live_set', 'appointed_device');
	debug('device id ==', finder.id, '\n');
	if(check_device_id(parseInt(finder.id), channel)>0)
	{
		_select_chain(selected.num);
	}
	//this.patcher.getnamed('devices').wclose();
}

//check to make sure previous found_device is valid
function check_device_id(id, channel)
{
	var found = 0;
	debug('device_id', id, '\n');
	if(id>0)
	{
		if(channel == 0)
		{
			finder.id = id;
			if(finder.get('class_name')=='DrumGroupDevice')
			{
				drumgroup_is_present = true;
				found = parseInt(finder.id);
				debug('found at:', finder.get('name'));
			}
			else
			{
				finder.goto('canonical_parent');
				finder.goto('canonical_parent');
				if(finder.get('class_name')=='DrumGroupDevice')
				{
					drumgroup_is_present = true;
					found = parseInt(finder.id);
					debug('found at 2nd pass: ', finder.get('name'));
				}
			}
		}
		else
		{
			finder.id = id;
			found = parseInt(finder.id);
			debug('non-drumrack found at:', finder.get('name'));
		}
	}
	devices[channel] = found;
	this.patcher.getnamed('devices').subpatcher().getnamed('devices').message('list', devices);
	return found;
}

//send the current chain assignment to mod.js
function _select_chain(chain_num)
{
	debug('select_chain', chain_num, selected.channel, devices[selected.channel], '\n');
	if((selected.channel==0)&&(drumgroup_is_present))
	{
		debug( 'send_explicit', 'receive_device_proxy', 'set_mod_device_parent', 'id', devices[selected.channel] );
		mod.Send( 'send_explicit', 'receive_device_proxy', 'set_mod_device_parent', 'id', devices[selected.channel]);
		mod.Send( 'send_explicit', 'receive_device_proxy', 'set_mod_drum_pad', Math.max(0, Math.min(chain_num + global_offset - global_chain_offset, 112)));
	}
	else
	{
		debug( 'send_explicit', 'receive_device', 'set_mod_device_parent', 'id', devices[selected.channel], 1);
		mod.Send('send_explicit', 'receive_device_proxy', 'set_mod_device_parent', 'id', devices[selected.channel], 1);

	}
	//mod.Send( 'receive_device', 'refresh_lcd');
	if(devices[selected.channel]==0)
	{
		showerror();
	}
	update_bank();
}

//sort calls to the internal LCD
function _lcd(obj, type, val)
{
	//post('new_lcd', obj, type, val, '\n');
	debuglcd('lcd', obj, type, val, '\n');
	if((type=='lcd_name')&&(val!=undefined))
	{
		if(pns[obj])
		{
			pns[obj].message('text', val.replace(/_/g, ' '));
		}
	}
	else if((type == 'lcd_value')&&(val!=undefined))
	{
		if(mps[obj])
		{
			mps[obj].message('text', val.replace(/_/g, ' '));
		}
	}
	else if((type == 'encoder_value')&&(val!=undefined))
	{
		if(params[obj])
		{
			params[obj].message('set', val);
		}
	}
}

//distribute gui knobs to their destinations
function _encoder(num, val)
{
	debug('encoder in', num, val, '\n');
	if(num<12)
	{
		mod.Send( 'receive_device_proxy', 'set_mod_parameter_value', num, val);
	}
	else
	{
		switch(num)
		{
			case 12:
				//neither are pattr linked
				//selected.channel = val;
				//selected.polyenable = selected.channel > 0;
				//selected.obj.polyenable.message('int', selected.polyenable);
				selected.obj.set.polyenable(val>0);
				//selected.obj.channel.message('int', selected.channel);
				selected.obj.set.channel(val);
				_select_chain(selected.num);
				break;
			case 13:
				//selected.swing = (val+50)/100;
				//selected.obj.swing.message('float', selected.swing);
				selected.obj.set.swing((val+50)/100);
				post('swing val', val, '\n');
				break;
			case 14:
				//selected.random = val;
				//selected.obj.random.message('float', selected.random);
				selected.obj.set.random(val);
				break;
			case 15:
				rot_length = val;
				break;
			case 16:
				//not pattr linked or exposed
				//selected.repeat = val;
				//selected.obj.repeat.message('int', selected.repeat);
				//selected.obj.set.repeat(val);
				selected.obj.set.basetime(val);
				break;
			case 17:
				//global speed
				break;
			case 18:
				//not pattr linked
				//selected.polyoffset = val;
				//selected.obj.polyoffset.message('int', selected.polyoffset);
				selected.obj.set.polyoffset(val);
				break;
			case 19:
				//selected.mode = val;
				//selected.obj.mode.message('int', selected.mode);
				selected.obj.set.mode(val);
				break;
			case 20:
				//repeat
				break;
			case 21:
				script['Speed'+(selected.num+1)].message('int', val);
				break;
		}
	}
}

//called from invisible ui controls that the MonoDeviceComponent latches to in 2nd/3rd bank indexes
function _speed(num, val)
{
	debug('speed', num, val, '\n');
	var new_time = 8, Part = part[num];
	if(TIMES[val])
	{
		new_time = TIMES[val+''];
	}
	if(new_time!=Part.notevalues)
	{
		Part.obj.set.notevalues(new_time);
	}
	Part.obj.set.timedivisor(val);
	if(Part == selected)
	{
		notevaluesgui.message('set', new_time);
	}
	Part.obj.nexttime.message('bang');
}

function _adjust(num, val)
{
	//debug('adjust', num, val, '\n');
	switch(STEPMODES[step_mode])
	{
		case 'rulebends':
			var value = Math.floor(val/8);
			if(selected.rulebends[num]!=value)
			{
				selected.rulebends[num]=value;
				selected.obj.set.rulebends(selected.rulebends);
				step.message('extra2', num+1, value);
			}
			break;
		case 'velocity':
			var value = Math.floor(val/8);
			if(Math.floor(selected.velocity[num]/8)!=value)
			{
				selected.velocity[num]=value*8;
				selected.obj.set.velocity(selected.velocity);
				step.message('velocity', num+1, value*8);
			}
			break;
		case 'duration':
			var value = Math.floor(val/16);
			if(selected.duration[num]!=value)
			{
				selected.duration[num]=value;
				selected.obj.set.duration(selected.duration);
				step.message('duration', num+1, value);
			}
			break;
		case 'pitch':
			break;
	}
}

//called from visible ui elements and distributed to MonoDeviceComponent in 2nd/3rd bank indexes
function set_speed(num, val)
{
	debug('set_speed', num, val, '\n');
	script['Speed'+(num+1)].message('set', val);
	_speed(num, val);
}

//Used for UI warning. Uses the lcd objects to display an error message.
function showerror()
{
	pns.device_name.message('text', 'Detect Instrument');
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
	for(var i=0;i<12;i++)
	{
		pns[Encoders[i]].message('text', ' ');
	}
}

forceload(this);
