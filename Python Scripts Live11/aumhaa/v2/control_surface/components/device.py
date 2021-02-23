# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.4 100918


import Live
import math
import sys

#from ableton.v2.control_surface.components import DeviceComponent as DeviceComponentBase
from _Generic.Devices import best_of_parameter_bank, device_parameters_to_map, number_of_parameter_banks, parameter_bank_names, parameter_banks
from ableton.v2.base import depends, listens, listens_group, liveobj_valid, EventObject
from ableton.v2.control_surface.component import Component
from ableton.v2.control_surface.elements import DisplayDataSource

class DeviceBankRegistry(EventObject):
	__events__ = ('device_bank',)

	def __init__(self, *a, **k):
		super(DeviceBankRegistry, self).__init__(*a, **k)
		self._device_bank_registry = {}
		self._device_bank_listeners = []

	def compact_registry(self):
		newreg = dict([k__ for k__ in list(self._device_bank_registry.items()) if k__[0] != None])
		self._device_bank_registry = newreg

	def set_device_bank(self, device, bank):
		key = self._find_device_bank_key(device) or device
		old = self._device_bank_registry[key] if key in self._device_bank_registry else 0
		if old != bank:
			self._device_bank_registry[key] = bank
			self.notify_device_bank(device, bank)

	def get_device_bank(self, device):
		return self._device_bank_registry.get(self._find_device_bank_key(device), 0)

	def _find_device_bank_key(self, device):
		for k in self._device_bank_registry.keys():
			if k == device:
				return k



