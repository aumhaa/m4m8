# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.3b8 RC on 083018


from __future__ import absolute_import, print_function
import Live
import math

from ableton.v2.base import inject, listens
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry
from ableton.v2.control_surface.elements import ButtonMatrixElement
from ableton.v2.control_surface.components import SessionRingComponent, SessionNavigationComponent, SessionComponent, TransportComponent, DeviceComponent, ViewControlComponent
from ableton.v2.control_surface.components.mixer import SimpleTrackAssigner

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import SendLividSysexMode
from aumhaa.v2.control_surface.elements import MonoEncoderElement, MonoBridgeElement
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import DeviceNavigator, MonoMixerComponent
from aumhaa.v2.livid import LividControlSurface, LividRGB
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent
from .Map import *

debug = initialize_debug()

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224


class GuitarWing(LividControlSurface):


	_sysex_id = 20
	_model_name = 'GuitarWing'

	def __init__(self, *a, **k):
		super(GuitarWing, self).__init__(*a, **k)
		self._skin = Skin(GuitarWingColors)
		with self.component_guard():
			self._setup_controls()
			self._setup_m4l_interface()
			self._setup_session_control()
			self._setup_mixer_control()
			self._setup_device_control()
			self._setup_transport_control()
			self._setup_view_control()


	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		self._button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = BUTTONS[index], name = 'Button_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(10)]
		self._fader = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = SLIDERS[index], name = 'Fader_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(3)]
		self._fader_button = [MonoEncoderElement(msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = SLIDERS[index], name = 'Fader_Button_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(3)]
		self._ccs = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CCS[index], name = 'CCs_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(4)]
		self._pad =  [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = PADS[index], name = 'Pad_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(5)]
		self._padCC = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = PADS[index], name = 'PadCC_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(5)]
		self._accel = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = ACCELS[index], name = 'Accel_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(3)]

		self._parameter_control_matrix = ButtonMatrixElement(rows = [ [ self._fader[0], self._fader[1], self._fader[2], self._accel[2], self._ccs[0], self._ccs[1], self._ccs[2], self._ccs[3] ]])
		self._scene_launch_matrix = ButtonMatrixElement(rows = [self._pad[:4]])


	def _setup_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks = 1, num_scenes = 4, tracks_to_use = lambda : self.song.visible_tracks + self.song.return_tracks)
		self._session_ring.set_enabled(False)

		self._session = SessionComponent(session_ring = self._session_ring, auto_name = True)
		hasattr(self._session, '_enable_skinning') and self._session._enable_skinning()
		self._session.layer = Layer(scene_launch_buttons = self._scene_launch_matrix)

		self._session_navigation =SessionNavigationComponent(name = 'SessionNavigation', session_ring = self._session_ring)

		self._session_navigation._horizontal_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_down_button.color = 'Session.NavigationButtonOn'

		self._session_navigation.layer = Layer(left_button = self._button[1], right_button = self._button[0])
		self._session_navigation.set_enabled(True)


	def _setup_mixer_control(self):
		self._mixer = MonoMixerComponent(name = 'Mixer', tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True)
		self.song.view.selected_track = self._mixer.channel_strip(0)._track


	def _setup_transport_control(self):
		self._transport = TransportComponent()
		self._transport.layer = Layer(play_button = self._button[6],
										loop_button = self._button[7],
										seek_backward_button = self._button[8],
										record_button = self._button[9])
		self._transport.set_enabled(True)


	def _setup_device_control(self):
		self._device = DeviceComponent(name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())
		self._device.layer = Layer(parameter_controls = self._parameter_control_matrix)
		self._device.set_enabled(True)


	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard)
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control


	def _setup_view_control(self):
		self._view_control = ViewControlComponent()
		self._view_control.layer = Layer(prev_track_button = self._button[1], next_track_button = self._button[0])


#	a
