# by amounra 0218 : http://www.aumhaa.com
# written against Live 10.0.4 100918


import Live
import time
import math
import sys

from ableton.v2.base import inject, listens, listens_group, inject
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry
from ableton.v2.control_surface.elements import ButtonMatrixElement, DoublePressElement, MultiElement, DisplayDataSource, SysexElement
from ableton.v2.control_surface.components import ClipSlotComponent, SceneComponent, SessionComponent, TransportComponent, BackgroundComponent, ViewControlComponent, SessionRingComponent, SessionRecordingComponent, SessionNavigationComponent, SessionOverviewComponent, MixerComponent, PlayableComponent
from ableton.v2.control_surface.components.mixer import SimpleTrackAssigner
from ableton.v2.control_surface.mode import AddLayerMode, ModesComponent, DelayMode, CompoundMode
from ableton.v2.control_surface.elements.physical_display import PhysicalDisplayElement
from ableton.v2.control_surface.components.session_recording import *
from ableton.v2.control_surface.control import PlayableControl, ButtonControl, control_matrix
from ableton.v2.control_surface.components.scroll import ScrollComponent
from ableton.v2.control_surface.components.view_control import BasicSceneScroller
from ableton.v2.control_surface.percussion_instrument_finder import PercussionInstrumentFinder, find_drum_group_device
from ableton.v2.control_surface.elements import PlayheadElement

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import SendLividSysexMode, MomentaryBehaviour, ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour, ShiftedBehaviour, LatchingShiftedBehaviour, FlashingBehaviour
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.elements import MonoEncoderElement, MonoBridgeElement, generate_strip_string, CodecEncoderElement
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import DeviceNavigator, TranslationComponent, MonoMixerComponent, ResetSendsComponent, DeviceSelectorComponent, MonoChannelStripComponent
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.components.mono_instrument import *
from aumhaa.v2.control_surface.mono_modes import CancellableBehaviour, SendLividSysexMode, SendSysexMode, CancellableBehaviourWithRelease, ColoredCancellableBehaviourWithRelease, MomentaryBehaviour, BicoloredMomentaryBehaviour, DefaultedBehaviour
from aumhaa.v2.livid import LividControlSurface, LividSettings, LividRGB
from aumhaa.v2.control_surface.components.fixed_length_recorder import FixedLengthSessionRecordingComponent
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

from pushbase.auto_arm_component import AutoArmComponent
from pushbase.grid_resolution import GridResolution
from pushbase.drum_group_component import DrumGroupComponent

debug = initialize_debug()


"""Custom files, overrides, and files from other scripts"""
from _Generic.Devices import *
from .ModDevices import *
from .Map import *



check_model = (240, 126, 127, 6, 1, 247)
factoryreset = (240,0,1,97,8,6,247)
SLOWENCODER = (240, 0, 1, 97, 8, 30, 69, 00, 247)
NORMALENCODER = (240, 0, 1, 97, 8, 30, 00, 00, 247)
FASTENCODER = (240, 0, 1, 97, 8, 30, 0o4, 00, 247)

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


def xstr(s):
	if s is None:
		return ''
	else:
		return str(s)


def special_number_of_parameter_banks(device, device_dict = DEVICE_DICT):
	""" Determine the amount of parameter banks the given device has """
	if device != None:
		if device.class_name in list(device_dict.keys()):
			device_bank = device_dict[device.class_name]
			return len(device_bank)/4 + (1 if len(device_bank)%4 else 0)
		else:
			if device.class_name in MAX_DEVICES:
				try:
					banks = device.get_bank_count()
				except:
					banks = 0
				if banks != 0:
					return banks
			param_count = len(device.parameters[1:])
			return param_count / 12 + (1 if param_count % 12 else 0)
	return 0


def special_parameter_bank_names(device, bank_name_dict = BANK_NAME_DICT):
	if device != None:
		if device.class_name in list(bank_name_dict.keys()):
			ret = group(bank_name_dict[device.class_name], 4)
			ret1 = [[i for i in bank_names if not i is None] for bank_names in ret]
			return [' - '.join(i) for i in ret1]
		banks = special_number_of_parameter_banks(device)
		def _default_bank_name(bank_index):
			return 'Bank ' + str(bank_index + 1)

		if device.class_name in MAX_DEVICES and banks != 0:
			def _is_ascii(c):
				return ord(c) < 128

			def _bank_name(bank_index):
				try:
					name = device.get_bank_name(bank_index)
				except:
					name = None
				if name:
					return str(list(filter(_is_ascii, name)))
				else:
					return _default_bank_name(bank_index)

			return list(map(_bank_name, list(range(0, banks))))
		else:
			return list(map(_default_bank_name, list(range(0, banks))))
	return []


def special_parameter_banks(device, device_dict = DEVICE_DICT):
	""" Determine the parameters to use for a device """
	if device != None:
		if device.class_name is 'LegacyModDeviceProxy':
			return group(device_parameters_to_map(device), 12)
		elif device.class_name in list(device_dict.keys()):
			def names_to_params(bank):
				return list(map(partial(get_parameter_by_name, device), bank))

			return group([i for i in flatten(list(map(names_to_params, device_dict[device.class_name])))], 12)
		else:
			if device.class_name in MAX_DEVICES:
				try:
					banks = device.get_bank_count()
				except:
					banks = 0
				if banks != 0:
					def _bank_parameters(bank_index):
						try:
							parameter_indices = device.get_bank_parameters(bank_index)
						except:
							parameter_indices = []
						if len(parameter_indices) != 32:
							return [ None for i in range(0, 32) ]
						else:
							return [ (device.parameters[i] if i != -1 else None) for i in parameter_indices ]

					return list(map(_bank_parameters, list(range(0, banks))))
			return group(device_parameters_to_map(device), 12)
	return []