class DeviceComponentBase(Component):
	""" Class representing a device in Live """

	@depends(device_bank_registry=None)
	@depends(device_provider=None)
	def __init__(self, device_provider = None, device_bank_registry = None, *a, **k):
		assert device_bank_registry is not None
		super(DeviceComponentBase, self).__init__(*a, **k)
		self._device_bank_registry = device_bank_registry
		self._device_provider = device_provider
		self._parameter_controls = None
		self._bank_up_button = None
		self._bank_down_button = None
		self._bank_buttons = None
		self._on_off_button = None
		self._device_name_data_source = None
		self._bank_index = 0
		self._bank_name = '<No Bank>'

		def make_button_slot(name):
			return self.register_slot(None, getattr(self, '_%s_value' % name), 'value')

		self._bank_up_button_slot = make_button_slot('bank_up')
		self._bank_down_button_slot = make_button_slot('bank_down')
		self._on_off_button_slot = make_button_slot('on_off')
		self.__on_device_bank_changed.subject = self._device_bank_registry
		self.__on_provided_device_changed.subject = self._device_provider
		self.__on_provided_device_changed()

	def disconnect(self):
		self._device_bank_registry = None
		self._release_parameters(self._parameter_controls)
		self._parameter_controls = None
		self._bank_up_button = None
		self._bank_down_button = None
		self._bank_buttons = None
		self._on_off_button = None
		self._device_provider = None
		super(DeviceComponentBase, self).disconnect()

	def _get_device(self):
		return self._device_provider.device

	def on_enabled_changed(self):
		self.update()

	@listens('device')
	def __on_provided_device_changed(self):
		self._on_device_changed(self._get_device())

	def _on_device_changed(self, device):
		if liveobj_valid(device):
			self._release_parameters(self._parameter_controls)
		self.__on_device_name_changed.subject = device
		self.__on_parameters_changed.subject = device
		self.__on_device_on_off_changed.subject = self._on_off_parameter()
		if liveobj_valid(device):
			self._bank_index = 0
		self._bank_index = self._device_bank_registry.get_device_bank(device)
		self._bank_name = '<No Bank>'
		self.__on_device_name_changed()
		self.update()

	def set_bank_prev_button(self, button):
		if button != self._bank_down_button:
			self._bank_down_button = button
			self._bank_down_button_slot.subject = button
			self.update()

	def set_bank_next_button(self, button):
		if button != self._bank_up_button:
			self._bank_up_button = button
			self._bank_up_button_slot.subject = button
			self.update()

	def set_bank_nav_buttons(self, down_button, up_button):
		self.set_bank_prev_button(down_button)
		self.set_bank_next_button(up_button)

	def set_bank_buttons(self, buttons):
		self._bank_buttons = buttons
		self.__on_bank_value.replace_subjects(buttons or [])
		self.update()

	def set_parameter_controls(self, controls):
		self._release_parameters(self._parameter_controls)
		self._parameter_controls = controls
		self.update()

	def set_on_off_button(self, button):
		self._on_off_button = button
		self._on_off_button_slot.subject = button
		self._update_on_off_button()

	def device_name_data_source(self):
		if self._device_name_data_source == None:
			self._device_name_data_source = DisplayDataSource()
			self.__on_device_name_changed()
		return self._device_name_data_source

	def update(self):
		super(DeviceComponentBase, self).update()
		if self.is_enabled() and liveobj_valid(self._get_device()):
			self._device_bank_registry.set_device_bank(self._get_device(), self._bank_index)
			if self._parameter_controls != None:
				old_bank_name = self._bank_name
				self._assign_parameters()
				#if self._bank_name != old_bank_name:
				#	self._show_msg_callback(self._get_device().name + u' Bank: ' + self._bank_name)
		elif self._parameter_controls != None:
			self._release_parameters(self._parameter_controls)
		if self.is_enabled():
			self._update_on_off_button()
			self._update_device_bank_buttons()
			self._update_device_bank_nav_buttons()

	def _bank_up_value(self, value):
		assert self._bank_up_button != None
		assert value != None
		assert isinstance(value, int)
		if self.is_enabled():
			if not self._bank_up_button.is_momentary() or value is not 0:
				if liveobj_valid(self._get_device()):
					num_banks = self._number_of_parameter_banks()
					if self._bank_down_button == None:
						self._bank_name = ''
						self._bank_index = (self._bank_index + 1) % num_banks if self._bank_index != None else 0
						self.update()
					elif self._bank_index == None or num_banks > self._bank_index + 1:
						self._bank_name = ''
						self._bank_index = self._bank_index + 1 if self._bank_index != None else 0
						self.update()

	def _bank_down_value(self, value):
		assert self._bank_down_button != None
		assert value != None
		assert isinstance(value, int)
		if self.is_enabled():
			if not self._bank_down_button.is_momentary() or value is not 0:
				if liveobj_valid(self._get_device()) and (self._bank_index == None or self._bank_index > 0):
					self._bank_name = ''
					self._bank_index = self._bank_index - 1 if self._bank_index != None else max(0, self._number_of_parameter_banks() - 1)
					self.update()

	def _on_off_value(self, value):
		assert self._on_off_button != None
		assert value in range(128)
		if not self._on_off_button.is_momentary() or value is not 0:
			parameter = self._on_off_parameter()
			if parameter != None and parameter.is_enabled:
				parameter.value = float(int(parameter.value == 0.0))

	@listens_group('value')
	def __on_bank_value(self, value, button):
		self._bank_value(value, button)

	def _bank_value(self, value, button):
		if self.is_enabled() and liveobj_valid(self._get_device()):
			if not button.is_momentary() or value is not 0:
				bank = list(self._bank_buttons).index(button)
				if bank != self._bank_index:
					if self._number_of_parameter_banks() > bank:
						self._bank_name = ''
						self._bank_index = bank
						self.update()
				#else:
				#	self._show_msg_callback(self._get_device().name + u' Bank: ' + self._bank_name)

	def _is_banking_enabled(self):
		direct_banking = self._bank_buttons != None
		roundtrip_banking = self._bank_up_button != None
		increment_banking = self._bank_up_button != None and self._bank_down_button != None
		return direct_banking or roundtrip_banking or increment_banking

	def _assign_parameters(self):
		assert self.is_enabled()
		assert liveobj_valid(self._get_device())
		assert self._parameter_controls != None
		self._bank_name, bank = self._current_bank_details()
		for control, parameter in zip(self._parameter_controls, bank):
			if control != None:
				if parameter != None:
					control.connect_to(parameter)
				else:
					control.release_parameter()

		self._release_parameters(self._parameter_controls[len(bank):])

	@listens('value')
	def __on_device_on_off_changed(self):
		self._update_on_off_button()

	@listens('name')
	def __on_device_name_changed(self):
		if self._device_name_data_source != None:
			self._device_name_data_source.set_display_string(self._get_device().name if self.is_enabled() and liveobj_valid(self._get_device()) else 'No Device')

	@listens('parameters')
	def __on_parameters_changed(self):
		self.update()

	def _on_off_parameter(self):
		result = None
		if liveobj_valid(self._get_device()):
			for parameter in self._get_device().parameters:
				if str(parameter.name).startswith('Device On'):
					result = parameter
					break

		return result

	def _update_on_off_button(self):
		if self.is_enabled() and self._on_off_button != None:
			turn_on = False
			if liveobj_valid(self._get_device()):
				parameter = self._on_off_parameter()
				turn_on = parameter != None and parameter.value > 0.0
			self._on_off_button.set_light(turn_on)

	def _update_device_bank_buttons(self):
		if self.is_enabled():
			for index, button in enumerate(self._bank_buttons or []):
				if button:
					turn_on = index == self._bank_index and liveobj_valid(self._get_device())
					button.set_light(turn_on)

	def _update_device_bank_nav_buttons(self):
		if self.is_enabled():
			if self._bank_up_button != None and self._bank_down_button != None:
				can_bank_up = self._bank_index == None or self._number_of_parameter_banks() > self._bank_index + 1
				can_bank_down = self._bank_index == None or self._bank_index > 0
				self._bank_up_button.set_light(self._get_device() and can_bank_up)
				self._bank_down_button.set_light(self._get_device() and can_bank_down)

	def _best_of_parameter_bank(self):
		return best_of_parameter_bank(self._get_device())

	def _parameter_banks(self):
		return parameter_banks(self._get_device())

	def _parameter_bank_names(self):
		return parameter_bank_names(self._get_device())

	def _device_parameters_to_map(self):
		return device_parameters_to_map(self._get_device())

	def _number_of_parameter_banks(self):
		return number_of_parameter_banks(self._get_device())

	def _current_bank_details(self):
		bank_name = self._bank_name
		bank = []
		best_of = self._best_of_parameter_bank()
		banks = self._parameter_banks()
		if banks:
			if self._bank_index != None and self._is_banking_enabled() or not best_of:
				index = self._bank_index if self._bank_index != None else 0
				bank = banks[index]
				bank_name = self._parameter_bank_names()[index]
			else:
				bank = best_of
				bank_name = 'Best of Parameters'
		return (bank_name, bank)

	@listens('device_bank')
	def __on_device_bank_changed(self, device, new_bank_index):
		if device == self._get_device() and new_bank_index != self._bank_index and self._number_of_parameter_banks() > new_bank_index:
			self._bank_index = new_bank_index
			self.update()

	def _release_parameters(self, controls):
		if controls != None:
			for control in controls:
				if control != None:
					control.release_parameter()


class DeviceComponent(DeviceComponentBase):


	def _get_device(self):
		return self._device_provider.device if self._device_provider else None
