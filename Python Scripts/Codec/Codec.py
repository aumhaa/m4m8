# by amounra 0216 : http://www.aumhaa.com

from __future__ import with_statement
import Live
import time
import math
import logging
logger = logging.getLogger(__name__)

from itertools import izip, izip_longest, product

from ableton.v2.base import slicer, to_slice, liveobj_changed, group, flatten, liveobj_valid
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement, EncoderElement, ComboElement, DoublePressElement, MultiElement, DoublePressContext
from ableton.v2.control_surface.components import ChannelStripComponent, MixerComponent, SessionComponent, TransportComponent, SessionNavigationComponent, BackgroundComponent, SessionRingComponent
from ableton.v2.control_surface import ControlSurface, ControlElement, Component, CompoundComponent, PrioritizedResource, Skin, DeviceBankRegistry, Layer
from ableton.v2.control_surface.input_control_element import *
from ableton.v2.control_surface.mode import AddLayerMode, LayerMode, ModesComponent, ModeButtonBehaviour, DelayMode
from ableton.v2.base.event import *
from ableton.v2.base.task import *

from Push.mode_behaviours import CancellableBehaviour

from _Generic.Devices import *

from aumhaa.v2.control_surface.elements import CodecEncoderElement, MonoBridgeElement, MonoButtonElement
from aumhaa.v2.control_surface.components import DeviceSelectorComponent, DeviceNavigator
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.mono_modes import SendLividSysexMode, MomentaryBehaviour, ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour, CancellableBehaviourWithRelease, ShiftedBehaviour, LatchingShiftedBehaviour, FlashingBehaviour, DefaultedBehaviour
from aumhaa.v2.livid import LividControlSurface, LividSettings
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import initialize_debug
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

debug = initialize_debug()

from Map import *

def tracks_to_use(self):
	return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)
	
MixerComponent.tracks_to_use = tracks_to_use


""" Here we define some global variables """
factoryreset = (240,0,1,97,4,6,247)
btn_channels = (240, 0, 1, 97, 4, 19, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, 0, 247);
enc_channels = (240, 0, 1, 97, 4, 20, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, CHANNEL, 247);

SLOWENCODER = (240, 0, 1, 97, 4, 30, 00, 00, 247)
NORMALENCODER = (240, 0, 1, 97, 4, 30, 02, 00, 247)
FASTENCODER = (240, 0, 1, 97, 4, 30, 04, 00, 247)
SHOW_PLAYING_CLIP_DELAY = 5
ENCODER_SPEED = [NORMALENCODER, SLOWENCODER]

DEVICE_COMPONENTS = ['device_0', 'device_1', 'device_2', 'device_3']

FAST_ENCODER_MSG = [4, 0]
NORMAL_ENCODER_MSG = [2, 0]
SLOW_ENCODER_MSG = [0, 0]


def xstr(s):
	if s is None:
		return ''
	else:
		return str(s)


def special_number_of_parameter_banks(device, device_dict = DEVICE_DICT):
	""" Determine the amount of parameter banks the given device has """
	if device != None:
		if device.class_name in device_dict.keys():
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
			return param_count / 32 + (1 if param_count % 32 else 0)
	return 0


def special_parameter_bank_names(device, bank_name_dict = BANK_NAME_DICT):
	if device != None:
		if device.class_name in bank_name_dict.keys():
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
					return str(filter(_is_ascii, name))
				else:
					return _default_bank_name(bank_index)
			
			return map(_bank_name, range(0, banks))
		else:
			return map(_default_bank_name, range(0, banks))
	return []


def special_parameter_banks(device, device_dict = DEVICE_DICT):
	""" Determine the parameters to use for a device """
	if device != None:
		if device.class_name is 'LegacyModDeviceProxy':
			return group(device_parameters_to_map(device), 32)
		elif device.class_name in device_dict.keys():
			def names_to_params(bank):
				return map(partial(get_parameter_by_name, device), bank)
			
			return group([i for i in flatten(map(names_to_params, device_dict[device.class_name]))], 32)
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
					
					return map(_bank_parameters, range(0, banks))
			return group(device_parameters_to_map(device), 32)
	return []



class CancellableBehaviourWithRelease(CancellableBehaviour):


	def release_delayed(self, component, mode):
		component.pop_mode(mode)
	

	def update_button(self, component, mode, selected_mode):
		button = component.get_mode_button(mode)
		groups = component.get_mode_groups(mode)
		selected_groups = component.get_mode_groups(selected_mode)
		value = (mode == selected_mode or bool(groups & selected_groups))*32 or 1
		#button.send_value(value, True)
		button.color = value
	


