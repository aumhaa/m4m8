autowatch = 1;

var alt_val = 0;
var ccmutes=[];
var leader;

var last_grid = [];
for(var i=0;i<16;i++){
	last_grid[i] = [];
	for(var j=0;j<16;j++){
		last_grid[i][j] = 0;
	}
}

function initialize_instance()
{
	for(var i=0;i<8;i++)
	{
		ccmutes[i]=this.patcher.getnamed('ccmute['+i+']');
		ccmutes[i].val = ccmutes[i].getvalueof();
	}
	leader = this.patcher.getnamed('leader');
	leader.val = leader.getvalueof();
	mod.Send('set_legacy', 1);
	outlet(0, 'init');
}

function _alt(v)
{
	debug('alt in', v);
	alt_val = v;
	mod.Send('grid', 'batch_row', 0, 0);
	mod.Send('grid', 'batch_row', 15, 0);
	update_display(alt_val);
}

function update_display(v)
{
	if(v > 0)
	{
		leader.val = leader.getvalueof();
		for(var i=0;i<8;i++)
		{
			ccmutes[i].val = ccmutes[i].getvalueof();
			mod.Send('grid', 'value', i, 15, ccmutes[i].val);
			mod.Send('grid', 'value', i, 0, (leader.val==i)*6);
		}
	}
	else
	{
		mod.Send('grid', 'batch_row', 0, 0);
		mod.Send('grid', 'batch_row', 15, 0);
	}
}


function _grid(x, y, val)
{
	debug('grid', x, y, val);
	if(val> 0)
	{
		if(alt_val > 0)
		{
			if((y == 0)&&(x < 8))
			{
				leader.message(x);
			}
			else if((y == 15)&&(x < 8))
			{
				ccmutes[x].message('bang');
			}
			update_display(alt_val);
		}
		else
		{
			outlet(0, 'gravpoint', x/15, y/15);
		}
	}
}

function _key(num, val)
{
	if(val)
	{
		messnamed(unique+'key', num, 1);
	}
}

function _grid_in(x, y, val)
{
	debug('_grid_in', x, y, val);
	if(last_grid[x][y]!=val){
		last_grid[x][y]=val;
		mod.Send('grid', 'value', x, y, val);
	}
}

function _key_in(x, val)
{
	mod.Send('key', 'value', x, val);
}
