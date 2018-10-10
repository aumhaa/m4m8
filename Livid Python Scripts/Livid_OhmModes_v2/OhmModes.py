# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.4 100918

from __future__ import absolute_import, print_function
import Live
import math
import sys
from re import *
from itertools import imap, chain, starmap, izip, izip_longest

from ableton.v2.base import inject, listens, listens_group
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry
from ableton.v2.control_surface.elements import EncoderElement, ButtonMatrixElement, DoublePressElement, MultiElement, DisplayDataSource, SysexElement
from ableton.v2.control_surface.components import DrumGroupComponent, SessionOverviewComponent, ClipSlotComponent, SceneComponent, SessionComponent, TransportComponent, BackgroundComponent, ViewControlComponent, SessionRingComponent, SessionRecordingComponent, SessionNavigationComponent, MixerComponent, PlayableComponent
from ableton.v2.control_surface.components.mixer import SimpleTrackAssigner
from ableton.v2.control_surface.mode import AddLayerMode, ModesComponent, DelayMode
from ableton.v2.control_surface.elements.physical_display import PhysicalDisplayElement
from ableton.v2.control_surface.components.session_recording import *

from ableton.v2.control_surface.control import PlayableControl, ButtonControl, control_matrix

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import SendLividSysexMode, MomentaryBehaviour, ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour, ShiftedBehaviour, LatchingShiftedBehaviour, FlashingBehaviour, DefaultedBehaviour, CancellableBehaviourWithRelease
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.elements import MonoEncoderElement, MonoBridgeElement, generate_strip_string
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import MonoKeyGroupComponent, MonoDrumGroupComponent, MonoDeviceComponent, DeviceNavigator, TranslationComponent, MonoMixerComponent
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.components.mono_instrument import *
from aumhaa.v2.livid import LividControlSurface, LividSettings, LividRGB
from aumhaa.v2.control_surface.components.fixed_length_recorder import FixedLengthSessionRecordingComponent
from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent
from .Map import *

debug = initialize_debug()

TEMPO_TOP = 200.0
TEMPO_BOTTOM = 60.0
MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224

SCALES = ['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian', 'major']


class OhmMixerComponent(MonoMixerComponent):


	#overriding to accomodate only having 4 of our 7 channelstrips assigned send controls
	def set_send_controls(self, controls):
		self._send_controls = controls
		if controls:
			for index in range(min(len(self._channel_strips), controls.width())):
				send_controls = [controls.get_button(row, index) for row in range(controls.height())]
				if self.send_index > controls.height():
					send_controls = send_controls + [None for _ in range(self.send_index - controls.height)]
				self._channel_strips[index].set_send_controls(send_controls)
		else:
			for strip in self._channel_strips:
				if self.send_index is None:
					strip.set_send_controls([None])
				else:
					strip.set_send_controls([None for _ in range(self.send_index)])


	def set_instrument_send_controls(self, controls):
		self._send_controls = controls
		if controls:
			for strip, control in izip(self._channel_strips, controls or []):
				strip.set_send_controls([control])
		else:
			for strip in self._channel_strips:
				if self.send_index is None:
					strip.set_send_controls([None])
				else:
					strip.set_send_controls([None for _ in range(self.send_index)])


	def set_eq_gain_controls(self, controls):
		self._eq_controls = controls
		if controls:
			for index in range(min(len(self._channel_strips), controls.width())):
				eq_controls = [controls.get_button(row, index) for row in range(controls.height())]
				self._channel_strips[index].set_eq_gain_controls(eq_controls)
		else:
			for strip in self._channel_strips:
				strip.set_eq_gain_controls(None)


	#sorry, too tired to think of a good way to do this
	def set_pan_controls(self, controls):
		for strip, control in izip(self._channel_strips, controls or []):
			#debug('strip is:', strip, 'control is:', control)
			strip.set_pan_control(control)


	def set_end_pan_controls(self, controls):
		for strip, control in izip(self._channel_strips[4:], controls or []):
			#debug('strip is:', strip, 'control is:', control)
			strip.set_pan_control(control)



