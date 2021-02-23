#by amounra 0915 : http://www.aumhaa.com


import Live
from re import *
from _Generic.Devices import *

from aumhaa.v2.control_surface.components.live8_device import Live8DeviceComponent as DeviceComponent
from ableton.v2.base import depends, listenable_property, listens, listens_group, liveobj_changed, liveobj_valid, EventObject
#from ableton.v2.control_surface.components.device import DeviceProvider, select_and_appoint_device, device_to_appoint
#from ableton.v2.control_surface.components import Devicecomponent


from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()


class MonoDeviceComponent(DeviceComponent):
	__doc__ = ' Class representing a device linked to a Monomodular client, to be redirected by it from Max '


	def __init__(self, parent = None, bank_dict={}, mod_types={}, *a, **k):
		super(MonoDeviceComponent, self).__init__(*a, **k)
		self._MOD_BANK_DICT = bank_dict
		self._MOD_TYPES = mod_types
		self._type = None
		self._device_parent = None
		self._parent = parent
		self._chain = 0
		self._device_chain = 0
		self._number_params = 12
		self._params = []
		self._custom_parameter = []
		self._nodevice = NoDevice()
		self._is_alted = False


	def disconnect(self):
		if self._device_parent != None:
			if self._device_parent.canonical_parent != None:
				if self._device_parent.canonical_parent.devices_has_listener(self._parent_device_changed):
					self._device_parent.canonical_parent.remove_devices_listener(self._parent_device_changed)
		if self._device != None:
			if self._device.canonical_parent != None:
				if self._device.canonical_parent != None:
					if self._device.canonical_parent.devices_has_listener(self._device_changed):
						self._device.canonical_parent.remove_devices_listener(self._device_changed)
		self._type = None
		self._device_parent = None
		self._device_chain = None
		super(MonoDeviceComponent, self).disconnect()


	def disconnect_client(self):
		self.set_device(None)
		self._custom_parameter = []
		self._device_parent = None
		self._device_chain = 0
		self._set_type(None)



	def set_device_defs(self, bank_dict={}, mod_types={}):
		debug('set device defs', bank_dict, mod_types)
		self._MOD_BANK_DICT = bank_dict
		self._MOD_TYPES = mod_types
		self.update()


	def _set_type(self, mod_device_type):
		#self.log_message('set type: ' + str(mod_device_type))
		if mod_device_type == None:
			self._device_banks = DEVICE_DICT
			self._device_best_banks = DEVICE_BOB_DICT
			self._device_bank_names = BANK_NAME_DICT
			self._set_device_parent(None)
			self.set_enabled(False)
		elif mod_device_type in self._MOD_TYPES.keys():
			self.set_enabled(True)
			self._type = mod_device_type
			self._device_banks = self._MOD_TYPES[self._type]
			self._device_best_banks = self._MOD_TYPES[self._type]
			self._device_bank_names = self._MOD_BANK_DICT
			self._set_device_parent(self._device_parent)


	def _set_device_parent(self, mod_device_parent, single = None):
		#self.log_message('_set_device_parent ' + str(mod_device_parent) + ' ' + str(single))
		if self._device_parent != None:
			if self._device_parent.canonical_parent != None:
				if self._device_parent.canonical_parent.devices_has_listener(self._parent_device_changed):
					self._device_parent.canonical_parent.remove_devices_listener(self._parent_device_changed)
		if isinstance(mod_device_parent, Live.Device.Device):
			#self.log_message('_set_device_parent is device')
			if mod_device_parent.can_have_chains and single is None:
				self._device_parent = mod_device_parent
				if self._device_parent.canonical_parent != None:
					if not self._device_parent.canonical_parent.devices_has_listener(self._parent_device_changed):
						self._device_parent.canonical_parent.add_devices_listener(self._parent_device_changed)
				self._select_parent_chain(self._device_chain)
			else:
				self._device_parent = mod_device_parent
				self.set_device(self._device_parent, True)
		elif 'NoDevice' in self._device_banks.keys():
			#self.log_message('_set_device_parent is NoDevice')
			self._device_parent = self._nodevice
			self._device_chain = 0
			self.set_device(self._device_parent, True)
		else:
			#self.log_message('_set_device_parent is \"None\"')
			self._device_parent = None
			self._device_chain = 0
			self.set_device(self._device_parent, True)


	def _select_parent_chain(self, chain, force = False):
		#self.log_message('_select_parent_chain ' + str(chain)) # + ' ' + str(self.is_enabled()))
		self._device_chain = chain  #self._chain = chain
		if self._device_parent != None:
			if isinstance(self._device_parent, Live.Device.Device):
				if self._device_parent.can_have_chains:
					if len(self._device_parent.chains) > chain:
						if len(self._device_parent.chains[chain].devices) > 0:
							self.set_device(self._device_parent.chains[chain].devices[0], force)
					elif 'NoDevice' in self._device_banks.keys():
						self.set_device(self._nodevice, True)
					else:
						self.set_device(None)
						if self.is_enabled():
							for host in self._parent._active_handlers:
								for control in host._parameter_controls:
									control.reset()


	def _select_drum_pad(self, pad, force = False):
		if self._device_parent != None:
			if isinstance(self._device_parent, Live.Device.Device):
				if self._device_parent.can_have_drum_pads and self._device_parent.has_drum_pads:
					pad = self._device_parent.drum_pads[pad]
					#self._parent.log_message('pad is: ' + str(pad))
					if pad.chains and pad.chains[0] and pad.chains[0].devices and isinstance(pad.chains[0].devices[0], Live.Device.Device):
						self.set_device(pad.chains[0].devices[0], force)
					elif 'NoDevice' in self._device_banks.keys():
						self.set_device(self._nodevice, True)
					else:
						self.set_device(None)
						if self.is_enabled():
							for host in self._parent._active_handlers:
								for control in host._parameter_controls:
									control.reset()


	def _parent_device_changed(self):
		#self.log_message('parent_device_changed')
		self._set_device_parent(None)
		self._parent.send('lcd', 'parent', 'check')


	def _device_changed(self):
		#self.log_message('device_changed')
		self.set_device(None)
		self._parent.send('lcd', 'device', 'check')


	def _number_of_parameter_banks(self):
		return self.number_of_parameter_banks(self._device) #added


	def get_parameter_by_name(self, device, name):
		""" Find the given device's parameter that belongs to the given name """
		#self.log_message('get parameter: device-' + str(device) + ' name-' + str(name))
		result = None
		for i in device.parameters:
			if (i.original_name == name):
				result = i
				break
		if result == None:
			if name == 'Mod_Chain_Pan':
				if device.canonical_parent.mixer_device != None:
					if device.canonical_parent.mixer_device.panning != None:
						result = device.canonical_parent.mixer_device.panning
			elif name == 'Mod_Chain_Vol':
				if device.canonical_parent.mixer_device !=None:
					if device.canonical_parent.mixer_device.panning != None:
						result = device.canonical_parent.mixer_device.volume
			elif(match('Mod_Chain_Send_', name)):
				name = int(name.replace('Mod_Chain_Send_', ''))
				if device.canonical_parent != None:
					if device.canonical_parent.mixer_device != None:
						if device.canonical_parent.mixer_device.sends != None:
							if len(device.canonical_parent.mixer_device.sends)>name:
								result = device.canonical_parent.mixer_device.sends[name]
			elif(match('ModDevice_', name) and self._parent.device != None):
				name = name.replace('ModDevice_', '')
				#self.log_message('modDevice with name: ' + str(name))
				for i in self._parent.device.parameters:
					if (i.name == name):
						result = i
						break
			elif match('CustomParameter_', name):
				index = int(name.replace('CustomParameter_', ''))
				if len(self._custom_parameter)>index:
					 if isinstance(self._custom_parameter[index], Live.DeviceParameter.DeviceParameter):
						 result = self._custom_parameter[index]

		return result


	def _turn_on_filter(self, param):
		param.value = 1
		param.value = 0
		self.update()


	def _recheck_FF(self, device):
		if get_parameter_by_name(device, "Filter Freq") != None:
			self.update()


	def _assign_parameters(self, host, *a):
		#debug('assign_parameters '+str(host))
		assert (self._device != None)
		if(host.is_enabled()):
			for control in host._parameter_controls:
				control.clear_send_cache()
			self._bank_name = ('Bank ' + str(self._bank_index + 1)) #added
			if (self._device.class_name in self._device_banks.keys()):
				class_name = self._device.class_name
			else:
				class_name = 'Other'
			if (class_name in self._device_banks.keys()): #modified
				assert (class_name in self._device_best_banks.keys())
				banks = self._device_banks[class_name]
				if '_alt_device_banks' in dir(host):
					if self._type in host._alt_device_banks.keys():
						if (class_name in host._alt_device_banks[self._type].keys()):
							banks = host._alt_device_banks[self._type][class_name]
				bank = None
				if (len(banks) > self._bank_index):
					bank = banks[self._bank_index]
					if self._is_banking_enabled(): #added
						if class_name in self._device_bank_names.keys(): #added
							self._bank_name[self._bank_index] = self._device_bank_names[class_name] #added *recheck
				#assert (bank == None)	# or (len(bank) >= len(self._parameter_controls)))
				if not host._parameter_controls is None:
					for index in range(len(host._parameter_controls)):
						parameter = None
						corrected_index = index + (self._is_alted * 8)
						if (bank != None) and (corrected_index in range(len(bank))):
							parameter = self.get_parameter_by_name(self._device, bank[corrected_index])
						if (parameter != None):
							host._parameter_controls[index].connect_to(parameter)
						else:
							host._parameter_controls[index].release_parameter()
							host._parameter_controls[index].send_value(0, True)
			else:
				#debug('setting defautl parameters-------------------')
				parameters = self._device_parameters_to_map()
				if not host._parameter_controls is None:
					num_controls = len(host._parameter_controls)
					index = (self._bank_index * num_controls)
					for control in host._parameter_controls:
						if (index < len(parameters)):
							control.connect_to(parameters[index])
						else:
							control.release_parameter()
							control.send_value(0, True)
						index += 1


	def _assign_params(self, *a):
		#self.log_message('assign params!')
		if self._device != None and not len(self._params) is 0:
			self._bank_name = ('ModBank ' + str(self._bank_index + 1)) #added
			if (self._device.class_name in self._device_banks.keys()):
				class_name = self._device.class_name
			else:
				class_name = 'Other'
			if (class_name in self._device_banks.keys()): #modified
				assert (class_name in self._device_best_banks.keys())
				banks = self._device_banks[class_name]
				bank = None
				if (len(banks) > self._bank_index):
					bank = banks[self._bank_index]
					if self._is_banking_enabled(): #added
						if class_name in self._device_bank_names.keys(): #added
							self._bank_name[self._bank_index] = self._device_bank_names[class_name] #added *recheck
				for index in range(len(self._params)):
					parameter = None
					if (bank != None) and (index in range(len(bank))):
						parameter = self.get_parameter_by_name(self._device, bank[index])
					if (parameter != None):
						self._params[index]._parameter=self._connect_param(self._params[index], parameter)
					else:
						self._params[index]._parameter=self._connect_param(self._params[index], None)
			else:
				#self.log_message('not in keys ')
				parameters = self._device.parameters[1:]
				num_controls = len(self._params)
				index = (self._bank_index * num_controls)
				for param in self._params:
					#self.log_message('assigning to param ')
					if (index < len(parameters)):
						self._params[index]._parameter=self._connect_param(self._params[index], parameters[index])
					else:
						self._params[index]._parameter=self._connect_param(self._params[index], None)
					index += 1

		else:
			index = 0
			for param in self._params:
				self._params[index]._parameter = self._connect_param(self._params[index], None)
				index += 1

		for param in self._params:
			param._value_change()


	def _connect_param(self, holder, parameter):
		#self.log_message('connecting ') # + str(holder._parameter) + ' ' + str(parameter))
		self._mapped_to_midi_velocity = False
		if (holder._parameter!= None):
			if holder._parameter.value_has_listener(holder._value_change):
				holder._parameter.remove_value_listener(holder._value_change)
				#self.log_message('removing ' + str(holder._parameter.name))
		if parameter != None:
			assignment = parameter
			if(str(parameter.name) == str('Track Volume')):		#checks to see if parameter is track volume
				if(parameter.canonical_parent.canonical_parent.has_audio_output is False):		#checks to see if track has audio output
					if(len(parameter.canonical_parent.canonical_parent.devices) > 0):
						if(str(parameter.canonical_parent.canonical_parent.devices[0].class_name)==str('MidiVelocity')):	#if not, looks for velicty as first plugin
							assignment = parameter.canonical_parent.canonical_parent.devices[0].parameters[6]				#if found, assigns fader to its 'outhi' parameter
							self._mapped_to_midi_velocity = True
			assignment.add_value_listener(holder._value_change)
			#self.log_message('adding ' + str(assignment.name))
			return assignment
		else:

			return None


	def _on_device_name_changed(self):
		if (self._device != None):
			self._parent.send('lcd', 'device_name', 'lcd_name', str(self.generate_strip_string(str(self._device.name))))
		else:
			self._parent.send('lcd', 'device_name', 'lcd_name', ' ')


	def _params_value_change(self, sender, control_name, feedback = True):
		#self.log_message('params change ' + str(sender) + str(control_name))
		pn = ' '
		pv = ' '
		val = 0
		if(sender != None):
			pn = str(self.generate_strip_string(str(sender.name)))
			if sender.is_enabled:
				try:
					value = str(sender)
				except:
					value = ' '
				pv = str(self.generate_strip_string(value))
			else:
				pv = '-bound-'
			val = ((sender.value - sender.min) / (sender.max - sender.min))  * 127
		self._parent.send('lcd', control_name, 'lcd_name', pn)
		self._parent.send('lcd', control_name, 'lcd_value', pv)
		if feedback == True:
			self._parent.send('lcd', control_name, 'encoder_value', val)


	def generate_strip_string(self, display_string):
		NUM_CHARS_PER_DISPLAY_STRIP = 12
		if (not display_string):
			return (' ' * NUM_CHARS_PER_DISPLAY_STRIP)
		if ((len(display_string.strip()) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)) and (display_string.endswith('dB') and (display_string.find('.') != -1))):
			display_string = display_string[:-2]
		if (len(display_string) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)):
			for um in [' ',
			 'i',
			 'o',
			 'u',
			 'e',
			 'a']:
				while ((len(display_string) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)) and (display_string.rfind(um, 1) != -1)):
					um_pos = display_string.rfind(um, 1)
					display_string = (display_string[:um_pos] + display_string[(um_pos + 1):])
		else:
			display_string = display_string.center((NUM_CHARS_PER_DISPLAY_STRIP - 1))
		ret = u''
		for i in range((NUM_CHARS_PER_DISPLAY_STRIP - 1)):
			if ((ord(display_string[i]) > 127) or (ord(display_string[i]) < 0)):
				ret += ' '
			else:
				ret += display_string[i]

		ret += ' '
		ret = ret.replace(' ', '_')
		assert (len(ret) == NUM_CHARS_PER_DISPLAY_STRIP)
		return ret


	def set_device(self, device, force = False):
		#debug('set device: ' + str(device) + ' ' + str(force))
		#debug('set device 0')
		assert ((device == None) or isinstance(device, Live.Device.Device) or isinstance(device, NoDevice))
		if self._device != None:
			if self._device.canonical_parent != None:
				if self._device.canonical_parent.devices_has_listener(self._device_changed):
					self._device.canonical_parent.remove_devices_listener(self._device_changed)
		#debug('set device 1')
		if ((not self._locked_to_device) and (device != self._device)) or force==True:
			if (self._device != None):
				if self._device.name_has_listener(self._on_device_name_changed):
					self._device.remove_name_listener(self._on_device_name_changed)
				if self._device.parameters_has_listener(self._on_parameters_changed):
					self._device.remove_parameters_listener(self._on_parameters_changed)
				parameter = self._on_off_parameter()
				if (parameter != None):
					if parameter.value_has_listener(self._on_on_off_changed):
						parameter.remove_value_listener(self._on_on_off_changed)
				for host in self._parent._active_handlers:
					if (host._parameter_controls != None):
						for control in host._parameter_controls:
							control.release_parameter()
			self._device = device
			#debug('set device 2')
			if (self._device != None):
				if self._device.canonical_parent != None:
					if not self._device.canonical_parent.devices_has_listener(self._device_changed):
						self._device.canonical_parent.add_devices_listener(self._device_changed)
				self._bank_index = 0
				self._device.add_name_listener(self._on_device_name_changed)
				self._device.add_parameters_listener(self._on_parameters_changed)
				parameter = self._on_off_parameter()
				if (parameter != None):
					parameter.add_value_listener(self._on_on_off_changed)
			#debug('set device 3')
			for key in self._device_bank_registry.keys():
				if (key == self._device):
					self._bank_index = self._device_bank_registry.get(key, 0)
					del self._device_bank_registry[key]
					break
			self._bank_name = '<No Bank>' #added
			#debug('set device 4')
			self._on_device_name_changed()
			self.update()


	def update(self):
		#debug('monoDevice update!')
		if self._device != None:
			self._device_bank_registry[self._device] = self._bank_index
			for host in self._parent.active_handlers():
				if host.is_enabled() and not host._parameter_controls is None and len(host._parameter_controls) > 0:
					old_bank_name = self._bank_name
					self._assign_parameters(host)
		else:
			#debug('device is none')
			for host in self._parent._active_handlers:
				if host._parameter_controls != None:
					for control in host._parameter_controls:
						control.release_parameter()
		self._update_params()
		self._assign_params()
		for host in self._parent._active_handlers:
			if host.is_enabled():
				if not host._parameter_controls is None:
					if len(host._parameter_controls) > 0:
						host._script.request_rebuild_midi_map()
				else:
					host.update_device()


	def _update_params(self):
		count = self._number_params
		used_host = None
		if self._number_params > 0:
			count = self._number_params
		if count != len(self._params):
			if self._number_params > 0:
				self._params = [ParamHolder(self, None, index) for index in range(self._number_params)]
			else:
				for param in self._params:
					self._connect_param(param, None)
				self._params = []


	def _device_parameters_to_map(self):
		assert(self._device != None)
		return self._device.parameters[1:]


	def set_number_params(self, number, *a):
		#debug('set number params' + str(number))
		self._number_params = number
		#self._parent._host.schedule_message(1, self.update)
		self.update()


	def set_number_custom(self, number, *a):
		self._custom_parameter = [None for index in range(number)]


	def set_custom_parameter(self, number, parameter, *a):
		if number < len(self._custom_parameter):
			#debug('custom='+str(parameter))
			if isinstance(parameter, Live.DeviceParameter.DeviceParameter) or parameter is None:
				#debug('custom is device:'+str(parameter))
				self._custom_parameter[number] = parameter
				self.update()


	def set_mod_device_type(self, mod_device_type, *a):
		#debug('set type ' + str(mod_device_type))
		for host in self._parent._active_handlers:
			host.on_enabled_changed()
		self._set_type(mod_device_type)


	def set_mod_device(self, mod_device, *a):
		#debug('set device ' + str(mod_device))
		self.set_device(mod_device, True)
		for host in self._parent._active_handlers:
			host.update()


	def set_mod_device_parent(self, mod_device_parent, single=None, *a):
		#debug('set parent ' + str(mod_device_parent))
		self._set_device_parent(mod_device_parent, single)
		for host in self._parent._active_handlers:
			host.update()


	def set_mod_device_chain(self, chain, *a):
		#debug('set_chain ' + str(chain))
		self._select_parent_chain(chain, True)
		for host in self._parent._active_handlers:
			host.update()


	def set_mod_drum_pad(self, pad, *a):
		self._select_drum_pad(pad, True)
		for host in self._parent._active_handlers:
			host.update()


	def set_mod_parameter_value(self, num, val, *a):
		#debug('set_pval ' + str(num) + ' ' + str(val))
		if self._device != None:
			if num < len(self._params):
				self._params[num]._change_value(val)


	def set_custom_parameter_value(self, num, value, *a):
		if num < len(self._custom_parameter):
			parameter = self._custom_parameter[num]
			if parameter != None:
				newval = float(float(float(value)/127) * float(parameter.max - parameter.min)) + parameter.min
				parameter.value = newval


	def set_mod_device_bank(self, bank_index, *a):
		#debug('set bank ' + str(bank_index))
		if self.is_enabled():
			if (self._device != None):
				if (self._number_of_parameter_banks() > bank_index):
					self._bank_name = ''
					self._bank_index = bank_index
					self.update()


	def number_of_parameter_banks(self, device):
		""" Determine the amount of parameter banks the given device has """
		result = 0
		if (device != None):
			result = 1
			if (device.class_name in self._device_banks.keys()):
				device_bank = self._device_banks[device.class_name]
				result = len(device_bank)
			elif len(self._params > 0):
				param_count = len(list(device.parameters))
				result = (param_count / len(self._params))
				if (not ((param_count % len(self._params)) == 0)):
					result += 1
		return result


	def on_enabled_changed(self):
		#debug('on_enabled_changed '+str(self._parent)+' '+str(self.is_enabled()))
		self.update()


	def set_all_params_to_defaults(self, *a):
		debug('set all parmas to default')
		if self._params:
			for holder in self._params:
				name = None
				try:
					param = holder._parameter
				except:
					param = None
				if param:
					name = param.name
					#debug('param name:', name)
					if name:
						for item in name.split(' '):
							if len(str(item)) and str(item)[0]=='@':
								vals = item[1:].split(':')
								if vals[0] in ['def', 'rst']:
									#self.set_param_to_default(param, vals[1])
									rst_val = float(vals[1])/100
									newval = float(rst_val * (param.max - param.min)) + param.min
									param.value = newval
								else:
									debug('no def value...')




