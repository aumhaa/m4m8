# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

"""
GuitarWing_Map.py

Created by amounra on 2012-12-30.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""

CHANNEL = 0		#main channel (0 - 15)

PADS = [36, 37, 38, 39, 4]

BUTTONS = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

SLIDERS = [1, 2, 3]

ACCELS = [5, 6, 7]

CCS = [8, 9, 10, 11]


""" The default assignment of colors within the OhmRGB is:
Note 2 = white
Note 4 = cyan 
Note 8 = magenta 
Note 16 = red 
Note 32 = blue 
Note 64 = yellow
Note 127 = green
Because the colors are reassignable, and the default colors have changed from the initial prototype,
	MonOhm script utilizes a color map to assign colors to the buttons.	 This color map can be changed 
	here in the script.	 The color ordering is from 1 to 7.	 
"""
COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]


class GuitarWingColors:


	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

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
		XFadeOff = LividRGB.OFF
		XFadeAOn = LividRGB.YELLOW
		XFadeBOn = LividRGB.MAGENTA
	

	class Transport:
		OverdubOn = LividRGB.RED
		OverdubOff = LividRGB.RED
		PlayOff = LividRGB.GREEN
		PlayOn = LividRGB.GREEN
		StopOn = LividRGB.BLUE
		StopOff = LividRGB.OFF
		LoopOn = LividRGB.YELLOW
		LoopOff = LividRGB.YELLOW
		RecordOn = LividRGB.RED
		RecordOff = LividRGB.RED
	

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
	
