# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.3b8 RC on 083018

from __future__ import with_statement
import Live
import time
import math
import logging
logger = logging.getLogger(__name__)

from itertools import izip, izip_longest, product

from ableton.v2.base import slicer, to_slice, liveobj_changed, group, flatten, listens
from ableton.v2.control_surface.elements.button import ButtonElement
from ableton.v2.control_surface.elements.button_matrix import ButtonMatrixElement
from ableton.v2.control_surface.components.channel_strip import ChannelStripComponent
from ableton.v2.control_surface.compound_component import CompoundComponent
from ableton.v2.control_surface.control_element import ControlElement
from ableton.v2.control_surface.control_surface import ControlSurface
from ableton.v2.control_surface.component import Component as ControlSurfaceComponent
from ableton.v2.control_surface.elements.encoder import EncoderElement
from ableton.v2.control_surface.input_control_element import *
from ableton.v2.control_surface.components.mixer import MixerComponent, SimpleTrackAssigner
from ableton.v2.control_surface.components.session import SessionComponent
from ableton.v2.control_surface.components.transport import TransportComponent
from ableton.v2.control_surface.components.session_navigation import SessionNavigationComponent
from ableton.v2.control_surface.mode import AddLayerMode, LayerMode, ModesComponent, ModeButtonBehaviour, DelayMode
from ableton.v2.control_surface.resource import PrioritizedResource
from ableton.v2.control_surface.skin import Skin
from ableton.v2.control_surface import DeviceBankRegistry
from ableton.v2.control_surface.components.device import DeviceComponent
from ableton.v2.control_surface.layer import Layer
#from ableton.v2.control_surface.components.m4l_interface import M4LInterfaceComponent
from ableton.v2.control_surface.elements.combo import ComboElement, DoublePressElement, MultiElement, DoublePressContext
from ableton.v2.control_surface.components.background import BackgroundComponent
from ableton.v2.control_surface.components.session_ring import SessionRingComponent
from ableton.v2.base.event import *
from ableton.v2.base.task import *
from ableton.v2.control_surface.percussion_instrument_finder import PercussionInstrumentFinder, find_drum_group_device
from ableton.v2.control_surface.elements import PlayheadElement

from Push.mode_behaviours import CancellableBehaviour
#from pushbase.instrument_component import InstrumentComponent, NoteLayout
from aumhaa.v2.control_surface.components.fixed_length_recorder import FixedLengthSessionRecordingComponent
from pushbase.auto_arm_component import AutoArmComponent
from pushbase.grid_resolution import GridResolution
#from pushbase.playhead_element import PlayheadElement
#from pushbase.percussion_instrument_finder import PercussionInstrumentFinder, find_drum_group_device

from _Generic.Devices import *

from aumhaa.v2.control_surface import SendLividSysexMode, ShiftedBehaviour, LatchingShiftedBehaviour, DelayedExcludingMomentaryBehaviour
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.instrument_consts import *
from aumhaa.v2.control_surface.components import DeviceNavigator, DeviceSelectorComponent, MonoMixerComponent
from aumhaa.v2.control_surface.components.mono_instrument import *
from aumhaa.v2.control_surface.elements import MonoBridgeElement, MonoButtonElement, MonoEncoderElement
from aumhaa.v2.livid import LividControlSurface
from aumhaa.v2.livid import LividSettings
from aumhaa.v2.base.debug import initialize_debug
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

debug = initialize_debug()

from Map import *

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224




class MinimMonoInstrumentComponent(MonoInstrumentComponent):


	def __init__(self, *a, **k):
		super(MinimMonoInstrumentComponent, self).__init__(*a, **k)



