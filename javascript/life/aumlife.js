autowatch = 1;

inlets = 4;
outlets = 4;

var script = this;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);

var finder;
var mod;
var mod_finder;
var Mod = ModComponent.bind(script);

var Alive = false;
var slots_init = false;
var unique = jsarguments[1];
var alt_val = 0;
var last_mask = 0;
var solo = 0;
var mute = [1, 1, 1, 1]; 
var steps = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
var colors = [1, 2, 3, 4];
var key_colors = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0];
var plane = 0;
var solo = 0;
var preset = 1;
var lifeset = new JitterObject('jit.matrix', 'lifeset');
var repos = new JitterObject("jit.repos");
repos.boundmode=1;
repos.mode=1;
repos.offset_y = -1;
repos.outputmode="Normal";
var falling = new JitterMatrix(2, 'char', 16, 14);
var temp = new JitterMatrix(4, 'char', 16, 14);

var gravity = 0;
var imprint = 0;
var monoui = this.patcher.getnamed('monoui');
var gravityui = this.patcher.getnamed('gravityui');
var imprintui = this.patcher.getnamed('imprintui');

falling.setall(0, -1);
lifeset.clear();

var storage;

function init()
{
	mod = new Mod(script, 'life', unique, false);
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
	Alive = true;
	initialize(val);
}

function initialize()
{
	deprivatize_script_functions(script);
	storage = this.patcher.getnamed('life');
	for(var i=0;i<16;i++)
	{
		outlet(0, i, 14, 6 - steps[i]);
	}
	outlet(0, 0, 15, solo * 10);
	for(var i=0;i<4;i++)
	{
		outlet(0, i+12, 15, mute[i] * colors[i]);
	}
	mod.Send('set_legacy', 1);
	mod.Send('key', 'value', 1, 1);
	display_gameboard();
	storage.message('getslotlist');
}

function anything()
{
	args = arrayfromargs(messagename, arguments);
	debug('anything args', args);
	switch(inlet)
	{
		case 0:
			grid(args[0], args[1], args[2]);
			break;
		case 1:
			if(args[0]<5)
			{
				if(Alive)
				{
					plane = args[0]-1;
					var i=4;do{
						mod.Send('key', 'value', i, i==plane ? i+1 : 0);
					}while(i--);
					display_gameboard();
				}
			}
			break;
		case 2:
			step(args[0]);
			break;
	}
}

function step(num)
{
	if(alt_val == 0)
	{
		mod.Send('grid', 'mask', last_mask, 14, -1);
		last_mask = num;
		mod.Send('grid', 'mask', num, 14, 0);
		if(num==0)
		{
			if(imprint > 0)
			{
				for(var i=0;i<16;i++)
				{
					var cell = lifeset.getcell(i, 13);
					if(solo>0)
					{
						steps[i] = Math.floor(cell[plane]>0);
					}
					else
					{
						steps[i] = Math.floor(((cell[0] * mute[0]) + (cell[1] * mute[1]) + (cell[2] * mute[2]) + (cell[3] * mute[3]))>0);
					}
					outlet(0, i, 14, 6 - steps[i]);
				}
			}
			outlet(1, 'bang');
			if(gravity > 0)
			{
				debug('falling....');
				repos.matrixcalc([lifeset,falling],temp);
				lifeset.frommatrix(temp);
			}	 
		}
		display_gameboard();	
		if(steps[num]>0)
		{
			outlet(0, 'getcolumn', num);
		}
	}
}

function display_gameboard()
{
	for(var x=0;x<16;x++)
	{
		for(var y=0;y<14;y++)
		{
			var cell = lifeset.getcell(x, y);
			var empty = true;
			if(solo > 0)
			{
				outlet(0, x, y, (cell[plane]>0) * (plane+1));
			}
			else
			{
				for(var p=0;p<4;p++)
				{
					if((mute[p]>0)&&(cell[p]>0))
					{
						outlet(0, x, y, p + 1);
						var empty = false;
						break;
					}
				}
				if(empty == true)
				{
					outlet(0, x, y, 0);
				}
			}
		}
	}
}

function key(num, val)
{
	messnamed(unique+'key', num, val);
}

function _key_out(keyword, num, val)
{
	debug('key_out', num, val);
	mod.Send('key', 'value', num, val);
}

