
autowatch = 1;

//jsarguments[1] = dim_x;
//jsarguments[2] = dim_y;
data = [];


function dump()
{
	data = arrayfromargs(arguments);
	// = array;
	//post('received dump', data, '\n');
	notifyclients();
}
function getvalueof()
{	
	//post('getvalueof')
	return data;
}

function setvalueof()
{
	data = arrayfromargs(arguments);
	//post('setvalueof')
	outlet(0, 'restore', data);
}