class OhmSessionComponent(SessionComponent):


	def set_clip_launch_buttons(self, buttons):
		#assert(not buttons or buttons.width() == self._session_ring.num_tracks and buttons.height() == self._session_ring.num_scenes)
		if buttons:
			for button, (x, y) in buttons.iterbuttons():
				#debug('clip:', button, x, y)
				scene = self.scene(y)
				slot = scene.clip_slot(x)
				slot.set_launch_button(button)

		else:
			for x, y in product(xrange(self._session_ring.num_tracks), xrange(self._session_ring.num_scenes)):
				scene = self.scene(y)
				slot = scene.clip_slot(x)
				slot.set_launch_button(None)


	def set_scene_launch_buttons(self, buttons):
		#assert(buttons or buttons.width() == self._session_ring.num_scenes and buttons.height() == 1)
		if buttons:
			for button, (x, y) in buttons.iterbuttons():
				#debug('scene:', button, x, y)
				scene = self.scene(y)
				scene.set_launch_button(button)
				button.set_light('Session.Scene')

		else:
			for x in xrange(self._session_ring.num_scenes):
				scene = self.scene(x)
				scene.set_launch_button(None)



class OhmDeviceComponent(DeviceComponent):


	_alt_pressed = False

	def __init__(self, script = None, *a, **k):
		self._script = script
		super(OhmDeviceComponent, self).__init__(*a, **k)


	"""
	def _current_bank_details(self):
		#debug('current bank deets...')
		if not self._script.modhandler.active_mod() is None:
			if self._script.modhandler.active_mod() and self._script.modhandler.active_mod()._param_component._device_parent != None:
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

class OhmTransportComponent(TransportComponent):


	def _update_stop_button_color(self):
		self._stop_button.color = 'Transport.StopOn' if self._play_toggle.is_toggled else 'Transport.StopOff'



class OhmBassGroupComponent(MonoKeyGroupComponent):


	def _note_translation_for_button(self, button):
		x, y = button.coordinate
		note = int(PAGE1_BASS_MAP[x][y])
		return (note, self._translation_channel)


	def _update_button_color(self, button):
		button.color = 'MonoInstrument.Bass.OnValue'



class OhmKeyGroupComponent(MonoKeyGroupComponent):


	def _note_translation_for_button(self, button):
		x, y = button.coordinate
		note = int(PAGE1_KEYS_MAP[y][x]) + int(PAGE1_MODES_MAP[self._scale][y]) + int(self._offset)
		return (note, self._translation_channel)


	def _update_button_color(self, button):
		button.color = 'MonoInstrument.Keys.OnValue'



class OhmModes(LividControlSurface):


	_sysex_id = 2
	_alt_sysex_id = 7
	_model_name = 'Ohm'
	_version_check = 'b996'
	_host_name = 'Ohm'
	device_provider_class = ModDeviceProvider

	def __init__(self, c_instance):
		super(OhmModes, self).__init__(c_instance)
		self._skin = Skin(OhmColors)
		with self.component_guard():
			self._define_sysex()
			self._setup_controls()
			self._setup_background()
			self._setup_m4l_interface()
			self._setup_translations()
			self._setup_session_control()
			self._setup_mixer_control()
			self._setup_device_control()
			self._setup_transport_control()
			self._setup_drumgroup()
			self._setup_keygroup()
			self._setup_bassgroup()
			self._setup_mod()
			self._setup_modswitcher()
			self._setup_modes()
		self._on_device_changed.subject = self._device_provider


	def _define_sysex(self):
		#self._send_midi(tuple(switchxfader))
		self._reverse_crossfader = SendLividSysexMode(self._livid_settings, call = 'reverse crossfader', message = [1])


	def update_display(self):
		super(OhmModes, self).update_display()
		#self.strobe()


	def _initialize_hardware(self):
		super(OhmModes, self)._initialize_hardware()
		#self._reverse_crossfader.enter_mode()


	def _initialize_script(self):
		super(OhmModes, self)._initialize_script()
		self._main_modes.selected_mode = 'Mix'
		self._session.update()
		self._mixer.update()


	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		self._fader = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = OHM_FADERS[index], name = 'Fader_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource) for index in range(8)]
		self._button = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = OHM_BUTTONS[index], name = 'Button_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for index in range(8)]
		self._dial = [MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = OHM_DIALS[index], name = 'Encoder_' + str(index), num = index, script = self, optimized_send_midi = optimized, resource_type = resource) for index in range(16)]
		self._menu = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = OHM_MENU[index], name = 'Menu_' + str(index), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for index in range(6)]
		self._crossfader = MonoEncoderElement(msg_type = MIDI_CC_TYPE, channel = CHANNEL, identifier = CROSSFADER, name = 'Crossfader', script = self, optimized_send_midi = optimized, resource_type = resource)
		self._livid = MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = LIVID, name = 'Livid_Button', skin = self._skin, script = self, optimized_send_midi = optimized, resource_type = resource)
		self._shift_l = MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = SHIFT_L, name = 'Page_Button_Left', script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource)
		self._shift_r = MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = SHIFT_R, name = 'Page_Button_Right', script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource)
		self._grid = [[MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = column * 8 + row, name = 'Grid_' + str(column + (row*8)), script = self, skin = self._skin, optimized_send_midi = optimized, resource_type = resource) for column in range(8)] for row in range(8)]
		self._matrix = ButtonMatrixElement(name = 'Matrix', rows = [[self._grid[row][column] for column in range(8)] for row in range(8)])
		self._dial_matrix = ButtonMatrixElement(name = 'DialMatrix', rows = [self._dial[index*4:(index*4)+4] for index in range(4)])
		self._menu_matrix = ButtonMatrixElement(name = 'MenuMatrix', rows = [self._menu])
		self._fader_matrix = ButtonMatrixElement(name = 'FaderMatrix', rows = [self._fader])
		self._button_matrix = ButtonMatrixElement(name = 'ButtonMatrix', rows = [self._button])

		self._parameter_controls = ButtonMatrixElement(rows = [self._dial[:4], self._dial[4:8]])


	def _setup_background(self):
		self._background = BackgroundComponent(name = 'Background')
		self._background.layer = Layer(priority = 3, matrix = self._matrix.submatrix[:,:],
													livid_button = self._livid,
													shift_l_button = self._shift_l,
													shift_r_button = self._shift_r,
													crossfader = self._crossfader,
													dial_matrix = self._dial_matrix.submatrix[:,:],
													menu_matrix = self._menu_matrix.submatrix[:,:],
													fader_matrix = self._fader_matrix.submatrix[:,:],
													button_matrix = self._button_matrix.submatrix[:,:])
		self._background.set_enabled(False)


	def _setup_m4l_interface(self):
		self._m4l_interface = M4LInterfaceComponent(controls=self.controls, component_guard=self.component_guard)
		self.get_control_names = self._m4l_interface.get_control_names
		self.get_control = self._m4l_interface.get_control
		self.grab_control = self._m4l_interface.grab_control
		self.release_control = self._m4l_interface.release_control


	def _setup_translations(self):
		controls = []
		for array in self._grid:
			for button in array:
				controls.append(button)
		if FADER_BANKING:
			controls = controls + self._dial
		if DIAL_BANKING:
			controls = controls + self._dial
		self._translations = TranslationComponent(controls = controls, user_channel_offset = USER_CHANNEL, channel = 8)
		self._translations.layer = Layer(priority = 5, channel_selector_buttons = self._menu_matrix.submatrix[:,:])
		self._translations.set_enabled(False)

		dj_controls = [self._grid[7][index] for index in range(7)]
		self._dj_translation = TranslationComponent(controls = dj_controls, channel = 12)


	def _setup_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks = 7, num_scenes = 5)
		self._session_ring.set_enabled(True)

		self._session_navigation = SessionNavigationComponent(session_ring = self._session_ring)
		self._session_navigation.scroll_navigation_layer = AddLayerMode(self._session_navigation, Layer(priority = 5, up_button = self._menu[2], down_button = self._menu[5], left_button = self._menu[3], right_button = self._menu[4]))
		self._session_navigation.page_navigation_layer = AddLayerMode(self._session_navigation, Layer(priority = 5, page_up_button = self._menu[2], page_down_button = self._menu[5], page_left_button = self._menu[3], page_right_button = self._menu[4]))
		self._session_navigation._vertical_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation.set_enabled(False)

		self._session = OhmSessionComponent(name = 'Session', session_ring = self._session_ring, auto_name = True)
		hasattr(self._session, '_enable_skinning') and self._session._enable_skinning()
		self._session.set_enabled(False)
		self._session.clip_launch_layer = AddLayerMode(self._session, Layer(priority = 5,  clip_launch_buttons = self._matrix.submatrix[:7,:5]))
		self._session.scene_launch_layer = AddLayerMode(self._session, Layer(priority = 5,  scene_launch_buttons = self._matrix.submatrix[7,:5]))

		self._session_zoom = SessionOverviewComponent(name = 'Session_Overview', session_ring = self._session_ring, enable_skinning = True)
		self._session_zoom.layer = Layer(priority = 5, button_matrix = self._matrix.submatrix[:7,:5])
		self._session_zoom.set_enabled(False)

		self._session_modes = ModesComponent(name = 'Session_Modes')
		self._session_modes.add_mode('disabled', [self._session,
														self._session.clip_launch_layer,
														self._session.scene_launch_layer,
														self._session_navigation,
														self._session_navigation.scroll_navigation_layer])
		self._session_modes.add_mode('enabled', [self._session,
														self._session.scene_launch_layer,
														self._session_zoom,
														self._session_navigation,
														self._session_navigation.page_navigation_layer],
														behaviour = DefaultedBehaviour())
		self._session_modes.layer = Layer(priority = 5, enabled_button = self._grid[7][7])
		self._session_modes.selected_mode = 'disabled'
		self._session_modes.set_enabled(False)


	def _setup_mixer_control(self):
		self._mixer = OhmMixerComponent(name = 'Mixer', tracks_provider = self._session_ring, track_assigner = SimpleTrackAssigner(), invert_mute_feedback = True, auto_name = True, enable_skinning = True)
		self._mixer.layer = Layer(priority = 5, volume_controls = self._fader_matrix.submatrix[:7, :], prehear_volume_control = self._dial[15], crossfader_control = self._crossfader)
		self._mixer.master_strip().layer = Layer(priority = 5, volume_control = self._fader[7], select_button = self._button[7])
		self._mixer.mix_layer = AddLayerMode(self._mixer, Layer(priority = 5, mute_buttons = self._matrix.submatrix[:7,5],
													solo_buttons = self._matrix.submatrix[:7,6],
													arm_buttons = self._matrix.submatrix[:7,7],
													send_controls = self._dial_matrix.submatrix[:,:2],
													pan_controls = self._dial_matrix.submatrix[:7,2:],
													track_select_buttons = self._button_matrix.submatrix[:7,:],))
		self._mixer.dj_layer = AddLayerMode(self._mixer, Layer(priority = 5, mute_buttons = self._matrix.submatrix[:7,5],
													crossfade_toggles = self._matrix.submatrix[:7,6],
													end_pan_controls = self._dial_matrix.submatrix[:3,3],
													eq_gain_controls = self._dial_matrix.submatrix[:,:3],
													track_select_buttons = self._button_matrix.submatrix[:7,:],))
		self._mixer.instrument_layer = AddLayerMode(self._mixer, Layer(priority = 5,
													instrument_send_controls = self._dial_matrix.submatrix[:,2:],
													arming_track_select_buttons = self._button_matrix.submatrix[:7,:]))


	def _setup_device_control(self):
		self._device = OhmDeviceComponent(script = self, name = 'Device_Component', device_provider = self._device_provider, device_bank_registry = DeviceBankRegistry())
		self._device.layer = Layer(priority = 5, parameter_controls = self._parameter_controls )
		self._device.set_enabled(False)

		self._device_navigator = DeviceNavigator(self._device_provider, self._mixer, self, name = 'Device_Navigator', )
		self._device_navigator.layer = Layer(priority = 5, prev_button = self._menu[3], next_button = self._menu[4])
		self._device_navigator.set_enabled(False)


	def _setup_transport_control(self):
		self._transport = OhmTransportComponent()
		self._transport.name = 'Transport'
		self._transport.layer = Layer(priority = 5, play_button = self._menu[0], stop_button = self._menu[1])
		self._transport.set_enabled(False)


	def _setup_drumgroup(self):
		self._drumgroup = MonoDrumGroupComponent(translation_channel = PAGE1_DRUM_CHANNEL, set_pad_translations = self.set_pad_translations)
		self._drumgroup._on_selected_track_changed.subject = None
		self._drumgroup.translation_channel = PAGE1_DRUM_CHANNEL
		self._drumgroup.layer = Layer(priority = 6, matrix = self._matrix.submatrix[:4, :4])
		self._drumgroup.set_enabled(False)


	def _setup_keygroup(self):
		self._scale_mode = ModesComponent(name = 'ScaleMode')
		for scale in SCALES:
			debug('making scale mode:', scale, str(scale))
			self._scale_mode.add_mode(str(scale), [])
		self._scale_mode.layer = Layer(priority = 5,
										ionian_button = self._grid[7][0],
										dorian_button = self._grid[7][1],
										phrygian_button = self._grid[7][2],
										lydian_button = self._grid[7][3],
										mixolydian_button = self._grid[7][4],
										aeolian_button = self._grid[7][5],
										locrian_button = self._grid[7][6],
										major_button = self._grid[7][7])
		self._scale_mode.selected_mode = 'ionian'
		self._scale_mode.set_enabled(False)
		self._on_scale_change.subject = self._scale_mode

		self._octave_offset_component = ScrollingChannelizedSettingsComponent(name = 'NoteOffset', parent_task_group = self._task_group, value_dict = range(104), default_value_index = 36, default_channel = 0, bank_increment = 12, bank_on_color = 'MonoInstrument.OffsetOnValue', bank_off_color = 'MonoInstrument.OffsetOffValue')
		self._octave_offset_component.layer = Layer(priority = 5, bank_up_button = self._menu[2], bank_down_button = self._menu[5])
		self._on_octave_change.subject = self._octave_offset_component

		self._keygroup = OhmKeyGroupComponent()
		self._keygroup._on_selected_track_changed.subject = None
		self._keygroup.translation_channel = PAGE1_KEYS_CHANNEL
		self._keygroup.layer = Layer(priority = 6, matrix = self._matrix.submatrix[:, 4:7])
		self._keygroup.set_enabled(False)


	def _setup_bassgroup(self):
		self._bassgroup = OhmBassGroupComponent()
		self._bassgroup._on_selected_track_changed.subject = None
		self._bassgroup.translation_channel = PAGE1_BASS_CHANNEL
		self._bassgroup.layer = Layer(priority = 6, matrix = self._matrix.submatrix[4:, :4])
		self._bassgroup.set_enabled(False)


	def _setup_mod(self):
		self.monomodular = get_monomodular(self)
		self.monomodular.name = 'monomodular_switcher'
		self.modhandler = OhmModHandler(script = self, device_provider = self._device_provider)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer(priority = 5,
									grid = self._matrix.submatrix[:,:],
									nav_up_button = self._menu[2],
									nav_down_button = self._menu[5],
									nav_left_button = self._menu[3],
									nav_right_button =  self._menu[4],
									shift_button = self._menu[1],
									alt_button = self._menu[0],)
									#parameter_controls = self._dial_matrix)
		self.modhandler.legacy_shift_mode = AddLayerMode(self.modhandler, Layer(priority = 6,
									channel_buttons = self._matrix.submatrix[:, 1],
									nav_matrix = self._matrix.submatrix[4:8, 2:6]))
		self.modhandler.shift_mode = AddLayerMode(self.modhandler, Layer(priority = 6,
									device_selector_matrix = self._matrix.submatrix[:, 0],
									lock_button = self._livid,
									key_buttons = self._matrix.submatrix[:, 7]))

		self.modhandler.set_enabled(False)
		self.modhandler.set_mod_button(self._livid)


	def _setup_modswitcher(self):
		self._modswitcher = ModesComponent(name = 'ModSwitcher')
		self._modswitcher.add_mode('mod', [self.modhandler, self._device, DelayMode(self.modhandler.update, delay = .5)])
		self._modswitcher.add_mode('translations', [self._translations])
		self._modswitcher.selected_mode = 'translations'
		self._modswitcher.set_enabled(False)


	def _setup_modes(self):

		self._main_modes = ModesComponent(name = 'MainModes')
		self._main_modes.add_mode('disabled', [self._background])
		self._main_modes.add_mode('Mix', [self._session_modes,
											self._mixer,
											self._mixer.mix_layer,
											self._transport])

		self._main_modes.add_mode('DJ', [self._session_modes,
											self._mixer,
											self._mixer.dj_layer,
											self._dj_translation,
											tuple([self._assign_tempo, self._deassign_tempo])],
											behaviour = DefaultedBehaviour(default_mode = 'Mix'))
											#tuple([ lambda:self._set_tempo_buttons([self._grid[7][5], self._grid[7][6]]), self._set_tempo_buttons([])])],

		self._main_modes.add_mode('Instrument', [self._update_keygroup_colors,
											self._bassgroup,
											self._keygroup,
											self._scale_mode,
											self._octave_offset_component,
											self._device,
											self._device_navigator,
											self._mixer,
											self._mixer.instrument_layer,
											self._drumgroup],
											behaviour = DefaultedBehaviour(default_mode = 'Mix'))

		self._main_modes.add_mode('Mod', [self._modswitcher,
											self._device,
											self._mixer,
											self._mixer.instrument_layer],
											behaviour = DefaultedBehaviour(default_mode = 'Mix'))
		self._main_modes.layer = Layer(priority = 5, Instrument_button = self._shift_l, DJ_button = self._shift_r, Mod_button = self._livid)
		self._main_modes.selected_mode = 'disabled'
		self._main_modes.set_enabled(True)


	def disconnect(self):
		super(OhmModes, self).disconnect()


	def strobe(self):
		if self._backlight_type != 'static':
			if self._backlight_type is 'pulse':
				self._backlight = int(math.fabs(self._timer * 16 % 64 - 32) + 32)
			if self._backlight_type is 'up':
				self._backlight = int(self._timer * 8 % 64 + 16)
			if self._backlight_type is 'down':
				self._backlight = int(math.fabs(int(self._timer * 8 % 64 - 64)) + 16)
		self._send_midi(tuple([176, 27, int(self._backlight)]))
		if self._ohm_type != 'static':
			if self._ohm_type is 'pulse':
				self._ohm = int(math.fabs(self._timer * 16 % 64 - 32) + 32)
			if self._ohm_type is 'up':
				self._ohm = int(self._timer * 8 % 64 + 16)
			if self._ohm_type is 'down':
				self._ohm = int(math.fabs(int(self._timer * 8 % 64 - 64)) + 16)
		self._send_midi(tuple([176, 63, int(self._ohm)]))
		self._send_midi(tuple([176, 31, int(self._ohm)]))


	def handle_sysex(self, midi_bytes):
		debug('sysex: ', str(midi_bytes))
		if len(midi_bytes) > 14:
			if midi_bytes[:6] == tuple([240, 0, 1, 97, 12, 64]):
				self._register_pad_pressed(midi_bytes[6:14])
			elif midi_bytes[:6] == tuple([240, 0, 1, 97, 17, 64]):
				self._register_pad_pressed(midi_bytes[6:14])
			elif midi_bytes[3:11] == tuple([6, 2, 0, 1, 97, 1, 0]  + [self._sysex_id]) or midi_bytes[3:11] == tuple([6, 2, 0, 1, 97, 1, 0]  + [self._alt_sysex_id]):
				if not self._connected:
					#self._connection_routine.kill()
					self._connected = True
					self._livid_settings.set_model(midi_bytes[11])
					self._initialize_hardware()
					self.schedule_message(1, self._initialize_script)


	@listens('device')
	def _on_device_changed(self):
		self.schedule_message(1, self._update_modswitcher)
		#debug('base on_device_changed')
		self._update_modswitcher()


	def _on_selected_track_changed(self):
		super(OhmModes, self)._on_selected_track_changed()
		if not len(self.song.view.selected_track.devices):
			self._update_modswitcher()


	def _update_modswitcher(self):
		debug('update modswitcher, mod is:', self.modhandler.active_mod())
		if self.modhandler.active_mod():
			self._modswitcher.selected_mode = 'mod'
		else:
			self._modswitcher.selected_mode = 'translations'


	@listens('selected_mode')
	def _on_scale_change(self, mode):
		debug('new scale is:', mode, self._scale_mode.selected_mode)
		self._keygroup.scale = SCALES.index(self._scale_mode.selected_mode)


	@listens('value')
	def _on_octave_change(self, value):
		self._keygroup.offset = value


	#stupid hack....4 hours wasted on two buttons is too long, so we're doing this instead
	def _update_keygroup_colors(self):
		self._grid[5][7].send_value(2, force = True)
		self._grid[6][7].send_value(2, force = True)


	#everything below needs to be consolidated into transport component
	def _assign_tempo(self):
		self._grid[5][7].send_value(4, True)
		self._grid[6][7].send_value(4, True)
		self._tempo_up_value.subject = self._grid[5][7]
		self._tempo_down_value.subject = self._grid[6][7]


	def _deassign_tempo(self):
		self._tempo_up_value.subject and self._tempo_up_value.subject.turn_off()
		self._tempo_down_value.subject and self._tempo_down_value.subject.turn_off()
		self._tempo_up_value.subject = None
		self._tempo_down_value.subject = None


	@listens('value')
	def _tempo_up_value(self, value):
		if value:
			self.song.tempo = round(min(self.song.tempo + 1, 999))


	@listens('value')
	def _tempo_down_value(self, value):
		if value:
			self.song.tempo = round(max(self.song.tempo - 1, 20))



class OhmModHandler(ModHandler):


	def __init__(self, *a, **k):
		super(OhmModHandler, self).__init__(*a, **k)
		self._shift_mode = ModesComponent()
		self._color_type = 'RGB'
		self._shift_mode.add_mode('shift', tuple([self._enable_shift, self._disable_shift]), behaviour = CancellableBehaviourWithRelease())
		self.nav_box = NavigationBox(self, 16, 16, 8, 8, self.set_offset)
		self._mod_button = None


	def _enable_shift(self):
		self._shift_value(1)


	def _disable_shift(self):
		self._shift_value(0)


	def set_shift_button(self, button):
		self._shift_mode.shift_button.set_control_element(button)


	def set_nav_matrix(self, matrix):
		self.nav_box.set_matrix(matrix)


	def _receive_grid(self, x, y, value, *a, **k):
		#self._receive_grid(x, y, value, *a, **k)
		legacy = self.active_mod().legacy
		if self._active_mod:
			if not self._grid_value.subject is None:
				if legacy:
					x = x - self.x_offset
					y = y - self.y_offset
				if x in range(8) and y in range(8):
					try:
						self._grid_value.subject.send_value(x, y, self._colors[value], True)
					except:
						pass


	def set_device_selector_matrix(self, matrix):
		self._device_selector.set_matrix(matrix)


	@listens('value')
	def _grid_value(self, value, x, y, *a, **k):
		#self.log_message('_base_grid_value ' + str(x) + str(y) + str(value))
		if self.active_mod():
			if self.active_mod().legacy:
				x += self.x_offset
				y += self.y_offset
			self._active_mod.send('grid', x, y, value)


	@listens('value')
	def _shift_value(self, value, *a, **k):
		self._is_shifted = not value is 0
		mod = self.active_mod()
		if mod:
			mod.send('shift', value)
		if self._is_shifted:
			self.shift_mode.enter_mode()
			if mod and mod.legacy:
				self.legacy_shift_mode.enter_mode()
		else:
			self.legacy_shift_mode.leave_mode()
			self.shift_mode.leave_mode()
		self.update()


	def set_mod_button(self, button):
		self._mod_button = button


	def update(self, *a, **k):
		mod = self.active_mod()
		if self.is_enabled():
			if not mod is None:
				mod.restore()
			else:
				if not self._grid_value.subject is None:
					self._grid_value.subject.reset()
				if not self._keys_value.subject is None:
					self._keys_value.subject.reset()
			self._alt_value.subject and self._alt_value.subject.send_value(2 + int(self.is_alted())*7, True)
			if self._on_lock_value.subject:
				self._on_lock_value.subject.send_value(1 + (int(self.is_locked())*4), True)
			else:
				self._mod_button and self._mod_button.send_value(7 + (not self.active_mod() is None)*7, True)

		else:
			self._mod_button and self._mod_button.send_value((not self.active_mod() is None)*3, True)
