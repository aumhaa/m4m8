# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.3b8 RC on 083018



import Live
import math

from ableton.v2.base import inject, listens
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry
from ableton.v2.control_surface.elements import ButtonMatrixElement
from ableton.v2.control_surface.components import SessionRingComponent
from ableton.v2.control_surface.components.mixer import SimpleTrackAssigner
from ableton.v2.control_surface.mode import AddLayerMode, ModesComponent, DelayMode, CompoundMode

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import SendLividSysexMode
from aumhaa.v2.control_surface.elements import MonoEncoderElement, MonoBridgeElement
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import DeviceNavigator, MonoMixerComponent
from aumhaa.v2.livid import LividControlSurface, LividRGB
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent
from .Map import *

debug = initialize_debug()

class Alias(LividControlSurface):


	_sysex_id = 11
	_model_name = 'Alias'
	_color_type = 'OhmRGB'

	def __init__(self, c_instance):
		super(Alias, self).__init__(c_instance)
		self._skin = Skin(AliasColors)
		with self.component_guard():
			self._setup_controls()
			self._setup_m4l_interface()
			self._setup_session_control()
			self._setup_mixer_control()
			self._setup_mixer_nav()


	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		self._fader = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = ALIAS_FADERS[index], name = 'Fader_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(9)]
		self._button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = ALIAS_BUTTONS[index], name = 'Button_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge) for index in range(16)]
		self._dial = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = ALIAS_DIALS[index], name = 'Dial_' + str(index), num = index + 8, script = self) for index in range(16)]
		self._encoder = MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = ALIAS_ENCODER, name = 'Encoder', script = self, optimized_send_midi = optimized, resource_type = resource, monobridge = self._monobridge)
		self._fader_matrix = ButtonMatrixElement(name = 'FaderMatrix', rows = [self._fader[:8]])
		self._button_matrix = ButtonMatrixElement(name = 'ButtonMatrix', rows = [self._button[:8], self._button[8:]])
		self._dial_matrix = ButtonMatrixElement(name = 'DialMatrix', rows = [self._dial[:8], self._dial[8:]])


	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard)
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control


	def _setup_mixer_control(self):
		self._mixer = MonoMixerComponent(name = 'Mixer', tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True)
		self._mixer.layer = Layer(volume_controls = self._fader_matrix,
									send_controls = self._dial_matrix,
									mute_buttons = self._button_matrix.submatrix[:,0],
									arm_buttons = self._button_matrix.submatrix[:,1])
		self._mixer.master_strip().layer = Layer(volume_control = self._fader[8])
		self._mixer.set_enabled(True)
		self.song.view.selected_track = self._mixer.channel_strip(0)._track


	def _setup_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks = 8, num_scenes = 1, tracks_to_use = lambda : self.song.visible_tracks + self.song.return_tracks)
		self._session_ring.set_enabled(True)


	def _setup_mixer_nav(self):
		self._nav_change.subject = self._encoder


	@listens('value')
	def _nav_change(self, value):
		self._session_ring.set_offsets(int((float(value)/float(127))*max(8, len(self._session_ring.tracks_to_use())-8)), self._session_ring.scene_offset)



#	a
