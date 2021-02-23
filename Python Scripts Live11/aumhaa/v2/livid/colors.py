
from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()


class MonoColor(Color):


	def draw(self, interface):
		try:
			interface.set_darkened_value(0)
			super(MonoColor, self).draw(interface)
		except:
			super(MonoColor, self).draw(interface)
	


class BiColor(MonoColor):


	def __init__(self, darkened_value = 0, *a, **k):
		super(BiColor, self).__init__(*a, **k)
		self._darkened_value = darkened_value
	

	def draw(self, interface):
		try:
			interface.set_darkened_value(self._darkened_value)
			interface.send_value(self.midi_value)
		except:
			debug(interface, 'is not MonoButtonElement, cannot use BiColor')
			super(BiColor, self).draw(interface)
			
	


class LividRGB:

	OFF = MonoColor(0)
	WHITE = MonoColor(1)
	YELLOW = MonoColor(2)
	CYAN = MonoColor(3)
	MAGENTA = MonoColor(4)
	RED = MonoColor(5)
	GREEN = MonoColor(6)
	BLUE = MonoColor(7)
	
	class BlinkFast:
		WHITE = MonoColor(8)
		YELLOW = MonoColor(9)
		CYAN = MonoColor(10)
		MAGENTA = MonoColor(11)
		RED = MonoColor(12)
		GREEN = MonoColor(13)
		BLUE = MonoColor(14)
	

	class BlinkMedium:
		WHITE = MonoColor(15)
		YELLOW = MonoColor(16)
		CYAN = MonoColor(17)
		MAGENTA = MonoColor(18)
		RED = MonoColor(19)
		GREEN = MonoColor(20)
		BLUE = MonoColor(21)
	

	class BlinkSlow:
		WHITE = MonoColor(22)
		YELLOW = MonoColor(23)
		CYAN = MonoColor(24)
		MAGENTA = MonoColor(25)
		RED = MonoColor(26)
		GREEN = MonoColor(27)
		BLUE = MonoColor(28)
	

	class BiColor:
		class WHITE:
			YELLOW = BiColor(1, 16)
			CYAN = BiColor(1, 17)
			MAGENTA = BiColor(1, 18)
			RED = BiColor(1, 19)
			GREEN = BiColor(1, 20)
			BLUE = BiColor(1, 21)
		

		class YELLOW:
			WHITE = BiColor(2, 15)
			CYAN = BiColor(2, 17)
			MAGENTA = BiColor(2, 18)
			RED = BiColor(2, 19)
			GREEN = BiColor(2, 20)
			BLUE = BiColor(2, 21)
	

		class CYAN:
			WHITE = BiColor(3, 15)
			YELLOW = BiColor(3, 16)
			MAGENTA = BiColor(3, 18)
			RED = BiColor(3, 19)
			GREEN = BiColor(3, 20)
			BLUE = BiColor(3, 21)

		class MAGENTA:
			WHITE = BiColor(4, 15)
			YELLOW = BiColor(4, 16)
			CYAN = BiColor(4, 17)
			RED = BiColor(4, 19)
			GREEN = BiColor(4, 20)
			BLUE = BiColor(4, 21)

		class RED:
			WHITE = BiColor(5, 15)
			YELLOW = BiColor(5, 16)
			CYAN = BiColor(5, 17)
			MAGENTA = BiColor(5, 18)
			GREEN = BiColor(5, 20)
			BLUE = BiColor(5, 21)

		class GREEN:
			WHITE = BiColor(6, 15)
			YELLOW = BiColor(6, 16)
			CYAN = BiColor(6, 17)
			MAGENTA = BiColor(6, 18)
			RED = BiColor(6, 19)
			BLUE = BiColor(6, 21)
	
		class BLUE:
			WHITE = BiColor(7, 15)
			YELLOW = BiColor(7, 16)
			CYAN = BiColor(7, 17)
			MAGENTA = BiColor(7, 18)
			RED = BiColor(7, 19)
			GREEN = BiColor(7, 20)
		
	