class CntrlrDeviceSelector(DeviceSelectorComponent):



	def has_mod_entry(self, index):
		has_entry = False
		preset = None
		if index < len(self._device_registry):
			preset = self._device_registry[index]
		if not preset is None and isinstance(preset, Live.Device.Device):
			has_entry = not self._script.monomodular.is_mod(preset) is None
		return has_entry


	def select_device(self, index):
		if self.is_enabled():
			self.scan_all()
			debug('is_enabled')
			debug('reg:', self._device_registry)
			preset = None
			if index < len(self._device_registry):
				preset = self._device_registry[index]
			if not preset is None and isinstance(preset, Live.Device.Device):
				self.song.view.select_device(preset)
				self._script._device_provider.device = preset
				#self._script.set_appointed_device(preset)
				try:
					if not self._script.monomodular.is_mod(preset) is None:
						self._script.modhandler._is_locked = False
						self._script.modhandler.select_mod(self._script.monomodular.is_mod(preset))
						self._script.modhandler.set_lock(True)
					else:
						self._script.modhandler.select_mod()
				except:
					pass
			else:
				self._script.modhandler.select_mod()


	def scan_all(self):
		debug('scan all--------------------------------')
		self._device_registry = [None for index in range(4)]
		prefix = str(self._prefix)+':'
		offset = self._offset
		preset = None
		tracks = self.song.tracks + self.song.return_tracks + tuple([self.song.master_track])
		for track in tracks:
			for device in enumerate_track_device(track):
				for index, entry in enumerate(self._device_registry):
					key = str(prefix + str(index + 1 + offset))
					if device.name.startswith(key+' ') or device.name == key:
						self._device_registry[index] = device
					elif (device.name.startswith('*' +key+' ') or device.name == ('*' +key))  and device.can_have_chains and len(device.chains) and len(device.chains[0].devices):
						self._device_registry[index] = device.chains[0].devices[0]
		debug('device registry: ' + str(self._device_registry))


	def update(self):
		pass



class CancellableBehaviour(ModeButtonBehaviour):


	_previous_mode = None

	def press_immediate(self, component, mode):
		active_modes = component.active_modes
		groups = component.get_mode_groups(mode)
		can_cancel_mode = mode in active_modes or any(map(lambda other: groups & component.get_mode_groups(other), active_modes))
		if can_cancel_mode:
			if groups:
				component.pop_groups(groups)
			else:
				component.pop_mode(mode)
			self.restore_previous_mode(component)
		else:
			self.remember_previous_mode(component)
			component.push_mode(mode)


	def remember_previous_mode(self, component):
		self._previous_mode = component.active_modes[0] if component.active_modes else None


	def restore_previous_mode(self, component):
		if len(component.active_modes) == 0 and self._previous_mode is not None:
			component.push_mode(self._previous_mode)



class SpecialCntrlrDeviceComponent(DeviceComponent):


	def __init__(self, script, *a, **k):
		self._script = script
		super(SpecialCntrlrDeviceComponent, self).__init__(*a, **k)


	def display_device(self):
		track = self.find_track(livedevice(self._get_device()))
		if (self.song.view.selected_track is not track):
			self.song.view.selected_track = track
		self.song.view.select_device(livedevice(self._get_device()))
		if ((not self.application.view.is_view_visible('Detail')) or (not self.application.view.is_view_visible('Detail/DeviceChain'))):
			self.application.view.show_view('Detail')
			self.application.view.show_view('Detail/DeviceChain')


	def find_track(self, obj):
		if obj != None:
			if(type(obj.canonical_parent)==type(None)) or (type(obj.canonical_parent)==type(self.song)):
				return None
			elif(type(obj.canonical_parent) == type(self.song.tracks[0])):
				return obj.canonical_parent
			else:
				return self.find_track(obj.canonical_parent)
		else:
			return None


	def update(self):
		super(SpecialCntrlrDeviceComponent, self).update()


	def set_nav_prev_button(self, prev_button):
		self._on_nav_prev_value.subject = prev_button


	def set_nav_next_button(self, next_button):
		self._on_nav_next_value.subject = next_button


	@listens('value')
	def _on_nav_prev_value(self, value):
		"""
		if self.is_enabled() and not self.is_locked() and value != 0:		# and (not self._shift_pressed)):
			if value:
				if self._script._device_component != self:
					self._script.set_device_component(self)
				direction = Live.Application.Application.View.NavDirection.left
				self.application.view.scroll_view(direction, 'Detail/DeviceChain', True)
				self.update()"""
		pass


	@listens('value')
	def _on_nav_next_value(self, value):
		"""if self.is_enabled() and not self.is_locked() and value != 0:
			direction = Live.Application.Application.View.NavDirection.left
			self.application.view.scroll_view(direction, 'Detail/DeviceChain', True)
			self.update()"""
		pass


	def _current_bank_details(self):
		bank_name = self._bank_name
		bank = []
		best_of = self._best_of_parameter_bank()
		banks = self._parameter_banks()
		if banks:
			if self._bank_index != None and self._is_banking_enabled() or not best_of:
				index = self._bank_index if self._bank_index != None else 0
				bank = banks[index]
				#debug('bank is:', bank)
				bank_name = self._parameter_bank_names()[index]
			else:
				bank = best_of
				bank_name = 'Best of Parameters'
		#debug('current_bank_details:', bank_name, bank)
		return (bank_name, bank)


	def _parameter_banks(self):
		return special_parameter_banks(self._get_device())


	def _parameter_bank_names(self):
		return special_parameter_bank_names(self._get_device())


	def _number_of_parameter_banks(self):
		return special_number_of_parameter_banks(self._get_device())


	def _release_parameters(self, controls):
		if controls != None:
			for control in controls:
				if control != None:
					control.release_parameter()
					control.reset()



