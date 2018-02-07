# by amounra 0216 : http://www.aumhaa.com

from __future__ import with_statement
import Live
import time
import math
from re import *

from _Generic.Devices import *

from ableton.v2.control_surface.components.device import DeviceComponent

from ableton.v2.control_surface.mode import DelayMode

from ableton.v2.control_surface.components.session_ring import SessionRingComponent

"""Imports from aumhaa"""
from aumhaa.v2.control_surface.elements.mono_button import MonoButtonElement

from aumhaa.v2.control_surface.elements.mono_encoder import MonoEncoderElement

from aumhaa.v2.control_surface.components.device_selector import DeviceSelectorComponent

from aumhaa.v2.control_surface.components.reset_sends import ResetSendsComponent

from aumhaa.v2.control_surface.mono_modes import ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour

from Codec.Codec import *

TROLL_OFFSET = 0

DEVICE_COLORS = {'midi_effect':22,
				'audio_effect':8,
				'instrument':15,
				'Operator':22,
				'DrumGroupDevice':15,
				'MxDeviceMidiEffect':22,
				'MxDeviceInstrument':15,
				'MxDeviceAudioEffect':8,
				'InstrumentGroupDevice':15,
				'MidiEffectGroupDevice':22,
				'AudioEffectGroupDevice':8}


def release_control(control):
	if control != None:
		control.release_parameter()



class CodexDeviceProvider(EventObject):

	device_selection_follows_track_selection = False

	def __init__(self, return_index = 0, song = None, *a, **k):
		self._return_index = return_index
		super(CodexDeviceProvider, self).__init__(*a, **k)
		returns = song.return_tracks
		self._device = returns[self._return_index].devices[0] if (len(returns)>self._return_index and len(returns[self._return_index].devices)>0) else None
	

	@listenable_property
	def device(self):
		return self._device
	

		
class Codex(Codec):


	def __init__(self, *a, **k):
		self._shifted = False
		super(Codex, self).__init__(*a, **k)
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<<< Codex subclass log opened >>>>>>>>>>>>>>>>>>>>>>>>>')
	

	def _setup_send_reset(self):
		super(Codex, self)._setup_send_reset()

		self._alt_send_reset = ResetSendsComponent(self)
		self._alt_send_reset.name = 'Alt_Reset_Sends'
		self._alt_send_reset.layer = Layer(priority = 4, buttons = self._button_matrix.submatrix[4:, 2])
		self._alt_send_reset.set_enabled(False)
	

	def _setup_device_controls(self):
		super(Codex, self)._setup_device_controls()
		self._device1 = DeviceComponent(device_provider = CodexDeviceProvider(song = self.song, return_index = 0), device_bank_registry = DeviceBankRegistry())
		self._device1.name = 'Device_Component1'
		self._device1.layer = Layer(priority = 4, parameter_controls = self._encoder_matrix.submatrix[:4,:2])
		self._device1.set_enabled(False)


		self._device2 = DeviceComponent(device_provider = CodexDeviceProvider(song = self.song, return_index = 1), device_bank_registry = DeviceBankRegistry())
		self._device2.name = 'Device_Component2'
		self._device2.layer = Layer(priority = 4, parameter_controls = self._encoder_matrix.submatrix[4:,:2])
		self._device2.set_enabled(False)
	

	def _setup_mixer_controls(self):
		super(Codex, self)._setup_mixer_controls()
		self._mixer._selected_strip_layer = AddLayerMode(self._mixer._selected_strip, Layer(priority = 4, send_controls = self._encoder_matrix.submatrix[:4, 2]))
		self._mixer._returns_layer = AddLayerMode(self._mixer, Layer(priority = 4, return_controls = self._encoder_matrix.submatrix[4:7,2]))
		self._mixer._xfade_layer = AddLayerMode(self._mixer, Layer(priority = 4, crossfader_control = self._dial[7][2]))
		self._mixer._troll_layer = AddLayerMode(self._mixer, Layer(priority = 4, volume_controls = self._encoder_matrix.submatrix[:8,3],
									mute_buttons = self._button_matrix.submatrix[:8,3],
									))
	

	def _setup_modes(self):

		self._mixer._mute_layer = AddLayerMode(self._mixer, Layer(priority = 4, mute_buttons = self._button_matrix.submatrix[:8,3],
									))

		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [])
		self._main_modes.add_mode('mix_shifted', [self._mixer, self._mixer._troll_layer, self._device_selector, self._background, DelayMode(delay = .1, mode = tuple([self._troll_shifted_enabled, self._troll_shifted_disabled]), parent_task_group = self._task_group)], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('mix', [self._alt_send_reset, self._device1, self._device2, self._mixer, self._mixer._returns_layer, self._mixer._xfade_layer, self._mixer._troll_layer, self._mixer._select_layer, self._mixer._mute_layer, self._mixer._selected_strip_layer, self._session_navigation, self._background, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('sends_shifted', [self._mixer, self._mixer._sends_layer, self._mixer._select_layer, self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('sends', [self._mixer, self._mixer._sends_layer, self._mixer._select_layer, self._background, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('device_shifted', [self._selected_device_modes, self._device_selector, self._device[0], self._device[1], self._device[2], self._device[3], self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('device', [self._selected_device_modes, self._device[0], self._device[1], self._device[2], self._device[3], self._background, self._mixer._select_layer, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('special_device_shifted', [self._modswitcher, self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('special_device', [self._modswitcher, self._background], behaviour = self._shift_latching(color = 'Mode.Main'))
		#self._main_modes.add_mode('select', [self.normal_encoder_sysex], behaviour = DelayedExcludingMomentaryBehaviour(excluded_groups = ['shifted']))
		self._main_modes.layer = Layer(priority = 4,
										mix_button = self._row_button[0],
										sends_button = self._row_button[1],
										device_button = self._row_button[2],
										special_device_button = self._row_button[3],
										)
		self._main_modes.selected_mode = 'disabled'
		self._main_modes.set_enabled(False)
	

	def _troll_shifted_enabled(self):
		debug('_troll_shifted_enabled')
		inputs = self.find_inputs()
		if not inputs is None:
			for index in range(4):
				release_control(self._dial[index][2])
				debug('assigning inputs:', inputs.parameters[index+1].name)
				self._dial[index][2].connect_to(inputs.parameters[index+1])
			self._dial[6][2].connect_to(inputs.parameters[5])
		xfade = self.find_perc_crossfader()
		xfade and self._dial[7][2].connect_to(xfade)
		returns = self.song.return_tracks
		if len(returns) >= 2:
			self._dial[4][2].connect_to(returns[0].mixer_device.sends[1])
			self._dial[5][2].connect_to(returns[1].mixer_device.sends[0])
		self.request_rebuild_midi_map()
	

	def _troll_shifted_disabled(self):
		for control in self._dial[:][2]:
			release_control(control)
		self.request_rebuild_midi_map()
	

	def find_inputs(self):
		found_device = None
		tracks = self.song.tracks
		for track in tracks:
			if track.name == 'Inputs':
				for device in track.devices:
					if bool(device.can_have_chains) and device.name.endswith('Inputs'):
						found_device = device
		return found_device
	

	def find_perc_crossfader(self):
		found_parameter = None
		tracks = self.song.tracks
		for track in tracks:
			if track.name == 'Perc':
				for device in track.devices:
					if bool(device.can_have_chains) and device.name == 'Perc':
						for parameter in device.parameters:
							if parameter.name == 'XFade':
								found_parameter = parameter
		return found_parameter
	


#
#