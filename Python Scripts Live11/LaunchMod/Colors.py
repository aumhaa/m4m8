

from ableton.v2.control_surface.elements import Color as ColorBase

class Color(ColorBase):
	
	def __int__(self):
	   return self.midi_value


class Rgb:
	BLACK = Color(4)
	RED = Color(7)
	RED_HALF = Color(6)
	RED_THIRD = Color(5)
	RED_BLINK = Color(11)
	GREEN = Color(52)
	GREEN_HALF = Color(36)
	GREEN_THIRD = Color(20)
	GREEN_BLINK = Color(56)
	AMBER = Color(55)
	AMBER_HALF = Color(38)
	AMBER_THIRD = Color(21)
	AMBER_BLINK = Color(59)


