# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

"""
Base_Map.py

Created by amounra on 2014-7-26.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""

USER_OFFSET = 10

SHIFT_LATCHING = False

CAP_BUTTON_TRANSLATIONS = False   #include the top 8 capacitive touch buttons in UserMode translations.

CHANNEL = 0		#main channel (0 - 15)

AFTERTOUCH = True   #when True, sends AT in instrument modes and UserMode.  When false, turns CC's off for instrument modes and transmits CC's in UserModes.

BASE_PADS = [60, 61, 62, 63, 64, 65, 66, 67, 52, 53, 54, 55, 56, 57, 58, 59, 44, 45, 46, 47, 48, 49, 50, 51, 36, 37, 38, 39, 40, 41, 42, 43]	#there are 16 of these

BASE_TOUCHSTRIPS = [1, 2, 3, 4, 5, 6, 7, 8, 9]		#there are 9 of these

BASE_TOUCHPADS = [10, 11, 12, 13, 14, 15, 16, 17]

BASE_BUTTONS = [18, 19, 20, 21, 22, 23, 24, 25]		#there are 16 of these

BASE_RUNNERS = [68, 69, 70, 71, 72, 73, 74, 75]

BASE_LCDS = [34, 35]

COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]

"""You can change the orientation of the Up, Down, Left, and Right buttons (where applicable) by changing the array.  The values correspond to the buttons from top to bottom."""
UDLR = [0, 1, 2, 3]

"""The values in this array determine the choices for what length of clip is created when "Fixed Length" is turned on:
0 = 1 Beat
1 = 2 Beat
2 = 1 Bar
3 = 2 Bars
4 = 4 Bars
5 = 8 Bars
6 = 16 Bars
7 = 32 Bars
"""
LENGTH_VALUES = [2, 3, 4]

CHANNELS = ['Ch. 2', 'Ch. 3', 'Ch. 4', 'Ch. 5', 'Ch. 6', 'Ch. 7', 'Ch. 8', 'Ch. 9', 'Ch. 10', 'Ch. 11', 'Ch. 12', 'Ch. 13', 'Ch. 14']

"""These are the scales we have available.  You can freely add your own scales to this """
SCALES = 	{'Mod':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Session':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Keys':[0,2,4,5,7,9,11,12,1,3,3,6,8,10,10,13],
			'Auto':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Chromatic':[0,1,2,3,4,5,6,7,8,9,10,11],
			'DrumPad':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
			'Major':[0,2,4,5,7,9,11],
			'Minor':[0,2,3,5,7,8,10],
			'Dorian':[0,2,3,5,7,9,10],
			'Mixolydian':[0,2,4,5,7,9,10],
			'Lydian':[0,2,4,6,7,9,11],
			'Phrygian':[0,1,3,5,7,8,10],
			'Locrian':[0,1,3,4,7,8,10],
			'Diminished':[0,1,3,4,6,7,9,10],
			'Whole-half':[0,2,3,5,6,8,9,11],
			'Whole_Tone':[0,2,4,6,8,10],
			'Minor_Blues':[0,3,5,6,7,10],
			'Minor_Pentatonic':[0,3,5,7,10],
			'Major_Pentatonic':[0,2,4,7,9],
			'Harmonic_Minor':[0,2,3,5,7,8,11],
			'Melodic_Minor':[0,2,3,5,7,9,11],
			'Dominant_Sus':[0,2,5,7,9,10],
			'Super_Locrian':[0,1,3,4,6,8,10],
			'Neopolitan_Minor':[0,1,3,5,7,8,11],
			'Neopolitan_Major':[0,1,3,5,7,9,11],
			'Enigmatic_Minor':[0,1,3,6,7,10,11],
			'Enigmatic':[0,1,4,6,8,10,11],
			'Composite':[0,1,4,6,7,8,11],
			'Bebop_Locrian':[0,2,3,5,6,8,10,11],
			'Bebop_Dominant':[0,2,4,5,7,9,10,11],
			'Bebop_Major':[0,2,4,5,7,8,9,11],
			'Bhairav':[0,1,4,5,7,8,11],
			'Hungarian_Minor':[0,2,3,6,7,8,11],
			'Minor_Gypsy':[0,1,4,5,7,8,10],
			'Persian':[0,1,4,5,6,8,11],
			'Hirojoshi':[0,2,3,7,8],
			'In-Sen':[0,1,5,7,10],
			'Iwato':[0,1,5,6,10],
			'Kumoi':[0,2,3,7,9],
			'Pelog':[0,1,3,4,7,8],
			'Spanish':[0,1,3,4,5,6,8,10]
			}

SCALEABBREVS = {'Auto':'-A','Keys':'-K','Chromatic':'12','DrumPad':'-D','Major':'M-','Minor':'m-','Dorian':'II','Mixolydian':'V',
			'Lydian':'IV','Phrygian':'IH','Locrian':'VH','Diminished':'d-','Whole-half':'Wh','Whole_Tone':'WT','Minor_Blues':'mB',
			'Minor_Pentatonic':'mP','Major_Pentatonic':'MP','Harmonic_Minor':'mH','Melodic_Minor':'mM','Dominant_Sus':'D+','Super_Locrian':'SL',
			'Neopolitan_Minor':'mN','Neopolitan_Major':'MN','Enigmatic_Minor':'mE','Enigmatic':'ME','Composite':'Cp','Bebop_Locrian':'lB',
			'Bebop_Dominant':'DB','Bebop_Major':'MB','Bhairav':'Bv','Hungarian_Minor':'mH','Minor_Gypsy':'mG','Persian':'Pr',
			'Hirojoshi':'Hr','In-Sen':'IS','Iwato':'Iw','Kumoi':'Km','Pelog':'Pg','Spanish':'Sp'}


"""This is the default scale used by Auto when something other than a drumrack is detected for the selected track"""
DEFAULT_AUTO_SCALE = 'Major'

"""This is the default Vertical Offset for any scale other than DrumPad """
DEFAULT_VERTOFFSET = 4

"""This is the default NoteOffset, aka RootNote, used for scales other than DrumPad"""
DEFAULT_OFFSET = 48

"""This is the default NoteOffset, aka RootNote, used for the DrumPad scale;  it is a multiple of 4, so an offset of 4 is actually a RootNote of 16"""
DEFAULT_DRUMOFFSET = 9

"""This is the default Scale used for all MIDI Channels"""
DEFAULT_SCALE = 'Auto'

"""This is the default SplitMode used for all MIDI Channels"""
DEFAULT_MODE = 'seq'

SCALENAMES = [scale for scale in sorted(SCALES.iterkeys())]

"""It is possible to create a custom list of scales to be used by the script.  For instance, the list below would include major, minor, auto, drumpad, and chromatic scales, in that order."""
#SCALENAMES = ['Major', 'Minor', 'Auto', 'DrumPad', 'Chromatic']

DEFAULT_INSTRUMENT_SETTINGS = {'Scales':SCALES, 
								'ScaleAbbrevs':SCALEABBREVS, 
								'ScaleNames':SCALENAMES,
								'DefaultAutoScale':DEFAULT_AUTO_SCALE,
								'DefaultVertOffset':DEFAULT_VERTOFFSET,
								'DefaultOffset':DEFAULT_OFFSET,
								'DefaultDrumOffset':DEFAULT_DRUMOFFSET,
								'DefaultScale':DEFAULT_SCALE,
								'DefaultMode':DEFAULT_MODE,
								'Channels':CHANNELS}

class BaseColors:


	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

	class MainModes:
		Clips = LividRGB.WHITE
		Clips_shifted = LividRGB.BlinkFast.WHITE
		Sends = LividRGB.MAGENTA
		Sends_shifted = LividRGB.BlinkFast.MAGENTA
		Device = LividRGB.CYAN
		Device_shifted = LividRGB.BlinkFast.CYAN
		User = LividRGB.RED
		User_shifted = LividRGB.BlinkFast.RED
	

	class Session:
		StopClipTriggered = LividRGB.BlinkFast.BLUE
		StopClip = LividRGB.BLUE
		Scene = LividRGB.CYAN
		NoScene = LividRGB.OFF
		SceneTriggered = LividRGB.BlinkFast.BLUE
		ClipTriggeredPlay = LividRGB.BlinkFast.GREEN
		ClipTriggeredRecord = LividRGB.BlinkFast.RED
		RecordButton = LividRGB.OFF
		ClipEmpty = LividRGB.OFF
		ClipStopped = LividRGB.WHITE
		ClipStarted = LividRGB.GREEN
		ClipRecording = LividRGB.RED
		NavigationButtonOn = LividRGB.BLUE
		PageNavigationButtonOn = LividRGB.CYAN
		Empty = LividRGB.OFF
	

	class NoteEditor:

		class Step:
			Low = LividRGB.CYAN
			High = LividRGB.WHITE 
			Full = LividRGB.YELLOW
			Muted = LividRGB.YELLOW
			StepEmpty = LividRGB.OFF
		

		class StepEditing:
			High = LividRGB.GREEN
			Low = LividRGB.CYAN
			Full = LividRGB.YELLOW
			Muted = LividRGB.WHITE
		

		StepEmpty = LividRGB.OFF
		StepEmptyBase = LividRGB.OFF
		StepEmptyScale = LividRGB.OFF
		StepDisabled = LividRGB.OFF
		Playhead = Color(31)
		PlayheadRecord = Color(31)
		StepSelected = LividRGB.GREEN
		QuantizationSelected = LividRGB.RED
		QuantizationUnselected = LividRGB.MAGENTA
	

	class LoopSelector:
		Playhead = LividRGB.YELLOW
		OutsideLoop = LividRGB.BLUE
		InsideLoopStartBar = LividRGB.CYAN
		SelectedPage = LividRGB.WHITE
		InsideLoop = LividRGB.CYAN
		PlayheadRecord = LividRGB.RED
	

	class DrumGroup:
		PadAction = LividRGB.WHITE
		PadFilled = LividRGB.GREEN
		PadFilledAlt = LividRGB.MAGENTA
		PadSelected = LividRGB.WHITE
		PadSelectedNotSoloed = LividRGB.WHITE
		PadEmpty = LividRGB.OFF
		PadMuted = LividRGB.YELLOW
		PadSoloed = LividRGB.CYAN
		PadMutedSelected = LividRGB.BLUE
		PadSoloedSelected = LividRGB.BLUE
		PadInvisible = LividRGB.OFF
		PadAction = LividRGB.RED
	

	class Mixer:
		SoloOn = LividRGB.CYAN
		SoloOff = LividRGB.OFF
		MuteOn = LividRGB.YELLOW
		MuteOff = LividRGB.OFF
		ArmSelected = LividRGB.GREEN
		ArmUnselected = LividRGB.RED
		ArmOff = LividRGB.OFF
		StopClip = LividRGB.BLUE
		SelectedOn = LividRGB.BLUE
		SelectedOff = LividRGB.OFF
	

	class Recording:
		On = LividRGB.BlinkFast.GREEN
		Off = LividRGB.GREEN
		Transition = LividRGB.BlinkSlow.GREEN
	

	class Recorder:
		On = LividRGB.WHITE
		Off = LividRGB.BLUE
		NewOn = LividRGB.BlinkFast.YELLOW
		NewOff = LividRGB.YELLOW
		FixedOn = LividRGB.BlinkFast.CYAN
		FixedOff = LividRGB.CYAN
		RecordOn = LividRGB.BlinkFast.GREEN
		RecordOff = LividRGB.GREEN
		FixedAssigned = LividRGB.MAGENTA
		FixedNotAssigned = LividRGB.OFF
		OverdubOn = LividRGB.BlinkFast.RED
		OverdubOff = LividRGB.RED
	

	class Transport:
		OverdubOn = LividRGB.BlinkFast.RED
		OverdubOff = LividRGB.RED
		StopOn = LividRGB.BLUE
		StopOff = LividRGB.BLUE
	

	class Sequencer:
		OctaveOn = LividRGB.BlinkFast.CYAN
		OctaveOff = LividRGB.OFF
		On = LividRGB.WHITE
		Off = LividRGB.OFF
	

	class Device:
		NavOn = LividRGB.MAGENTA
		NavOff = LividRGB.OFF
		BankOn = LividRGB.YELLOW
		BankOff = LividRGB.OFF
		ChainNavOn = LividRGB.RED
		ChainNavOff = LividRGB.OFF
		ContainNavOn = LividRGB.CYAN
		ContainNavOff = LividRGB.OFF
	

	class DeviceNavigator:
		DevNavOff = LividRGB.OFF
		DevNavOn = LividRGB.MAGENTA
		ChainNavOn = LividRGB.RED
		ChainNavOff = LividRGB.OFF
		LevelNavOn = LividRGB.CYAN
		LevelNavOff = LividRGB.OFF
	

	class Mod:
		class Nav:
			OnValue = LividRGB.RED
			OffValue = LividRGB.WHITE
		
	

	class MonoInstrument:

		PressFlash = LividRGB.WHITE
		OffsetOnValue = LividRGB.GREEN
		OffsetOffValue = LividRGB.OFF
		ScaleOffsetOnValue = LividRGB.RED
		ScaleOffsetOffValue = LividRGB.OFF
		SplitModeOnValue = LividRGB.WHITE
		SplitModeOffValue = LividRGB.OFF
		SequencerModeOnValue = LividRGB.CYAN
		SequencerModeOffValue = LividRGB.OFF
		DrumOffsetOnValue = LividRGB.MAGENTA
		DrumOffsetOffValue = LividRGB.OFF
		VerticalOffsetOnValue = LividRGB.BLUE
		VerticalOffsetOffValue = LividRGB.OFF

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
		

	

	class Translation:

		SelectorOn = LividRGB.WHITE
		SelectorOff = LividRGB.OFF

		class Channel_10:
			Pad_0 = LividRGB.OFF
			Pad_1 = LividRGB.OFF
			Pad_2 = LividRGB.OFF
			Pad_3 = LividRGB.OFF
			Pad_4 = LividRGB.OFF
			Pad_5 = LividRGB.OFF
			Pad_6 = LividRGB.OFF
			Pad_7 = LividRGB.OFF
			Pad_8 = LividRGB.OFF
			Pad_9 = LividRGB.OFF
			Pad_10 = LividRGB.OFF
			Pad_11 = LividRGB.OFF
			Pad_12 = LividRGB.OFF
			Pad_13 = LividRGB.OFF
			Pad_14 = LividRGB.OFF
			Pad_15 = LividRGB.OFF
			Pad_16 = LividRGB.OFF
			Pad_17 = LividRGB.OFF
			Pad_18 = LividRGB.OFF
			Pad_19 = LividRGB.OFF
			Pad_20 = LividRGB.OFF
			Pad_21 = LividRGB.OFF
			Pad_22 = LividRGB.OFF
			Pad_23 = LividRGB.OFF
			Pad_24 = LividRGB.OFF
			Pad_25 = LividRGB.OFF
			Pad_26 = LividRGB.OFF
			Pad_27 = LividRGB.OFF
			Pad_28 = LividRGB.OFF
			Pad_29 = LividRGB.OFF
			Pad_30 = LividRGB.OFF
			Pad_31 = LividRGB.OFF
		

		class Channel_11:
			Pad_0 = LividRGB.OFF
			Pad_1 = LividRGB.OFF
			Pad_2 = LividRGB.OFF
			Pad_3 = LividRGB.OFF
			Pad_4 = LividRGB.OFF
			Pad_5 = LividRGB.OFF
			Pad_6 = LividRGB.OFF
			Pad_7 = LividRGB.OFF
			Pad_8 = LividRGB.OFF
			Pad_9 = LividRGB.OFF
			Pad_10 = LividRGB.OFF
			Pad_11 = LividRGB.OFF
			Pad_12 = LividRGB.OFF
			Pad_13 = LividRGB.OFF
			Pad_14 = LividRGB.OFF
			Pad_15 = LividRGB.OFF
			Pad_16 = LividRGB.OFF
			Pad_17 = LividRGB.OFF
			Pad_18 = LividRGB.OFF
			Pad_19 = LividRGB.OFF
			Pad_20 = LividRGB.OFF
			Pad_21 = LividRGB.OFF
			Pad_22 = LividRGB.OFF
			Pad_23 = LividRGB.OFF
			Pad_24 = LividRGB.OFF
			Pad_25 = LividRGB.OFF
			Pad_26 = LividRGB.OFF
			Pad_27 = LividRGB.OFF
			Pad_28 = LividRGB.OFF
			Pad_29 = LividRGB.OFF
			Pad_30 = LividRGB.OFF
			Pad_31 = LividRGB.OFF
		

		class Channel_12:
			Pad_0 = LividRGB.OFF
			Pad_1 = LividRGB.OFF
			Pad_2 = LividRGB.OFF
			Pad_3 = LividRGB.OFF
			Pad_4 = LividRGB.OFF
			Pad_5 = LividRGB.OFF
			Pad_6 = LividRGB.OFF
			Pad_7 = LividRGB.OFF
			Pad_8 = LividRGB.OFF
			Pad_9 = LividRGB.OFF
			Pad_10 = LividRGB.OFF
			Pad_11 = LividRGB.OFF
			Pad_12 = LividRGB.OFF
			Pad_13 = LividRGB.OFF
			Pad_14 = LividRGB.OFF
			Pad_15 = LividRGB.OFF
			Pad_16 = LividRGB.OFF
			Pad_17 = LividRGB.OFF
			Pad_18 = LividRGB.OFF
			Pad_19 = LividRGB.OFF
			Pad_20 = LividRGB.OFF
			Pad_21 = LividRGB.OFF
			Pad_22 = LividRGB.OFF
			Pad_23 = LividRGB.OFF
			Pad_24 = LividRGB.OFF
			Pad_25 = LividRGB.OFF
			Pad_26 = LividRGB.OFF
			Pad_27 = LividRGB.OFF
			Pad_28 = LividRGB.OFF
			Pad_29 = LividRGB.OFF
			Pad_30 = LividRGB.OFF
			Pad_31 = LividRGB.OFF
		

		class Channel_13:
			Pad_0 = LividRGB.OFF
			Pad_1 = LividRGB.OFF
			Pad_2 = LividRGB.OFF
			Pad_3 = LividRGB.OFF
			Pad_4 = LividRGB.OFF
			Pad_5 = LividRGB.OFF
			Pad_6 = LividRGB.OFF
			Pad_7 = LividRGB.OFF
			Pad_8 = LividRGB.OFF
			Pad_9 = LividRGB.OFF
			Pad_10 = LividRGB.OFF
			Pad_11 = LividRGB.OFF
			Pad_12 = LividRGB.OFF
			Pad_13 = LividRGB.OFF
			Pad_14 = LividRGB.OFF
			Pad_15 = LividRGB.OFF
			Pad_16 = LividRGB.OFF
			Pad_17 = LividRGB.OFF
			Pad_18 = LividRGB.OFF
			Pad_19 = LividRGB.OFF
			Pad_20 = LividRGB.OFF
			Pad_21 = LividRGB.OFF
			Pad_22 = LividRGB.OFF
			Pad_23 = LividRGB.OFF
			Pad_24 = LividRGB.OFF
			Pad_25 = LividRGB.OFF
			Pad_26 = LividRGB.OFF
			Pad_27 = LividRGB.OFF
			Pad_28 = LividRGB.OFF
			Pad_29 = LividRGB.OFF
			Pad_30 = LividRGB.OFF
			Pad_31 = LividRGB.OFF
		

	








	