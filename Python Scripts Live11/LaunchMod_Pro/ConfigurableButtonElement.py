

from ableton.v2.base.event import has_event
from ableton.v2.control_surface import SkinColorMissingError
from ableton.v2.control_surface.elements import ButtonElement #, ON_VALUE, OFF_VALUE

from aumhaa.v2.base.debug import *
debug = initialize_debug()

class ConfigurableButtonElement(ButtonElement):
	"""
	Special button class (adapted from Push script for LP Pro)
	that can be configured with custom on- and off-values.

	A ConfigurableButtonElement can have states other than True or
	False, which can be defined by setting the 'states' property.
	Thus 'set_light' can take any state or skin color.
	"""
	default_states = {True: 'DefaultButton.On',
	 False: 'DefaultButton.Disabled'}
	send_depends_on_forwarding = False

	def __init__(self, is_momentary, msg_type, channel, identifier, skin = None, default_states = None, *a, **k):
		#debug(self.name, default_states)
		super(ConfigurableButtonElement, self).__init__(is_momentary, msg_type, channel, identifier, skin=skin, **k)
		if default_states is not None:
			self.default_states = default_states
		self.states = dict(self.default_states)
		#debug(self.name, 'default states:', self.default_states)

	@property
	def _on_value(self):
		return self.states[True]

	@property
	def _off_value(self):
		return self.states[False]

	@property
	def on_value(self):
		return self._try_fetch_skin_value(self._on_value)

	@property
	def off_value(self):
		return self._try_fetch_skin_value(self._off_value)

	def _try_fetch_skin_value(self, value):
		try:
			return self._skin[value]
		except SkinColorMissingError:
			return value

	def reset(self):
		self.set_light('DefaultButton.Disabled')
		self.reset_state()

	def reset_state(self):
		self.states = dict(self.default_states)
		super(ConfigurableButtonElement, self).reset_state()
		self.set_enabled(True)

	def set_on_off_values(self, on_value, off_value):
		self.states[True] = on_value
		self.states[False] = off_value

	def set_enabled(self, enabled):
		self.suppress_script_forwarding = not enabled

	def is_enabled(self):
		return not self.suppress_script_forwarding


	"""
	def _set_skin_light(self, value):
		color = None
		try:
			color = self._skin[value]
			self._do_draw(color)
		except:
			self.send_value(color)
		finally:
			if has_event(color, u'midi_value'):
				self.__on_midi_value_changed.subject = color
			else:
				self._disconnect_color_listener()

	"""

	# def _set_skin_light(self, value):
	# 	#debug(self.name, '_set_skin_light', value, self.default_states, self.states, self.states.get(value, value))
	# 	try:
	# 		color = self._skin[value]
	# 		self._do_draw(color)
	# 	except SkinColorMissingError:
	# 		if isinstance(value, int) and value in range(127):
	# 			super(ButtonElement, self).send_value(value)



	# def set_light(self, value):
	# 	#debug(self.name if hasattr(self, 'name') else 'unnamed', 'set_light', value, self.states.get(value, value))
	# 	super(ConfigurableButtonElement, self).set_light(self.states.get(value, value))

	# def send_value(self, value, **k):
	# 	if value is 127:
	# 		self._do_send_on_value()
	# 	elif value is 0:
	# 		self._do_send_off_value()
	# 	else:
	# 		super(ConfigurableButtonElement, self).send_value(value, **k)

	def _do_send_on_value(self):
		self._skin[self._on_value].draw(self)

	def _do_send_off_value(self):
		self._skin[self._off_value].draw(self)

	def script_wants_forwarding(self):
		return not self.suppress_script_forwarding
