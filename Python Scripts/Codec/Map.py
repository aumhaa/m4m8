# by amounra 0216 : http://www.aumhaa.com

"""
Codec_Map.py

Created by amounra on 2010-10-05.
Copyright (c) 2010 __artisia__. All rights reserved.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""
CHANNEL = 0		#main channel (0 - 15)

CODE_BUTTONS = 		[[1, 5, 9, 13, 17, 21, 25, 29],
    				 [2, 6, 10, 14, 18, 22, 26, 30],
					 [3, 7, 11, 15, 19, 23, 27, 31],
					 [4, 8, 12, 16, 20, 24, 28, 32]]

CODE_DIALS = 		[[1, 5, 9, 13, 17, 21, 25, 29],
    				 [2, 6, 10, 14, 18, 22, 26, 30],
					 [3, 7, 11, 15, 19, 23, 27, 31],
					 [4, 8, 12, 16, 20, 24, 28, 32]]	

CODE_COLUMN_BUTTONS = [38, 39, 40, 41, 42, 43, 44, 45]

CODE_ROW_BUTTONS = [33, 34, 35, 36]

LIVID = 37			#single

FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track

COLOR_MAP = [127, 127, 127, 127, 127, 127, 127]

USE_DEVICE_SELECTOR = True

FACTORY_RESET = False

SHIFT_LATCHING = True

from aumhaa.v2.livid.colors import *

class CodecColors:

	ResetSendsColor = LividRGB.WHITE

	class Mod:
		ShiftOff = LividRGB.OFF
		ShiftOn = LividRGB.WHITE
	

	class Mode:
		Main = LividRGB.WHITE
		Main_shifted = LividRGB.BlinkFast.WHITE
	

	class ShiftMode:
		Enabled = LividRGB.BlinkFast.WHITE
		Disabled = LividRGB.OFF
	

	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

	class Session:
		StopClipTriggered = LividRGB.BlinkFast.BLUE
		StopClip = LividRGB.BLUE
		Scene = LividRGB.CYAN
		NoScene = LividRGB.OFF
		SceneTriggered = LividRGB.BlinkFast.BLUE
		ClipTriggeredPlay = LividRGB.BlinkFast.GREEN
		ClipTriggeredRecord = LividRGB.BlinkFast.RED
		RecordButton = LividRGB.OFF
		ClipStopped = LividRGB.WHITE
		ClipStarted = LividRGB.GREEN
		ClipRecording = LividRGB.RED
		NavigationButtonOn = LividRGB.BLUE
	

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
	

	class Transport:
		OverdubOn = LividRGB.BlinkFast.RED
		OverdubOff = LividRGB.RED
	

	class Device:
		NavOn = LividRGB.MAGENTA
		NavOff = LividRGB.OFF
		BankOn = LividRGB.YELLOW
		BankOff = LividRGB.OFF
		ChainNavOn = LividRGB.RED
		ChainNavOff = LividRGB.OFF
		ContainNavOn = LividRGB.CYAN
		ContainNavOff = LividRGB.OFF
	

## a



