autowatch = 1;

var stored = [];
for(var i = 0;i < 8;i++)
{
	stored[i] = [];
	for(var j = 0;j < 8;j++)
	{
		stored[i][j] = [];
		stored[i][j].inType = 0;
		stored[i][j].inId = -1;
		stored[i][j].outClient = 'all';
		stored[i][j].outScript = [];
	}
}

var curMsg = stored[0][0];

function anything()
{
	var args = arrayfromargs(arguments)
	//post('modRemote in', messagename, args, '\n');
	switch(messagename)
	{
		case 'current':
			if(args[2]>0)
			{
				curMsg = stored[args[0]][args[1]];
				//this.patcher.getnamed('inType').message('set', curMsg.inType);
				//this.patcher.getnamed('inId').message('set', curMsg.inId);
				if(curMsg.outClient=='all')
				{
					this.patcher.getnamed('outClient').message('set', 0);
				}
				else
				{
					this.patcher.getnamed('outClient').message('set', curMsg.outClient + 1);
				}
				this.patcher.getnamed('outScript').message('set', curMsg.outScript);
			}
			break;
		case 'inType':
			curMsg.inType = args[0];
			break;
		case 'inId':
			curMsg.inId = args[0];
			break;
		case 'outClient':
			if(args[0]!='all')
			{
				args[0] -= 1;
			}
			curMsg.outClient = args[0];
			notifyclients();
			break;
		case 'outScript':
			curMsg.outScript = args;
			notifyclients();
			break;
	}
}
			
function trigger(x, y)
{
	//post('trigger', x, y, '\n');
	if(stored[x][y].outScript.length>0)
	{
		switch(stored[x][y].outScript[0])
		{
			case 'multi':
				var multiScript = [];
				var tempScript = [];
				var outScript = stored[x][y].outScript.slice(1);
				while(outScript.length > 0)
				{
					if(outScript[0]=='|')
					{
						outScript.shift();
						multiScript.push(tempScript);
						tempScript = [];
					}
					else
					{
						tempScript.push(outScript.shift());
					}
				}
				for(var index in multiScript)
				{
					var curScript = multiScript[index];
					switch(curScript[0])
					{
						case 'press':
							var outScript = curScript.slice(1);
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', outScript, 1);
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', outScript, 0);
							break;
						case 'random':
							var outScript = curScript.slice(1);
							var tempScript = [];
							while(outScript.length > 0)
							{
								if(outScript[0]=='*r')
								{
									outScript.shift();
									tempScript.push(Math.floor((Math.random()*outScript.shift())+outScript.shift()));
								}
								else
								{
									tempScript.push(outScript.shift());
								}
							}
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript);
							//post('tempScript:', tempScript, '\n');
							break;
						case 'press_random':
							var outScript = curScript.slice(1);
							var tempScript = [];
							while(outScript.length > 0)
							{
								if(outScript[0]=='*r')
								{
									outScript.shift();
									tempScript.push(Math.floor((Math.random()*outScript.shift())+outScript.shift()));
								}
								else
								{
									tempScript.push(outScript.shift());
								}
							}
							//post('tempScript:', tempScript, '\n');
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript, 1);
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript, 0);
							break;
						case 'literal':
							outlet(0, 'send_hotline', curScript.slice(1));
							break;
						default:
							outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', curScript);
							break;
					}
				}
				break;
			case 'press':
				var outScript = stored[x][y].outScript.slice(1);
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', outScript, 1);
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', outScript, 0);
				break;
			case 'random':
				var outScript = stored[x][y].outScript.slice(1);
				var tempScript = [];
				while(outScript.length > 0)
				{
					if(outScript[0]=='*r')
					{
						outScript.shift();
						tempScript.push(Math.floor((Math.random()*outScript.shift())+outScript.shift()));
					}
					else
					{
						tempScript.push(outScript.shift());
					}
				}
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript);
				//post('tempScript:', tempScript, '\n');
				break;
			case 'press_random':
				var outScript = stored[x][y].outScript.slice(1);
				var tempScript = [];
				while(outScript.length > 0)
				{
					if(outScript[0]=='*r')
					{
						outScript.shift();
						tempScript.push(Math.floor((Math.random()*outScript.shift())+outScript.shift()));
					}
					else
					{
						tempScript.push(outScript.shift());
					}
				}
				//post('tempScript:', tempScript, '\n');
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript, 1);
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', tempScript, 0);
				break;
			case 'literal':
				outlet(0, 'send_hotline', stored[x][y].outScript.slice(1));
				break;
			default:
				outlet(0, 'send_hotline', stored[x][y].outClient, 'pipe', 'value', stored[x][y].outScript);
				break;
		}
	}
}


function getvalueof()
{
	//post('getvalueof\n');
    return mux();
}

function setvalueof()
{
    args=arrayfromargs(arguments);
	//post('setvalueof', args, '\n');
 	stored = [];
	for(var i = 0;i < 8;i++)
	{
		stored[i] = [];
		for(var j = 0;j < 8;j++)
		{
			stored[i][j] = [];
			stored[i][j].outClient=args.shift();
			var tempScript = args.shift();
			if(tempScript != 0)
			{
				stored[i][j].outScript=tempScript.split('^');
			}
			else 
			{
				stored[i][j].outScript = [];
			}
			//post('x', i, 'y', j, stored[i][j].outClient, stored[i][j].outScript, '\n');
		}
	}	   
}
			
function mux()
{
	new_data = [];
	for(var i = 0;i < 8;i++)
	{
		for(var j = 0;j < 8;j++)
		{
			//new_data.push('^');
			new_data.push(stored[i][j].outClient);
			if(stored[i][j].outScript.length>0)
			{
				new_data.push(stored[i][j].outScript.join('^'));
			}
			else
			{
				new_data.push(0);
			}
		}
	}
	return new_data;
}		