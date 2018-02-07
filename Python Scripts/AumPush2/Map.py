# by amounra 0914 : http://www.aumhaa.com


from aumhaa.v2.livid.colors import *

DEVICE_COLORS = {'midi_effect':2,
				'audio_effect':5,
				'instrument':7,
				'Operator':3,
				'DrumGroupDevice':6,
				'MxDeviceMidiEffect':4,
				'MxDeviceInstrument':4,
				'MxDeviceAudioEffect':4,
				'InstrumentGroupDevice':1,
				'MidiEffectGroupDevice':1,
				'AudioEffectGroupDevice':1}


class AumPushColors:


	class Mod:
		
		class Nav:
			OnValue = LividRGB.RED
			OffValue = LividRGB.WHITE
		

	class MonoInstrument:

		PressFlash = LividRGB.WHITE
		OffsetOnValue = LividRGB.GREEN
		ScaleOffsetOnValue = LividRGB.RED
		SplitModeOnValue = LividRGB.WHITE
		SequencerModeOnValue = LividRGB.CYAN
		DrumOffsetOnValue = LividRGB.MAGENTA
		VerticalOffsetOnValue = LividRGB.BLUE

		class Keys:
			SelectedNote = LividRGB.GREEN
			RootWhiteValue = LividRGB.RED
			RootBlackValue = LividRGB.MAGENTA
			WhiteValue = LividRGB.CYAN
			BlackValue = LividRGB.BLUE
	

		class Drums:
			SelectedNote = LividRGB.BLUE
			EvenValue = LividRGB.GREEN
			OddValue = LividRGB.MAGENTA
		

	