class CntrlrTransportComponent(TransportComponent):


	def _update_stop_button_color(self):
		if hasattr(self, '_stop_button'):
			self._stop_button.color = 'Transport.StopOn' if self._play_toggle.is_toggled else 'Transport.StopOff'



class CntrlrViewControlComponent(ViewControlComponent):


	def __init__(self, *a, **k):
		super(CntrlrViewControlComponent, self).__init__(*a, **k)
		#self._basic_scroll_scenes = self.register_component(ScrollComponent(BasicSceneScroller()))
		self._basic_scroll_scenes = ScrollComponent(BasicSceneScroller())
		self.register_slot(self.song, self._basic_scroll_scenes.update, 'scenes')
		self.register_slot(self.song.view, self._basic_scroll_scenes.update, 'selected_scene')


	def set_scene_select_dial(self, dial):
		self._on_scene_select_dial_value.subject = dial


	@listens('value')
	def _on_scene_select_dial_value(self, value):
		#debug('_on_scene_select_dial_value', value)
		self._basic_scroll_scenes.scroll_up() if value == 127 else self._basic_scroll_scenes.scroll_down()


	def set_track_select_dial(self, dial):
		self._on_track_select_dial_value.subject = dial


	@listens('value')
	def _on_track_select_dial_value(self, value):
		#debug('_on_scene_select_dial_value', value)
		self._scroll_tracks.scroll_up() if value == 127 else self._scroll_tracks.scroll_down()



class CntrlrResetSendsComponent(ResetSendsComponent):


	def reset_send(self, send_number):
		track = self._script._mixer.channel_strip(send_number)
		for index in range(len(track._send_controls)):
			if track._send_controls[index].mapped_parameter()!=None:
				track._send_controls[index].mapped_parameter().value = 0



class CntrlrSessionNavigationComponent(SessionNavigationComponent):


	def set_scene_bank_dial(self, dial):
		self._on_scene_bank_dial_value.subject = dial


	@listens('value')
	def _on_scene_bank_dial_value(self, value):
		#debug('_on_scene_bank_dial_value', value)
		#self._can_scroll_page_up() and self._scroll_page_up() if value == 127 else self._can_scroll_page_down() and self._scroll_page_down()
		self._vertical_paginator.can_scroll_up() and self._vertical_paginator.scroll_up() if value == 127 else self._vertical_paginator.can_scroll_down() and self._vertical_paginator.scroll_down()


	def set_track_bank_dial(self, dial):
		self._on_track_bank_dial_value.subject = dial


	@listens('value')
	def _on_track_bank_dial_value(self, value):
		#debug('_on_track_bank_dial_value', value)
		#self._can_scroll_page_left() and self._scroll_page_left() if value == 127 else self._can_scroll_page_right() and self._scroll_page_right()
		self._horizontal_paginator.can_scroll_up() and self._horizontal_paginator.scroll_up() if value == 127 else self._horizontal_paginator.can_scroll_down() and self._horizontal_paginator.scroll_down()


	def set_scene_nav_dial(self, dial):
		self._on_scene_nav_dial_value.subject = dial


	@listens('value')
	def _on_scene_nav_dial_value(self, value):
		#debug('_on_scene_nav_dial_value', value)
		self._vertical_banking.can_scroll_up() and self._vertical_banking.scroll_up() if value == 127 else self._vertical_banking.can_scroll_down() and self._vertical_banking.scroll_down()


	def set_track_nav_dial(self, dial):
		self._on_track_nav_dial_value.subject = dial


	@listens('value')
	def _on_track_nav_dial_value(self, value):
	#	debug('_on_track_nav_dial_value', value)
		self._horizontal_banking.can_scroll_up() and self._horizontal_banking.scroll_up() if value == 127 else self._horizontal_banking.can_scroll_down() and self._horizontal_banking.scroll



"""We need to add an extra mode to the instrument to deal with session shifting, thus the _matrix_modes and extra functions."""
"""We also set up the id's for the note_editor here"""
"""We also make use of a shift_mode instead of the original shift mode included in the MonoInstrument so that we can add a custom behaviour locking behaviour to it"""



"""We need to override the update notification call in AutoArmComponent"""

class CntrlrAutoArmComponent(AutoArmComponent):


	def _update_notification(self):
		pass



class CntrlrDeviceComponent(DeviceComponent):


	_alt_pressed = False

	def __init__(self, script = None, *a, **k):
		self._script = script
		super(CntrlrDeviceComponent, self).__init__(*a, **k)



