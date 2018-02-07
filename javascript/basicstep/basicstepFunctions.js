autowatch = 1;

function _base_grid_out(x, y, val)
{
	mod.Send('base_grid', 'value', x, y, val);
	mod.Send('grid', 'value', x, y, val);
}

function _grid(x, y, val)
{
	outlet(0, 'base_grid', x, y, val);
}

function _base_grid(x, y, val)
{
	outlet(0, 'base_grid', x, y, val);
}

