# by amounra 0216 : http://www.aumhaa.com

import Live
from re import *

from ableton.v2.control_surface.component import Component
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement
from aumhaa.v2.control_surface.components.mode_selector import ModeSelectorComponent
from ableton.v2.base.event import listens, listens_group
from ableton.v2.control_surface.control import ButtonControl

from aumhaa.v2.control_surface.elements.mono_button import MonoButtonElement

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

DEVICE_COLORS = {'midi_effect':2,
				'audio_effect':5,
				'instrument':3,
				'Operator':4,
				'DrumGroupDevice':6,
				'MxDeviceMidiEffect':2,
				'MxDeviceInstrument':3,
				'MxDeviceAudioEffect':5,
				'InstrumentGroupDevice':3,
				'MidiEffectGroupDevice':2,
				'AudioEffectGroupDevice':5}

SELECTED_COLORSHIFT = 7


def enumerate_track_device(track):
	devices = []
	if hasattr(track, 'devices'):
		for device in track.devices:
			devices.append(device)
			if device.can_have_chains:
				for chain in device.chains:
					for chain_device in enumerate_track_device(chain):
						devices.append(chain_device)
	return devices



class DeviceSelectorComponent(Component):


	assign_button = ButtonControl(color = 'DeviceSelector.AssignOff', pressed_color = 'DeviceSelector.AssignOn')

	def __init__(self, script, prefix = '@d', *a, **k):
		super(DeviceSelectorComponent, self).__init__(*a, **k)
		self.log_message = script.log_message
		self._script = script
		self._prefix = prefix
		self._offset = 0
		self._buttons = []
		self._device_registry = []
		self._watched_device = None
		self._device_colors = DEVICE_COLORS
		self._selected_colorshift = SELECTED_COLORSHIFT
		self._device_listener.subject = self.song
		self._device_listener()
		self._off_value = 0


	def disconnect(self, *a, **k):
		super(DeviceSelectorComponent, self).disconnect()


	def set_offset(self, offset):
		self._offset = offset
		self.update()


	def set_matrix(self, matrix):
		buttons = []
		if not matrix is None:
			for button, address in matrix.iterbuttons():
				#self._script.log_message('button is: ' + str(button))
				if not button is None:
					button.use_default_message()
					if hasattr(button, 'set_enabled'):
 						button.set_enabled(True)
					elif hasattr(button, 'suppress_script_forwarding'):
						button.suppress_script_forwarding = False
					buttons.append(button)
		self.set_buttons(buttons)


	def set_buttons(self, buttons):
		for button in self._buttons:
			button and button.reset()
		self._buttons = buttons or []
		self._on_button_value.replace_subjects(self._buttons)
		self.update()


	def set_assign_button(self, button):
		debug('set assign button:', button)
		self.assign_button.set_control_element(button)


	@listens_group('value')
	def _on_button_value(self, value, sender):
		if self.is_enabled():
			if value:
				if self.assign_button.is_pressed:
					self.assign_device(self._buttons.index(sender))
				else:
					self.select_device(self._buttons.index(sender))


	def assign_device(self, index):
		device = self.song.appointed_device
		if not device is None and hasattr(device, 'name'):
			prefix = str(self._prefix)+'_'
			offset = self._offset
			key =  prefix + str(index + 1 + offset)
			name = device.name.split(' ')
			if key in name:
				name.remove(key)
			else:
				old_entry = self._device_registry[index]
				if old_entry and hasattr(old_entry, 'name'):
					old_name = old_entry.name.split(' ')
					if key in old_name:
						old_name.remove(key)
						old_entry.name = ' '.join(old_name)
				for sub in name:
					sub.startswith(prefix) and name.remove(sub)
				name.insert(0, key)
			device.name = ' '.join(name)
			self.scan_all()
			self.update()


	def select_device(self, index):
		if self.is_enabled():
			preset = None
			if index < len(self._device_registry):
				preset = self._device_registry[index]
			if not preset is None and isinstance(preset, Live.Device.Device):
				self.song.view.select_device(preset)
				self._script._device_provider.device = preset
				#self._script.set_appointed_device(preset)
				try:
					self._script.monomodular.is_mod(preset) and self._script.modhandler.select_mod(self._script.monomodular.is_mod(preset))
				except:
					pass
			self.update()


	def scan_all(self):
		#debug('scan all--------------------------------')
		self._device_registry = [None for index in range(len(self._buttons))]
		prefix = str(self._prefix)+':'
		prefix2 = str(self._prefix)+'_'
		offset = self._offset
		preset = None
		tracks = self.song.tracks + self.song.return_tracks + tuple([self.song.master_track])
		for track in tracks:
			for device in enumerate_track_device(track):
				for index, entry in enumerate(self._device_registry):
					key = str(prefix + str(index + 1 + offset))
					key2 = str(prefix2 + str(index + 1 + offset))
					if device.name.startswith(key+' ') or device.name == key:
						self._device_registry[index] = device
					elif device.name.startswith(key2+' ') or device.name == key2:
						self._device_registry[index] = device
					elif (device.name.startswith('*' +key+' ') or device.name == ('*' +key))  and device.can_have_chains and len(device.chains) and len(device.chains[0].devices):
						self._device_registry[index] = device.chains[0].devices[0]
		self.update()
		#debug('device registry: ' + str(self._device_registry))



	@listens('appointed_device')
	def _device_listener(self, *a, **k):
		#debug('device_listener')
		self._on_name_changed.subject = self.song.appointed_device
		self._watched_device = self.song.appointed_device
		if self.is_enabled():
			self.update()


	@listens('name')
	def _on_name_changed(self):
		#debug('on name changed')
		if self._watched_device == self.song.appointed_device:
			self.scan_all()


	def on_enabled_changed(self):
		if self.is_enabled():
			self.update()


	def update(self):
		if self.is_enabled():
			if len(self._device_registry) != len(self._buttons):
				self.scan_all()
			name = 'None'
			dev = self.song.appointed_device
			offset = self._offset
			if self._buttons:
				for index in range(len(self._buttons)):
					preset = self._device_registry[index]
					button = self._buttons[index]
					if isinstance(button, ButtonElement):
						if isinstance(preset, Live.Device.Device) and hasattr(preset, 'name'):
							name = preset.name
							dev_type = preset.type
							dev_class = preset.class_name
							val = (dev_class in self._device_colors and self._device_colors[dev_class]) or (dev_type in self._device_colors and self._device_colors[dev_type]) or 7
							selected_shift = (dev == preset)*self._selected_colorshift
							button.send_value(val + selected_shift)
						else:
							button.send_value(self._off_value)
