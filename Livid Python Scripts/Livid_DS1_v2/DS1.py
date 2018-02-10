# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516

from __future__ import absolute_import, print_function
import Live
import math
import sys
from re import *
from itertools import imap, chain, starmap

from ableton.v2.base import inject, listens, listens_group
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry
from ableton.v2.control_surface.elements import ComboElement, ButtonMatrixElement, DoublePressElement, MultiElement, DisplayDataSource, SysexElement
from ableton.v2.control_surface.components import ClipSlotComponent, SceneComponent, SessionComponent, TransportComponent, BackgroundComponent, ViewControlComponent, SessionRingComponent, SessionRecordingComponent, SessionNavigationComponent, MixerComponent, PlayableComponent
from ableton.v2.control_surface.components.mixer import simple_track_assigner
from ableton.v2.control_surface.control import control_color
from ableton.v2.control_surface.mode import AddLayerMode, ModesComponent, DelayMode
from ableton.v2.control_surface.elements.physical_display import PhysicalDisplayElement
from ableton.v2.control_surface.components.session_recording import *

from ableton.v2.control_surface.control import PlayableControl, ButtonControl, control_matrix

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import SendLividSysexMode, MomentaryBehaviour, ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour, ShiftedBehaviour, LatchingShiftedBehaviour, FlashingBehaviour
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.elements import MonoEncoderElement, MonoBridgeElement, generate_strip_string
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import MonoDeviceComponent, DeviceNavigator, TranslationComponent, MonoMixerComponent
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.components.mono_instrument import *
from aumhaa.v2.livid import LividControlSurface, LividSettings, LividRGB
from aumhaa.v2.control_surface.components.fixed_length_recorder import FixedLengthSessionRecordingComponent
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

from .Map import *



ENCODER_SPEED = [0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0, 21, 0, 22, 0, 23, 0, 24, 0, 127, 1, 26, 0, 127, 1, 127, 1]


MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224


def is_device(device):
	return (not device is None and isinstance(device, Live.Device.Device) and hasattr(device, 'name'))


def make_pad_translations(chan):
	return tuple((x%4, int(x/4), x+16, chan) for x in range(16))


def return_empty():
	return []


debug = initialize_debug()

class DS1SessionComponent(SessionComponent):


	def set_scene_launch_buttons(self, buttons):
		assert(not buttons or buttons.width() == self._session_ring.num_scenes and buttons.height() == 1)
		if buttons:
			for button, (x, _) in buttons.iterbuttons():
				scene = self.scene(x)
				#debug('setting scene launch for button:', button, 'scene:', scene)
				scene.set_launch_button(button)

		else:
			for x in xrange(self._session_ring.num_scenes):
				scene = self.scene(x)
				scene.set_launch_button(None)
	


class DS1SessionNavigationComponent(SessionNavigationComponent):


	def set_track_select_dial(self, dial):
		self._on_track_select_dial_value.subject = dial
	

	@listens('value')
	def _on_track_select_dial_value(self, value):
		#debug('_on_track_select_dial_value:', value)
		#self._can_bank_left() and self._bank_left() if value == 127 else self._can_bank_right() and self._bank_right()
		self._horizontal_banking.can_scroll_up() and self._horizontal_banking.scroll_up() if value == 127 else self._horizontal_banking.can_scroll_down() and self._horizontal_banking.scroll_down()
	

class DS1TransportComponent(TransportComponent):


	def _update_stop_button_color(self):
		self._stop_button.color = 'Transport.StopOn' if self._play_toggle.is_toggled else 'Transport.StopOff'
	



