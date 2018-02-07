# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

"""
Alias_Map.py

Created by amounra on 2012-12-30.
Copyright (c) 2010 __artisia__. All rights reserved.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""

CHANNEL = 0		#main channel (0 - 15)

ALIAS_BUTTONS = [index for index in range(16)]    #there are 16 of these

ALIAS_FADERS = [(index+17) for index in range(9)]		#there are 9 of these

ALIAS_DIALS = [(index+1) for index in range(16)]		#there are 16 of these

ALIAS_ENCODER = 42

"""	The default assignment of colors within the OhmRGB is:
Note 2 = white
Note 4 = cyan 
Note 8 = magenta 
Note 16 = red 
Note 32 = blue 
Note 64 = yellow
Note 127 = green
Because the colors are reassignable, and the default colors have changed from the initial prototype,
	MonOhm script utilizes a color map to assign colors to the buttons.  This color map can be changed 
	here in the script.  The color ordering is from 1 to 7.  
"""
COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]


class AliasColors:


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
	

#a

