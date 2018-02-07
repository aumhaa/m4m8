
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements.button_slider import ButtonSliderElement
from ableton.v2.control_surface.input_control_element import *
SLIDER_MODE_SINGLE = 0
SLIDER_MODE_VOLUME = 1
SLIDER_MODE_PAN = 2
SLIDER_MODE_SEND = 3

from aumhaa.v2.base.debug import *
debug = initialize_debug()

SINGLE_VALUE_MAP = tuple([ float(float(index) / float(7)) for index in range(8) ])
PAN_VALUE_MAP = (-1.0, -0.634921, -0.31746, 0.0, 0.0, 0.31746, 0.634921, 1.0)
VOL_VALUE_MAP = (0.0, 0.142882, 0.302414, 0.4, 0.55, 0.7, 0.85, 1.0)
SEND_VALUE_MAP = (0.0, 0.103536, 0.164219, 0.238439, 0.343664, 0.55, 0.774942, 1.0)

VALUE_MAPS = (SINGLE_VALUE_MAP, VOL_VALUE_MAP, PAN_VALUE_MAP, SEND_VALUE_MAP)

class PreciseButtonSliderElement(ButtonSliderElement):
	u""" Class representing a set of buttons used as a slider """

	def __init__(self, buttons):
		super(PreciseButtonSliderElement, self).__init__(buttons)
		num_buttons = len(buttons)
		self._disabled = False
		self._mode = SLIDER_MODE_VOLUME
		self._value_map = tuple([ float(float(index) / float(num_buttons-1)) for index in range(num_buttons) ])
	

	def set_disabled(self, disabled):
		assert isinstance(disabled, type(False))
		self._disabled = disabled

	def set_mode(self, mode):
		assert mode in (SLIDER_MODE_SINGLE, SLIDER_MODE_VOLUME, SLIDER_MODE_PAN, SLIDER_MODE_SEND)
		if mode != self._mode:
			self._mode = mode
			self.set_value_map(VALUE_MAPS[mode])
	

	def set_value_map(self, map):
		assert isinstance(map, (tuple, type(None)))
		assert len(map) == len(self._buttons)
		self._value_map = map

	def send_value(self, value):
		assert self._disabled or value != None
		assert isinstance(value, int)
		assert value in range(128)
		if value != self._last_sent_value:
			if self._mode == SLIDER_MODE_SINGLE:
				super(PreciseButtonSliderElement, self).send_value(value)
			elif self._mode == SLIDER_MODE_VOLUME:
				self._send_value_volume(value)
			elif self._mode == SLIDER_MODE_PAN:
				self._send_value_pan(value)
			self._last_sent_value = value

	def connect_to(self, parameter):
		super(PreciseButtonSliderElement, self).connect_to(parameter)
		if self._parameter_to_map_to != None:
			self._last_sent_value = -1
			self._on_parameter_changed()

	def release_parameter(self):
		old_param = self._parameter_to_map_to
		super(PreciseButtonSliderElement, self).release_parameter()
		if not self._disabled and old_param != None:
			for button in self._buttons:
				button.reset()

	def reset(self):
		if not self._disabled and self._buttons != None:
			for button in self._buttons:
				if button != None:
					button.reset()

	def _send_value_volume(self, value):
		#debug('_send_value_volume', value)
		index_to_light = -1
		normalised_value = float(value) / 127.0
		if normalised_value > 0.0:
			for index in range(len(self._value_map)):
				if normalised_value <= self._value_map[index]:
					index_to_light = index
					break

		self._send_mask(tuple([ index <= index_to_light for index in range(len(self._buttons)) ]))
	
	"""
	def _send_value_pan(self, value):
		#debug('_send_value_pan', value)
		num_buttons = len(self._buttons)
		button_bits = [ False for index in range(num_buttons) ]
		normalised_value = float(float(2 * value) / float(127.0)) - 1.0
		#debug('norm:', normalised_value)
		if value in (63, 64):
			normalised_value = 0.0
		if normalised_value < 0.0:
			#debug('norm < 0')
			for index in range(len(self._buttons)):
				button_bits[index] = ((self._value_map[index]*2)-1) >= normalised_value and index < 4

		elif normalised_value > 0.0:
			debug('norm > 0')
			for index in range(len(self._buttons)):
				#index = len(self._buttons) - 1 - index
				button_bits[index] = ((self._value_map[index]*2)-1) <= normalised_value and index > 3

		else:
			for index in range(len(self._buttons)):
				button_bits[index] = ((self._value_map[index]*2)-1) == normalised_value

		self._send_mask(tuple(button_bits))
	"""

	def _send_value_pan(self, value):
		num_buttons = len(self._buttons)
		button_bits = [ False for index in range(num_buttons) ]
		normalised_value = float(2 * value / 127.0) - 1.0
		if value in (63, 64):
			normalised_value = 0.0
		if normalised_value < 0.0:
			for index in range(len(self._buttons)):
				button_bits[index] = self._value_map[index] >= normalised_value
				if self._value_map[index] >= 0:
					break

		elif normalised_value > 0.0:
			for index in range(len(self._buttons)):
				r_index = len(self._buttons) - 1 - index
				button_bits[r_index] = self._value_map[r_index] <= normalised_value
				if self._value_map[r_index] <= 0:
					break

		else:
			for index in range(len(self._buttons)):
				button_bits[index] = self._value_map[index] == normalised_value

		self._send_mask(tuple(button_bits))
	

	def _send_mask(self, mask):
		assert isinstance(mask, tuple)
		assert len(mask) == len(self._buttons)
		for index in range(len(self._buttons)):
			if mask[index]:
				#self._buttons[index].turn_on()
				self._buttons[index].send_value(127)
			else:
				#self._buttons[index].turn_off()
				self._buttons[index].send_value(4)

	def _button_value(self, value, sender):
		assert isinstance(value, int)
		assert sender in self._buttons
		self._last_sent_value = -1
		if not value == 0:
			index_of_sender = list(self._buttons).index(sender)
			if self._parameter_to_map_to != None and self._parameter_to_map_to.is_enabled:
				#param_range = abs(self._parameter_to_map_to.max - self._parameter_to_map_to.min)
				#self._parameter_to_map_to.value = (self._value_map[index_of_sender] * param_range) + self._parameter_to_map_to.min
				index_of_sender = (value != 0 or not sender.is_momentary()) and list(self._buttons).index(sender)
				self._parameter_to_map_to.value = self._parameter_to_map_to != None and self._parameter_to_map_to.is_enabled and self._value_map[index_of_sender]
		self.notify_value(value)
	
	"""
	def _on_parameter_changed(self):
		assert self._parameter_to_map_to != None
		param_range = abs(self._parameter_to_map_to.max - self._parameter_to_map_to.min)
		param_value = self._parameter_to_map_to.value
		param_min = self._parameter_to_map_to.min
		param_mid = param_range / 2 + param_min
		midi_value = 0
		#debug('min:', param_min, 'max:', self._parameter_to_map_to.max, 'range:', param_range, 'mid:', param_mid, 'value:', param_value)
		if self._mode == SLIDER_MODE_PAN:
			if param_value == param_mid:
				midi_value = 64
			else:
				diff = abs(param_value - param_mid) / param_range * 127
				if param_value > param_mid:
					midi_value = 64 + int(diff)
				else:
					midi_value = 63 - int(diff)
		else:
			midi_value = int(127 * abs(param_value - self._parameter_to_map_to.min) / param_range)
		self.send_value(midi_value)
	"""

	def _on_parameter_changed(self):
		assert self._parameter_to_map_to != None
		param_range = abs(self._parameter_to_map_to.max - self._parameter_to_map_to.min)
		param_value = self._parameter_to_map_to.value
		param_min = self._parameter_to_map_to.min
		param_mid = param_range / 2 + param_min
		midi_value = 0
		if self._mode == SLIDER_MODE_PAN:
			if param_value == param_mid:
				midi_value = 64
			else:
				diff = abs(param_value - param_mid) / param_range * 127
				if param_value > param_mid:
					midi_value = 64 + int(diff)
				else:
					midi_value = 63 - int(diff)
		else:
			midi_value = int(127 * abs(param_value - self._parameter_to_map_to.min) / param_range)
		self.send_value(midi_value)