class ShiftCancellableBehaviourWithRelease(CancellableBehaviour):


	def release_delayed(self, component, mode):
		component.pop_mode(mode)
	

	def update_button(self, component, mode, selected_mode):
		pass
	


class CodecStaticDeviceProvider(EventObject):


	device_selection_follows_track_selection = False

	def __init__(self, *a, **k):
		super(CodecStaticDeviceProvider, self).__init__(*a, **k)
		self._device = None
	

	@listenable_property
	def device(self):
		#debug('returning:', self._device)
		return self._device
	

	@device.setter
	def device(self, device):
		#debug('provider device_setter:', device)
		if liveobj_changed(self._device, device):
			self._device = device
			self.notify_device()
	


class CodecDeviceComponent(DeviceComponent):


	def __init__(self, script, preset_index, *a, **k):
		self._script = script
		self._preset_index = str(preset_index)
		provider = CodecStaticDeviceProvider() 
		self._dynamic_device_provider = None
		self._preset_device = None
		super(CodecDeviceComponent, self).__init__(device_provider = provider, *a, **k)
		self.scan_all()
	

	def update(self):
		super(CodecDeviceComponent, self).update()
	

	def scan_all(self):
		debug('scan all device--------------------------------')
		preset = None
		tracks = self.song.tracks + self.song.return_tracks + tuple([self.song.master_track])
		key = str('@d:'+self._preset_index)
		debug('key is:', key)
		for track in tracks:
			for device in enumerate_track_device(track):
				if device.name.startswith(key+' ') or device.name == key:
					preset = device
				elif (device.name.startswith('*' +key+' ') or device.name == ('*' +key))  and device.can_have_chains and len(device.chains) and len(device.chains[0].devices):
					preset = device.chains[0].devices[0]
		self._preset_device = preset
		debug('preset is:', preset)
		if not preset == None:
			self._device_provider.device = preset
	

	@listens('device')
	def _on_dynamic_device_changed(self):
		if self._preset_device is None:
			device = self._dynamic_device_provider.device if self._dynamic_device_provider else None
			#debug('_on_provided_device_changed:', self.name, device)
			if liveobj_valid(self._device_provider):
				self._device_provider.device = device
	

	def set_dynamic_device_provider(self, provider):
		self._dynamic_device_provider = provider
		self._on_dynamic_device_changed.subject = self._dynamic_device_provider
		if self._get_device() is None:
			self._on_dynamic_device_changed()
	

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
	

	def _on_device_changed(self, device):
		super(CodecDeviceComponent, self)._on_device_changed(device)
	

	def _release_parameters(self, controls):
		if controls != None:
			for control in controls:
				if control != None:
					control.release_parameter()
					control.reset()
	


class SpecialCodecDeviceComponent(DeviceComponent):


	def __init__(self, script, *a, **k):
		self._script = script
		super(SpecialCodecDeviceComponent, self).__init__(*a, **k)
	

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
		super(SpecialCodecDeviceComponent, self).update()
	

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
	


class CodecResetSendsComponent(Component):
	' Special Component to reset all track sends to zero for the first four returns '
	__module__ = __name__


	def __init__(self, script, *a, **k):
		super(CodecResetSendsComponent, self).__init__(*a, **k)
		self._script = script
		self._buttons = [[None for index in range(4)] for index in range(8)]
	

	def disconnect(self):
		if (self._buttons != None):
			for column in self._buttons:
				for button in column:
					if (button != None):
						button.remove_value_listener(self.reset_send)
		self._buttons = []
	

	def on_enabled_changed(self):
		self.update()
	

	def set_buttons(self, buttons):
		for column in buttons:
			for button in column:
				assert isinstance(button, ButtonElement) or (button == None)
		#assert(for button in buttons(isinstance(button, ButtonElement) or (button == None)))
		for column in self._buttons:
			for button in column:
				if (button != None):
					button.remove_value_listener(self.reset_send)
		self._buttons = buttons
		for column in self._buttons:
			for button in column:
				if (button != None):
					button.add_value_listener(self.reset_send, identify_sender = True)
	

	def update(self):
		pass
	

	def reset_send(self, value, sender):
		if self.is_enabled() and not self._script._shift_pressed:
			assert (self._buttons != None)
			assert isinstance(value, int)
			tracks = self.tracks_to_use()
			returns = self.returns_to_use()
			if ((value is not 0) or (not sender.is_momentary())):
				for column in range(8):
					for row in range(4):
						if sender is self._buttons[column][row]:
							if (row < len(returns)):
								for track in tracks:
									track.mixer_device.sends[row].value = 0
								for track in returns:
									track.mixer_device.sends[row].value = 0
							break
	

	def tracks_to_use(self):
		return self.song.tracks
	

	def returns_to_use(self):
		return self.song.return_tracks
	


