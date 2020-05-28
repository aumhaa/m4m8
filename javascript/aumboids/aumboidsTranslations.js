autowatch = 1;

/*exports.Push = function(mod)
{ 
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
}

exports.Base = function(mod)
{
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
}

exports.Code = function(mod)
{
	//Code stuff:
	for(var i = 0;i < 16;i++)
	{
		mod.Send( 'add_translation', 'pads_'+i, 'code_grid', 'code_pads', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys_'+i, 'code_grid', 'code_keys', i%8, Math.floor(i/8));
		mod.Send( 'add_translation', 'keys2_'+i, 'code_grid', 'code_keys2', i%8, Math.floor(i/8)+2);
	}
	mod.Send( 'add_translation', 'pads_batch', 'code_grid', 'code_pads', 0);
	mod.Send( 'add_translation', 'keys_batch', 'code_grid', 'code_keys', 0);
	mod.Send( 'add_translation', 'keys_batch_fold', 'code_grid', 'code_keys', 0, 8);
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
}

exports.CNTRLR = function(mod)
{
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
*/