class Cntrlr(LividControlSurface):
	__module__ = __name__
	__doc__ = " Monomodular controller script for Livid CNTRLR "


	_sysex_id = 8
	_model_name = 'Cntrlr'
	_host_name = 'Cntrlr'
	_version_check = 'b996'
	monomodular = None
	device_provider_class = ModDeviceProvider


	def __init__(self, *a, **k):
		super(Cntrlr, self).__init__(*a, **k)
		self._skin = Skin(CntrlrColors)
		self._device_selection_follows_track_selection = FOLLOW
		with self.component_guard():
			self._setup_monobridge()
			self._setup_controls()
			self._define_sysex()
			self._setup_background()
			self._setup_translations()
			#self._setup_autoarm()
			self._setup_session_control()
			self._setup_send_reset_controls()
			self._setup_mixer_control()
			self._setup_transport_control()
			self._setup_device_control()
			self._setup_mod_device_control()
			self._setup_device_selector()
			#self._setup_session_recording_component()
			#self._setup_viewcontrol()
			#self._setup_instrument()
			self._setup_mod()
			self._setup_modswitcher()
			self._setup_translations()
			self._setup_modes()
			self._setup_m4l_interface()
			self._on_device_changed.subject = self.song
			#self.set_feedback_channels(range(14, 15))


	def _initialize_script(self):
		super(Cntrlr, self)._initialize_script()
		self._connected = True
		self._main_modes.selected_mode = 'MixMode'
		self._main_modes.set_enabled(True)
		#self._instrument.set_enabled(True)
		#self._main_modes.selected_mode = 'disabled'
		#self._main_modes.selected_mode = 'MixMode'
		self._session_ring._update_highlight()
		self._session_ring.track_offset = 0
		if liveobj_valid(self.song.visible_tracks[0]):
			self.song.view.selected_track = self.song.visible_tracks[0]


	def _initialize_hardware(self):
		super(Cntrlr, self)._initialize_hardware()
		for index in range(4):
			self._encoder[index].send_value(0)


	def port_settings_changed(self):
		self._main_modes.selected_mode = 'disabled'
		super(Cntrlr, self).port_settings_changed()


	def _setup_monobridge(self):
		self._monobridge = MonoBridgeElement(self)
		self._monobridge.name = 'MonoBridge'


	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		self._fader = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CNTRLR_FADERS[index], name = 'Fader_' + str(index), num = index, script = self,  optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(8)]
		self._dial_left = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CNTRLR_KNOBS_LEFT[index], name = 'Dial_Left_' + str(index), num = CNTRLR_KNOBS_LEFT[index], script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(12)]
		self._dial_right = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CNTRLR_KNOBS_RIGHT[index], name = 'Dial_Right_' + str(index), num = CNTRLR_KNOBS_RIGHT[index], script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(12)]
		self._encoder = [CodecEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CNTRLR_DIALS[index], name = 'Encoder_' + str(index), num = CNTRLR_DIALS[index], script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(12)]
		self._encoder_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CNTRLR_DIAL_BUTTONS[index], name = 'Encoder_Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(12)]
		self._grid = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CNTRLR_GRID[index], name = 'Grid_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(16)]
		self._button = [MonoButtonElement(is_momentary = is_momentary,msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CNTRLR_BUTTONS[index], name = 'Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(32)]
		self._knobs = self._dial_left + self._dial_right

		self._fader_matrix = ButtonMatrixElement(name = 'Fader_Matrix', rows = [self._fader])
		self._matrix = ButtonMatrixElement(name = 'Matrix', rows = [self._grid[index*4:(index*4)+4] for index in range(4)])
		self._knob_left_matrix = ButtonMatrixElement(name = 'Knob_Left_Matrix', rows = [self._dial_left[index*4:(index*4)+4] for index in range(3)])
		self._knob_right_matrix = ButtonMatrixElement(name = 'Knob_Right_Matrix', rows = [self._dial_right[index*4:(index*4)+4] for index in range(3)])
		self._dial_matrix = ButtonMatrixElement(name = 'Dial_Matrix', rows = [self._encoder[index*4:(index*4)+4] for index in range(3)])
		self._dial_button_matrix = ButtonMatrixElement(name = 'Dial_Button_Matrix', rows = [self._encoder_button[index*4:(index*4)+4] for index in range(1,3)])
		self._key_matrix = ButtonMatrixElement(name = 'Key_Matrix', rows = [self._button[0:16], self._button[16:32]])

		self._translated_controls = self._grid + self._button


	def _setup_background(self):
		self._background = BackgroundComponent(name = 'Background')
		self._background.layer = Layer(priority = 3, matrix = self._matrix.submatrix[:,:], faders = self._fader_matrix.submatrix[:,:], left_knobs = self._knob_left_matrix.submatrix[:,:], right_knobs = self._knob_right_matrix.submatrix[:,:], dials = self._dial_matrix, dial_buttons = self._dial_button_matrix.submatrix[:,:], keys = self._key_matrix.submatrix[:,:])
		self._background.set_enabled(True)


	def _define_sysex(self):
		self.encoder_navigation_on = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_encosion_mode', message = [0, 0, 0, 0])


	def _setup_transport_control(self):
		self._transport = CntrlrTransportComponent(name = 'Transport')
		if hasattr(self._transport, '_play_toggle'):
			self._transport._play_toggle.view_transform = lambda value: 'Transport.PlayOn' if value else 'Transport.PlayOff'
		if hasattr(self._transport, '_record_toggle'):
			self._transport._record_toggle.view_transform = lambda value: 'Transport.RecordOn' if value else 'Transport.RecordOff'
		self._transport.layer = Layer(priority = 4,
									play_button = self._button[28],
									stop_button = self._button[29],
									record_button = self._button[30])
		self._transport.set_enabled(False)


	def _setup_autoarm(self):
		self._auto_arm = CntrlrAutoArmComponent(name='Auto_Arm')
		#self._auto_arm._update_notification = lambda a: None
		self._auto_arm.can_auto_arm_track = self._can_auto_arm_track


	def _setup_session_recording_component(self):
		self._clip_creator = ClipCreator()
		self._clip_creator.name = 'ClipCreator'
		self._recorder = FixedLengthSessionRecordingComponent(clip_creator = self._clip_creator, view_controller = ViewControlComponent(), name = 'SessionRecorder') # is_enabled = False)
		self._recorder.main_layer = AddLayerMode(self._recorder, Layer(priority = 4, record_button = self._button[29]))
		self._recorder.shift_layer = AddLayerMode(self._recorder, Layer(priority = 4, automation_button = self._button[29]))
		self._recorder.set_enabled(False)


	def _setup_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks = 4, num_scenes = 4)
		self._session_ring.set_enabled(False)

		self._session_navigation = CntrlrSessionNavigationComponent(name = 'SessionNavigation', session_ring = self._session_ring)

		self._session_navigation._vertical_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'

		self._session_navigation.layer = Layer(priority = 4,
									down_button = self._button[14],
									up_button = self._button[15],
									left_button = self._button[12],
									right_button = self._button[13])

		self._session_navigation.set_enabled(False)

		self._session = SessionComponent(session_ring = self._session_ring, auto_name = True)
		hasattr(self._session, '_enable_skinning') and self._session._enable_skinning()

		self._session.layer = Layer(priority = 4, clip_launch_buttons = self._matrix.submatrix[:,:])
		self._session.set_enabled(False)

		self._session_zoom = SessionOverviewComponent(name = 'SessionZoom', session_ring = self._session_ring, enable_skinning = True)
		self._session_zoom.layer = Layer(priority = 4, button_matrix = self._matrix.submatrix[:,:])
		self._session_zoom.set_enabled(False)


	def _setup_send_reset_controls(self):
		self._send_reset = ResetSendsComponent(script = self)
		self._send_reset.layer = Layer(priority = 4, buttons = self._key_matrix.submatrix[8:12, :1])
		self._send_reset.set_enabled(False)


	def _setup_mixer_control(self):
		self._mixer = MonoMixerComponent(name = 'Mixer', num_returns = 2,tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True, channel_strip_component_type = MonoChannelStripComponent)
		self._mixer.fader_layer = AddLayerMode(self._mixer, Layer(priority = 4, volume_controls = self._fader_matrix.submatrix[:4, :],
											return_controls = self._fader_matrix.submatrix[4:6, :],
											prehear_volume_control = self._fader[6],
											send_controls = self._knob_left_matrix,
											eq_gain_controls = self._knob_right_matrix))
		self._mixer.button_layer = AddLayerMode(self._mixer, Layer(priority = 4, mute_buttons = self._key_matrix.submatrix[:4, 1:],
											stop_clip_buttons = self._key_matrix.submatrix[8:12, 1:],
											solo_buttons = self._key_matrix.submatrix[:4, :1],
											arm_buttons = self._key_matrix.submatrix[4:8, :1],
											track_select_buttons = self._key_matrix.submatrix[4:8, 1:],))
		self._mixer.master_strip().layer = Layer(priority = 4, volume_control = self._fader[7],)

		self._mixer.set_enabled(False)


	def _setup_device_control(self):
		self._device_selection_follows_track_selection = FOLLOW
		self._device = CntrlrDeviceComponent(script = self, name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())
		self._device.layer = Layer(priority = 4, parameter_controls = self._dial_matrix.submatrix[:, 1:],
													on_off_button = self._encoder_button[4],
													bank_prev_button = self._encoder_button[8],
													bank_next_button = self._encoder_button[9],)
													#lock_button = self._encoder_button[7])
		self._device.set_enabled(False)

		self._device_navigator = DeviceNavigator(self._device_provider, self._mixer, self)
		self._device_navigator.name = 'Device_Navigator'
		self._device_navigator.layer = Layer(priority = 4,
											prev_button = self._encoder_button[10],
											next_button = self._encoder_button[11],)
		self._device_navigator.set_enabled(False)


	def _setup_mod_device_control(self):
		self._mod_device = SpecialCntrlrDeviceComponent(script = self, name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())
		self._mod_device.layer = Layer(priority = 4, parameter_controls = self._dial_matrix.submatrix[:, :],)
		self._mod_device.set_enabled(False)


	def _setup_device_selector(self):
		self._device_selector = CntrlrDeviceSelector(self)
		self._device_selector.name = 'Device_Selector'
		#self._device_selector.select_layer = AddLayerMode(self._device_selector, Layer(priority = 6 , matrix = self._matrix.submatrix[:, :]))
		#self._device_selector.select_layer = AddLayerMode(self._device_selector, Layer(priority = 6, matrix = ButtonMatrixElement(rows = [self._grid[:4],self._grid[4:8],self._grid[8:12],self._grid[12:14]])))
		#self._device_selector.assign_layer = AddLayerMode(self._device_selector, Layer(priority = 7, assign_button = self._grid[14]))
		self._device_selector.set_enabled(False)


	def _setup_translations(self):
		self._translations = TranslationComponent(self._translated_controls, user_channel_offset = 4, channel = 4)	# is_enabled = False)
		self._translations.name = 'TranslationComponent'
		self._translations.layer = Layer(priority = 10,)
		self._translations._color = 127
		self._translations.selector_layer = AddLayerMode(self._translations, Layer(priority = 10, channel_selector_buttons = self._dial_button_matrix))
		self._translations.set_enabled(False)

		#self._optional_translations = CompoundMode(TranslationComponent(controls = self._fader, user_channel_offset = 4, channel = 4, name = 'FaderTranslation', is_enabled = False, layer = Layer(priority = 10)) if FADER_BANKING else None
		#TranslationComponent(controls = self._knobs, user_channel_offset = 4, channel = 4, name = 'DialTranslation', is_enabled = False, layer = Layer(priority = 10)) if DIAL_BANKING else None)


	def _setup_mod(self):
		self.monomodular = get_monomodular(self)
		self.monomodular.name = 'monomodular_switcher'
		self.modhandler = CntrlrModHandler(self, device_provider = self._device_provider) # is_enabled = False)
		self.modhandler.name = 'ModHandler'
		self.modhandler.lock_layer = AddLayerMode(self.modhandler, Layer(priority=8, lock_button=self._grid[15]))
		self.modhandler.layer = Layer(priority = 8,
										cntrlr_encoder_button_grid = self._dial_button_matrix.submatrix[:,:],
										cntrlr_grid = self._matrix.submatrix[:,:],
										cntrlr_keys = self._key_matrix.submatrix[:,:],)
										#parameter_controls = self._dial_matrix.submatrix[:,:])
		self.modhandler.set_enabled(False)
		self._modHandle = ModControl(modscript = self, monomodular = self.monomodular, name = 'ModHandle')


	def _setup_modswitcher(self):
		self._modswitcher = ModesComponent(name = 'ModSwitcher')  # is_enabled = False)
		self._modswitcher.set_enabled(False)


	def _setup_viewcontrol(self):
		self._view_control = CntrlrViewControlComponent(name='View_Control')
		self._view_control.main_layer = AddLayerMode(self._view_control, Layer(scene_select_dial = self._encoder[2],
																				track_select_dial = self._encoder[3],))
		#self._view_control.main_layer = AddLayerMode(self._view_control, Layer(prev_track_button=self._button[24],
		#											next_track_button= self._button[25],
		#											next_scene_button=self._button[27],
		#											prev_scene_button = self._button[26]))
		self._view_control.set_enabled(False)


	def _setup_modes(self):

		self._modswitcher = ModesComponent(name = 'ModSwitcher')
		self._modswitcher.add_mode('mod', [self._mixer,
													self._mixer.fader_layer,
													self.modhandler,
													self._mod_device,
													self._device_selector,])
		self._modswitcher.add_mode('translations', [self._translations,
													self._device,
													self._mixer,
													self._mixer.fader_layer,
													self._device_navigator,
													self._device_selector])
		self._modswitcher.selected_mode = 'translations'
		self._modswitcher.set_enabled(False)

		self._session_modes = ModesComponent(name = 'SessionModes')
		self._session_modes.add_mode('Launch', [self._session])
		self._session_modes.add_mode('Zoom', [self._session_zoom])
		self._session_modes.layer = Layer(priority = 4, cycle_mode_button = self._button[31])
		self._session_modes.set_enabled(False)

		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [self._background, self.encoder_navigation_on])
		self._main_modes.add_mode('MixMode', [self._mixer,
													self._mixer.fader_layer,
													self._mixer.button_layer,
													self._session_modes,
													self._session_navigation,
													self._session_ring,
													self._device,
													self._device_navigator,
													self._send_reset,
													self._transport])

		self._main_modes.add_mode('ModMode1', [self._modswitcher,
													self._choose_mod,
													DelayMode(self._update_modswitcher, delay = .1, parent_task_group = self._task_group),
													DelayMode(self.modhandler.update, delay = .2, parent_task_group = self._task_group)],
													behaviour = DefaultedBehaviour(default_mode = 'MixMode'))
		self._main_modes.add_mode('ModMode2', [self._modswitcher,
													self._choose_mod,
													DelayMode(self._update_modswitcher, delay = .1, parent_task_group = self._task_group),
													DelayMode(self.modhandler.update, delay = .2, parent_task_group = self._task_group)],
													behaviour = DefaultedBehaviour(default_mode = 'MixMode'))
		self._main_modes.add_mode('ModMode3', [self._modswitcher,
													self._choose_mod,
													DelayMode(self._update_modswitcher, delay = .1, parent_task_group = self._task_group),
													DelayMode(self.modhandler.update, delay = .2, parent_task_group = self._task_group)],
													behaviour = DefaultedBehaviour(default_mode = 'MixMode'))
		self._main_modes.add_mode('ModMode4', [self._modswitcher,
													self._choose_mod,
													DelayMode(self._update_modswitcher, delay = .1, parent_task_group = self._task_group),
													DelayMode(self.modhandler.update, delay = .2, parent_task_group = self._task_group)],
													behaviour = DefaultedBehaviour(default_mode = 'MixMode'))

		self._main_modes.layer = Layer(priority = 4, ModMode1_button = self._encoder_button[0], ModMode2_button = self._encoder_button[1], ModMode3_button = self._encoder_button[2], ModMode4_button = self._encoder_button[3]) #,
		self._main_modes.selected_mode = 'disabled'
		self._main_modes.set_enabled(True)


	def _choose_mod(self):
		modes = ('ModMode1', 'ModMode2', 'ModMode3', 'ModMode4')
		mode = self._main_modes.selected_mode
		debug('choose_mod:', self._main_modes.selected_mode)
		if mode in modes:
			index = modes.index(mode)
			self._translations._channel = index + self._translations._user_channel_offset
			self._translations.update()
			self._device_selector.select_device(index)


	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard, priority = 10)
		self._m4l_interface.name = "M4LInterface"
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control


	def _can_auto_arm_track(self, track):
		routing = track.current_input_routing
		return routing == 'Ext: All Ins' or routing == 'All Ins' or routing.startswith('Cntrlr Input')


	@listens('appointed_device')
	def _on_device_changed(self):
		debug('appointed device changed, script')
		#self._main_modes.selected_mode is 'ModSwitcher' and self._update_modswitcher()


	def _on_selected_track_changed(self):
		super(Cntrlr, self)._on_selected_track_changed()
		#self._drum_group_finder.device_parent = self.song.veiw.selected_track
		#if not len(self.song.view.selected_track.devices):
		#	self._main_modes.selected_mode is 'ModSwitcher' and self._update_modswitcher()


	def _update_modswitcher(self):
		debug('update modswitcher', self.modhandler.active_mod())
		if self.modhandler.active_mod() and self._device_selector.has_mod_entry(['ModMode1', 'ModMode2', 'ModMode3', 'ModMode4'].index(self._main_modes.selected_mode)):
			self._modswitcher.selected_mode = 'mod'
		else:
			self._modswitcher.selected_mode = 'translations'


	def update_display(self):
		super(Cntrlr, self).update_display()
		self.modhandler.send_ring_leds()


	def restart_monomodular(self):
		#debug('restart monomodular')
		self.modhandler.disconnect()
		with self.component_guard():
			self._setup_mod()