class CodecMixerComponent(MixerComponent):


	def __init__(self, num_returns = 4, *a, **k):
		self._return_strips = []
		self._return_controls = None
		super(CodecMixerComponent, self).__init__(*a, **k)
		for index in range(num_returns):
			self._return_strips.append(self._create_strip())
			self.register_components(self._return_strips[index])
		self._reassign_tracks()
	

	def return_strip(self, index):
		assert(index in range(len(self._return_strips)))
		return self._return_strips[index]
	

	def _reassign_tracks(self):
		super(CodecMixerComponent, self)._reassign_tracks()
		for track, channel_strip in izip(self.song.return_tracks, self._return_strips):
			channel_strip.set_track(track)
	

	def set_send_controls(self, controls):
		self._send_controls and self._send_controls.reset()
		self._send_controls = controls
		if controls:
			for index in range(len(self._channel_strips)):
				send_controls = [controls.get_button(row, index) for row in range(controls.height())]
				if self.send_index > controls.height:
					send_controls = send_controls + [None for _ in range(self.send_index - controls.height)]
				self._channel_strips[index].set_send_controls(send_controls)
		else:
			for strip in self._channel_strips:
				if self.send_index is None:
					strip.set_send_controls([None])
				else:
					strip.set_send_controls([None for _ in range(self.send_index)])
	

	def set_return_controls(self, controls):
		self._return_controls and self._return_controls.reset()
		self._return_controls = controls
		for control, channel_strip in izip(controls or [], self._return_strips):
			channel_strip.set_volume_control(control)
	


class CodecModDeviceProvider(ModDeviceProvider):


	def mod_device_from_device(self, device):
		modrouter = get_modrouter()
		if modrouter:
			mod_device = modrouter.is_mod(device)
			if mod_device:
				device = mod_device._codec_device_proxy if hasattr(mod_device, '_codec_device_proxy') else mod_device._device_proxy
		debug('DEVICE PROVIDER RETURNING:', device, device._name if hasattr(device, '_name') else None)
		if device:
			debug('parameters from provider:', [parameter.name if hasattr(parameter, 'name') else None for parameter in device.parameters])
		return device
	