class DS1(LividControlSurface):


	_sysex_id = 16
	_model_name = 'DS1'


	def __init__(self, c_instance):
		super(DS1, self).__init__(c_instance)
		self._skin = Skin(DS1Colors)
		with self.component_guard():
			self._define_sysex()
			self._setup_controls()
			self._setup_background()
			self._setup_m4l_interface()
			self._setup_session_control()
			self._setup_mixer_control()
			self._setup_transport_control()
			self._setup_device_control()
			self._setup_session_recording_component()
			self._setup_main_modes()
	

	def _initialize_script(self):
		super(DS1, self)._initialize_script()
		self._main_modes.set_enabled(True)
		self._main_modes.selected_mode = 'Main'
	

	def _initialize_hardware(self):
		super(DS1, self)._initialize_hardware()
		self.local_control_off.enter_mode()
		self.encoder_absolute_mode.enter_mode()
		self.encoder_speed_sysex.enter_mode()
	


	def _define_sysex(self):
		self.encoder_speed_sysex = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_mapping', message = ENCODER_SPEED)
		self.encoder_absolute_mode = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_encosion_mode', message = [2])
		self.local_control_off = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_local_control', message = [0])

	

	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		self._fader = [MonoEncoderElement(mapping_feedback_delay = -1, msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = DS1_FADERS[index], name = 'Fader_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource) for index in range(8)]
		self._dial = [[MonoEncoderElement(mapping_feedback_delay = -1, msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = DS1_DIALS[x][y], name = 'Dial_' + str(x) + '_' + str(y), num = x + (y*5), script = self, optimized_send_midi = optimized, resource_type = resource) for x in range(8)] for y in range(5)]
		self._side_dial = [MonoEncoderElement(mapping_feedback_delay = -1, msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = DS1_SIDE_DIALS[x], name = 'Side_Dial_' + str(x), num = x, script = self, optimized_send_midi = optimized, resource_type = resource) for x in range(4)]
		self._encoder = [MonoEncoderElement(mapping_feedback_delay = -1, msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = DS1_ENCODERS[x], name = 'Encoder_' + str(x), num = x, script = self, optimized_send_midi = optimized, resource_type = resource) for x in range(4)]
		self._encoder_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = DS1_ENCODER_BUTTONS[index], name = 'EncoderButton_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for index in range(4)]
		self._master_fader = MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = DS1_MASTER, name = 'MasterFader', num = 0, script = self, optimized_send_midi = optimized, resource_type = resource)
		self._button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = DS1_BUTTONS[index], name = 'Button_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for index in range(16)]
		self._grid = [[MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = DS1_GRID[x][y], name = 'Button_' + str(x) + '_' + str(y), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for x in range(3)] for y in range(3)]
		self._dummy = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = 120+x, name = 'Dummy_Dial_' + str(x), num = x, script = self, optimized_send_midi = optimized, resource_type = resource) for x in range(5)]

		self._fader_matrix = ButtonMatrixElement(name = 'FaderMatrix', rows = [self._fader])
		self._top_buttons = ButtonMatrixElement(name = 'TopButtonMatrix', rows = [self._button[:8]])
		self._bottom_buttons = ButtonMatrixElement(name = 'BottomButtonMatrix', rows = [self._button[8:]])
		self._dial_matrix = ButtonMatrixElement(name = 'DialMatrix', rows = self._dial)
		self._side_dial_matrix = ButtonMatrixElement(name = 'SideDialMatrix', rows = [self._side_dial])
		self._encoder_matrix = ButtonMatrixElement(name = 'EncoderMatrix', rows = [self._encoder])
		self._encoder_button_matrix = ButtonMatrixElement(name = 'EncoderButtonMatrix', rows = [self._encoder_button])
		self._grid_matrix = ButtonMatrixElement(name = 'GridMatrix', rows = self._grid)
		self._selected_parameter_controls = ButtonMatrixElement(name = 'SelectedParameterControls', rows = [self._dummy + self._encoder[:1] + self._encoder[2:]])
	

	def _setup_background(self):
		self._background = BackgroundComponent(name = 'Background')
		self._background.layer = Layer(priority = 0, fader_matrix = self._fader_matrix, 
													top_buttons = self._top_buttons,
													bottom_buttons = self._bottom_buttons,
													dial_matrix = self._dial_matrix,
													side_dial_matrix = self._side_dial_matrix,
													encoder_button_matrix = self._encoder_button_matrix,
													grid_matrix = self._grid_matrix)
		self._background.set_enabled(True)
	

	def _setup_autoarm(self):
		self._auto_arm = AutoArmComponent(name='Auto_Arm')
		self._auto_arm.can_auto_arm_track = self._can_auto_arm_track
	

	def _tracks_to_use(self):
		return self.song.visible_tracks + self.song.return_tracks
	

	def _setup_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks = 8, num_scenes = 1, tracks_to_use = self._tracks_to_use)
		self._session_ring.set_enabled(True)

		self._session_navigation = DS1SessionNavigationComponent(name = 'SessionNavigation', session_ring = self._session_ring)
		self._session_navigation._vertical_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation.layer = Layer(priority = 4, track_select_dial = ComboElement(control = self._encoder[1], modifier = [self._encoder_button[1]] ), up_button = self._grid[0][1], down_button = self._grid[0][2])
		self._session_navigation.set_enabled(False)
		
		self._session = DS1SessionComponent(session_ring = self._session_ring, auto_name = True)
		hasattr(self._session, '_enable_skinning') and self._session._enable_skinning()
		self._session.layer = Layer(priority = 4, scene_launch_buttons = self._grid_matrix.submatrix[1:2, 1:2])
		self._session.clips_layer = AddLayerMode(self._session, Layer(priority = 4, clip_launch_buttons = self._top_buttons, stop_track_clip_buttons = self._bottom_buttons))
		self._session.set_enabled(False)
	

	def _setup_mixer_control(self):

		self._mixer = MonoMixerComponent(name = 'Mixer', num_returns = 2, tracks_provider = self._session_ring, track_assigner = simple_track_assigner, invert_mute_feedback = True, auto_name = True, enable_skinning = True)
		self._mixer.master_strip().set_volume_control(self._master_fader)
		self._mixer.set_prehear_volume_control(self._side_dial[3])
		self._mixer.layer = Layer(volume_controls = self._fader_matrix, track_select_dial = self._encoder[1])
		self._strip = [self._mixer.channel_strip(index) for index in range(8)]
		if KNOBS_ARE_SENDS:
			for index in range(8):
				self._strip[index].layer = Layer(priority = 4, send_controls = self._dial_matrix.submatrix[index:index+1, :4], pan_control = self._dial[4][index])
		else:
			for index in range(8):
				self._strip[index].layer = Layer(priority = 4, parameter_controls = self._dial_matrix.submatrix[index:index+1, :])
		self._mixer.selected_strip().layer = Layer(priority = 4, parameter_controls = self._selected_parameter_controls)
		self._mixer.master_strip().layer = Layer(priority = 4, parameter_controls = self._side_dial_matrix.submatrix[:3, :])
		self._mixer.main_layer = AddLayerMode(self._mixer, Layer(priority = 4, solo_buttons = self._bottom_buttons, mute_buttons = self._top_buttons))
		self._mixer.select_layer = AddLayerMode(self._mixer, Layer(priority = 4, arm_buttons = self._bottom_buttons, track_select_buttons = self._top_buttons))
		self.song.view.selected_track = self._mixer.channel_strip(0)._track 
		self._mixer.set_enabled(False)
	

	def _setup_transport_control(self):
		self._transport = DS1TransportComponent()
		self._transport.name = 'Transport'
		self._transport._record_toggle.view_transform = lambda value: 'Transport.RecordOn' if value else 'Transport.RecordOff'
		self._transport.layer = Layer(priority = 4, stop_button = self._grid[1][0], play_button = self._grid[0][0], record_button = self._grid[2][0])
		self._transport.set_enabled(True)
	

	def _setup_device_control(self):
		self._device = DeviceComponent(name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())

		self._device_navigator = DeviceNavigator(self._device_provider, self._mixer, self)
		self._device_navigator.name = 'Device_Navigator'
	

	def _setup_session_recording_component(self):
		self._clip_creator = ClipCreator()
		self._clip_creator.name = 'ClipCreator'
		self._recorder = SessionRecordingComponent(ViewControlComponent())
		self._recorder.set_enabled(True)
		self._recorder.layer = Layer(priority = 4, automation_button = self._grid[1][2], record_button  = self._grid[2][1],)
	

	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard, priority = 10)
		self._m4l_interface.name = "M4LInterface"
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control
	

	def _setup_translations(self):
		controls = []
		for control in self.controls:
			controls.append(control)
		self._translations = TranslationComponent(controls, 10)
		self._translations.name = 'TranslationComponent'
		self._translations.set_enabled(False)
	

	def _setup_main_modes(self):
		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('Main', [self._mixer, self._mixer.main_layer, self._session, self._session_navigation], cycle_mode_button_color = 'ModeButtons.Main')
		self._main_modes.add_mode('Select', [self._mixer, self._mixer.select_layer, self._session, self._session_navigation], cycle_mode_button_color = 'ModeButtons.Select')
		self._main_modes.add_mode('Clips', [self._mixer, self._session, self._session.clips_layer, self._session_navigation], cycle_mode_button_color = 'ModeButtons.Clips')
		self._main_modes.layer = Layer(priority = 4, cycle_mode_button = self._grid[2][2])
		self._main_modes.selected_mode = 'Main'
		self._main_modes.set_enabled(False)
	

	def _can_auto_arm_track(self, track):
		routing = track.current_input_routing
		return routing == 'Ext: All Ins' or routing == 'All Ins' or routing.startswith('DS1 Input')
		#self._main_modes.selected_mode in ['Sends', 'Device'] and
	

#	a