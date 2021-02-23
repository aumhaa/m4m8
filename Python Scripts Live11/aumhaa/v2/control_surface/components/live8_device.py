import Live
from _Generic.Devices import *

from ableton.v2.control_surface.component import Component as ControlSurfaceComponent
from ableton.v2.control_surface.elements import EncoderElement, ButtonElement, DisplayDataSource
	
class Live8DeviceComponent(ControlSurfaceComponent):
	
	__doc__ = ' Class representing a device in Live '
	def __init__(self, *a, **k):
		super(Live8DeviceComponent, self).__init__(*a, **k)
		self._device_banks = DEVICE_DICT
		self._device_best_banks = DEVICE_BOB_DICT
		self._device_bank_names = BANK_NAME_DICT
		self._device = None
		self._parameter_controls = None
		self._bank_up_button = None
		self._bank_down_button = None
		self._bank_buttons = None
		self._on_off_button = None
		self._lock_button = None
		self._lock_callback = None
		self._device_name_data_source = None
		self._device_bank_registry = {}
		self._bank_index = 0
		self._bank_name = '<No Bank>'
		self._locked_to_device = False
		return None
	
	def disconnect(self):
		self._lock_callback = None
		self._device_bank_registry = None
		if self._parameter_controls != None:
			for control in self._parameter_controls:
				control.release_parameter()
			self._parameter_controls = None
		if self._bank_up_button != None:
			self._bank_up_button.remove_value_listener(self._bank_up_value)
			self._bank_up_button = None
		if self._bank_down_button != None:
			self._bank_down_button.remove_value_listener(self._bank_down_value)
			self._bank_down_button = None
		if self._bank_buttons != None:
			for button in self._bank_buttons:
				button.remove_value_listener(self._bank_value)
		self._bank_buttons = None
		if self._on_off_button != None:
			if self._on_off_button.value_has_listener(self._on_off_value):
				self._on_off_button.remove_value_listener(self._on_off_value)
			self._on_off_button = None
		if self._lock_button != None:
			if self._lock_button.value_has_listener(self._lock_value):
				self._lock_button.remove_value_listener(self._lock_value)
			self._lock_button = None
		if self._device != None:
			parameter = self._on_off_parameter()
			if parameter != None:
				if parameter.value_has_listener(self._on_on_off_changed):
					parameter.remove_value_listener(self._on_on_off_changed)
			if self._device.name_has_listener(self._on_device_name_changed):
				self._device.remove_name_listener(self._on_device_name_changed)
			if self._device.parameters_has_listener(self._on_parameters_changed):
				self._device.remove_parameters_listener(self._on_parameters_changed)
			self._device = None
		return None
	
	def on_enabled_changed(self):
		self.update()
	

	def set_device(self, device):
		assert ((device == None) or isinstance(device, Live.Device.Device))
		if ((not self._locked_to_device) and (device != self._device)):
			if (self._device != None):
				self._device.remove_name_listener(self._on_device_name_changed)
				self._device.remove_parameters_listener(self._on_parameters_changed)
				parameter = self._on_off_parameter()
				if (parameter != None):
					parameter.remove_value_listener(self._on_on_off_changed)
				if (self._parameter_controls != None):
					for control in self._parameter_controls:
						control.release_parameter()
			self._device = device
			if (self._device != None):
				self._bank_index = 0
				self._device.add_name_listener(self._on_device_name_changed)
				self._device.add_parameters_listener(self._on_parameters_changed)
				parameter = self._on_off_parameter()
				if (parameter != None):
					parameter.add_value_listener(self._on_on_off_changed)
			for key in list(self._device_bank_registry.keys()):
				if (key == self._device):
					self._bank_index = self._device_bank_registry.get(key, 0)
					del self._device_bank_registry[key]
					break
			self._bank_name = '<No Bank>' #added
			self._on_device_name_changed()
			self.update()		 
		
	def set_bank_nav_buttons(self, down_button, up_button):
		assert ((down_button != None) or (up_button == None))
		assert ((up_button == None) or isinstance(up_button, ButtonElement))
		assert ((down_button == None) or isinstance(down_button, ButtonElement))
		do_update = False
		if up_button != self._bank_up_button:
			do_update = True
			if self._bank_up_button != None:
				self._bank_up_button.remove_value_listener(self._bank_up_value)
			self._bank_up_button = up_button
			if self._bank_up_button != None:
				self._bank_up_button.add_value_listener(self._bank_up_value)
		if down_button != self._bank_down_button:
			do_update = True
			if self._bank_down_button != None:
				self._bank_down_button.remove_value_listener(self._bank_down_value)
			self._bank_down_button = down_button
			if self._bank_down_button != None:
				self._bank_down_button.add_value_listener(self._bank_down_value)
		if do_update:
			self.update()
		return None
	
	def set_bank_buttons(self, buttons):
		assert ((buttons == None) or isinstance(buttons, tuple))
		if self._bank_buttons != None:
			for button in self._bank_buttons:
				button.remove_value_listener(self._bank_value)
		self._bank_buttons = buttons
		if self._bank_buttons != None:
			identify_sender = True
			for button in self._bank_buttons:
				button.add_value_listener(self._bank_value, identify_sender)
		self.update()
		return None
	
	def set_parameter_controls(self, controls):
		assert (controls != None)
		assert isinstance(controls, tuple)
		if self._device != None and self._parameter_controls != None:
			for control in self._parameter_controls:
				control.release_parameter()
		for control in controls:
			assert (control != None)
			assert isinstance(control, EncoderElement)
		self._parameter_controls = controls
		self.update()
		return None
	

	def set_lock_to_device(self, lock, device):
		assert isinstance(lock, type(False))
		assert (lock is not self._locked_to_device)
		if lock:
			self.set_device(device)
		else:
			assert (device == self._device)
		self._locked_to_device = lock
		if self.is_enabled():
			if (self._lock_button != None):
				if self._locked_to_device:
					self._lock_button.turn_on()
				else:
					self._lock_button.turn_off()		

					
	def set_lock_button(self, button):
		assert ((button == None) or isinstance(button, ButtonElement))
		if self._lock_button != None:
			self._lock_button.remove_value_listener(self._lock_value)
			self._lock_button = None
		self._lock_button = button
		if self._lock_button != None:
			self._lock_button.add_value_listener(self._lock_value)
		self.update()
		return None

	
	def set_on_off_button(self, button):
		assert ((button == None) or isinstance(button, ButtonElement))
		if self._on_off_button != None:
			self._on_off_button.remove_value_listener(self._on_off_value)
			self._on_off_button = None
		self._on_off_button = button
		if self._on_off_button != None:
			self._on_off_button.add_value_listener(self._on_off_value)
		self.update()
		return None
	
	def set_lock_callback(self, callback):
		assert (self._lock_callback == None)
		assert (callback != None)
		assert (dir(callback).count('im_func') is 1)
		self._lock_callback = callback
		return None
	
	def restore_bank(self, bank_index):
		if self._device != None and self._is_banking_enabled() and self._locked_to_device and self._number_of_parameter_banks() > bank_index and self._bank_index != bank_index:
			self._bank_index = bank_index
			self.update()
		return None
	
	def device_name_data_source(self):
		if self._device_name_data_source == None:
			self._device_name_data_source = DisplayDataSource()
			self._on_device_name_changed()
		return self._device_name_data_source
	

	def update(self):
		if (self.is_enabled() and (self._device != None)):
			self._device_bank_registry[self._device] = self._bank_index
			if (self._parameter_controls != None):
				old_bank_name = self._bank_name #added
				self._assign_parameters()
				if self._bank_name != old_bank_name: #added
					try:
						self._show_msg_callback(self._device.name + ' Bank: ' + self._bank_name) #added
					except:
						pass
			if ((self._bank_up_button != None) and (self._bank_down_button != None)):
				if (self._number_of_parameter_banks()) > (self._bank_index + 1):
					self._bank_up_button.turn_on()
				else:
					self._bank_up_button.turn_off()
				if (self._bank_index > 0):
					self._bank_down_button.turn_on()
				else:
					self._bank_down_button.turn_off()
			if (self._bank_buttons != None):
				for index in range(len(self._bank_buttons)):
					if (index == self._bank_index):
						self._bank_buttons[index].turn_on()
					else:
						self._bank_buttons[index].turn_off()
		else:
			if (self._lock_button != None):
				self._lock_button.turn_off()
			if (self._bank_up_button != None):
				self._bank_up_button.turn_off()
			if (self._bank_down_button != None):
				self._bank_down_button.turn_off()
			if (self._bank_buttons != None):
				for button in self._bank_buttons:
					button.turn_off()
			if (self._parameter_controls != None):
				for control in self._parameter_controls:
					control.release_parameter()
		#self._rebuild_callback()		
		

	def _bank_up_value(self, value):
		assert (self._bank_up_button != None)
		assert (value != None)
		assert isinstance(value, int)
		if self.is_enabled():
			if ((not self._bank_up_button.is_momentary()) or (value is not 0)):
				if (self._device != None):
					num_banks = self._number_of_parameter_banks()
					if (self._bank_down_button == None):
						self._bank_name = ''
						self._bank_index = ((self._bank_index + 1) % num_banks)
						self.update()
					elif (num_banks > (self._bank_index + 1)):
						self._bank_name = ''
						self._bank_index += 1
						self.update()
						

	def _bank_down_value(self, value):
		assert (self._bank_down_button != None)
		assert (value != None)
		assert isinstance(value, int)
		if self.is_enabled():
			if ((not self._bank_down_button.is_momentary()) or (value is not 0)):
				if ((self._device != None) and (self._bank_index > 0)):
					self._bank_name = ''
					self._bank_index -= 1
					self.update()
					
					
	def _lock_value(self, value):
		assert (self._lock_button != None)
		assert (self._lock_callback != None)
		assert (value != None)
		assert isinstance(value, int)
		if not self._lock_button.is_momentary() or value is not 0:
			self._lock_callback()
		return None
	
	def _on_off_value(self, value):
		assert (self._on_off_button != None)
		assert (value in range(128))
		if not self._on_off_button.is_momentary() or value is not 0:
			parameter = self._on_off_parameter()
			if parameter != None and parameter.is_enabled:
				parameter.value = float(int(parameter.value == 0.0))
		return None
	

	def _bank_value(self, value, button):
		assert (self._bank_buttons != None)
		assert (value != None)
		assert (button != None)
		assert isinstance(value, int)
		assert isinstance(button, ButtonElement)
		assert (list(self._bank_buttons).count(button) == 1)
		if self.is_enabled() and self._device != None: #added
			if ((not button.is_momentary()) or (value is not 0)):
				bank = list(self._bank_buttons).index(button)
				if (bank != self._bank_index):
					if (self._number_of_parameter_banks() > bank):
						self._bank_name = '' #added
						self._bank_index = bank
						self.update()
				else:
					try:
						self._show_msg_callback(self._device.name + ' Bank: ' + self._bank_name)
					except:
						pass

	def _is_banking_enabled(self):
		direct_banking = (self._bank_buttons != None)
		roundtrip_banking = (self._bank_up_button != None)
		increment_banking = ((self._bank_up_button != None) and (self._bank_down_button != None))
		return (direct_banking or (roundtrip_banking or increment_banking))


	def _assign_parameters(self):
		assert self.is_enabled()
		assert (self._device != None)
		assert (self._parameter_controls != None)
		self._bank_name = ('Bank ' + str(self._bank_index + 1)) #added
		if (self._device.class_name in list(self._device_banks.keys())): #modified
			assert (self._device.class_name in list(self._device_best_banks.keys()))
			banks = self._device_banks[self._device.class_name]
			bank = None
			#if (not self._is_banking_enabled()):
			#	 banks = self._device_best_banks[self._device.class_name]
			#	 self._bank_name = 'Best of Parameters' #added
			if (len(banks) > self._bank_index):
				bank = banks[self._bank_index]
				if self._is_banking_enabled(): #added
					if self._device.class_name in list(self._device_bank_names.keys()): #added
						self._bank_name = self._device_bank_names[self._device.class_name] #added *recheck
			assert ((bank == None) or (len(bank) >= len(self._parameter_controls)))
			for index in range(len(self._parameter_controls)):
				parameter = None
				if (bank != None):
					parameter = get_parameter_by_name(self._device, bank[index])
				if (parameter != None):
					self._parameter_controls[index].connect_to(parameter)
				else:
					self._parameter_controls[index].release_parameter()
		else:
			parameters = self._device_parameters_to_map()
			num_controls = len(self._parameter_controls)
			index = (self._bank_index * num_controls)
			for control in self._parameter_controls:
				if (index < len(parameters)):
					control.connect_to(parameters[index])
				else:
					control.release_parameter()
				index += 1


	def _on_device_name_changed(self):
		if (self._device_name_data_source != None):
			if (self.is_enabled() and (self._device != None)):
				self._device_name_data_source.set_display_string(self._device.name)
			else:
				self._device_name_data_source.set_display_string('No Device')


	def _on_parameters_changed(self):
		self.update()


	def _on_off_parameter(self):
		result = None
		if (self._device != None):
			for parameter in self._device.parameters:
				if str(parameter.name).startswith('Device On'):
					result = parameter
					break
		return result


	def _on_on_off_changed(self):
		if (self.is_enabled() and (self._on_off_button != None)):
			turn_on = False
			if (self._device != None):
				parameter = self._on_off_parameter()
				turn_on = ((parameter != None) and (parameter.value > 0.0))
			if turn_on:
				self._on_off_button.turn_on()
			else:
				self._on_off_button.turn_off()


	def _device_parameters_to_map(self):
		assert self.is_enabled()
		assert (self._device != None)
		assert (self._parameter_controls != None)
		return self._device.parameters[1:] #check this...


	def _number_of_parameter_banks(self):
		return number_of_parameter_banks(self._device) #added