class Codec(LividControlSurface):


	_sysex_id = 4
	_model_name = 'Code'
	_host_name = 'Codec'
	_version_check = 'b996'
	monomodular = None
	device_provider_class = CodecModDeviceProvider
	def __init__(self, c_instance, *a, **k):
		self.log_message = logger.warning
		super(Codec, self).__init__(c_instance, *a, **k)
		self._locked = False
		self._shift_button = None
		self._device_selection_follows_track_selection=FOLLOW
		self._leds_last = 0
		self._shift_latching = LatchingShiftedBehaviour if SHIFT_LATCHING else ShiftedBehaviour
		self._skin = Skin(CodecColors)
		with self.component_guard():
			self._define_sysex()
			self._setup_controls()
			self._setup_background()
			self._setup_mixer_controls()
			self._setup_device_navigator()
			self._setup_device_controls()
			self._setup_special_device_control() 
			self._setup_device_chooser()
			self._setup_device_selector()
			self._setup_send_reset()
			self._setup_default_buttons()
			self._setup_shift_modes()
			self._setup_mod()
			self._setup_modswitcher()
			self._setup_modes() 
			self._setup_m4l_interface()
		self._background.set_enabled(True)
	

	def _initialize_hardware(self):
		super(Codec, self)._initialize_hardware()
	

	def _initialize_script(self):
		super(Codec, self)._initialize_script()
		self._on_device_changed.subject = self._device_provider
		self._main_modes.set_enabled(True)
		self._main_modes.selected_mode = 'mix'
	

	def _define_sysex(self):
		self.fast_encoder_sysex = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_speed', message = FAST_ENCODER_MSG)
		self.normal_encoder_sysex = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_speed', message = NORMAL_ENCODER_MSG)
		self.slow_encoder_sysex = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_speed', message = SLOW_ENCODER_MSG)
	

	def _setup_controls(self):
		is_momentary = True
		optimized = False
		resource = PrioritizedResource
		self._livid = DoublePressElement(MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = LIVID, name = 'Livid_Button', script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge))
		self._dial = [[CodecEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CODE_DIALS[row][column], name = 'Dial_' + str(column) + '_' +	str(row), num = (column + (row*8)), script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge)	for row in range(4)] for column in range(8)]
		self._button = [[MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CODE_BUTTONS[row][column], name = 'Button_' + str(column) + '_' + str(row), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for row in range(4)] for column in range(8)]
		self._column_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CODE_COLUMN_BUTTONS[index], name = 'Column_Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(8)]		
		self._row_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = CODE_ROW_BUTTONS[index], name = 'Row_Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(4)]	
		self._code_keys = ButtonMatrixElement(name = 'Code_Keys', rows = [self._column_button])
		self._code_buttons = ButtonMatrixElement(name = 'Code_Buttons', rows = [self._row_button])
		self._encoder_matrix = ButtonMatrixElement(name = 'Encoder_Matrix', rows = [[self._dial[column][row] for column in range(8)] for row in range(4)])
		self._button_matrix = ButtonMatrixElement(name = 'Button_Matrix', rows = [[self._button[column][row] for column in range(8)] for row in range(4)])
	

	def _setup_background(self):
		self._background = BackgroundComponent()
		self._background.layer = Layer(priority = 3, matrix = self._button_matrix, encoders = self._encoder_matrix, livid = self._livid, buttons = self._code_buttons, keys = self._code_keys)
		self._background.set_enabled(False)
	

	def _setup_transport_control(self):
		self._transport = TransportComponent() 
		self._transport.name = 'Transport'
		self._transport.set_enabled(False)
	

	def _setup_mixer_controls(self):
		self._session_ring = SessionRingComponent(name = 'Session_Ring', num_tracks = 8, num_scenes = 0)
		self._session_navigation = SessionNavigationComponent(name = 'Session_Navigation', session_ring = self._session_ring)
		self._session_navigation.layer = Layer(priority = 4, left_button = self._button[6][0], right_button = self._button[7][0])
		self._session_navigation.set_enabled(False)
		#self._session = SessionComponent(name = 'Session', session_ring = self._session_ring)
		self._mixer = CodecMixerComponent(num_returns = 4, name = 'Mixer', tracks_provider = self._session_ring, invert_mute_feedback = True, auto_name = True)
		self._mixer._mix_layer = AddLayerMode(self._mixer, Layer(priority = 4, volume_controls = self._encoder_matrix.submatrix[:8,3],
									pan_controls = self._encoder_matrix.submatrix[:8,2],
									send_controls = self._encoder_matrix.submatrix[:8, :2],
									))
		self._mixer._solo_mute_layer = AddLayerMode(self._mixer, Layer(priority = 4, solo_buttons = self._button_matrix.submatrix[:8,2],
									mute_buttons = self._button_matrix.submatrix[:8,3],
									))
		self._mixer._select_layer = AddLayerMode(self._mixer, Layer(priority = 4, track_select_buttons = self._code_keys))
		self._mixer._sends_layer = AddLayerMode(self._mixer, Layer(priority = 4, send_controls = self._encoder_matrix.submatrix[:, :]))
		self._mixer.set_enabled(False)
	

	def _setup_device_navigator(self):
		self._device_navigator = DeviceNavigator(self._device_provider, self._mixer, self)
		self._device_navigator._dev1_layer = AddLayerMode(self._device_navigator, Layer(priority = 4, prev_button = self._button[4][0], next_button = self._button[5][0], prev_chain_button = self._button[6][0], next_chain_button = self._button[7][0]))
		self._device_navigator._dev2_layer = AddLayerMode(self._device_navigator, Layer(priority = 4, prev_button = self._button[4][1], next_button = self._button[5][1], prev_chain_button = self._button[6][1], next_chain_button = self._button[7][1]))
		self._device_navigator._dev3_layer = AddLayerMode(self._device_navigator, Layer(priority = 4, prev_button = self._button[4][2], next_button = self._button[5][2], prev_chain_button = self._button[6][2], next_chain_button = self._button[7][2]))
		self._device_navigator._dev4_layer = AddLayerMode(self._device_navigator, Layer(priority = 4, prev_button = self._button[4][3], next_button = self._button[5][3], prev_chain_button = self._button[6][3], next_chain_button = self._button[7][3]))
		self._device_navigator.set_enabled(False)
	

	def _setup_device_controls(self):
		self._device = [None for index in range(4)]
		for index in range(4):
			self._device[index] = CodecDeviceComponent(self, index+1, device_bank_registry = DeviceBankRegistry())
			self._device[index].name = 'CodecDevice_Component_' + str(index+1)
			self._device[index].layer = Layer(priority = 4, parameter_controls = self._encoder_matrix.submatrix[:, index],
												on_off_button = self._button[1][index],
												bank_prev_button = self._button[2][index],
												bank_next_button = self._button[3][index],
												)
			self._device[index]._nav_layer = AddLayerMode(self._device[index], Layer(priority = 4, nav_prev_button = self._button[6][index],
																					nav_next_button = self._button[7][index],))
			self._device[index].set_enabled(False)
	

	def _setup_special_device_control(self):
		self._special_device = SpecialCodecDeviceComponent(self, device_bank_registry = DeviceBankRegistry(), device_provider = self._device_provider)
		self._special_device.name = 'SpecialCodecDeviceComponent'
		self._special_device.main_layer = AddLayerMode(self._special_device, Layer(priority = 4, parameter_controls = self._encoder_matrix.submatrix[:,:],
											on_off_button = self._button[1][0],
											bank_prev_button = self._button[4][0],
											bank_next_button = self._button[5][0],
											))
		self._special_device.set_enabled(False)
	

	def _setup_device_chooser(self):
		self._selected_device = self._device[0]
		self._last_selected_device = self._device[0]

		self._selected_device_modes = ModesComponent()
		self._selected_device_modes.add_mode('disabled', [None])
		self._selected_device_modes.add_mode('device_0', [self._device_navigator._dev1_layer], behaviour = DefaultedBehaviour())
		self._selected_device_modes.add_mode('device_1', [self._device_navigator._dev2_layer], behaviour = DefaultedBehaviour())
		self._selected_device_modes.add_mode('device_2', [self._device_navigator._dev3_layer], behaviour = DefaultedBehaviour())
		self._selected_device_modes.add_mode('device_3', [self._device_navigator._dev4_layer], behaviour = DefaultedBehaviour())
		self._selected_device_modes.layer = Layer(priority = 4, device_0_button = self._button[0][0], device_1_button = self._button[0][1], device_2_button = self._button[0][2], device_3_button = self._button[0][3])
		self._selected_device_modes.selected_mode = 'device_0'
		self._selected_device_modes.set_enabled(False)
		self._on_device_selector_mode_changed.subject = self._selected_device_modes
	

	def _setup_device_selector(self):
		self._device_selector = DeviceSelectorComponent(self)
		self._device_selector.name = 'Device_Selector'
		self._device_selector.layer = Layer(priority = 4, matrix = self._code_keys)
		self._device_selector.set_enabled(False)
	

	def _setup_send_reset(self):
		self._send_reset = CodecResetSendsComponent(self)
		self._send_reset.set_enabled(False)
		#self._send_reset.set_buttons(self._button)
	

	def _setup_default_buttons(self):
		self._value_default = ParameterDefaultComponent(script = self, dials = self._dial)
		self._value_default.layer = Layer(priority = 3, matrix = self._button_matrix)
		self._value_default.set_enabled(False)
	

	def _setup_shift_modes(self):
		self._main_shift_modes = ModesComponent(name = 'MainShiftModes')
		self._main_shift_modes.add_mode('disabled', [self.normal_encoder_sysex], cycle_mode_button_color = 'DefaultButton.Off')
		self._main_shift_modes.add_mode('enabled', [self.slow_encoder_sysex], cycle_mode_button_color = 'DefaultButton.On')  #, self._value_default
		self._main_shift_modes.layer = Layer(priority = 4, cycle_mode_button = self._livid)
		self._main_shift_modes.set_enabled(False)
		self._main_shift_modes.selected_mode = 'disabled'

		self._mod_shift_modes = ModesComponent(name = 'ModShiftModes')
		self._mod_shift_modes.layer = Layer(priority = 4, cycle_mode_button = self._livid)
		self._mod_shift_modes.set_enabled(False)
	

	def _setup_mod(self):
		self.monomodular = get_monomodular(self)
		self.monomodular.name = 'monomodular_switcher'
		self.modhandler = CodecModHandler(script = self, device_provider = self._device_provider)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer(priority = 4, code_grid = self._button_matrix.submatrix[:,:], code_encoder_grid = self._encoder_matrix.submatrix[:,:])
		self.modhandler.set_enabled(False)
		self.modhandler.code_buttons_layer = AddLayerMode(self.modhandler, Layer(priority = 5, code_buttons = self._code_buttons))
		self.modhandler.keys_layer = AddLayerMode(self.modhandler, Layer(priority = 5, key_buttons = self._code_keys))
		self.modhandler.code_keys_layer = AddLayerMode(self.modhandler, Layer(priority = 5, code_keys = self._code_buttons))
		self.modhandler.alt_layer = AddLayerMode(self.modhandler, Layer(priority = 4, lock_button = self._livid))

		self._device_provider.restart_mod()
	

	def _setup_modswitcher(self):
		self._modswitcher = ModesComponent(name = 'ModSwitcher')
		self._modswitcher.add_mode('mod', [self._special_device, self.modhandler, self._mod_shift_modes])
		self._modswitcher.add_mode('special_device', [self._special_device, self._special_device.main_layer, self._mixer, self._mixer._select_layer, self._main_shift_modes])
		self._modswitcher.selected_mode = 'special_device'
		self._modswitcher.set_enabled(False)

		self._mod_shift_modes.add_mode('disabled', [self.modhandler.keys_layer], cycle_mode_button_color = 'Mod.ShiftOff')
		self._mod_shift_modes.add_mode('enabled', [self.modhandler.code_keys_layer, self.modhandler.code_buttons_layer, tuple([self._send_mod_shift, self._release_mod_shift])], cycle_mode_button_color = 'Mod.ShiftOn')
		self._mod_shift_modes.selected_mode = 'disabled'
	

	def _setup_modes(self):
		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [])
		self._main_modes.add_mode('mix_shifted', [self._mixer, self._mixer._mix_layer, self._mixer._solo_mute_layer, self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('mix', [self._mixer, self._mixer._mix_layer, self._mixer._select_layer, self._mixer._solo_mute_layer, self._session_navigation, self._background, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('sends_shifted', [self._mixer, self._mixer._sends_layer, self._mixer._select_layer, self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('sends', [self._mixer, self._mixer._sends_layer, self._mixer._select_layer, self._background, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('device_shifted', [self._selected_device_modes, self._device_selector, self._device[0], self._device[1], self._device[2], self._device[3], self._device_selector, self._background], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Main'))
		self._main_modes.add_mode('device', [self._mixer, self._mixer._select_layer, self._selected_device_modes, self._device[0], self._device[1], self._device[2], self._device[3], self._background, self._mixer._select_layer, self._main_shift_modes], behaviour = self._shift_latching(color = 'Mode.Main'))
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
	

	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard)
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control
	

	@listens('selected_mode')
	def _on_device_selector_mode_changed(self, mode):
		if mode == 'disabled':
			for device in self._device:
				device.set_dynamic_device_provider(None)
		elif mode in DEVICE_COMPONENTS:
			active_device = self._device[DEVICE_COMPONENTS.index(self._selected_device_modes.selected_mode)]
			for device in self._device:
				if device is active_device:
					device.set_dynamic_device_provider(self._device_provider)
				else:
					device.set_dynamic_device_provider(None)
			if active_device.find_track(active_device._get_device()) == self.song.view.selected_track:
				active_device.display_device()
	

	@listens('device')
	def _on_device_changed(self):
		self._on_device_name_changed.subject = self._device_provider.device
		self.schedule_message(1, self._update_modswitcher)
	

	@listens('name')
	def _on_device_name_changed(self):
		for device in self._device:
			device.scan_all()
	

	def _on_selected_track_changed(self):
		super(Codec, self)._on_selected_track_changed()
		#self.schedule_message(1, self._update_modswitcher)
		if not len(self.song.view.selected_track.devices):
			self._update_modswitcher()
	

	def _update_modswitcher(self):
		debug('update modswitcher', self.modhandler.active_mod())
		if self.modhandler.active_mod():
			self._modswitcher.selected_mode = 'mod'
		else:
			self._modswitcher.selected_mode = 'special_device'
	

	"""general functionality"""
	def disconnect(self):
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<<< Codec log closed >>>>>>>>>>>>>>>>>>>>>>>>>')
		super(Codec, self).disconnect()
	

	def update_display(self):
		super(Codec, self).update_display()
		self.modhandler.send_ring_leds()
	

	def restart_monomodular(self):
		#self.log_message('restart monomodular')
		self.modhandler.disconnect()
		with self.component_guard():
			self._setup_mod()
	

	def _send_mod_shift(self):
		self.modhandler._shift_value(1)
	

	def _release_mod_shift(self):
		self.modhandler._shift_value(0)
	


class ParameterDefaultComponent(Component):
	__module__ = __name__
	__doc__ = " MonoCode controller script "


	def __init__(self, script, dials = None):
		"""everything except the '_on_selected_track_changed' override and 'disconnect' runs from here"""
		Component.__init__(self)
		self._script = script
		self._dials = dials
	

	def set_matrix(self, matrix):
		#self._value_to_default.subject and self._value_to_default.subject.reset()
		self._value_to_default.subject = matrix
	

	def set_dials(self, dials):
		self._dials = dials
	

	@listens('value')
	def _value_to_default(self, value, x, y, *a):
		if value > 0 and self._dials and len(self._dials) >=x and len(self._dials[x]) >= y:
			dial = self._dials[x][y]
			if dial != None:
				if dial.mapped_parameter() != None:
					if hasattr(dial.mapped_parameter(), 'default_value'):
						dial.mapped_parameter().value = dial.mapped_parameter().default_value
	

	def update(self):
		pass
	

	def disconnect(self):
		self._value_to_default.subject = None
		self._dials = None
	


class CodecModHandler(ModHandler):


	def __init__(self, *a, **k):
		self._name = 'CodecModHandler'
		self._local = True
		self._encoders_to_device = True
		self._last_sent_leds = 1
		self._code_grid = None
		self._code_encoder_grid = None
		self._code_keys = None
		self._code_buttons = None
		addresses = {'code_encoders_to_device': {'obj':StoredElement(_name = 'code_encoders_to_device', _value = True), 'method':self._receive_code_encoders_to_device},
					'code_grid': {'obj':Grid('code_grid', 8, 4), 'method':self._receive_code_grid},
					'code_encoder_grid': {'obj':RingedGrid('code_encoder_grid', 8, 4), 'method':self._receive_code_encoder_grid},
					'code_key': {'obj':  Array('code_key', 8), 'method': self._receive_code_key},
					'code_button': {'obj':  Array('code_button', 4), 'method': self._receive_code_button}}
		super(CodecModHandler, self).__init__(addresses = addresses, *a, **k)
		self._color_type = 'Monochrome'
		self.nav_box = self.register_component(NavigationBox(self, 16, 16, 2, 2, self.set_offset))

		self._colors = range(128)
	
		#'code_encoder_grid_relative': {'obj':StoredElement(_name = 'code_encoder_grid_relative', _value = 'True'), 'method':self._receive_code_encoder_grid_relative},
		#'code_encoder_grid_local': {'obj':StoredElement(_name = 'code_encoder_grid_local'), 'method':self._receive_code_encoder_grid_local},


	def _receive_code_grid(self, x, y, value, *a, **k):
		#debug('_receive_code_grid:', x, y, value)
		if self.is_enabled() and self._active_mod and not self._active_mod.legacy and not self._code_grid_value.subject is None and x < 8 and y < 4:
			self._code_grid_value.subject.send_value(x, y, self._colors[value], True)
	

	def _receive_code_encoder_grid(self, x, y, *a, **k):
		#debug('_receive_code_encoder_grid:', x, y, k)
		if self.is_enabled() and self._active_mod and not self._code_encoder_grid is None and x < 8 and y < 4:
			keys = k.keys()
			if 'value' in keys:
				if self._local:
					self._code_encoder_grid.send_value(x, y, k['value'], True)
				else:
					self._code_encoder_grid.get_button(y, x)._ring_value = k['value']
			if 'mode' in keys:
				self._code_encoder_grid.get_button(y, x).set_mode(k['mode'])
			if 'green' in keys:
				self._code_encoder_grid.get_button(y, x).set_green(k['green'])
			if 'custom' in keys:
				self._code_encoder_grid.get_button(y, x).set_custom(k['custom'])
			if 'local' in keys:
				self._receive_code_encoder_grid_local(k['local'])
			if 'relative' in keys:
				self._receive_code_encoder_grid_relative(k['relative'])
	

	def _receive_code_encoder_grid_relative(self, value, *a):
		debug('_receive_code_encoder_grid_relative:', value)
		if self.is_enabled() and self._active_mod:
			value and self._script._send_midi(tuple([240, 0, 1, 97, 4, 17, 127, 127, 127, 127, 127, 127, 127, 127, 247])) or self._script._send_midi(tuple([240, 0, 1, 97, 4, 17, 0, 0, 0, 0, 0, 0, 0, 0, 247]))
	

	def _receive_code_encoder_grid_local(self, value, *a):
		debug('_receive_code_encoder_grid_local:', value)
		if self.is_enabled() and self._active_mod:
			self.clear_rings()
			self._local = bool(value)
			value and self._script._send_midi(tuple([240, 0, 1, 97, 4, 8, 72, 247])) or self._script._send_midi(tuple([240, 0, 1, 97, 4, 8, 64, 247]))
	

	def _receive_code_encoders_to_device(self, value, *a):
		debug('_receive_code_encoders_to_device:', value)
		if self.is_enabled() and self._active_mod:
			self._encoders_to_device = bool(value)
			self._script._special_device.set_parameter_controls(self._code_encoder_grid if value else None)
	

	def _receive_code_button(self, num, value, *a):
		#debug('receive code_button', num, value)
		if self.is_enabled() and self._active_mod:
			if not self._code_buttons_value.subject is None:
				self._code_buttons_value.subject.send_value(num, 0, self._colors[value], True)
	

	def _receive_code_key(self, num, value, *a):
		if self.is_enabled() and self._active_mod and not self._active_mod.legacy:
			if not self._code_keys_value.subject is None:
				self._code_keys_value.subject.send_value(num, 0, self._colors[value], True)
	

	def _receive_grid(self, x, y, value, *a, **k):
		if self.is_enabled() and self._active_mod and self._active_mod.legacy:
			if not self._code_grid_value.subject is None:
				if (x - self.x_offset) in range(8) and (y - self.y_offset) in range(4):
					self._code_grid_value.subject.send_value(x - self.x_offset, y - self.y_offset, self._colors[value], True)
	

	def set_code_grid(self, grid):
		self._code_grid and self._code_grid.reset()
		self._code_grid = grid
		self._code_grid_value.subject = self._code_grid
	

	def set_code_encoder_grid(self, grid):
		self._code_encoder_grid = grid
		if self._encoders_to_device:
			self._script._special_device.set_parameter_controls(grid)
		else:
			self._code_encoder_grid and self._code_encoder_grid.reset()
			self._code_encoder_grid_value.subject = self._code_encoder_grid

		#self.set_parameter_controls(grid)
		#debug('parameter controls are:', self._parameter_controls)
	

	def set_code_keys(self, keys):
		self._code_keys and self._code_keys.reset()
		self._code_keys = keys
		self._code_keys_value.subject = self._code_keys
	

	def set_code_buttons(self, buttons):
		#debug('set code buttons', buttons)
		self._code_buttons and self._code_buttons.reset()
		self._code_buttons = buttons
		self._code_buttons_value.subject = self._code_buttons
		if not self.active_mod() is None:
			self.active_mod()._addresses['code_button'].restore()
	

	@listens('value')
	def _alt_value(self, value, *a, **k):
		self._is_alted = not value is 0
		mod = self.active_mod()
		if mod:
			mod.send('alt', value)
		self.update()
	

	@listens('value')
	def _code_keys_value(self, value, x, y, *a, **k):
		#debug('_code_keys_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('code_key', x, int(value>0))
	

	@listens('value')
	def _code_buttons_value(self, value, x, y, *a, **k):
		#debug('_code_buttons_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('code_button', x, int(value>0))
	

	@listens('value')
	def _code_grid_value(self, value, x, y, *a, **k):
		#debug('_code_grid_value', x, y, value)
		if self._active_mod:
			if self._active_mod.legacy:
				self._active_mod.send('grid', x + self.x_offset, y + self.y_offset, int(value>0))
			else:
				self._active_mod.send('code_grid', x, y, int(value>0))
	

	@listens('value')
	def _code_encoder_grid_value(self, value, x, y, *a, **k):
		#debug('_code_encoder_grid_value:', x, y, value)
		if self._active_mod:
			self._active_mod.send('code_encoder_grid', x, y, value)
	

	def update(self, *a, **k):
		mod = self.active_mod()
		#debug('modhandler update:', mod)
		if self.is_enabled() and not mod is None:
			mod.restore()
		else:
			#debug('disabling modhandler')
			self._script._send_midi(tuple([240, 0, 1, 97, 4, 17, 0, 0, 0, 0, 0, 0, 0, 0, 247]))
			self._script._send_midi(tuple([240, 0, 1, 97, 4, 8, 72, 247]))
			if not self._code_grid_value.subject is None:
				self._code_grid_value.subject.reset()
			if not self._code_encoder_grid_value.subject is None:
				self._code_encoder_grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()
	

	def send_ring_leds(self):
		if self.is_enabled() and self._active_mod and not self._local:
			grid = self._script._special_device._parameter_controls if self._encoders_to_device else self._code_encoder_grid
			if not grid is None:
				leds = [240, 0, 1, 97, 4, 31]
				def xiterbuttons(matrix):
					for i, j in product(xrange(matrix.width()), xrange(matrix.height())):
						button = matrix.get_button(j, i)
						yield (button, (i, j))
				
				for encoder, coords in xiterbuttons(grid):
					bytes = encoder._get_ring()
					leds.append(bytes[0])
					leds.append(int(bytes[1]) + int(bytes[2]))
				leds.append(247)
				if not leds==self._last_sent_leds:
					self._script._send_midi(tuple(leds))
					self._last_sent_leds = leds
					#debug('sending ring leds:', leds)
	

	def clear_rings(self):
		self._last_sent_leds = 1
	




#
#