class ParamHolder(object):

	__doc__ = ' Simple class to hold the owner of a Device.parameter and forward its value when receiving updates from Live, or update its value from a mod '


	def __init__(self, parent, control, index):
		self._control = control
		self._control_name = 'Encoder_'+str(index)
		self._parent = parent
		self._parameter = None
		self._feedback = True


	def _value_change(self):
		control_name = self._control_name
		#if not self._control is None:
		#	control_name = self._control.name
		self._parent._params_value_change(self._parameter, control_name, self._feedback)
		self._feedback = True


	def _change_value(self, value):
		if(self._parameter != None):
			if(self._parameter.is_enabled):
				self._feedback = False
				newval = float(float(float(value)/127) * float(self._parameter.max - self._parameter.min)) + self._parameter.min
				#self._parent._parent._host.log_message('newval ' + str(newval))
				self._parameter.value = newval




class NoDevice(object):
	__doc__ = 'Dummy Device with no parameters and custom class_name that is used when no device is selected, but parameter assignment is still necessary'


	def __init__(self):
		self.class_name = 'NoDevice'
		self.parameters = []
		self.canonical_parent = None
		self.can_have_chains = False
		self.name = 'NoDevice'


	def add_name_listener(self, callback=None):
		pass


	def remove_name_listener(self, callback=None):
		pass


	def name_has_listener(self, callback=None):
		return False


	def add_parameters_listener(self, callback=None):
		pass


	def remove_parameters_listener(self, callback=None):
		pass


	def parameters_has_listener(self, callback=None):
		return False


	def store_chosen_bank(self, callback=None):
		pass




#a
