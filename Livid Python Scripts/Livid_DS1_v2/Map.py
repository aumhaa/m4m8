# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *


CHANNEL = 0		#main channel (0 - 15)

DS1_BUTTONS = [0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15]	#there are 16 of these

DS1_GRID = [[16, 19, 22],
			[17, 20, 23],
			[18, 21, 24]]


DS1_FADERS = [41, 42, 43, 44, 45, 46, 47, 48]

DS1_MASTER = 49

DS1_DIALS = [[1, 2, 3, 4, 5],
				[6, 7, 8, 9, 10],
				[11, 12, 13, 14, 15],
				[16, 17, 18, 19, 20],
				[21, 22, 23, 24, 25],
				[26, 27, 28, 29, 30],
				[31, 32, 33, 34, 35],
				[36, 37, 38, 39, 40]]

DS1_ENCODERS = [96, 97, 98, 99]

DS1_ENCODER_BUTTONS = [25, 26, 27, 28]

DS1_SIDE_DIALS = [50, 51, 52, 53]



class DS1Colors:


	class ModeButtons:
		Main = LividRGB.WHITE
		Select = LividRGB.RED
		Clips = LividRGB.GREEN
	

	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

	class Session:
		StopClipTriggered = LividRGB.BiColor.BLUE.WHITE
		StopClip = LividRGB.BLUE
		Scene = LividRGB.CYAN
		NoScene = LividRGB.OFF
		SceneTriggered = LividRGB.GREEN
		ClipTriggeredPlay = LividRGB.BlinkFast.GREEN
		ClipTriggeredRecord = LividRGB.BlinkFast.RED
		RecordButton = LividRGB.OFF
		ClipEmpty = LividRGB.OFF
		ClipStopped = LividRGB.WHITE
		ClipStarted = LividRGB.GREEN
		ClipRecording = LividRGB.RED
		NavigationButtonOn = LividRGB.CYAN
		NavigationButtonOff = LividRGB.YELLOW
		ZoomOn = LividRGB.BlinkFast.WHITE
		ZoomOff = LividRGB.WHITE
	

	class Zooming:
		Selected = LividRGB.BlinkFast.YELLOW
		Stopped = LividRGB.WHITE
		Playing = LividRGB.GREEN
		Empty = LividRGB.OFF
	

	class LoopSelector:
		Playhead = LividRGB.YELLOW
		OutsideLoop = LividRGB.BLUE
		InsideLoopStartBar = LividRGB.CYAN
		SelectedPage = LividRGB.WHITE
		InsideLoop = LividRGB.CYAN
		PlayheadRecord = LividRGB.RED
	

	class Transport:
		PlayOn = LividRGB.BiColor.WHITE.GREEN
		PlayOff = LividRGB.GREEN
		StopOn = LividRGB.BLUE
		StopOff = LividRGB.BLUE
		RecordOn = LividRGB.BiColor.WHITE.RED
		RecordOff = LividRGB.RED
		OverdubOn = LividRGB.BiColor.WHITE.MAGENTA
		OverdubOff = LividRGB.MAGENTA
		SeekBackwardOn = LividRGB.BlinkMedium.CYAN
		SeekBackwardOff = LividRGB.CYAN
		LoopOn = LividRGB.BlinkMedium.YELLOW
		LoopOff = LividRGB.YELLOW
	

	class Mixer:
		SoloOn = LividRGB.BLUE
		SoloOff = LividRGB.CYAN
		MuteOn = LividRGB.YELLOW
		MuteOff = LividRGB.WHITE
		ArmSelected = LividRGB.RED
		ArmUnselected = LividRGB.RED
		ArmOff = LividRGB.GREEN
		StopClip = LividRGB.BLUE
		SelectedOn = LividRGB.BLUE
		SelectedOff = LividRGB.MAGENTA
	

	class Recording:
		On = LividRGB.BiColor.WHITE.MAGENTA
		Transition = LividRGB.BlinkFast.MAGENTA
		Off = LividRGB.MAGENTA
	

	class Automation:
		On = LividRGB.BiColor.WHITE.YELLOW
		Off = LividRGB.YELLOW
	

	class Recorder:
		On = LividRGB.WHITE
		Off = LividRGB.BLUE
		NewOn = LividRGB.BlinkMedium.YELLOW
		NewOff = LividRGB.YELLOW
		FixedOn = LividRGB.BlinkMedium.CYAN
		FixedOff = LividRGB.CYAN
		RecordOn = LividRGB.BiColor.WHITE.MAGENTA
		RecordOff = LividRGB.MAGENTA
		AutomationOn = LividRGB.BiColor.WHITE.YELLOW
		AutomationOff = LividRGB.YELLOW
		FixedAssigned = LividRGB.MAGENTA
		FixedNotAssigned = LividRGB.OFF
	

	class Device:
		NavOn = LividRGB.MAGENTA
		NavOff = LividRGB.OFF
		BankOn = LividRGB.YELLOW
		BankOff = LividRGB.OFF
		ChainNavOn = LividRGB.RED
		ChainNavOff = LividRGB.OFF
		ContainNavOn = LividRGB.CYAN
		ContainNavOff = LividRGB.OFF
	

