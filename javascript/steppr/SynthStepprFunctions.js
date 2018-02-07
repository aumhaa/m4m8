autowatch = 1;

var error_text="Synth Stepp:r requires an Instrument. Place one on this track then press here to initialize. Press the ? button for more help.";
var enc_max = 6; //we only link 6 encoders to the API in synth mode.
var error_rect=[142, 32, 311, 79];

var Dials = ['Repeater', 'Groover', 'Random', 'RotSize'];

var DEVICE_BANKS = {'InstrumentGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'DrumGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'MidiEffectGroupDevice':[['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'Operator':[['Osc-A Level', 'Osc-B Level', 'Osc-C Level', 'Osc-D Level', 'Transpose', 'Filter Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'UltraAnalog':[['AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'OSC1 Semi', 'F1 Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'OriginalSimpler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'MultiSampler':[['Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Transpose', 'Filter Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'LoungeLizard':[['M Force', 'F Release', 'F Tone Decay', 'F Tone Vol', 'Semitone', 'P Distance', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'StringStudio':[['E Pos', 'Exc ForceMassProt', 'Exc FricStiff', 'Exc Velocity', 'Semitone', 'Filter Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'Collision':[['Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release', 'Res 1 Tune', 'Res 1 Brightness', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'InstrumentImpulse':[['1 Start', '1 Envelope Decay', '1 Stretch Factor', 'Global Time', 'Global Transpose', '1 Filter Freq', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']],
			'NoDevice':[['None', 'None', 'None', 'None', 'None', 'None', 'ModDevice_chord_steps', 'ModDevice_chord_thin', 'ModDevice_Repeat', 'ModDevice_Groover', 'ModDevice_Random', 'ModDevice_RotSize']]}

//find the synth
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
		if(parseInt(finder.id)!=this_id)
		{
			var found = 0;
			for(var j in LiveClassNames)
			{
				if(finder.get('class_name')==LiveClassNames[j])
				{
					found = 1;
					break;
				}
			}
			if(found>0)
			{
				debug("Synth found");
				found_device = parseInt(finder.id);
			}
		}
	}
	if(found_device == 0)
	{
		showerror();
	}
	else
	{
		hideerror();
		report_drumrack_id();
	}
}

//send the drumrack id to mod.js
function report_drumrack_id()
{
	mod.Send('send_explicit', 'receive_device', 'set_mod_device', 'id', found_device);
	//mod.Send('set_device', found_device);
}