function grid(x, y, val)
{
	if((y< 14)&&(val > 0))
	{
		if(alt_val>0)
		{
			outlet(3, x, y, 'inc');
		}
		else
		{
			var cell = lifeset.getcell(x, y);
			cell[plane] = Math.abs(cell[plane] - 255);
			lifeset.setcell2d(x, y, cell[0], cell[1], cell[2], cell[3]);
			outlet(0, x, y, (cell[plane]/255) * colors[plane]);
		}
	}
	else if((y==14)&&(val>0))
	{
		steps[x] = Math.abs(steps[x]-1);
		for(var i=0;i<16;i++)
		{
			outlet(0, i, 14, 6 - steps[i]);
		}
	}
	else if((y==15)&&(val>0))
	{
		if(x == 11)
		{
			if(alt_val>0)
			{
				outlet(3, 'clear');
			}
			else
			{
				clear_plane();
			}
		}
		else if(x > 11)
		{
			mute[x-12]=Math.abs(mute[x-12]-1);
			for(var i=0;i<4;i++)
			{
				outlet(0, i+12, 15, mute[i] * colors[i]);
			}
			display_gameboard();
		}
		else if(x==0)
		{
			solo = Math.abs(solo-1);
			outlet(0, 0, 15, solo * 10);
			display_gameboard();
		}
		else
		{
			if(alt_val > 0)
			{
				debug('from grid store');
				store_preset(preset);
			}
			recall_preset(x);
		}
	}
}

function _grid_out(x, y, val)
{
	mod.Send('grid', 'value', x, y, val);
}

function alt(val)
{
	alt_val = val;
	if(alt_val > 0)
	{
		//display_presets();
		for(var i=0;i<14;i++)
		{
			mod.Send('grid', 'row', i, 0);
		}
		recall_preset(preset);
	}
	else
	{
		debug('from alt store');
		store_preset(preset);
		messnamed(unique+'refresh', 'bang');
	}
}

function store_preset(num)
{
	storage.message('store', num);
	debug('store_preset', num);
}

function recall_preset(num)
{
	preset = num;
	debug('recall_preset', num);
	for(var j=1;j<11;j++)
	{
		outlet(0, j, 15, Math.floor(j==preset) + 4);
	}
	storage.message('int', num);
	outlet(3, 'bang');
}

function slotlist()
{
	if(Alive)
	{
		var args = arrayfromargs(arguments);
		if(slots_init == false)
		{
			debug('initializing presets');
			for(var i=1;i<11;i++)
			{
				var exists = false;
				for(var j=0;j<args.length;j++)
				{
					if(args[j]==i)
					{
						exists = true;
					}
				}
				if(exists == false)
				{
					debug('resetting preset', i);
					outlet(3, 'clear');
					store_preset(i);
				}
			}
			slots_init = true;
		}		 
		debug('slotlist', args);
		recall_preset(1);
	}
}

function recall(num)
{
	debug('recalled', num);
	if(alt_val == 0)
	{
		//display_presets();
		display_gameboard();
	}
}

function preset_data(x, y, val)
{
	debug('preset_data', x, y, val);
	if(alt_val>0)
	{
		debug('grid value', x, y, val);
		mod.Send('grid', 'value', x, y, Math.floor(val>0)*6);
	}
	else if(alt_val==0)
	{
		if(val>0)
		{
			cell = lifeset.getcell(x, y);
			cell[plane] = 255;
			lifeset.setcell2d(x, y, cell[0], cell[1], cell[2], cell[3]);
			debug('setcell', x, y, val);
		}
		if((x==15)&&(y==13))
		{
			display_gameboard();
		}
	}
}

function clear_plane()
{
	for(var x=0;x<16;x++)
	{
		for(var y=0;y<14;y++)
		{
			cell = lifeset.getcell(x, y);
			cell[plane] = 0;
			lifeset.setcell2d(x, y, cell[0], cell[1], cell[2], cell[3]);
		}
	}
	display_gameboard();
}

function set_gravity(val)
{
	gravity = val;
}

function set_imprint(val)
{
	imprint = val;
}

function pattrstorage()
{
	args=arrayfromargs(arguments);
	debug('pattrstorage', args);
}

/*function display_presets()
{
	storage.message('getslotlist');
}*/

forceload(this);
	