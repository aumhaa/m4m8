autowatch = 1;

exports.Base = function()
{
	for(var i = 0;i < 16;i++)
	{
		mod.Send('add_translation', 'pads_'+i, 'base_grid', 'base_pads', i%4, Math.floor(i/4));
		mod.Send('add_translation', 'keys_'+i, 'base_grid', 'base_keys', (i%4)+4, Math.floor(i/4));
		mod.Send('add_translation', 'keys2_'+i, 'base_grid', 'base_keys2', (i%4)+4, Math.floor(i/4));
	}
	mod.Send('add_translation', 'pads_batch_fold', 'base_grid', 'base_pads', 0, 4);
	mod.Send('add_translation', 'keys_batch_fold', 'base_grid', 'base_keys', 0, 4);
	mod.Send('add_translation', 'keys2_batch_fold', 'base_grid', 'base_keys2', 0, 8, 4);
	for(var i=0;i<8;i++)
	{
		mod.Send('add_translation', 'buttons_'+i, 'key', 'base_buttons', i);
	}
	mod.Send('enable_translation_group', SYNTH ? 'base_pads' : 'base_keys', 0);
}