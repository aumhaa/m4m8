# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

"""
Cntrlr_Map.py

Created by amounra on 2010-10-05.
Copyright (c) 2010 __aumhaa__. All rights reserved.
http://www.aumhaa.com

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""

CHANNEL = 0		#main channel (0 - 15)

FADER_BANKING = False	#When "True", the faders will be remapped to a User channel when in modMode.

DIAL_BANKING = False		#When "True", the dials will be remapped to a User channel when in modMode.

EQS_INSTEAD_OF_MACROS = False  #Maps right dials to EQs when "True"

SHIFT_LOCK = False		#Setting this flag to "True" will allow the shift control to be toggled when pressed quickly in the same manner as the top mode buttons.

FREE_ENCODER_IS_CROSSFADER = False   #Setting this flag to "True" will cause the second top encoder to be assigned to the crossfader 

CNTRLR_BUTTONS = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]  #there are 16x2 of these

CNTRLR_GRID = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]	#there are 4x4 of these

CNTRLR_FADERS = [4, 8, 12, 16, 20, 24, 28, 32]		#there are 8 of these

CNTRLR_KNOBS_LEFT = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]	#there are 12 of these

CNTRLR_KNOBS_RIGHT = [17, 21, 25, 29, 18, 22, 26, 30, 19, 23, 27, 31]		#there are 12 of these

CNTRLR_DIALS = [48, 51, 54, 57, 49, 52, 55, 58, 50, 53, 56, 59]		#there are 12 of these

CNTRLR_DIAL_BUTTONS = [48, 51, 54, 57, 49, 52, 55, 58, 50, 53, 56, 59]		#there are 12 of these

FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track

COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]


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

class CntrlrColors:


	ResetSendsColor = LividRGB.MAGENTA

	class ModeButtons:
		ModSwitcher = LividRGB.BlinkMedium.CYAN
		ModSwitcherDisabled = LividRGB.CYAN
		Translations = LividRGB.BlinkMedium.MAGENTA
		TranslationsDisabled = LividRGB.MAGENTA
		DeviceSelector = LividRGB.BlinkMedium.YELLOW
		DeviceSelectorDisabled = LividRGB.YELLOW
	

	class ShiftButtons:
		SessionOn = LividRGB.YELLOW
		SessionOff = LividRGB.OFF
	

	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

	class Session:
		StopClipTriggered = LividRGB.BlinkFast.BLUE
		StopClip = LividRGB.WHITE
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
		NavigationButtonOn = LividRGB.CYAN
		NavigationButtonOff = LividRGB.YELLOW
		PageNavigationButtonOn = LividRGB.BLUE
		PageNavigationButtonOff = LividRGB.OFF
		ZoomOn = LividRGB.BlinkFast.WHITE
		ZoomOff = LividRGB.WHITE
	

	class Zooming:
		Selected = LividRGB.BlinkFast.YELLOW
		Stopped = LividRGB.WHITE
		Playing = LividRGB.GREEN
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
	

	class Transport:
		PlayOn = LividRGB.BlinkMedium.GREEN
		PlayOff = LividRGB.GREEN
		StopOn = LividRGB.BLUE
		StopOff = LividRGB.BLUE
		RecordOn = LividRGB.BlinkMedium.RED
		RecordOff = LividRGB.RED
		OverdubOn = LividRGB.BlinkFast.RED
		OverdubOff = LividRGB.RED	
	

	class Mixer:
		SoloOn = LividRGB.CYAN
		SoloOff = LividRGB.OFF
		MuteOn = LividRGB.YELLOW
		MuteOff = LividRGB.OFF
		ArmSelected = LividRGB.BiColor.WHITE.RED
		ArmSelectedImplicit = LividRGB.MAGENTA
		ArmUnselected = LividRGB.RED
		ArmOff = LividRGB.OFF
		StopClip = LividRGB.WHITE
		SelectedOn = LividRGB.BLUE
		SelectedOff = LividRGB.OFF
	

	class Recording:
		On = LividRGB.RED
		Off = LividRGB.MAGENTA
		Transition = LividRGB.BlinkFast.MAGENTA
	

	class Recorder:
		On = LividRGB.WHITE
		Off = LividRGB.BLUE
		NewOn = LividRGB.BlinkMedium.YELLOW
		NewOff = LividRGB.YELLOW
		FixedOn = LividRGB.BlinkMedium.CYAN
		FixedOff = LividRGB.CYAN
		RecordOn = LividRGB.BlinkMedium.MAGENTA
		RecordOff = LividRGB.MAGENTA
		AutomationOn = LividRGB.BlinkMedium.CYAN
		AutomationOff = LividRGB.CYAN
		FixedAssigned = LividRGB.MAGENTA
		FixedNotAssigned = LividRGB.OFF
	

	class Automation:
		On = LividRGB.BlinkMedium.CYAN
		Off = LividRGB.CYAN
	

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
	

	class DeviceSelector:
		AssignOn = LividRGB.BlinkFast.YELLOW
		AssignOff = LividRGB.YELLOW
	

	class Mod:
		
		AltOn = LividRGB.BlinkFast.BLUE
		AltOff = LividRGB.BLUE
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
		ShiftOn = LividRGB.BlinkFast.YELLOW
		ShiftOff = LividRGB.YELLOW

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

		class Channel_4:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_5:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_6:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_7:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_8:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_9:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_10:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

		class Channel_11:
			Grid_0 = LividRGB.OFF
			Grid_1 = LividRGB.OFF
			Grid_2 = LividRGB.OFF
			Grid_3 = LividRGB.OFF
			Grid_4 = LividRGB.OFF
			Grid_5 = LividRGB.OFF
			Grid_6 = LividRGB.OFF
			Grid_7 = LividRGB.OFF
			Grid_8 = LividRGB.OFF
			Grid_9 = LividRGB.OFF
			Grid_10 = LividRGB.OFF
			Grid_11 = LividRGB.OFF
			Grid_12 = LividRGB.OFF
			Grid_13 = LividRGB.OFF
			Grid_14 = LividRGB.OFF
			Grid_15 = LividRGB.OFF

			Button_0 = LividRGB.OFF
			Button_1 = LividRGB.OFF
			Button_2 = LividRGB.OFF
			Button_3 = LividRGB.OFF
			Button_4 = LividRGB.OFF
			Button_5 = LividRGB.OFF
			Button_6 = LividRGB.OFF
			Button_7 = LividRGB.OFF
			Button_8 = LividRGB.OFF
			Button_9 = LividRGB.OFF
			Button_10 = LividRGB.OFF
			Button_11 = LividRGB.OFF
			Button_12 = LividRGB.OFF
			Button_13 = LividRGB.OFF
			Button_14 = LividRGB.OFF
			Button_15 = LividRGB.OFF
			Button_16 = LividRGB.OFF
			Button_17 = LividRGB.OFF
			Button_18 = LividRGB.OFF
			Button_19 = LividRGB.OFF
			Button_20 = LividRGB.OFF
			Button_21 = LividRGB.OFF
			Button_22 = LividRGB.OFF
			Button_23 = LividRGB.OFF
			Button_24 = LividRGB.OFF
			Button_25 = LividRGB.OFF
			Button_26 = LividRGB.OFF
			Button_27 = LividRGB.OFF
			Button_28 = LividRGB.OFF
			Button_29 = LividRGB.OFF
			Button_30 = LividRGB.OFF
			Button_31 = LividRGB.OFF
		

	

## a  http://www.aumhaa.com

