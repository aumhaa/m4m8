# by amounra 0218 : http://www.aumhaa.com
# written against Live 10.0.5 on 102318


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
from aumhaa.v2.control_surface.mono_modes import SendLividSysexMode, SendSysexMode, CancellableBehaviourWithRelease, ColoredCancellableBehaviourWithRelease, MomentaryBehaviour, BicoloredMomentaryBehaviour, DefaultedBehaviour
from aumhaa.v2.livid import LividControlSurface, LividSettings, LividRGB
from aumhaa.v2.control_surface.components.fixed_length_recorder import FixedLengthSessionRecordingComponent
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

from pushbase.auto_arm_component import AutoArmComponent
from pushbase.grid_resolution import GridResolution
#from pushbase.playhead_element import PlayheadElement
#from pushbase.percussion_instrument_finder import PercussionInstrumentFinder, find_drum_group_device
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



class CntrlrViewControlComponent(ViewControlComponent):


	def __init__(self, *a, **k):
		super(CntrlrViewControlComponent, self).__init__(*a, **k)
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
		self._horizontal_banking.can_scroll_up() and self._horizontal_banking.scroll_up() if value == 127 else self._horizontal_banking.can_scroll_down() and self._horizontal_banking.scroll_down()



"""We need to add an extra mode to the instrument to deal with session shifting, thus the _matrix_modes and extra functions."""
"""We also set up the id's for the note_editor here"""
"""We also make use of a shift_mode instead of the original shift mode included in the MonoInstrument so that we can add a custom behaviour locking behaviour to it"""

class CntrlrMonoInstrumentComponent(MonoInstrumentComponent):


	def __init__(self, *a, **k):
		self._matrix_modes = ModesComponent(name = 'MatrixModes')
		super(CntrlrMonoInstrumentComponent, self).__init__(*a, **k)
		self._keypad._note_sequencer._playhead_component._notes=tuple(range(16,32))
		self._keypad._note_sequencer._playhead_component._triplet_notes=tuple(range(16, 28))
		self._keypad._note_sequencer._note_editor._visible_steps_model = lambda indices: [k for k in indices if k % 16 not in (13, 14, 15, 16)]
		self._drumpad._step_sequencer._playhead_component._notes=tuple(range(16,32))
		self._drumpad._step_sequencer._playhead_component._triplet_notes=tuple(range(16, 28))
		self._drumpad._step_sequencer._note_editor._visible_steps_model = lambda indices: [k for k in indices if k % 16 not in (13, 14, 15, 16)]
		self._matrix_modes.add_mode('disabled', [DelayMode(self.update, delay = .1, parent_task_group = self._parent_task_group)])
		self._matrix_modes.add_mode('enabled', [DelayMode(self.update, delay = .1, parent_task_group = self._parent_task_group)], behaviour = DefaultedBehaviour())
		self._matrix_modes._last_selected_mode = 'enabled'
		self._matrix_modes.selected_mode = 'disabled'

		self.set_session_mode_button = self._matrix_modes.enabled_button.set_control_element



	def _setup_shift_mode(self):
		self._shifted = False
		self._shift_mode = ModesComponent()
		self._shift_mode.add_mode('shift', tuple([lambda: self._on_shift_value(True), lambda: self._on_shift_value(False)]), behaviour = ColoredCancellableBehaviourWithRelease(color = 'MonoInstrument.ShiftOn', off_color = 'MonoInstrument.ShiftOff') if SHIFT_LOCK else BicoloredMomentaryBehaviour(color = 'MonoInstrument.ShiftOn', off_color = 'MonoInstrument.ShiftOff'))
		self._shift_mode.add_mode('disabled', None)
		self._shift_mode.selected_mode = 'disabled'


	def update(self):
		super(MonoInstrumentComponent, self).update()
		self._main_modes.selected_mode = 'disabled'
		if self.is_enabled():
			new_mode = 'disabled'
			drum_device = find_drum_group_device(self.song.view.selected_track)
			self._drumpad._drumgroup.set_drum_group_device(drum_device)
			cur_track = self.song.view.selected_track
			if cur_track.has_audio_input and cur_track in self.song.visible_tracks:
				new_mode = 'audioloop'
				if self._shifted:
					new_mode += '_shifted'
			elif cur_track.has_midi_input:
				scale, mode = self._scale_offset_component.value, self._mode_component.value
				new_mode = get_instrument_type(cur_track, scale, self._settings)
				if mode is 'split':
					new_mode += '_split'
				elif mode is 'seq':
					new_mode +=  '_sequencer'
				if self._shifted:
					new_mode += '_shifted'
				if self._matrix_modes.selected_mode is 'enabled':
					new_mode += '_session'
				self._script.set_feedback_channels([self._scale_offset_component.channel])
				self._script.set_controlled_track(self.song.view.selected_track)
			if new_mode in self._main_modes._mode_map or new_mode is None:
				self._main_modes.selected_mode = new_mode
				self._script.set_controlled_track(self.song.view.selected_track)
			else:
				self._main_modes.selected_mode = 'disabled'
				self._script.set_controlled_track(None)
			debug('monoInstrument mode is:', self._main_modes.selected_mode, '  inst:', self.is_enabled(), '  modes:', self._main_modes.is_enabled(), '   key:', self._keypad.is_enabled(), '   drum:', self._drumpad.is_enabled())