class CntrlrModHandler(ModHandler):


	_device = None

	def __init__(self, *a, **k):
		self._local = True
		self._last_sent_leds = 1
		self._cntrlr_grid = None
		self._cntrlr_encoder_grid = None
		self._cntrlr_encoder_button_grid = None
		self._cntrlr_keys = None
		self._encoders_to_device = True
		addresses = {'cntrlr_grid': {'obj':Grid('cntrlr_grid', 4, 4), 'method':self._receive_cntrlr_grid},
					'cntrlr_encoder_grid': {'obj':RingedGrid('cntrlr_encoder_grid', 4, 2), 'method':self._receive_cntrlr_encoder_grid},
					'cntrlr_encoder_button_grid': {'obj':Grid('cntrlr_encoder_button_grid', 4, 2), 'method':self._receive_cntrlr_encoder_button_grid},
					'cntrlr_key': {'obj':  Grid('cntrlr_key', 16, 2), 'method': self._receive_cntrlr_key}}
		super(CntrlrModHandler, self).__init__(addresses = addresses, *a, **k)
		self._color_type = 'RGB'
		self.nav_box = NavigationBox(self, 16, 16, 4, 4, self.set_offset)


	def _receive_cntrlr_grid(self, x, y, value = -1, *a, **k):
		#debug('_receive_cntrlr_grid:', x, y, value)
		if self.is_enabled() and self._active_mod and not self._active_mod.legacy and not self._cntrlr_grid is None and x < 4 and y < 4:
			value > -1 and self._cntrlr_grid.send_value(x, y, self._colors[value], True)


	def _receive_cntrlr_encoder_grid(self, x, y, value = -1, mode = None, green = None, custom = None, local = None, relative = None, *a, **K):
		#debug('_receive_cntrlr_encoder_grid:', x, y, value, mode, green, custom, local, relative)
		if self.is_enabled() and self._active_mod and not self._encoders_to_device and self._cntrlr_encoder_grid and x < 4 and y < 2:
			if value > -1:
				if self._local:
					self._cntrlr_encoder_grid.send_value(x, y, value, True)
				else:
					self._cntrlr_encoder_grid.get_button(y, x)._ring_value = value
			button = self._cntrlr_encoder_grid.get_button(y, x)
			if button:
				mode and button.set_mode(mode)
				green and button.set_green(green)
				custom and button.set_custom(custom)
			not local is None and self._receive_cntrlr_encoder_grid_local(local)
			not relative is None and self._receive_cntrlr_encoder_grid_relative(relative)


	def _receive_cntrlr_encoder_button_grid(self, x, y, value, *a, **k):
		if self.is_enabled() and self._active_mod:
			if not self._cntrlr_encoder_button_grid is None:
				self._cntrlr_encoder_button_grid.send_value(x, y, self._colors[value], True)


	def _receive_cntrlr_encoder_grid_relative(self, value, *a):
		#debug('_receive_cntrlr_encoder_grid_relative:', value)
		if self.is_enabled() and self._active_mod:
			value and self._script._send_midi(tuple([240, 0, 1, 97, 8, 17, 127, 127, 127, 127, 247])) or self._script._send_midi(tuple([240, 0, 1, 97, 8, 17, 15, 0, 0, 0, 247]))


	def _receive_cntrlr_encoder_grid_local(self, value, *a):
		#debug('_receive_cntrlr_encoder_grid_local:', value)
		if self.is_enabled() and self._active_mod:
			self.clear_rings()
			self._local = value
			value and self._script._send_midi(tuple([240, 0, 1, 97, 8, 8, 72, 247])) or self._script._send_midi(tuple([240, 0, 1, 97, 8, 8, 64, 247]))


	def _receive_cntrlr_encoders_to_device(self, value, *a):
		debug('_receive_cntrlr_encoders_to_device:', value)
		if self.is_enabled() and self._active_mod:
			self._encoders_to_device = bool(value)
			self._script._device.set_parameter_controls(self._cntrlr_encoder_grid if value else None)


	def _receive_cntrlr_key(self, x, y=0, value=0, *a):
		#debug('_receive_cntrlr_key:', x, y, value)
		if self.is_enabled() and self._active_mod and not self._active_mod.legacy:
			if not self._cntrlr_keys is None:
				self._cntrlr_keys.send_value(x, y, self._colors[value], True)


	def _receive_grid(self, x, y, value = -1, *a, **k):
		if self.is_enabled() and self._active_mod and self._active_mod.legacy:
			if not self._cntrlr_grid is None:
				if (x - self.x_offset) in range(4) and (y - self.y_offset) in range(4):
					self._cntrlr_grid.send_value(x - self.x_offset, y - self.y_offset, self._colors[value], True)



	def set_cntrlr_grid(self, grid):
		self._cntrlr_grid = grid
		self._cntrlr_grid_value.subject = self._cntrlr_grid


	def set_cntrlr_encoder_grid(self, grid):
		self._cntrlr_encoder_grid = grid
		#self._cntrlr_encoder_grid_value.subject = self._cntrlr_encoder_grid
		#self._device.set_parameter_controls(grid)
		#self._device.update()
		if self._encoders_to_device:
			self._script._device.set_parameter_controls(grid)
			#self._script._device._on_device_changed(self._device_provider.device)
			self._device_provider.notify_device()
		else:
			self.set_cntrlr_encoder_grid and self.set_cntrlr_encoder_grid.reset()
			self.set_cntrlr_encoder_grid_value.subject = self.set_cntrlr_encoder_grid
		#self.log_message('parameter controls are: ' + str(self._parameter_controls))


	def set_cntrlr_encoder_button_grid(self, buttons):
		self._cntrlr_encoder_button_grid = buttons
		self._cntrlr_encoder_button_grid_value.subject = self._cntrlr_encoder_button_grid


	def set_cntrlr_keys(self, keys):
		self._cntrlr_keys = keys
		if keys:
			for key, _ in keys.iterbuttons():
				key and key.set_darkened_value(0)
		self._cntrlr_keys_value.subject = self._cntrlr_keys



	@listens('value')
	def _cntrlr_keys_value(self, value, x, y, *a, **k):
		#debug('_cntrlr_keys_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('cntrlr_key', x, y, value)


	@listens('value')
	def _cntrlr_grid_value(self, value, x, y, *a, **k):
		#debug('_cntrlr_grid_value:', x, y, value)
		if self._active_mod:
			if self._active_mod.legacy:
				self._active_mod.send('grid', x + self.x_offset, y + self.y_offset, value)
			else:
				self._active_mod.send('cntrlr_grid', x, y, value)


	@listens('value')
	def _cntrlr_encoder_grid_value(self, value, x, y, *a, **k):
		#debug('_cntrlr_encoder_grid_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('cntrlr_encoder_grid', x, y, value)


	@listens('value')
	def _cntrlr_encoder_button_grid_value(self, value, x, y, *a, **k):
		#debug('_cntrlr_encoder_button_grid_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('cntrlr_encoder_button_grid', x, y, value)


	def update(self, *a, **k):
		mod = self.active_mod()
		#debug('modhandler update:', mod)
		if self.is_enabled() and not mod is None:
			mod.restore()
		else:
			#debug('disabling modhandler')
			#self._script._send_midi(tuple([240, 0, 1, 97, 8, 17, 0, 0, 0, 0, 0, 0, 0, 0, 247]))
			self._script._send_midi(tuple([240, 0, 1, 97, 8, 8, 72, 247]))
			if not self._cntrlr_grid_value.subject is None:
				self._cntrlr_grid_value.subject.reset()
			if not self._cntrlr_encoder_grid_value.subject is None:
				self._cntrlr_encoder_grid_value.subject.reset()
			if not self._cntrlr_encoder_button_grid_value.subject is None:
				self._cntrlr_encoder_button_grid_value.subject.reset()
			if not self._cntrlr_keys_value.subject is None:
				self._cntrlr_keys_value.subject.reset()
		if not self._on_lock_value.subject is None:
			self._on_lock_value.subject.send_value((not mod is None) + ((not mod is None) and self.is_locked() * 4))


	def send_ring_leds(self):
		if self.is_enabled() and self._active_mod and not self._local and self._cntrlr_encoder_grid:
			leds = [240, 0, 1, 97, 8, 31, 0, 0, 0, 0, 0, 0, 0, 0]
			for encoder, coords in self._cntrlr_encoder_grid.iterbuttons():
				bytes = encoder._get_ring()
				leds.append(bytes[0])
				leds.append(int(bytes[1]) + int(bytes[2]))
			leds.append(247)
			if not leds==self._last_sent_leds:
				self._script._send_midi(tuple(leds))
				self._last_sent_leds = leds


	def clear_rings(self):
		self._last_sent_leds = 1


#	a
