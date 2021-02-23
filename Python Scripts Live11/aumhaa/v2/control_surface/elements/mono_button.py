# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.3b1 on 061218



import Live
import math

from ableton.v2.control_surface.elements.button import ButtonElement
from ableton.v2.control_surface.skin import Skin, SkinColorMissingError
from aumhaa.v2.control_surface.elements.mono_bridge import MonoBridgeProxy
from aumhaa.v2.base.debug import initialize_debug

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE,
 MIDI_CC_TYPE,
 MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224

debug = initialize_debug()



class MonoButtonElement(ButtonElement):
	__module__ = __name__
	__doc__ = ' Special button class that can be configured with custom on- and off-values, some of which flash at specified intervals called by _Update_Display'


	def __init__(self, name = 'MonoButton', script = None, color_map = None, monobridge = None, *a, **k):
		super(MonoButtonElement, self).__init__(name = name, *a, **k)
		self._script = script
		self._color_map = color_map or [2, 64, 4, 8, 16, 127, 32]
		self._num_colors = 7
		self._num_flash_states = 18
		self._flash_state = 0
		self._color = 0
		self._on_value = 127
		self._off_value = 0
		self._darkened = 0
		self._is_enabled = True
		#self._force_forwarding = False
		#self._is_notifying = False
		self._force_next_value = False
		self._parameter = None
		#self._report_input = True
		if not monobridge is None:
			self._monobridge = monobridge
		elif hasattr(script, '_monobridge'):
			self._monobridge = script._monobridge
		else:
			self._monobridge = MonoBridgeProxy()


	def set_color_map(self, color_map):
		assert isinstance(color_map, tuple)
		assert len(color_map) > 0
		self._num_colors = len(color_map)
		self._num_flash_states = int(127/len(color_map))
		self._color_map = color_map


	def set_on_off_values(self, on_value, off_value):
		self._last_sent_message = None
		self._on_value = on_value
		self._off_value = off_value


	def set_on_value(self, value):
		self._last_sent_message = None
		self._on_value = value


	def set_off_value(self, value):
		self._last_sent_message = None
		self._off_value = value


	def set_darkened_value(self, value = 0):
		#debug('setting darkened:', value)
		if value:
			value = self._color_map[value-1]
		self._darkened = value


	def set_force_next_value(self):
		self._last_sent_message = None
		self._force_next_value = True


	def set_enabled(self, enabled):
		self._is_enabled = enabled
		self._request_rebuild()


	def turn_on(self, force = False):
		self.force_next_send()
		if self._on_value in range(0, 128):
			self.send_value(self._on_value)
		else:
			try:
				color = self._skin[self._on_value]
				color.draw(self)
			except SkinColorMissingError:
				#super(MonoButtonElement, self).turn_on()
				debug('skin color missing', self._on_value)
				self.send_value(127)


	def turn_off(self, force = False):
		self.force_next_send()
		#debug('turn off:', self._off_value)
		if self._off_value in range(0, 128):
			self.send_value(self._off_value)
		else:
			try:
				color = self._skin[self._off_value]
				color.draw(self)
			except SkinColorMissingError:
				#super(MonoButtonElement, self).turn_off()
				debug('skin color missing', self._off_value)
				self.send_value(0)


	def reset(self, force = False):
		self._darkened = 0;
		self.force_next_send()
		self.send_value(0)


	def set_light(self, value, *a, **k):
		if value is None:
			value = False
		if isinstance(value, bool):
			value = 'DefaultButton.On' if value else 'DefaultButton.Off'
		try:
			self._skin[value]
		except SkinColorMissingError:
			debug('skin missing for', value)
			value = 'DefaultButton.On'
		#debug(self.name, 'skin value:', value)
		super(MonoButtonElement, self).set_light(value, *a, **k)


	def send_value(self, value, force = False):
		# debug(self.name, 'send_value', value)
		if (value != None) and isinstance(value, int) and (value in list(range(128))):
			if (force or self._force_next_send or ((value != self._last_sent_value) and self._is_being_forwarded)):
				data_byte1 = self._original_identifier
				if value in range(1, 127):
					data_byte2 = self._color_map[(value - 1) % (self._num_colors)]
				elif value == 127:
					data_byte2 = self._color_map[self._num_colors-1]
				else:
					data_byte2 = self._darkened
				self._color = data_byte2
				status_byte = self._original_channel
				if (self._msg_type == MIDI_NOTE_TYPE):
					status_byte += MIDI_NOTE_ON_STATUS
				elif (self._msg_type == MIDI_CC_TYPE):
					status_byte += MIDI_CC_STATUS
				else:
					assert False
				self.send_midi(tuple([status_byte,
				 data_byte1,
				 data_byte2]))
				self._last_sent_message = [value]
				if self._report_output:
					is_input = True
					self._report_value(value, (not is_input))
				self._flash_state = math.floor((value -1)/self._num_colors)
				self._force_next_value = False
		else:
			debug('Button bad send value:', value)


	#def script_wants_forwarding(self):
	#	if not self._is_enabled and not self._force_forwarding:
	#		return False
	#	else:
	#		return super(MonoButtonElement, self).script_wants_forwarding()


	def set_enabled(self, enabled):
		self.suppress_script_forwarding = not enabled


	def flash(self, timer):
		if (self._is_being_forwarded and self._flash_state in list(range(1, self._num_flash_states)) and (timer % self._flash_state) == 0):
			data_byte1 = self._original_identifier
			data_byte2 = self._color if math.floor((timer % (self._flash_state * 2)) > 0) else self._darkened
			status_byte = self._original_channel
			if (self._msg_type == MIDI_NOTE_TYPE):
				status_byte += MIDI_NOTE_ON_STATUS
			elif (self._msg_type == MIDI_CC_TYPE):
				status_byte += MIDI_CC_STATUS
			else:
				assert False
			self.send_midi((status_byte,
			 data_byte1,
			 data_byte2))



	def release_parameter(self):
		self._darkened = 0
		super(MonoButtonElement, self).release_parameter()