"""We need to override the update notification call in AutoArmComponent"""

class CntrlrAutoArmComponent(AutoArmComponent):


	def _update_notification(self):
		pass



class CntrlrDeviceComponent(DeviceComponent):


	_alt_pressed = False

	def __init__(self, script = None, *a, **k):
		self._script = script
		super(CntrlrDeviceComponent, self).__init__(*a, **k)


	"""
	def _current_bank_details(self):
		#debug('current bank deets...')
		if not self._script.modhandler.active_mod() is None:
			if self._script.modhandler.active_mod() and hasattr(self._script.modhandler.active_mod(), '_param_component') and self._script.modhandler.active_mod()._param_component._device_parent != None:
				bank_name = self._script.modhandler.active_mod()._param_component._bank_name
				bank = [param._parameter for param in self._script.modhandler.active_mod()._param_component._params]
				if self._script.modhandler._alt_value.subject and self._script.modhandler._alt_value.subject.is_pressed():
					bank = bank[8:]
				return (bank_name, bank)
			else:
				return DeviceComponent._current_bank_details(self)
		else:
			return DeviceComponent._current_bank_details(self)

	"""


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
			self._setup_autoarm()
			self._setup_session_control()
			self._setup_mixer_control()
			self._setup_transport_control()
			self._setup_device_control()
			self._setup_device_selector()
			self._setup_session_recording_component()
			self._setup_viewcontrol()
			self._setup_instrument()
			self._setup_mod()
			self._setup_modswitcher()
			self._setup_modes()
			self._setup_m4l_interface()
			self._on_device_changed.subject = self.song
			self.set_feedback_channels(list(range(14, 15)))


	def _initialize_script(self):
		super(Cntrlr, self)._initialize_script()
		self._connected = True
		self._main_modes.selected_mode = 'MixMode'
		self._main_modes.set_enabled(True)
		self._instrument.set_enabled(True)
		self._main_modes.selected_mode = 'disabled'
		self._main_modes.selected_mode = 'MixMode'
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

		self._translated_controls = self._fader + self._knobs + self._encoder[4:] + self._grid + self._button


	def _setup_background(self):
		self._background = BackgroundComponent(name = 'Background')
		self._background.layer = Layer(priority = 5, matrix = self._matrix.submatrix[:,:], faders = self._fader_matrix.submatrix[:,:], left_knobs = self._knob_left_matrix.submatrix[:,:], right_knobs = self._knob_right_matrix.submatrix[:,:], dials = self._dial_matrix, dial_buttons = self._dial_button_matrix.submatrix[:,:], keys = self._key_matrix.submatrix[:,:])
		self._background.set_enabled(True)


	def _define_sysex(self):
		self.encoder_navigation_on = SendLividSysexMode(livid_settings = self._livid_settings, call = 'set_encoder_encosion_mode', message = [13, 0, 0, 0])


	def _setup_transport_control(self):
		self._transport = TransportComponent(name = 'Transport')
		if hasattr(self._transport, '_play_toggle'):
			self._transport._play_toggle.view_transform = lambda value: 'Transport.PlayOn' if value else 'Transport.PlayOff'
		if hasattr(self._transport, '_record_toggle'):
			self._transport._record_toggle.view_transform = lambda value: 'Transport.RecordOn' if value else 'Transport.RecordOff'
		self._transport.layer = Layer(priority = 5,
									play_button = self._button[28],
									record_button = self._button[29])
		self._transport.set_enabled(False)


	def _setup_autoarm(self):
		self._auto_arm = CntrlrAutoArmComponent(name='Auto_Arm')
		#self._auto_arm._update_notification = lambda a: None
		self._auto_arm.can_auto_arm_track = self._can_auto_arm_track


	def _setup_session_recording_component(self):
		self._clip_creator = ClipCreator()
		self._clip_creator.name = 'ClipCreator'
		self._recorder = FixedLengthSessionRecordingComponent(clip_creator = self._clip_creator, view_controller = ViewControlComponent(), name = 'SessionRecorder') # is_enabled = False)
		self._recorder.main_layer = AddLayerMode(self._recorder, Layer(priority = 5, record_button = self._button[29]))
		self._recorder.shift_layer = AddLayerMode(self._recorder, Layer(priority = 5, automation_button = self._button[29]))
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

		self._session_navigation.bank_dial_layer = AddLayerMode(self._session_navigation, Layer(priority = 5,
									track_bank_dial = self._encoder[3],
									scene_bank_dial = self._encoder[2],))
		self._session_navigation.nav_dial_layer = AddLayerMode(self._session_navigation, Layer(priority = 5,
									scene_nav_dial = self._encoder[2],
									track_nav_dial = self._encoder[3],))
		self._session_navigation.select_dial_layer = AddLayerMode(self._session_navigation, Layer(priority = 5))
		"""self._session_navigation.nav_layer = AddLayerMode(self._session_navigation, Layer(priority = 5,
									page_down_button = self._button[14],
									page_up_button = self._button[15],
									page_left_button = self._button[12],
									page_right_button = self._button[13]))"""
		self._session_navigation.nav_layer = AddLayerMode(self._session_navigation, Layer(priority = 5))

		self._session_navigation.set_enabled(False)

		self._session = SessionComponent(session_ring = self._session_ring, auto_name = True)
		hasattr(self._session, '_enable_skinning') and self._session._enable_skinning()
		self._session.clip_launch_layer = LayerMode(self._session, Layer(priority = 5,
									clip_launch_buttons = self._matrix.submatrix[:,:]))
		self._session.scene_launch_layer = AddLayerMode(self._session._selected_scene, Layer(priority = 5,
									launch_button = self._button[28],))
		self._session.set_enabled(False)

		self._session_zoom = SessionOverviewComponent(name = 'SessionZoom', session_ring = self._session_ring, enable_skinning = True)
		self._session_zoom.layer = Layer(priority = 5, button_matrix = self._matrix.submatrix[:,:])
		self._session_zoom.set_enabled(False)


	def _setup_mixer_control(self):
		self._mixer = MonoMixerComponent(name = 'Mixer', num_returns = 2,tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True, channel_strip_component_type = MonoChannelStripComponent)

		if FREE_ENCODER_IS_CROSSFADER:
			self._mixer.layer = Layer(priority = 5, crossfader_control = self._encoder[1])
		self._mixer.main_faders_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											volume_controls = self._fader_matrix.submatrix[:4, :],
											return_controls = self._fader_matrix.submatrix[4:6, :],
											prehear_volume_control = self._fader[6],))
		self._mixer.main_buttons_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											mute_buttons = self._key_matrix.submatrix[8:12, 1:],
											stop_clip_buttons = self._key_matrix.submatrix[4:8, 1:],
											arming_track_select_buttons = self._key_matrix.submatrix[:4, 1:],))
		self._mixer.solo_buttons_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											solo_buttons = self._key_matrix.submatrix[8:12, 1:],))
		self._mixer.shifted_buttons_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											track_select_buttons = self._key_matrix.submatrix[:4, 1:],
											stop_clip_buttons = self._key_matrix.submatrix[4:8, 1:],
											solo_buttons = self._key_matrix.submatrix[8:12, 1:],))
		self._mixer.stop_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											stop_clip_buttons = self._key_matrix.submatrix[8:12, 1:],))
		if EQS_INSTEAD_OF_MACROS:
			self._mixer.main_knobs_layer = AddLayerMode(self._mixer, Layer(priority = 5,
												send_controls = self._knob_left_matrix,
												eq_gain_controls = self._knob_right_matrix))
		else:
			self._mixer.main_knobs_layer = AddLayerMode(self._mixer, Layer(priority = 5,
												send_controls = self._knob_left_matrix,
												parameter_controls = self._knob_right_matrix))
		#self._mixer.main_knobs_layer = AddLayerMode(self._mixer, Layer(priority = 5))
		self._mixer.master_fader_layer = AddLayerMode(self._mixer.master_strip(), Layer(priority = 5,
											volume_control = self._fader[7]))
		self._mixer.instrument_buttons_layer = AddLayerMode(self._mixer, Layer(priority = 5,
											mute_buttons = self._key_matrix.submatrix[:4, 1:],
											track_select_buttons = self._key_matrix.submatrix[4:8, 1:],))
		self._mixer.set_enabled(False)


	def _setup_device_control(self):
		self._device_selection_follows_track_selection = FOLLOW
		self._device = CntrlrDeviceComponent(script = self, name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())
		#self._device.layer = Layer(priority = 5, parameter_controls = self._dial_matrix.submatrix[:, 1:],
		#										on_off_button = self._encoder_button[4],
		#										bank_prev_button = self._encoder_button[6],
		#										bank_next_button = self._encoder_button[7],)
		#										#lock_button = self._encoder_button[5],
		self._device.dial_layer = AddLayerMode(self._device, Layer(priority = 5,
													parameter_controls = self._dial_matrix.submatrix[:, 1:],))
		self._device.button_layer = AddLayerMode(self._device, Layer(priority = 5,
													on_off_button = self._encoder_button[4],
													bank_prev_button = self._encoder_button[6],
													bank_next_button = self._encoder_button[7],))
		self._device.set_enabled(False)

		self._device_navigator = DeviceNavigator(self._device_provider, self._mixer, self)
		self._device_navigator.name = 'Device_Navigator'
		self._device_navigator.select_dial_layer = AddLayerMode(self._device_navigator, Layer(priority = 5, device_select_dial = self._encoder[0],))
		self._device_navigator.main_layer = AddLayerMode(self._device_navigator, Layer(priority = 5,
											prev_chain_button = self._encoder_button[8],
											next_chain_button = self._encoder_button[9],
											exit_button = self._encoder_button[10],
											enter_button = self._encoder_button[11],))
		self._device_navigator.set_enabled(False)


	def _setup_device_selector(self):
		self._device_selector = DeviceSelectorComponent(self)
		self._device_selector.name = 'Device_Selector'
		#self._device_selector.select_layer = AddLayerMode(self._device_selector, Layer(priority = 6 , matrix = self._matrix.submatrix[:, :]))
		self._device_selector.select_layer = AddLayerMode(self._device_selector, Layer(priority = 6, matrix = ButtonMatrixElement(rows = [self._grid[:4],self._grid[4:8],self._grid[8:12],self._grid[12:14]])))
		self._device_selector.assign_layer = AddLayerMode(self._device_selector, Layer(priority = 7, assign_button = self._grid[14]))
		self._device_selector.set_enabled(False)


	def _setup_translations(self):
		self._translations = TranslationComponent(self._translated_controls, user_channel_offset = 4, channel = 4)	# is_enabled = False)
		self._translations.name = 'TranslationComponent'
		self._translations.layer = Layer(priority = 10,)
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
		self.modhandler.layer = Layer(priority = 8, cntrlr_encoder_grid = self._dial_matrix.submatrix[:, 1:3],
										cntrlr_encoder_button_grid = self._dial_button_matrix.submatrix[:,:],
										cntrlr_grid = self._matrix.submatrix[:,:],
										cntrlr_keys = self._key_matrix.submatrix[:,:],)
										#parameter_controls = self._dial_matrix.submatrix[:,:])
		self.modhandler.set_enabled(False)
		self._modHandle = ModControl(modscript = self, monomodular = self.monomodular, name = 'ModHandle')


	def _setup_instrument(self):
		self._grid_resolution = self.register_disconnectable(GridResolution())
		self._c_instance.playhead.enabled = True
		self._playhead_element = PlayheadElement(self._c_instance.playhead)

		self._drum_group_finder = PercussionInstrumentFinder(device_parent=self.song.view.selected_track)

		self._instrument = CntrlrMonoInstrumentComponent(name = 'InstrumentComponent', is_enabled = True, script = self, skin = self._skin, grid_resolution = self._grid_resolution, drum_group_finder = self._drum_group_finder, parent_task_group = self._task_group, settings = DEFAULT_INSTRUMENT_SETTINGS, device_provider = self._device_provider)
		self._instrument.shift_button_layer = AddLayerMode(self._instrument, Layer(priority = 5, session_mode_button = self._button[30], shift_mode_button = self._button[31]))
		self._instrument.audioloop_layer = AddLayerMode(self._instrument, Layer(priority = 5, loop_selector_matrix = self._key_matrix.submatrix[:, 0]))

		self._instrument.keypad_shift_layer = AddLayerMode(self._instrument, Layer(priority = 5,
									scale_up_button = self._button[13],
									scale_down_button = self._button[12],
									offset_up_button = self._button[11],
									offset_down_button = self._button[10],
									vertical_offset_up_button = self._button[9],
									vertical_offset_down_button = self._button[8],
									split_button = self._button[14],
									sequencer_button = self._button[15]))

		self._instrument.drumpad_shift_layer = AddLayerMode(self._instrument, Layer(priority = 5,
									scale_up_button = self._button[13],
									scale_down_button = self._button[12],
									drum_offset_up_button = self._button[11],
									drum_offset_down_button = self._button[10],
									drumpad_mute_button = self._button[9],
									drumpad_solo_button = self._button[8],
									split_button = self._button[14],
									sequencer_button = self._button[15]))

		self._instrument._keypad.sequencer_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										playhead = self._playhead_element,
		 																								keypad_matrix = self._matrix.submatrix[:,:],
																										sequencer_matrix = self._key_matrix.submatrix[:,0]))
		self._instrument._keypad.split_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										keypad_matrix = self._matrix.submatrix[:,:],
																										split_matrix = self._key_matrix.submatrix[:14,0]))
		self._instrument._keypad.sequencer_shift_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										keypad_select_matrix = self._matrix.submatrix[:,:],
																										loop_selector_matrix = self._key_matrix.submatrix[:8, 0],
																										quantization_buttons = self._key_matrix.submatrix[:8, 1],))
																										#follow_button = self._button[23]))
		self._instrument._keypad.sequencer_session_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										playhead = self._playhead_element,
																										sequencer_matrix = self._key_matrix.submatrix[:,:1]))
		self._instrument._keypad.split_session_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										split_matrix = self._key_matrix.submatrix[:16,:1]))
		self._instrument._keypad.sequencer_session_shift_layer = LayerMode(self._instrument._keypad, Layer(priority = 5,
																										loop_selector_matrix = self._key_matrix.submatrix[:8, :1],
																										quantization_buttons = self._key_matrix.submatrix[:7, 1:],))
																										#follow_button = self._button[23]))

		self._instrument._drumpad.sequencer_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										playhead = self._playhead_element,
																										drumpad_matrix = self._matrix.submatrix[:,:],
																										sequencer_matrix = self._key_matrix.submatrix[:,0]))
		self._instrument._drumpad.split_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										drumpad_matrix = self._matrix.submatrix[:,:],
																										split_matrix = self._key_matrix.submatrix[:16,:1]))
		self._instrument._drumpad.sequencer_shift_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										drumpad_select_matrix = self._matrix.submatrix[:,:],
																										loop_selector_matrix = self._key_matrix.submatrix[:8, :1],
																										quantization_buttons = self._key_matrix.submatrix[:7, 1:],))
																										#follow_button = self._button[23]))
		self._instrument._drumpad.sequencer_session_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										playhead = self._playhead_element,
																										sequencer_matrix = self._key_matrix.submatrix[:,:1]))
		self._instrument._drumpad.split_session_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										split_matrix = self._key_matrix.submatrix[:16,:1]))
		self._instrument._drumpad.sequencer_session_shift_layer = LayerMode(self._instrument._drumpad, Layer(priority = 5,
																										loop_selector_matrix = self._key_matrix.submatrix[:8, :1],
																										quantization_buttons = self._key_matrix.submatrix[:8, 1:],))
																										#follow_button = self._button[23]))

		#self._instrument.set_session_mode_button(self._button[30])


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

		common = CompoundMode(self._mixer,
									self._session_ring)
		main_buttons=CompoundMode(self._mixer.main_buttons_layer,
									self._transport,
									self._recorder,
									self._recorder.main_layer,
									self._device,
									self._device.button_layer)
		shifted_main_buttons=CompoundMode(self._mixer.solo_buttons_layer,
									self._recorder,
									self._recorder.shift_layer,
									self._session,
									self._session.scene_launch_layer,
									self._device,
									self._device.button_layer)
		main_faders=CompoundMode(self._mixer.main_faders_layer,
									self._mixer.master_fader_layer)
		main_dials=CompoundMode(self._view_control,
									self._view_control.main_layer,
									self._device,
									self._device.dial_layer,
									self._device_navigator.select_dial_layer,
									self.encoder_navigation_on)
		shifted_dials=CompoundMode(self._session_navigation,
									self._session_navigation.nav_dial_layer,
									self._device,
									self._device.dial_layer,
									self._device_navigator.select_dial_layer,
									self.encoder_navigation_on)

		self._modalt_mode = ModesComponent(name = 'ModAltMode')
		self._modalt_mode.add_mode('disabled', None)
		self._modalt_mode.add_mode('enabled', [tuple([self._enable_mod_alt, self._disable_mod_alt])], behaviour = CancellableBehaviourWithRelease(), cycle_mode_button_color = 'Mod.AltOn')
		self._modalt_mode.selected_mode = 'disabled'
		self._modalt_mode.set_enabled(False)
		self._modalt_mode.layer = Layer(priority = 5, enabled_button = self._encoder_button[1])

		self._modswitcher = ModesComponent(name = 'ModSwitcher')
		self._modswitcher.add_mode('mod', [self.modhandler, self._modalt_mode, main_faders, self._mixer.main_knobs_layer, self._device, self._device.dial_layer, self._device_navigator.main_layer,	main_dials, DelayMode(self.modhandler.update, delay = .5, parent_task_group = self._task_group)])
		self._modswitcher.add_mode('instrument', [self._instrument, self._instrument.shift_button_layer, main_buttons, main_faders, self._mixer.main_knobs_layer, self._device, self._device.dial_layer, self._device.button_layer, self._device_navigator.main_layer,]) #self._instrument.shift_button_layer, self._optional_translations])
		self._modswitcher.selected_mode = 'instrument'
		self._modswitcher.set_enabled(False)

		self._instrument._main_modes = ModesComponent(parent = self._instrument, name = 'InstrumentModes')
		self._instrument._main_modes.add_mode('disabled', [main_buttons, main_dials, self._session, self._session, self._session.clip_launch_layer])
		self._instrument._main_modes.add_mode('drumpad', [self._instrument._drumpad.sequencer_layer,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_split', [self._instrument._drumpad.split_layer,
																					self._instrument._selected_session,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_sequencer', [self._instrument._drumpad.sequencer_layer,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_shifted', [self._instrument._drumpad.sequencer_shift_layer,
																					self._instrument.drumpad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('drumpad_split_shifted', [self._instrument._drumpad.split_layer,
																					self._instrument.drumpad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('drumpad_sequencer_shifted', [self._instrument._drumpad.sequencer_shift_layer,
																					self._instrument.drumpad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad', [self._instrument._keypad.sequencer_layer,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_split', [self._instrument._keypad.split_layer,
																					self._instrument._selected_session,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_sequencer', [self._instrument._keypad.sequencer_layer,
																					main_buttons,
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_shifted', [self._instrument._keypad.sequencer_shift_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad_split_shifted', [self._instrument._keypad.split_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad_sequencer_shifted', [self._instrument._keypad.sequencer_shift_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					shifted_dials])
		self._instrument._main_modes.add_mode('drumpad_session', [self._instrument._drumpad.sequencer_session_layer,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_split_session', [self._instrument._drumpad.split_session_layer,
																					self._instrument._selected_session,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_sequencer_session', [self._instrument._drumpad.sequencer_session_layer,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('drumpad_shifted_session', [self._instrument._drumpad.sequencer_session_shift_layer,
																					self._instrument.drumpad_shift_layer,
																					main_buttons,
																					self._session_zoom,
																					shifted_dials])
		self._instrument._main_modes.add_mode('drumpad_split_shifted_session', [self._instrument._drumpad.split_session_layer,
																					self._instrument.drumpad_shift_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])
		self._instrument._main_modes.add_mode('drumpad_sequencer_shifted_session', [self._instrument._drumpad.sequencer_session_shift_layer,
																					self._instrument.drumpad_shift_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad_session', [self._instrument._keypad.sequencer_session_layer,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_split_session', [self._instrument._keypad.split_session_layer,
																					self._instrument._selected_session,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_sequencer_session', [self._instrument._keypad.sequencer_session_layer,
																					main_buttons,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1),
																					main_dials])
		self._instrument._main_modes.add_mode('keypad_shifted_session', [self._instrument._keypad.sequencer_session_shift_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad_split_shifted_session', [self._instrument._keypad.split_session_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])
		self._instrument._main_modes.add_mode('keypad_sequencer_shifted_session', [self._instrument._keypad.sequencer_session_shift_layer,
																					self._instrument.keypad_shift_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])

		self._instrument._main_modes.add_mode('audioloop', [self._instrument.audioloop_layer,
																					main_buttons,
																					main_dials,
																					self._session,
																					DelayMode(self._session.clip_launch_layer, delay = .1)])
		self._instrument._main_modes.add_mode('audioloop_shifted', [self._instrument.audioloop_layer,
																					shifted_main_buttons,
																					self._session_zoom,
																					shifted_dials])
		#self._instrument._main_modes.add_mode('audioloop_shifted_session', [self._instrument.audioloop_layer, self._session, shifted_main_buttons, main_dials, shifted_dials])
		#self._instrument.register_component(self._instrument._main_modes)
		self._instrument._main_modes.selected_mode = 'disabled'
		self._instrument.set_enabled(True)

		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [self._background])
		self._main_modes.add_mode('MixMode', [common,
													self._instrument,
													self._instrument.shift_button_layer,
													self._mixer,
													main_faders,
													self._mixer.main_knobs_layer,
													self._device,
													self._device_navigator,
													self._device_navigator.main_layer,])
		self._main_modes.add_mode('ModSwitcher', [common,
													main_faders,
													main_dials,
													self._mixer.main_knobs_layer,
													self._session_navigation.select_dial_layer,
													self._view_control,
													self._view_control.main_layer,
													self._device_navigator.select_dial_layer,
													self.encoder_navigation_on, self._modswitcher,
													DelayMode(self._update_modswitcher, delay = .1)],
													behaviour = ColoredCancellableBehaviourWithRelease(color = 'ModeButtons.ModSwitcher', off_color = 'ModeButtons.ModSwitcherDisabled'))
		self._main_modes.add_mode('Translations', [common,
													main_faders,
													main_dials,
													self._mixer.main_knobs_layer,
													DelayMode(self._translations, delay = .1),
													DelayMode(self._translations.selector_layer, delay = .3)],
													behaviour = DefaultedBehaviour(default_mode = 'MixMode', color = 'ModeButtons.Translations', off_color = 'ModeButtons.TranslationsDisabled'))
		self._main_modes.add_mode('DeviceSelector', [common,
													self._device_selector,
													DelayMode(self._device_selector.select_layer, delay = .1),
													DelayMode(self.modhandler.lock_layer, delay = .1),
													DelayMode(self._device_selector.assign_layer, delay = .5),
													main_buttons,
													main_dials,
													main_faders,
													self._mixer.main_knobs_layer,
													self._device,
													self._device_navigator],
													behaviour = ColoredCancellableBehaviourWithRelease(color = 'ModeButtons.DeviceSelector', off_color = 'ModeButtons.DeviceSelectorDisabled'))
		self._main_modes.layer = Layer(priority = 5, ModSwitcher_button = self._encoder_button[2], DeviceSelector_button = self._encoder_button[0], Translations_button = self._encoder_button[3]) #,
		self._main_modes.selected_mode = 'disabled'
		self._main_modes.set_enabled(True)

		#self._test.subject = self._instrument._main_modes



	@listens('selected_mode')
	def _test(self, *a):
		comps = [self._main_modes, self._modswitcher, self._instrument, self._instrument._main_modes,  self._instrument._matrix_modes, self._instrument._selected_session, self._session,  self._device, self._mixer, self._session_navigation, self._session_zoom, self._recorder, self._transport]
		debug('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
		debug('main mode:', self._main_modes.selected_mode)
		debug('instrument mode:', self._instrument._main_modes.selected_mode)
		debug('modswitcher mode:', self._modswitcher.selected_mode)
		debug('instrument matrix mode:', self._instrument._matrix_modes.selected_mode)
		for comp in comps:
			debug(comp.name, 'is enabled:', comp.is_enabled())
		debug('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')


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
		self._main_modes.selected_mode is 'ModSwitcher' and self._update_modswitcher()


	def _on_selected_track_changed(self):
		super(Cntrlr, self)._on_selected_track_changed()
		self._drum_group_finder.device_parent = self.song.veiw.selected_track
		if not len(self.song.view.selected_track.devices):
			self._main_modes.selected_mode is 'ModSwitcher' and self._update_modswitcher()


	def _update_modswitcher(self):
		debug('update modswitcher', self.modhandler.active_mod())
		if self.modhandler.active_mod():
			self._modswitcher.selected_mode = 'mod'
		else:
			self._modswitcher.selected_mode = 'instrument'
			#self._instrument.update()


	def _enable_mod_alt(self):
		debug('mod alt enabled!')
		if self.modhandler.is_enabled():
			self.modhandler._alt_value(1)
			self._update_mod_alt_button()


	def _disable_mod_alt(self):
		debug('mod alt disabled!')
		if self.modhandler.is_enabled():
			self.modhandler._alt_value(0)
			self._update_mod_alt_button()


	def _update_mod_alt_button(self):
		self.modhandler.is_alted() and self._encoder_button[1].set_light('Mod.AltOn') or self._encoder_button[1].set_light('Mod.AltOff')


	def reset_controlled_track(self, track = None, *a):
		if not track:
			track = self.song.view.selected_track
		self.set_controlled_track(track)


	def set_controlled_track(self, track = None, *a):
		if isinstance(track, Live.Track.Track):
			super(Cntrlr, self).set_controlled_track(track)
		else:
			self.release_controlled_track()


	def update_display(self):
		super(Cntrlr, self).update_display()
		self.modhandler.send_ring_leds()


	def restart_monomodular(self):
		#debug('restart monomodular')
		self.modhandler.disconnect()
		with self.component_guard():
			self._setup_mod()


	def _get_num_tracks(self):
		return self.num_tracks



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
		#self._device = DeviceComponent(name = 'Mod_Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())




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
