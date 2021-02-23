

import Live
from ableton.v2.base import const, inject, listens
from ableton.v2.control_surface import ControlSurface, Layer
from ableton.v2.control_surface.components.background import BackgroundComponent
from ableton.v2.control_surface.input_control_element import *
from ableton.v2.control_surface.elements.button import ButtonElement
from ableton.v2.control_surface.elements.button_matrix import ButtonMatrixElement
from ableton.v2.control_surface.mode import ModesComponent, LayerMode, AddLayerMode, ReenterBehaviour, ModeButtonControl, SetAttributeMode
from ableton.v2.control_surface.components.session_ring import SessionRingComponent
from ableton.v2.control_surface.components.session_overview import SessionOverviewComponent
from ableton.v2.control_surface.components.session_navigation import SessionNavigationComponent
from ableton.v2.control_surface.components.session import SessionComponent
from ableton.v2.control_surface.components.mixer import MixerComponent

from .SkinDefault import make_default_skin
from .SpecialMidiMap import SpecialMidiMap, make_button, make_multi_button, make_slider
from .ConfigurableButtonElement import ConfigurableButtonElement
from .TranslationComponent import TranslationComponent
from .PreciseButtonSliderElement import PreciseButtonSliderElement
from .SpecialMixerComponent import SpecialMixerComponent
from .SpecialSessionComponent import SpecialSessionComponent

SIDE_NOTES = (8, 24, 40, 56, 72, 88, 104, 120)
DRUM_NOTES = (41, 42, 43, 44, 45, 46, 47, 57, 58, 59, 60, 61, 62, 63, 73, 74, 75, 76, 77, 78, 79, 89, 90, 91, 92, 93, 94, 95, 105, 106, 107)


from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import *
debug = initialize_debug()


