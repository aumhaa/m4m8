 
#from __future__ import absolute_import, print_function
from functools import partial
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import SelectedTrackColorFactory, SelectedClipColorFactory
from pushbase.colors import Blink, FallbackColor, Pulse
from Push2.skin_default import Colors as ColorsBase
from Push2.colors import Basic, determine_shaded_color_index, Rgb, translate_color_index

def shaded_color(color_index, shade_level = 1):
	return determine_shaded_color_index(translate_color_index(color_index), shade_level)


shade_transform = partial(shaded_color, shade_level=1)
shade_transform2 = partial(shaded_color, shade_level=2)
SelectedTrackColor = SelectedTrackColorFactory(transformation=translate_color_index)
SelectedClipColor = SelectedClipColorFactory(transformation=translate_color_index)
SelectedTrackColorShade = SelectedTrackColorFactory(transformation=shade_transform)
SelectedTrackColorShade2 = SelectedTrackColorFactory(transformation=shade_transform2)
SelectedClipColorShade = SelectedClipColorFactory(transformation=shade_transform)
SelectedClipColorShade2 = SelectedClipColorFactory(transformation=shade_transform2)
TRACK_SOLOED_COLOR = Rgb.OCEAN
RECORDING_COLOR = Rgb.RED
UNLIT_COLOR = Rgb.BLACK


class Colors(ColorsBase):


	class Mod:

		ShiftOn = Basic.ON
		ShiftOff = Basic.HALF
		AltOn = Basic.ON
		AltOff = Basic.HALF

		class Nav:
			OnValue = Rgb.RED
			OffValue = Rgb.WHITE
		
	

	class MonoInstrument:

		PressFlash = Rgb.WHITE
		OffsetOnValue = Rgb.GREEN
		ScaleOffsetOnValue = Rgb.RED
		SplitModeOnValue = Rgb.WHITE
		SequencerModeOnValue = Rgb.SKY
		DrumOffsetOnValue = Rgb.RED_SHADE
		VerticalOffsetOnValue = Rgb.BLUE

		class Keys:
			SelectedNote = Rgb.GREEN
			RootWhiteValue = Rgb.RED
			RootBlackValue = Rgb.RED_SHADE
			WhiteValue = Rgb.SKY
			BlackValue = Rgb.BLUE
	

		class Drums:
			SelectedNote = Rgb.BLUE
			EvenValue = Rgb.GREEN
			OddValue = Rgb.RED_SHADE

def make_default_skin():
	return Skin(Colors)


def make_drum_pad_coloring_skin():
	return Skin(ColorsWithDrumPadColoring)



