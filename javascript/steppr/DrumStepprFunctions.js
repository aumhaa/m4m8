autowatch = 1;

var error_text="Drum Stepp:r requires a properly configured Drum Rack. Place one on this track then press here to initialize. Press the ? button for more help.";
var error_rect=[104, 56, 355, 49];
var count_error_text="Drum Steppr:r requires 16 chains to be present in the Drum Rack. Add more chains and press here to initialize.";

var Dials =	 ['Repeat', 'Groover', 'Random', 'RotSize'];

var DEVICE_BANKS = {'InstrumentGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'DrumGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'MidiEffectGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'Operator':[['Osc-A Level', 'Osc-B Level', 'Osc-C Level', 'Osc-D Level', 'Transpose', 'Filter Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'UltraAnalog':[['AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'OSC1 Semi', 'F1 Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'OriginalSimpler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'MultiSampler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'LoungeLizard':[['M Force', 'F Release', 'F Tone Decay', 'F Tone Vol', 'Semitone', 'P Distance', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'StringStudio':[['E Pos', 'Exc ForceMassProt', 'Exc FricStiff', 'Exc Velocity', 'Semitone', 'Filter Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'Collision':[['Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release', 'Res 1 Tune', 'Res 1 Brightness', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'InstrumentImpulse':[['1 Start', '1 Envelope Decay', '1 Stretch Factor', 'Global Time', 'Global Transpose', '1 Filter Freq', 'Mod_Chain_Pan', 'Mod_Chain_Vol', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'NoDevice':[['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']]}

//find the drumrack
function detect_devices()
{
	//setup the initial API path:
	found_device = 0;
	finder.goto('this_device');
	var this_id = parseInt(finder.id);
	finder.goto('canonical_parent');
	var track_id = parseInt(finder.id);
	var devices = finder.getcount('devices');
	for (var i=0;i<devices;i++)
	{
		finder.id = track_id;
		finder.goto('devices', i);
		if(finder.get('class_name')=='DrumGroupDevice')
		{
			debug("DrumRack found", finder.get('name'));
			found_device = parseInt(finder.id);
			break;
		}
	}
	if(found_device == 0)
	{
		showerror();
	}
	else
	{
		finder.id = found_device;
		debug('chains:', finder.getcount('chains'));
		if(finder.getcount('chains')<16)
		{
			showCountError();
		}
		else
		{
			hideerror();
		}
		report_drumrack_id();
	}
}

//send the drumrack id to mod.js
function report_drumrack_id()
{
	//mod.Send('set_device_parent', found_device);
	mod.Send('send_explicit', 'receive_device', 'set_mod_device_parent', 'id', found_device);
	select_chain(chain);
}