class Minim(LividControlSurface):


	_sysex_id = 18
	_model_name = 'Minim'

	def __init__(self, c_instance, *a, **k):
		super(Minim, self).__init__(c_instance, *a, **k)
		self._shift_latching = LatchingShiftedBehaviour if SHIFT_LATCHING else ShiftedBehaviour
		self._skin = Skin(MinimColors)
		with self.component_guard():
			self._define_sysex()
			self._setup_monobridge()
			self._setup_controls()
			self._setup_background()
			self._setup_autoarm()
			self._setup_viewcontrol()
			self._setup_session()
			self._setup_mixer()
			self._setup_transport()
			self._setup_recorder()
			self._setup_instrument()
			self._setup_modes()
			self._setup_m4l_interface()
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<<< Minim log opened >>>>>>>>>>>>>>>>>>>>>>>>>')
		self.show_message('Minim Control Surface Loaded')
		self._background.set_enabled(True)


	def _check_connection(self):
		if not self._connected:
			debug(self._model_name, '_check_connection')
			self._livid_settings.new_query_surface()
			#self._connection_routine.restart()
			self.schedule_message(5, self._check_connection)


	def _initialize_hardware(self):
		debug('sending local control off')
		self.local_control_off.enter_mode()


	def _initialize_script(self):
		self._on_device_changed.subject = self._device_provider
		self._main_modes.set_enabled(True)
		self._main_modes.selected_mode = 'session'
		self._session_ring._update_highlight()
		self.refresh_state()


	def _setup_controls(self):
		is_momentary = True
		optimized = False
		resource = PrioritizedResource
		self._fader = MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = MINIM_SLIDER, name = 'Fader', script = self, mapping_feedback_delay = -1, optimized_send_midi = optimized, resource_type = resource)
		self._pad = [[MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = MINIM_PADS[row][column], name = 'Pad_' + str(column) + '_' + str(row), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for column in range(4)] for row in range(2)]
		self._button = [[MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = MINIM_BUTTONS[row][column], name = 'Button_' + str(column) + '_' + str(row), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for column in range(4)] for row in range(2)]
		self._side_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = MINIM_SIDE_BUTTONS[index], name = 'Side_Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for index in range(5)]
		self._top_button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = MINIM_TOP_BUTTONS[index], name = 'Top_Button_' + str(index), script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for index in range(2)]
		self._bottom_button = MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = MINIM_BOTTOM_BUTTON, name = 'Bottom_Button', script = self, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource)


		self._matrix = ButtonMatrixElement(name = 'Pad_Matrix', rows = [self._button[:][0], self._pad[:][0], self._pad[:][1],self._button[:][1]])
		self._side_button_matrix = ButtonMatrixElement(name = 'Side_Button_Matrix', rows = [self._side_button])
		self._top_button_matrix = ButtonMatrixElement(name = 'Button_Matrix', rows = [self._top_button])


	def _setup_background(self):
		self._background = BackgroundComponent()
		self._background.layer = Layer(priority = 3, matrix = self._matrix.submatrix[:,:], side_buttons = self._side_button_matrix, top_buttons = self._top_button_matrix.submatrix[:,:], bottom_button = self._bottom_button)
		self._background.set_enabled(False)


	def _define_sysex(self):
		self._livid_settings = LividSettings(model = 18, control_surface = self)
		self.local_control_off = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_local_control', message = [42, 42])


	def _setup_autoarm(self):
		self._auto_arm = AutoArmComponent(name='Auto_Arm')
		self._auto_arm.can_auto_arm_track = self._can_auto_arm_track
		self._auto_arm._update_notification = lambda: None


	def _setup_viewcontrol(self):
		self._viewcontrol = ViewControlComponent()
		self._viewcontrol.layer = Layer(priority = 4, prev_track_button = self._top_button[0], next_track_button = self._top_button[1])
		self._viewcontrol.set_enabled(False)


	def _setup_transport(self):
		self._transport = TransportComponent(name = 'Transport')
		self._transport.layer = Layer(priority = 4, play_button = self._side_button[0]) #, overdub_button = self._side_button[1])
		self._transport.set_enabled(False)


	def _setup_mixer(self):
		self._mixer = MonoMixerComponent(name = 'Mixer',tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True)
		self._mixer._selected_strip.layer = Layer(priority = 4, volume_control = self._fader)
		self._mixer.solo_mute_record_stop_layer = AddLayerMode(self._mixer, Layer(priority = 4,
																					mute_buttons = self._matrix.submatrix[:, 0],
																					solo_buttons = self._matrix.submatrix[:, 1],
																					arm_buttons = self._matrix.submatrix[:, 2],
																					))
		self._mixer.select_layer = AddLayerMode(self._mixer, Layer(priority = 4, arming_track_select_buttons = self._matrix.submatrix[:, 3]))
		self._mixer.mute_layer = AddLayerMode(self._mixer, Layer(priority = 4, mute_buttons = self._matrix.submatrix[:, 3]))


	def _setup_session(self):
		self._session_ring = SessionRingComponent(name = 'Session_Ring', num_tracks = 4, num_scenes = 4)

		self._session = SessionComponent(name = 'Session', session_ring = self._session_ring, auto_name = True)
		self._session.cliplaunch_layer = AddLayerMode(self._session, Layer(priority = 4, clip_launch_buttons = self._matrix.submatrix[:,:]))
		self._session.stop_layer = AddLayerMode(self._session, Layer(priority = 4, stop_track_clip_buttons = self._matrix.submatrix[:,3]))

		self._session_navigation = SessionNavigationComponent(name = 'Session_Navigation', session_ring = self._session_ring)
		self._session_navigation._horizontal_layer = AddLayerMode(self._session_navigation, Layer(priority = 4, left_button = self._top_button[0], right_button = self._top_button[1]))
		self._session_navigation._vertical_layer = AddLayerMode(self._session_navigation, Layer(priority = 4, up_button = self._top_button[0], down_button = self._top_button[1]))
		self._session_navigation.set_enabled(False)


	def _setup_recorder(self):
		self._recorder = SessionRecordingComponent(view_controller = self._viewcontrol)
		self._recorder.layer = Layer(priority = 4, new_button = self._side_button[2], record_button = self._side_button[1])
		self._recorder.set_enabled(False)


	def _setup_instrument(self):
		self._grid_resolution = GridResolution()

		self._c_instance.playhead.enabled = True
		self._playhead_element = PlayheadElement(self._c_instance.playhead)

		self._drum_group_finder = PercussionInstrumentFinder(device_parent=self.song.view.selected_track)

		self._instrument = MinimMonoInstrumentComponent(name = 'InstrumentComponent', script = self, skin = self._skin, drum_group_finder = self._drum_group_finder, grid_resolution = self._grid_resolution, settings = DEFAULT_INSTRUMENT_SETTINGS, device_provider = self._device_provider, parent_task_group = self._task_group)
		self._instrument._drumpad._drumgroup._button_coordinates_to_pad_index = lambda first_note, coordinates: coordinates[1] + (abs(coordinates[0]-1)*4) + first_note
		self._instrument._drumpad._drumgroup.create_translation_entry = lambda button: (button.coordinate[1], button.coordinate[0]+2, button.identifier, button.channel)

		self._instrument.layer = Layer(priority = 6, shift_button = self._side_button[3])

		self._instrument.keypad_options_layer = AddLayerMode(self._instrument, Layer(priority = 6,
									scale_up_button = self._button[0][3],
									scale_down_button = self._button[0][2],
									offset_up_button = self._button[0][1],
									offset_down_button = self._button[0][0],))
									#vertical_offset_up_button = self._top_button[1],
									#vertical_offset_down_button = self._top_button[0]))
		self._instrument.drumpad_options_layer = AddLayerMode(self._instrument, Layer(priority = 6,
									scale_up_button = self._button[0][3],
									scale_down_button = self._button[0][2],
									drum_offset_up_button = self._button[0][1],
									drum_offset_down_button = self._button[0][0],))

		self._instrument._keypad.main_layer = LayerMode(self._instrument._keypad, Layer(priority = 6, keypad_matrix = self._matrix.submatrix[:,1:3]))
		self._instrument._keypad.select_layer = LayerMode(self._instrument._keypad, Layer(priority = 6, keypad_select_matrix = self._matrix.submatrix[:, 1:3]))

		self._instrument._drumpad.main_layer = LayerMode(self._instrument._drumpad, Layer(priority = 6, drumpad_matrix = self._matrix.submatrix[:,1:3]))
		self._instrument._drumpad.select_layer = LayerMode(self._instrument._drumpad, Layer(priority = 6, drumpad_select_matrix = self._matrix.submatrix[:,1:3]))

		self._instrument._main_modes = ModesComponent(name = 'InstrumentModes')
		self._instrument._main_modes.add_mode('disabled', [])
		self._instrument._main_modes.add_mode('drumpad', [self._instrument._drumpad, self._instrument._drumpad.main_layer, self._instrument.drumpad_options_layer])
		self._instrument._main_modes.add_mode('drumpad_shifted', [self._instrument._drumpad, self._instrument._drumpad.select_layer, self._instrument.drumpad_options_layer])
		self._instrument._main_modes.add_mode('keypad', [self._instrument._keypad, self._instrument._keypad.main_layer, self._instrument.keypad_options_layer])
		self._instrument._main_modes.add_mode('keypad_shifted', [self._instrument._keypad, self._instrument._keypad.select_layer, self._instrument.keypad_options_layer])
		self._instrument.register_component(self._instrument._main_modes)

		self._instrument.set_enabled(False)
		#self._instrument.audioloop_layer = LayerMode(self._instrument, Layer(priority = 6, loop_selector_matrix = self._base_grid))


	def _setup_modes(self):
		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [])
		self._main_modes.add_mode('session_shifted', [self._recorder, self._mixer, self._mixer.solo_mute_record_stop_layer, self._session, self._session.stop_layer, self._session_navigation, self._session_navigation._vertical_layer, self._transport], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Session'))
		self._main_modes.add_mode('session', [self._recorder, self._mixer, self._session, self._session.cliplaunch_layer, self._session_navigation, self._session_navigation._horizontal_layer, self._transport], behaviour = self._shift_latching(color = 'Mode.Session'))
		self._main_modes.add_mode('instrument_shifted', [self._recorder, self._mixer, self._mixer.mute_layer, self._viewcontrol, self._instrument, self._transport], groups = ['shifted'], behaviour = self._shift_latching(color = 'Mode.Instrument'))
		self._main_modes.add_mode('instrument', [self._recorder, self._mixer, self._mixer.select_layer, self._viewcontrol, self._instrument, self._transport], behaviour = self._shift_latching(color = 'Mode.Instrument'))

		self._main_modes.layer = Layer(priority = 6, session_button = self._side_button[4], instrument_button = self._side_button[3])
		self._main_modes.set_enabled(False)
		self._main_modes.selected_mode = 'disabled'


	def _can_auto_arm_track(self, track):
		routing = track.current_input_routing
		return routing == 'Ext: All Ins' or routing == 'All Ins' or routing.startswith('Livid Minim Input')


	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard)
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control


	@listens('device')
	def _on_device_changed(self):
		pass


	def disconnect(self):
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<<< Minim log closed >>>>>>>>>>>>>>>>>>>>>>>>>')
		super(Minim, self).disconnect()


	def handle_sysex(self, midi_bytes):
		#debug('sysex: ', str(midi_bytes))
		#debug('matching:', midi_bytes[1:5], 'to', tuple([0, 1, 97]  + [self._sysex_id]))
		if len(midi_bytes)==9 and midi_bytes[1:5] == tuple([0, 1, 97]  + [self._sysex_id]):
			if not self._connected:
				#debug('connecting from sysex...')
				self._connected = True
				self._initialize_hardware()
				self._initialize_script()




#a