class Launchpad(ControlSurface):
	""" Script for Novation's Launchpad Controller """

	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		is_momentary = True
		self._suppress_send_midi = False
		with self.component_guard():
			self._skin = make_default_skin()
			#with inject(skin=const(self._skin)).everywhere():
			#	self._midimap = MidiMap()
			self._suggested_input_port = 'Launchpad'
			self._suggested_output_port = 'Launchpad'
			self._control_is_with_automap = False
			self._user_byte_write_button = ButtonElement(is_momentary, MIDI_CC_TYPE, 0, 16)
			self._user_byte_write_button.name = 'User_Byte_Button'
			self._user_byte_write_button.send_value(1)
			self._user_byte_write_button.add_value_listener(self._user_byte_value)
			self._wrote_user_byte = False
			self._challenge = Live.Application.get_random_int(0, 400000000) & 2139062143
			self._matrix = ButtonMatrixElement()
			self._matrix.name = 'Button_Matrix'
			#with inject(skin=const(self._skin)).everywhere():
			for row in range(8):
				button_row = []
				for column in range(8):
					button = ConfigurableButtonElement(is_momentary, MIDI_NOTE_TYPE, 0, row * 16 + column, skin = self._skin)
					button.name = str(column) + '_Clip_' + str(row) + '_Button'
					button_row.append(button)

				self._matrix.add_row(tuple(button_row))
			self._top_buttons = [ ConfigurableButtonElement(is_momentary, MIDI_CC_TYPE, 0, 104 + index, skin = self._skin) for index in range(8) ]
			self._side_buttons = [ ConfigurableButtonElement(is_momentary, MIDI_NOTE_TYPE, 0, SIDE_NOTES[index], skin = self._skin) for index in range(8) ]
			self._top_matrix = ButtonMatrixElement(name = 'Top_Button_Matrix', rows = [self._top_buttons])
			self._side_matrix = ButtonMatrixElement(name = 'Side_Button_Matrix', rows = [self._side_buttons])

			self._config_button = ButtonElement(is_momentary, MIDI_CC_TYPE, 0, 0, optimized_send_midi=False)
			self._config_button.add_value_listener(self._config_value)

			self._top_buttons[0].name = 'Bank_Select_Up_Button'
			self._top_buttons[1].name = 'Bank_Select_Down_Button'
			self._top_buttons[2].name = 'Bank_Select_Left_Button'
			self._top_buttons[3].name = 'Bank_Select_Right_Button'
			self._top_buttons[4].name = 'Session_Button'
			self._top_buttons[5].name = 'User1_Button'
			self._top_buttons[6].name = 'User2_Button'
			self._top_buttons[7].name = 'Mixer_Button'
			self._side_buttons[0].name = 'Vol_Button'
			self._side_buttons[1].name = 'Pan_Button'
			self._side_buttons[2].name = 'SndA_Button'
			self._side_buttons[3].name = 'SndB_Button'
			self._side_buttons[4].name = 'Stop_Button'
			self._side_buttons[5].name = 'Trk_On_Button'
			self._side_buttons[6].name = 'Solo_Button'
			self._side_buttons[7].name = 'Arm_Button'

			self._create_background()
			self._create_translations()
			self._create_session()
			self._create_mixer()
			self._create_modes()


	def _create_background(self):
		self._background = BackgroundComponent(name = 'Background')
		self._background.layer = Layer(priority = 5, matrix = self._matrix, side_buttons = self._side_matrix, top_buttons = self._top_matrix)
		self._background.set_enabled(True)


	def _create_translations(self):
		self._translations1 = TranslationComponent(name = 'User1Translation', translated_channel=2, should_enable=True, should_reset=True, is_enabled=False, layer=Layer(matrix = self._matrix, top_buttons = self._top_matrix.submatrix[:4,1], side_buttons = self._side_matrix))
		self._translations2 = TranslationComponent(name = 'User2Translation', translated_channel=3, should_enable=True, should_reset=True, is_enabled=False, layer=Layer(matrix = self._matrix, top_buttons = self._top_matrix.submatrix[:4,1], side_buttons = self._side_matrix))


	def _create_session(self):
		self._session_ring = SessionRingComponent(8,  8, name = 'Session_Ring')
		self._session = SpecialSessionComponent(session_ring = self._session_ring, name = 'Session', is_enabled = False, auto_name = True)
		self._session_navigation = SessionNavigationComponent(session_ring = self._session_ring, name = 'SessionNavigation', is_enabled = False)
		self._session_navigation._vertical_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_banking.scroll_up_button.disabled_color = 'Session.NavigationButtonOff'
		self._session_navigation._vertical_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._vertical_banking.scroll_down_button.disabled_color = 'Session.NavigationButtonOff'
		self._session_navigation._horizontal_banking.scroll_up_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_up_button.disabled_color = 'Session.NavigationButtonOff'
		self._session_navigation._horizontal_banking.scroll_down_button.color = 'Session.NavigationButtonOn'
		self._session_navigation._horizontal_banking.scroll_down_button.disabled_color = 'Session.NavigationButtonOff'
		self._session_navigation._vertical_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_up_button.disabled_color = 'Session.PageNavigationButtonOff'
		self._session_navigation._vertical_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._vertical_paginator.scroll_down_button.disabled_color = 'Session.PageNavigationButtonOff'
		self._session_navigation._horizontal_paginator.scroll_up_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_up_button.disabled_color = 'Session.PageNavigationButtonOff'
		self._session_navigation._horizontal_paginator.scroll_down_button.color = 'Session.PageNavigationButtonOn'
		self._session_navigation._horizontal_paginator.scroll_down_button.disabled_color = 'Session.PageNavigationButtonOff'
		self._zooming = SessionOverviewComponent(session_ring = self._session_ring, enable_skinning = True, name = 'Session_Zooming', is_enabled = False)
		self._zooming.layer = Layer(button_matrix = self._matrix)

		self._session_navigation.nav_layer = AddLayerMode(self._session_navigation, Layer(up_button = self._top_buttons[0], down_button = self._top_buttons[1], left_button = self._top_buttons[2], right_button = self._top_buttons[3]))
		self._session_navigation.page_layer = AddLayerMode(self._session_navigation, Layer(page_up_button = self._top_buttons[0], page_down_button = self._top_buttons[1], page_left_button = self._top_buttons[2], page_right_button = self._top_buttons[3]))
		self._session.cliplaunch_layer = AddLayerMode(self._session, Layer(priority = 1, clip_launch_buttons = self._matrix, scene_launch_buttons = self._side_matrix))
		self._session.clipstop_layer = AddLayerMode(self._session, Layer(priority = 1, stop_all_clips_button = self._side_buttons[4], stop_track_clip_buttons = self._matrix.submatrix[:, 4:5]))

	def _create_mixer(self):
		self._mixer = SpecialMixerComponent(tracks_provider = self._session_ring, auto_name=True, is_enabled=True, invert_mute_feedback=True)
		self._mixer.name = 'Mixer'
		self._mixer.master_strip().name = 'Master_Channel_strip'
		self._mixer.selected_strip().name = 'Selected_Channel_strip'
		self._sliders = []
		self._slider_volume_modes = []
		self._slider_pan_modes = []
		self._slider_single_modes = []
		for column in range(8):
			self._mixer.channel_strip(column).name = 'Channel_Strip_' + str(column)
			self._sliders.append(PreciseButtonSliderElement(buttons = tuple([ self._matrix._orig_buttons[7-row][column]for row in range(8) ])))
			self._sliders[-1].name = 'Button_Slider_' + str(column)
		self._slider_matrix = ButtonMatrixElement(name = 'SliderMatrix', rows = [self._sliders])
		self._mixer.overview_layer = AddLayerMode(self._mixer, Layer(priority = 1, default_volume_buttons = self._matrix.submatrix[:, :1],
																					default_panning_buttons = self._matrix.submatrix[:, 1:2],
																					default_send1_buttons = self._matrix.submatrix[:, 2:3],
																					default_send2_buttons = self._matrix.submatrix[:, 3:4],
																					mute_buttons = self._matrix.submatrix[:, 5:6],
																					solo_buttons = self._matrix.submatrix[:, 6:7],
																					arm_buttons = self._matrix.submatrix[:, 7:8],
																					unarm_all_button = self._side_buttons[7],
																					unsolo_all_button = self._side_buttons[6],
																					unmute_all_button = self._side_buttons[5]))
		self._mixer.volume_layer = AddLayerMode(self._mixer, Layer(priority = 1, volume_controls = self._slider_matrix))
		self._mixer.pan_layer = AddLayerMode(self._mixer, Layer(priority = 1, pan_controls = self._slider_matrix))
		self._mixer.send1_layer = AddLayerMode(self._mixer, Layer(priority = 1, send_controls = self._slider_matrix))
		self._mixer.send2_layer = AddLayerMode(self._mixer, Layer(priority = 1, send_controls = self._slider_matrix))


	def _create_modes(self):
		self._session_modes = ModesComponent(name = 'SessionModes')
		self._session_modes.add_mode('Session', [self._session, self._session.cliplaunch_layer, self._session_navigation, self._session_navigation.nav_layer], cycle_mode_button_color = 'MainModes.SelectedOn')
		self._session_modes.add_mode('Zoom', [self._zooming, self._session_navigation, self._session_navigation.page_layer], cycle_mode_button_color = 'MainModes.SelectedPressed')
		self._session_modes.selected_mode = 'Session'
		self._session_modes.layer = Layer(priority = 1, cycle_mode_button = self._top_buttons[4])
		self._session_modes.set_enabled(False)

		self._mixer_modes = ModesComponent(name = 'MixerModes')
		self._mixer_modes.add_mode('Overview', [self._session_navigation, self._session_navigation.nav_layer, self._session, self._session.clipstop_layer, self._mixer, self._mixer.overview_layer])
		self._mixer_modes.add_mode('TrackVolume', [self._session_navigation, self._session_navigation.nav_layer, self._mixer, self._mixer.volume_layer, tuple([self.set_slider_volume_mode, self.set_slider_single_mode])])
		self._mixer_modes.add_mode('TrackPan', [self._session_navigation, self._session_navigation.nav_layer, self._mixer, self._mixer.pan_layer, tuple([self.set_slider_pan_mode, self.set_slider_single_mode])])
		self._mixer_modes.add_mode('TrackSend1', [self._session_navigation, self._session_navigation.nav_layer, self._mixer, self._mixer.send1_layer, SetAttributeMode(obj=self._mixer, attribute='send_index', value=0), tuple([self.set_slider_send_mode, self.set_slider_single_mode])])
		self._mixer_modes.add_mode('TrackSend2', [self._session_navigation, self._session_navigation.nav_layer, self._mixer, self._mixer.send2_layer, SetAttributeMode(obj=self._mixer, attribute='send_index', value=1), tuple([self.set_slider_send_mode, self.set_slider_single_mode])])
		for mode in self._mixer_modes._mode_list:
			if mode == 'Overview':
				self._mixer_modes.get_mode_button(mode).mode_selected_color = 'MainModes.SelectedOn'
				self._mixer_modes.get_mode_button(mode).mode_unselected_color = 'MainModes.SelectedOn'
			else:
				self._mixer_modes.get_mode_button(mode).mode_selected_color = 'SubModes.SelectedOn'
				self._mixer_modes.get_mode_button(mode).mode_unselected_color = 'SubModes.SelectedOff'
		self._mixer_modes.selected_mode = 'Overview'
		self._mixer_modes.layer = Layer(priority = 1, Overview_button = self._top_buttons[7], TrackVolume_button = self._side_buttons[0], TrackPan_button = self._side_buttons[1], TrackSend1_button = self._side_buttons[2], TrackSend2_button = self._side_buttons[3])
		self._mixer_modes.set_enabled(False)

		self._selector = ModesComponent(name = 'Selector')
		self._selector.add_mode('disabled', [self._background])
		self._selector.add_mode('Session', [self._session_modes])
		self._selector.add_mode('User1', [self._translations1])
		self._selector.add_mode('User2', [self._translations2])
		self._selector.add_mode('Mixer', [tuple([self.enable_sliders, self.disable_sliders]), self._mixer_modes])
		for mode in self._selector._mode_list:
			self._selector.get_mode_button(mode).mode_selected_color = 'MainModes.SelectedOn'
			self._selector.get_mode_button(mode).mode_unselected_color = 'MainModes.SelectedOff'
		self._selector.layer = Layer(priority = 1, Session_button = self._top_buttons[4], User1_button = self._top_buttons[5], User2_button = self._top_buttons[6], Mixer_button = self._top_buttons[7])
		self._selector.set_enabled(True)
		self._selector.selected_mode = 'disabled'

	def enable_sliders(self):
		for slider in self._sliders:
			slider._disabled = False


	def disable_sliders(self):
		for slider in self._sliders:
			slider._disabled = True


	def set_slider_single_mode(self):
		for slider in self._sliders:
			slider.set_mode(0)


	def set_slider_volume_mode(self):
		for slider in self._sliders:
			slider.set_mode(1)


	def set_slider_pan_mode(self):
		for slider in self._sliders:
			slider.set_mode(2)


	def set_slider_send_mode(self):
		for slider in self._sliders:
			slider.set_mode(1)


	def disconnect(self):
		self._suppress_send_midi = True
		for control in self.controls:
			if isinstance(control, ConfigurableButtonElement):
				control.remove_value_listener(self._button_value)

		self._selector = None
		self._user_byte_write_button.remove_value_listener(self._user_byte_value)
		self._config_button.remove_value_listener(self._config_value)
		super(Launchpad, self).disconnect()
		self._suppress_send_midi = False
		self._config_button.send_value(32)
		self._config_button.send_value(0)
		self._config_button = None
		self._user_byte_write_button.send_value(0)
		self._user_byte_write_button = None


	def refresh_state(self):
		super(Launchpad, self).refresh_state()
		self.schedule_message(5, self._update_hardware)


	def process_midi_bytes(self, midi_bytes, midi_processor):
		#def handle_sysex(self, midi_bytes):
		if len(midi_bytes) == 8:
			if midi_bytes[1:5] == (0, 32, 41, 6):
				response = int(midi_bytes[5])
				response += int(midi_bytes[6]) << 8
				if response == Live.Application.encrypt_challenge2(self._challenge):
					self._on_handshake_successful()
		else:
			super(Launchpad, self).process_midi_bytes(midi_bytes, midi_processor)


	def _on_handshake_successful(self):
		debug('Launchpad._on_handshake_successful')
		self._suppress_send_midi = False
		self.set_enabled(True)
		self._selector.selected_mode = 'Session'
		self._selector.set_enabled(True)
		debug(self._selector.selected_mode)

	"""
	def build_midi_map(self, midi_map_handle):
		ControlSurface.build_midi_map(self, midi_map_handle)
		#if self._selector.mode_index == 1:
		#	new_channel = self._selector.channel_for_current_mode()
		#	for note in DRUM_NOTES:
		#		self._translate_message(MIDI_NOTE_TYPE, note, 0, note, new_channel)
	"""
	"""
	def _send_midi(self, midi_bytes, optimized = None):
		sent_successfully = False
		if not self._suppress_send_midi:
			sent_successfully = ControlSurface._send_midi(self, midi_bytes, optimized=optimized)
		return sent_successfully
	"""

	def _update_hardware(self):
		self._suppress_send_midi = False
		self._wrote_user_byte = True
		self._user_byte_write_button.send_value(1)
		self._suppress_send_midi = True
		self.set_enabled(False)
		self._suppress_send_midi = False
		self._send_challenge()


	def _send_challenge(self):
		for index in range(4):
			challenge_byte = self._challenge >> 8 * index & 127
			self._send_midi((176, 17 + index, challenge_byte))


	def _user_byte_value(self, value):
		if not value in range(128):
			raise AssertionError
			enabled = self._wrote_user_byte or value == 1
			self._control_is_with_automap = not enabled
			self._suppress_send_midi = self._control_is_with_automap
			if not self._control_is_with_automap:
				for control in self.controls:
					if isinstance(control, ConfigurableButtonElement):
						control.set_force_next_value()

			#self._selector.set_mode(0)
			self._selector.selected_mode = 'Session'
			self.set_enabled(enabled)
			self._suppress_send_midi = False
		else:
			self._wrote_user_byte = False


	def _button_value(self, value):
		debug('_button_value', value, self._selector.selected_mode, self._selector.is_enabled())
		#self._top_buttons[0].send_value(127)
		#assert value in range(128)


	def _config_value(self, value):
		assert value in range(128)

	"""
	def _set_session_highlight(self, track_offset, scene_offset, width, height, include_return_tracks):
		if not self._suppress_session_highlight:
			ControlSurface._set_session_highlight(self, track_offset, scene_offset, width, height, include_return_tracks)
	"""