class DescriptiveMonoButtonElement(MonoButtonElement):


	def __init__(self, *a, **k):
		super(DescriptiveMonoButtonElement, self).__init__(*a, **k)

		self._descriptor = None
		self._last_reported_descriptor = None

		monobridge = k['monobridge'] if 'monobridge' in k else None
		if not monobridge is None:
			self._monobridge = monobridge
		elif hasattr(self._script, 'notification_to_bridge'):
			self._monobridge = self._script
		else:
			self._monobridge = MonoBridgeProxy()


	def set_descriptor(self, descriptor):
		self._descriptor = '.' + str(descriptor) if descriptor else ''


	def _set_descriptor(self, descriptor):
		#debug('_set_descriptor:', descriptor)
		self.set_descriptor(descriptor)


	def _get_descriptor(self):
		#debug('_get_descriptor:', '' if self._descriptor is None else str(self._descriptor))
		return '' if self._descriptor is None else str(self._descriptor)


	descriptor = property(_get_descriptor, _set_descriptor)

	def report_descriptor(self, descriptor = None, force = False):
		if force or (descriptor != self._last_reported_descriptor):
			self._monobridge._send(self.name, 'button_function', str(descriptor) + self.descriptor)
		self._last_reported_descriptor = descriptor


	def set_light(self, value, *a, **k):
		try:
			self._skin[value]
		except SkinColorMissingError:
			pass
		super(MonoButtonElement, self).set_light(value, *a, **k)
		self.report_descriptor(value)


	def turn_on(self, force = False):
		self.force_next_send()
		if self._on_value in range(0, 128):
			self.send_value(self._on_value)
			self.report_descriptor('on')
		else:
			try:
				color = self._skin[self._on_value]
				color.draw(self)
			except SkinColorMissingError:
				#super(MonoButtonElement, self).turn_on()
				debug('skin color missing', self._on_value)
				self.send_value(127)
			self.report_descriptor(self._on_value)


	def turn_off(self, force = False):
		self.force_next_send()
		#debug('turn off:', self._off_value)
		if self._off_value in range(0, 128):
			self.send_value(self._off_value)
			self.report_descriptor('off')
		else:
			try:
				color = self._skin[self._off_value]
				color.draw(self)
			except SkinColorMissingError:
				#super(MonoButtonElement, self).turn_off()
				debug('skin color missing', self._off_value)
				self.send_value(0)
			self.report_descriptor(self._off_value)
