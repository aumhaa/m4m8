autowatch = 1;

exports.Base = function()
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
	mod.Send('enable_translation_group', 'base_keys', 0);
}

