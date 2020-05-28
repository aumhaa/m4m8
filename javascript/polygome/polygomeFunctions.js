autowatch = 1;

function initialize_instance()
{
	mod.Send('set_legacy', 1);
}

function _grid(x, y, val)
{
	outlet(0, 'grid', x, y, val ? 1 : 0);
}

function _key(x, val)
{
	outlet(0, 'key', x, val ? 1 : 0);
}

function _alt(val)
{
	outlet(0, 'alt', val ? 1 : 0);
}

function _grid_out(x, y, val)
{
	mod.Send('grid', 'value', x, y, val);
	mod.Send('push_grid', 'value', x, y, val);
}

function _key_out(x, val)
{
	mod.Send('key', 'value', x, val);
}

