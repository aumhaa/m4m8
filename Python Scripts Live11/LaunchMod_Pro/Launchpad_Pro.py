

from functools import partial
import Live
from ableton.v2.base import const, inject, listens
from ableton.v2.base import task
from ableton.v2.control_surface import Layer
from ableton.v2.control_surface import ControlSurface, DeviceBankRegistry
from ableton.v2.control_surface.components import SessionRingComponent, ViewControlComponent, SessionNavigationComponent
from ableton.v2.control_surface.identifiable_control_surface import IdentifiableControlSurface
from ableton.v2.control_surface.mode import ModesComponent as ModesComponentBase, LayerMode, AddLayerMode, ReenterBehaviour, ModeButtonControl
from ableton.v2.control_surface.elements import ComboElement, ButtonMatrixElement, ButtonElement
from ableton.v2.control_surface.control import ButtonControl

from .Colors import CLIP_COLOR_TABLE, RGB_COLOR_TABLE
from .SkinDefault import make_default_skin
from .SpecialMidiMap import SpecialMidiMap, make_button, make_multi_button, make_slider
from .BackgroundComponent import ModifierBackgroundComponent, BackgroundComponent
from .ActionsComponent import ActionsComponent
from .ClipActionsComponent import ClipActionsComponent
from .LedLightingComponent import LedLightingComponent
from .TranslationComponent import TranslationComponent
from .TargetTrackComponent import TargetTrackComponent
from .SpecialDeviceComponent import SpecialDeviceComponent
from .DeviceNavigationComponent import DeviceNavigationComponent
from .SpecialSessionRecordingComponent import SpecialSessionRecordingComponent
from .DrumGroupFinderComponent import DrumGroupFinderComponent
from .DrumGroupComponent import DrumGroupComponent
from .SpecialMixerComponent import SpecialMixerComponent
from .SpecialSessionComponent import SpecialSessionComponent as SessionComponent, SpecialClipSlotComponent, SpecialSessionZoomingComponent as SessionZoomingComponent, SessionZoomingManagerComponent
from .SpecialModesComponent import SpecialModesComponent, SpecialReenterBehaviour, CancelingReenterBehaviour
from .UserMatrixComponent import UserMatrixComponent
from . import consts

from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import *
debug = initialize_debug()

NUM_TRACKS = 8
NUM_SCENES = 8

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1


#Really need the ability to inject the mode_selected_color/mode_unselected_color into the ModesComponent more easily

def make_mode_button_control(modes_component, mode_name, behaviour, **k):
	button_control = ModeButtonControl(modes_component=modes_component, mode_name=mode_name, mode_selected_color = True, mode_unselected_color = False, **k)

	@button_control.pressed
	def button_control(modes_component, button):
		behaviour.press_immediate(modes_component, mode_name)

	@button_control.pressed_delayed
	def button_control(modes_component, button):
		behaviour.press_delayed(modes_component, mode_name)

	@button_control.released_immediately
	def button_control(modes_component, button):
		behaviour.release_immediate(modes_component, mode_name)

	@button_control.released_delayed
	def button_control(modes_component, button):
		behaviour.release_delayed(modes_component, mode_name)

	return button_control


class ModesComponent(ModesComponentBase):


	def add_mode_button_control(self, mode_name, behaviour):
		button_control = make_mode_button_control(self, mode_name, behaviour)
		self.add_control('%s_button' % mode_name, button_control)
		self._update_mode_buttons(self.selected_mode)



class MidiMap(SpecialMidiMap):


	def __init__(self, *a, **k):
		super(MidiMap, self).__init__(*a, **k)
		left_button_names = ('Session_Record_Button', 'Double_Loop_Button', 'Duplicate_Button', 'Quantize_Button', 'Delete_Button', 'Undo_Button', 'Click_Button', 'Shift_Button')
		default_states = {True: 'DefaultButton.On',
		 False: 'DefaultButton.Off'}
		rec_states = {True: 'Recording.On',
		 False: 'Recording.Off'}
		shift_states = {True: 'Misc.ShiftOn',
		 False: 'Misc.Shift'}
		for index, val in enumerate(left_button_names):
			if val in ('Session_Record_Button', 'Undo_Button', 'Click_Button'):
				self.add_button(val, 0, (index + 1) * 10, MIDI_CC_TYPE, default_states=rec_states if val == 'Session_Record_Button' else default_states)
			else:
				self.add_modifier_button(val, 0, (index + 1) * 10, MIDI_CC_TYPE, default_states=shift_states if val == 'Shift_Button' else default_states)

		self.add_button('Record_Arm_Mode_Button', 0, 1, MIDI_CC_TYPE, default_states={True: 'Mode.RecordArm.On',
		 False: 'Mode.RecordArm.Off'})
		self.add_button('Track_Select_Mode_Button', 0, 2, MIDI_CC_TYPE, default_states={True: 'Mode.TrackSelect.On',
		 False: 'Mode.TrackSelect.Off'})
		self.add_button('Mute_Mode_Button', 0, 3, MIDI_CC_TYPE, default_states={True: 'Mode.Mute.On',
		 False: 'Mode.Mute.Off'})
		self.add_button('Solo_Mode_Button', 0, 4, MIDI_CC_TYPE, default_states={True: 'Mode.Solo.On',
		 False: 'Mode.Solo.Off'})
		self.add_button('Volume_Mode_Button', 0, 5, MIDI_CC_TYPE, default_states={True: 'Mode.Volume.On',
		 False: 'Mode.Volume.Off'})
		self.add_button('Pan_Mode_Button', 0, 6, MIDI_CC_TYPE, default_states={True: 'Mode.Pan.On',
		 False: 'Mode.Pan.Off'})
		self.add_button('Sends_Mode_Button', 0, 7, MIDI_CC_TYPE, default_states={True: 'Mode.Sends.On',
		 False: 'Mode.Sends.Off'})
		self.add_button('Stop_Clip_Mode_Button', 0, 8, MIDI_CC_TYPE, default_states={True: 'Mode.StopClip.On',
		 False: 'Mode.StopClip.Off'})
		self._arrow_button_names = ['Arrow_Up_Button',
		 'Arrow_Down_Button',
		 'Arrow_Left_Button',
		 'Arrow_Right_Button']
		arrow_button_states = {'Pressed': 'DefaultButton.On',
		 'Enabled': 'DefaultButton.Off',
		 True: 'DefaultButton.On',
		 False: 'DefaultButton.Disabled'}
		for index, val in enumerate(self._arrow_button_names):
			self.add_button(val, 0, index + 91, MIDI_CC_TYPE, default_states=arrow_button_states)

		self.add_modifier_button('Session_Mode_Button', 0, 95, MIDI_CC_TYPE, default_states={True: 'Mode.Session.On',
		 False: 'Mode.Session.Off'}, element_factory=make_multi_button)
		self.add_button('Note_Mode_Button', 0, 96, MIDI_CC_TYPE, element_factory=make_multi_button)
		self.add_button('Device_Mode_Button', 0, 97, MIDI_CC_TYPE, default_states={True: 'Mode.Device.On',
		 False: 'Mode.Device.Off'}, element_factory=make_multi_button)
		self.add_button('User_Mode_Button', 0, 98, MIDI_CC_TYPE, default_states={True: 'Mode.User.On',
		 False: 'Mode.User.Off'}, element_factory=make_multi_button, color_slaves=True)
		self.add_matrix('Scene_Launch_Button_Matrix', make_button, 0, [[ identifier for identifier in range(89, 18, -10) ]], MIDI_CC_TYPE)
		self['Scene_Stop_Button_Matrix'] = self['Scene_Launch_Button_Matrix'].submatrix[:7, :]
		self['Scene_Stop_Button_Matrix'].name = 'Scene_Stop_Button_Matrix'
		self['Stop_All_Clips_Button'] = self['Scene_Launch_Button_Matrix_Raw'][0][7]
		self.add_matrix('Main_Button_Matrix', make_button, 0, [ [ identifier for identifier in range(start, start + NUM_TRACKS) ] for start in range(81, 10, -10) ], MIDI_NOTE_TYPE)
		self['Mixer_Button_Matrix'] = self['Main_Button_Matrix'].submatrix[:, 7:]
		self['Mixer_Button_Matrix'].name = 'Mixer_Button_Matrix'
		matrix_rows_with_session_button_raw = [ [ self.with_session_button(self['Main_Button_Matrix_Raw'][row][column]) for column in range(8) ] for row in range(8) ]
		self['Main_Button_Matrix_With_Session_Button'] = ButtonMatrixElement(rows=matrix_rows_with_session_button_raw, name='Main_Button_Matrix_With_Session_Button')
		note_buttons_raw = []
		for identifier in range(128):
			if identifier not in self['Main_Button_Matrix_Ids']:
				button = make_button('Note_Button_' + str(identifier), 0, identifier, MIDI_NOTE_TYPE)
				button.set_enabled(False)
				button.set_channel(consts.CHROM_MAP_CHANNEL)
				note_buttons_raw.append(button)

		self['Note_Button_Matrix'] = ButtonMatrixElement(rows=[note_buttons_raw], name='Note_Button_Matrix')

		def make_raw_drum_matrix():
			result = []
			for row in range(7, -1, -1):
				button_row = []
				row_offset = 8 + (7 - row) * 4
				for column in range(8):
					column_offset = 28 if column >= 4 else 0
					identifier = row * 8 + column + row_offset + column_offset
					matrix_coords = self['Main_Button_Matrix_Ids'].get(identifier)
					if matrix_coords:
						button_row.append(self['Main_Button_Matrix_Raw'][matrix_coords[1]][matrix_coords[0]])
					else:
						button_row.append(make_button('Drum_Note_Button_' + str(identifier), 0, identifier, MIDI_NOTE_TYPE))

				result.append(button_row)

			return result


		self['Drum_Button_Matrix'] = ButtonMatrixElement(rows=make_raw_drum_matrix(), name='Drum_Button_Matrix')
		self.add_matrix('Slider_Button_Matrix', make_slider, 0, [[ identifier for identifier in range(21, 29) ]], MIDI_CC_TYPE)
		for index, slider in enumerate(self['Slider_Button_Matrix_Raw'][0]):
			slider.set_index(index)

		self.create_user_mode_controls()


	def create_user_mode_controls(self):
		"""
		Creates control elements that aren't used in the script
		but need to exist so they can be grabbed and observed
		via Max for Live.
		"""
		for channel in consts.USER_MODE_CHANNELS:
			channel_name = channel + 1
			self.add_matrix('User_Button_Matrix_Ch_%d' % (channel_name,), make_button, channel, consts.USER_MATRIX_IDENTIFIERS, MIDI_NOTE_TYPE)
			self.add_matrix('User_Left_Side_Button_Matrix_Ch_%d' % (channel_name,), make_button, channel, [ [identifier] for identifier in range(108, 116) ], MIDI_NOTE_TYPE)
			self.add_matrix('User_Right_Side_Button_Matrix_Ch_%d' % (channel_name,), make_button, channel, [ [identifier] for identifier in range(100, 108) ], MIDI_NOTE_TYPE)
			self.add_matrix('User_Bottom_Button_Matrix_Ch_%d' % (channel_name,), make_button, channel, [[ identifier for identifier in range(116, 124) ]], MIDI_NOTE_TYPE)
			self.add_matrix('User_Arrow_Button_Matrix_Ch_%d' % (channel_name,), make_button, channel, [[ identifier for identifier in range(91, 95) ]], MIDI_CC_TYPE)


	def with_shift(self, button_name):
		return ComboElement(self[button_name], modifier=[self['Shift_Button']],) # name=u'Shifted_' + button_name)


	def with_session_button(self, button):
		return ComboElement(button, modifier=[self['Session_Mode_Button']],) #  name=button.name + u'_With_Session_Button')



class Launchpad_Pro(IdentifiableControlSurface):
	identity_request = consts.SYSEX_IDENTITY_REQUEST


	device_provider_class = ModDeviceProvider
	monomodular = None
	_monomod_version = 'b996'
	_host_name = 'LaunchMod'
	_color_type = 'Push'

	def __init__(self, c_instance, *a, **k):
		product_id_bytes = consts.MANUFACTURER_ID + consts.DEVICE_CODE
		self.log_message = logger.warning
		super(Launchpad_Pro, self).__init__(c_instance=c_instance, product_id_bytes=product_id_bytes, *a, **k)
		self._challenge = Live.Application.get_random_int(0, 400000000) & 2139062143
		with self.component_guard():
			self._skin = make_default_skin()
			with inject(skin=const(self._skin)).everywhere():
				self._midimap = MidiMap()
			self._target_track_component = TargetTrackComponent(name='Target_Track')
			self._create_background()
			self._create_global_component()
			self._last_sent_mode_byte = None
			with inject(layout_setup=const(self._layout_setup), should_arm=const(self._should_arm_track)).everywhere():
				self._create_session()
				self._create_recording()
				self._create_actions()
				self._create_drums()
				self._create_mixer()
				self._setup_mod()
				self._create_device()
				self._create_modes()
				self._create_user()
			self._on_session_record_changed.subject = self.song
		#self.set_device_component(self._device)
		self._on_session_record_changed()


	def disconnect(self):
		self._send_midi(consts.TURN_OFF_LEDS)
		self._send_midi(consts.QUIT_MESSAGE)
		super(Launchpad_Pro, self).disconnect()


	def _create_background(self):
		self._modifier_background_component = ModifierBackgroundComponent(name='Background_Component', is_enabled=False, layer=Layer(shift_button=self._midimap['Shift_Button']))
		self._shifted_background = BackgroundComponent(name='No_Op_Shifted_Buttons', is_enabled=False, layer=Layer(click_bitton=self._midimap.with_shift('Click_Button'), delete_button=self._midimap.with_shift('Delete_Button'), duplicate_button=self._midimap.with_shift('Duplicate_Button'), double_button=self._midimap.with_shift('Double_Loop_Button'), session_record_button=self._midimap.with_shift('Session_Record_Button')))


	def _create_global_component(self):
		self._actions_component = ActionsComponent(name='Global_Actions', is_enabled=False, layer=Layer(undo_button=self._midimap['Undo_Button'], redo_button=self._midimap.with_shift('Undo_Button'), metronome_button=self._midimap['Click_Button'], quantization_on_button=self._midimap.with_shift('Quantize_Button')))


	def _create_session(self):
		self._session_ring = SessionRingComponent(num_tracks = NUM_TRACKS, num_scenes = NUM_SCENES)
		self._session_ring.set_enabled(True)

		self._session = SessionComponent(session_ring = self._session_ring, auto_name = True, is_enabled=False,) # layer=Layer(track_bank_left_button=self._midimap[u'Arrow_Left_Button'], track_bank_right_button=self._midimap[u'Arrow_Right_Button'], scene_bank_up_button=self._midimap[u'Arrow_Up_Button'], scene_bank_down_button=self._midimap[u'Arrow_Down_Button']))
		#auto_name = True, enable_skinning=True,
		self._session.set_enabled(True)
		self._session.set_rgb_mode(CLIP_COLOR_TABLE, RGB_COLOR_TABLE)
		self._session_navigation = SessionNavigationComponent(session_ring = self._session_ring)
		self._session_navigation.layer = Layer(left_button=self._midimap['Arrow_Left_Button'], right_button=self._midimap['Arrow_Right_Button'], up_button=self._midimap['Arrow_Up_Button'], down_button=self._midimap['Arrow_Down_Button'])
		SpecialClipSlotComponent.quantization_component = self._actions_component
		for scene_index in range(NUM_SCENES):
			scene = self._session.scene(scene_index)
			scene.layer = Layer(select_button=self._midimap['Shift_Button'], delete_button=self._midimap['Delete_Button'], duplicate_button=self._midimap['Duplicate_Button'])
			for track_index in range(NUM_TRACKS):
				slot = scene.clip_slot(track_index)
				slot.layer = Layer(select_button=self._midimap['Shift_Button'], delete_button=self._midimap['Delete_Button'], duplicate_button=self._midimap['Duplicate_Button'], double_loop_button=self._midimap['Double_Loop_Button'], quantize_button=self._midimap['Quantize_Button'])

		self._session_zoom = SessionZoomingComponent(self._session_ring, name='Session_Overview', is_enabled=True, enable_skinning=True)


	def _create_recording(self):
		self._session_record = SpecialSessionRecordingComponent(target_track_component = self._target_track_component, name='Session_Recording', is_enabled=False, layer=Layer(record_button=self._midimap['Session_Record_Button']))


	def _create_actions(self):
		self._clip_actions_component = ClipActionsComponent(self._target_track_component, name='Clip_Actions', is_enabled=False, layer=Layer(duplicate_button=self._midimap['Duplicate_Button'], double_button=self._midimap['Double_Loop_Button'], quantize_button=self._midimap['Quantize_Button']))
		ClipActionsComponent.quantization_component = self._actions_component


	def _create_drums(self):
		self._drum_group_finder = DrumGroupFinderComponent(self._target_track_component, name='Drum_Group_Finder', is_enabled=False, layer=None)
		self._on_drum_group_changed.subject = self._drum_group_finder
		self._drum_group_finder.set_enabled(True)
		self._drum_group = DrumGroupComponent(self._clip_actions_component, name='Drum_Group_Control', translation_channel=consts.DR_MAP_CHANNEL)
		self._drum_group.set_enabled(True)


	def _create_mixer(self):
		self._mixer = SpecialMixerComponent(tracks_provider = self._session_ring, auto_name=True, is_enabled=True, invert_mute_feedback=True)
		self._mixer.name = 'Mixer_Control'
		#self._session.set_mixer(self._mixer)


	def _create_device(self):
		self._device = SpecialDeviceComponent(name = 'Device_Component', device_bank_registry = DeviceBankRegistry(), device_provider = self._device_provider)
		#name=u'Device_Control', is_enabled=False, device_selection_follows_track_selection=True
		self._device_navigation = DeviceNavigationComponent(name='Device_Navigation')
		self._device_background = BackgroundComponent(name='Device_Background_Component')


	def _setup_drum_group(self):
		self._drum_group.set_drum_group_device(self._drum_group_finder.drum_group)


	def _create_translation(self, comp_name, channel, button_layer, should_enable = True, should_reset = True):
		translation_component = TranslationComponent(name=comp_name, translated_channel=channel, should_enable=should_enable, should_reset=should_reset, is_enabled=False, layer=button_layer)
		setattr(self, '_' + comp_name.lower(), translation_component)
		return translation_component


	def _create_modes(self):
		self._modes = ModesComponent(name='Launchpad_Modes', is_enabled=False)
		self._session_layer_mode = AddLayerMode(self._session, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix'], clip_launch_buttons=self._midimap['Main_Button_Matrix'], delete_button=self._midimap['Delete_Button'], duplicate_button=self._midimap['Duplicate_Button'], double_button=self._midimap['Double_Loop_Button'], quantize_button=self._midimap['Quantize_Button']))
		action_button_background = BackgroundComponent(name='No_Op_Buttons')
		self._action_button_background_layer_mode = LayerMode(action_button_background, Layer(delete_button=self._midimap['Delete_Button'], quantize_button=self._midimap['Quantize_Button'], duplicate_button=self._midimap['Duplicate_Button'], double_button=self._midimap['Double_Loop_Button']))
		self._clip_delete_layer_mode = AddLayerMode(self._clip_actions_component, layer=Layer(delete_button=self._midimap['Delete_Button']))
		self._create_session_zooming_modes()
		self._create_session_mode()
		self._create_note_modes()
		self._create_device_mode()
		self._create_user_mode()
		self._create_record_arm_mode()
		self._create_track_select_mode()
		self._create_mute_mode()
		self._create_solo_mode()
		self._create_volume_mode()
		self._create_pan_mode()
		self._create_sends_mode()
		self._create_stop_clips_mode()
		self._modes.layer = Layer(session_mode_button=self._midimap['Session_Mode_Button'], note_mode_button=self._midimap['Note_Mode_Button'], device_mode_button=self._midimap['Device_Mode_Button'], user_mode_button=self._midimap['User_Mode_Button'], record_arm_mode_button=self._midimap['Record_Arm_Mode_Button'], track_select_mode_button=self._midimap['Track_Select_Mode_Button'], mute_mode_button=self._midimap['Mute_Mode_Button'], solo_mode_button=self._midimap['Solo_Mode_Button'], volume_mode_button=self._midimap['Volume_Mode_Button'], pan_mode_button=self._midimap['Pan_Mode_Button'], sends_mode_button=self._midimap['Sends_Mode_Button'], stop_clip_mode_button=self._midimap['Stop_Clip_Mode_Button'])
		self._modes.selected_mode = 'session_mode'
		self._on_layout_changed.subject = self._modes


	def _create_session_zooming_modes(self):
		session_zoom_layer = Layer(button_matrix=self._midimap['Main_Button_Matrix'], nav_left_button=self._midimap['Arrow_Left_Button'], nav_right_button=self._midimap['Arrow_Right_Button'], nav_up_button=self._midimap['Arrow_Up_Button'], nav_down_button=self._midimap['Arrow_Down_Button'])
		session_zooming_layer_mode = LayerMode(self._session_zoom, session_zoom_layer)
		self._session_zooming_manager = SessionZoomingManagerComponent(self._modes, is_enabled=False)
		session_zooming_button_layer_mode = LayerMode(self._session_zooming_manager, Layer(session_zooming_button=self._midimap['Session_Mode_Button']))
		self._prioritized_session_zooming_button_layer_mode = LayerMode(self._session_zooming_manager, Layer(session_zooming_button=self._midimap['Session_Mode_Button'], priority=1))
		self._session_zooming_background = BackgroundComponent(name='Session_Zooming_Background')
		session_zooming_background_layer_mode = LayerMode(self._session_zooming_background, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix'], delete_button=self._midimap['Delete_Button'], quantize_button=self._midimap['Quantize_Button'], duplicate_button=self._midimap['Duplicate_Button'], double_loop_button=self._midimap['Double_Loop_Button']))
		self._modes.add_mode('session_zooming_mode', [self._session_zooming_manager,
		 self._session_navigation,
		 session_zooming_button_layer_mode,
		 session_zooming_layer_mode,
		 session_zooming_background_layer_mode])
		self._modes.add_mode('prioritized_session_zooming_mode', [partial(self._layout_switch, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_navigation,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 session_zooming_layer_mode,
		 session_zooming_background_layer_mode,
		 self.update])


	def _create_session_mode(self):
		self._modes.add_mode('session_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE), self._session_layer_mode, self._session_navigation, self._session.update_navigation_buttons], behaviour=CancelingReenterBehaviour('session_zooming_mode'))


	def _create_note_modes(self):
		note_mode_matrix_translation = self._create_translation('Note_Mode_Matrix_Translation', consts.CHROM_MAP_CHANNEL, Layer(button_matrix=self._midimap['Main_Button_Matrix'], note_button_matrix=self._midimap['Note_Button_Matrix'], drum_matrix=self._midimap['Drum_Button_Matrix'], mixer_button_matrix=self._midimap['Mixer_Button_Matrix']), should_enable=False)
		note_mode_scene_launch_translation = self._create_translation('Note_Mode_Scene_Launch_Translation', consts.CHROM_MAP_CHANNEL, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix']))
		scale_setup_mode_button_lighting = LedLightingComponent(name='LED_Lighting_Component', is_enabled=False, layer=Layer(button=self._midimap.with_shift('Note_Mode_Button')))
		drum_mode_note_matrix_translation = self._create_translation('Drum_Mode_Note_Button_Translation', 0, Layer(note_button_matrix=self._midimap['Note_Button_Matrix']), should_enable=False, should_reset=False)
		drum_group_layer_mode = LayerMode(self._drum_group, layer=Layer(scroll_up_button=self._midimap['Arrow_Left_Button'], scroll_down_button=self._midimap['Arrow_Right_Button'], scroll_page_up_button=self._midimap['Arrow_Up_Button'], scroll_page_down_button=self._midimap['Arrow_Down_Button'], drum_matrix=self._midimap['Drum_Button_Matrix'], select_button=self._midimap['Shift_Button'], delete_button=self._midimap['Delete_Button']))
		self._note_modes = SpecialModesComponent(name='Note_Modes')
		self._note_modes.add_mode('chromatic_mode', [partial(self._layout_setup, consts.NOTE_LAYOUT_SYSEX_BYTE),
		 self._clip_delete_layer_mode,
		 note_mode_matrix_translation,
		 scale_setup_mode_button_lighting])
		self._note_modes.add_mode('drum_mode', [partial(self._layout_setup, consts.DRUM_LAYOUT_SYSEX_BYTE),
		 self._setup_drum_group,
		 drum_group_layer_mode,
		 drum_mode_note_matrix_translation])
		self._note_modes.add_mode('audio_mode', [partial(self._layout_setup, consts.AUDIO_LAYOUT_SYSEX_BYTE), self._clip_delete_layer_mode])
		self._note_modes.add_mode('mod', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE), self.modhandler])
		self._note_modes.set_enabled(False)
		self._modes.add_mode('note_mode', [note_mode_scene_launch_translation,
		 self._note_modes,
		 self._select_note_mode,
		 self._select_target_track,
		 self._clip_actions_component,
		 self._show_playing_clip,
		 self._set_clip_actions_type], behaviour=ReenterBehaviour(self.toggle_detail_view))
		self._session_record.set_modes_component(self._modes)
		self._session_record.set_note_mode_name('note_mode')


	def _create_device_mode(self):
		device_mode_scene_launch_translation = self._create_translation('Device_Mode_Scene_Launch_Translation', consts.DEVICE_MAP_CHANNEL, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix']))
		device_layer_mode = LayerMode(self._device, layer=Layer(parameter_controls=self._midimap['Slider_Button_Matrix']))
		device_nav_layer_mode = LayerMode(self._device_navigation, layer=Layer(device_nav_left_button=self._midimap['Arrow_Left_Button'], device_nav_right_button=self._midimap['Arrow_Right_Button']))
		device_background_layer_mode = LayerMode(self._device_background, layer=Layer(arrow_up_button=self._midimap['Arrow_Up_Button'], arrow_down_button=self._midimap['Arrow_Down_Button']))
		self._modes.add_mode('device_mode', [partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
		 self._device,
		 device_layer_mode,
		 device_nav_layer_mode,
		 device_background_layer_mode,
		 self._clip_actions_component,
		 self._clip_delete_layer_mode,
		 device_mode_scene_launch_translation,
		 self._show_playing_clip,
		 self._set_clip_actions_type], behaviour=ReenterBehaviour(self.toggle_detail_view))


	def _create_user_mode(self):
		self._modes.add_mode('user_mode', [partial(self._layout_setup, consts.USER_LAYOUT_SYSEX_BYTE)])


	def _create_record_arm_mode(self):
		arm_layer_mode = LayerMode(self._mixer, layer=Layer(arm_buttons=self._midimap['Mixer_Button_Matrix']))
		self._modes.add_mode('record_arm_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_layer_mode,
		 arm_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_track_select_mode(self):
		track_select_layer_mode = LayerMode(self._mixer, layer=Layer(track_select_buttons=self._midimap['Mixer_Button_Matrix']))
		self._modes.add_mode('track_select_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_layer_mode,
		 track_select_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_mute_mode(self):
		mute_layer_mode = LayerMode(self._mixer, layer=Layer(mute_buttons=self._midimap['Mixer_Button_Matrix']))
		self._modes.add_mode('mute_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_layer_mode,
		 mute_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_solo_mode(self):
		solo_layer_mode = LayerMode(self._mixer, layer=Layer(solo_buttons=self._midimap['Mixer_Button_Matrix']))
		self._modes.add_mode('solo_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_layer_mode,
		 solo_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_volume_mode(self):
		volume_mode_scene_launch_translation = self._create_translation('Volume_Mode_Scene_Launch_Translation', consts.VOLUME_MAP_CHANNEL, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix']))
		volume_layer_mode = LayerMode(self._mixer, layer=Layer(volume_controls=self._midimap['Slider_Button_Matrix']))
		self._modes.add_mode('volume_mode', [partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
		 volume_layer_mode,
		 self._action_button_background_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 volume_mode_scene_launch_translation,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_pan_mode(self):
		pan_mode_scene_launch_translation = self._create_translation('Pan_Mode_Scene_Launch_Translation', consts.PAN_MAP_CHANNEL, Layer(scene_launch_buttons=self._midimap['Scene_Launch_Button_Matrix']))
		pan_layer_mode = LayerMode(self._mixer, layer=Layer(pan_controls=self._midimap['Slider_Button_Matrix']))
		self._modes.add_mode('pan_mode', [partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
		 pan_layer_mode,
		 self._action_button_background_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 pan_mode_scene_launch_translation,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_sends_mode(self):
		send_layer_mode = LayerMode(self._mixer, layer=Layer(send_controls=self._midimap['Slider_Button_Matrix'], send_select_buttons=self._midimap['Scene_Launch_Button_Matrix']))
		self._modes.add_mode('sends_mode', [partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
		 send_layer_mode,
		 self._action_button_background_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def _create_stop_clips_mode(self):
		stop_layer_mode = AddLayerMode(self._session, Layer(stop_track_clip_buttons=self._midimap['Mixer_Button_Matrix'], stop_scene_clip_buttons=self._midimap['Scene_Stop_Button_Matrix'], stop_all_clips_button=self._midimap['Stop_All_Clips_Button']))
		self._modes.add_mode('stop_clip_mode', [partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
		 self._session_layer_mode,
		 stop_layer_mode,
		 self._session_zooming_manager,
		 self._prioritized_session_zooming_button_layer_mode,
		 self._session.update_navigation_buttons], behaviour=SpecialReenterBehaviour('session_mode'))


	def toggle_detail_view(self):
		view = self.application.view
		if view.is_view_visible('Detail'):
			if view.is_view_visible('Detail/DeviceChain'):
				view.show_view('Detail/Clip')
			else:
				view.show_view('Detail/DeviceChain')


	def _create_user(self):
		self._user_matrix_component = UserMatrixComponent(name='User_Matrix_Component', is_enabled=False, layer=Layer(user_button_matrix_ch_6=self._midimap['User_Button_Matrix_Ch_6'], user_button_matrix_ch_7=self._midimap['User_Button_Matrix_Ch_7'], user_button_matrix_ch_8=self._midimap['User_Button_Matrix_Ch_8'], user_button_matrix_ch_14=self._midimap['User_Button_Matrix_Ch_14'], user_button_matrix_ch_15=self._midimap['User_Button_Matrix_Ch_15'], user_button_matrix_ch_16=self._midimap['User_Button_Matrix_Ch_16'], user_left_side_button_matrix_ch_6=self._midimap['User_Left_Side_Button_Matrix_Ch_6'], user_left_side_button_matrix_ch_7=self._midimap['User_Left_Side_Button_Matrix_Ch_7'], user_left_side_button_matrix_ch_8=self._midimap['User_Left_Side_Button_Matrix_Ch_8'], user_left_side_button_matrix_ch_14=self._midimap['User_Left_Side_Button_Matrix_Ch_14'], user_left_side_button_matrix_ch_15=self._midimap['User_Left_Side_Button_Matrix_Ch_15'], user_left_side_button_matrix_ch_16=self._midimap['User_Left_Side_Button_Matrix_Ch_16'], user_right_side_button_matrix_ch_6=self._midimap['User_Right_Side_Button_Matrix_Ch_6'], user_right_side_button_matrix_ch_7=self._midimap['User_Right_Side_Button_Matrix_Ch_7'], user_right_side_button_matrix_ch_8=self._midimap['User_Right_Side_Button_Matrix_Ch_8'], user_right_side_button_matrix_ch_14=self._midimap['User_Right_Side_Button_Matrix_Ch_14'], user_right_side_button_matrix_ch_15=self._midimap['User_Right_Side_Button_Matrix_Ch_15'], user_right_side_button_matrix_ch_16=self._midimap['User_Right_Side_Button_Matrix_Ch_16'], user_bottom_button_matrix_ch_6=self._midimap['User_Bottom_Button_Matrix_Ch_6'], user_bottom_button_matrix_ch_7=self._midimap['User_Bottom_Button_Matrix_Ch_7'], user_bottom_button_matrix_ch_8=self._midimap['User_Bottom_Button_Matrix_Ch_8'], user_bottom_button_matrix_ch_14=self._midimap['User_Bottom_Button_Matrix_Ch_14'], user_bottom_button_matrix_ch_15=self._midimap['User_Bottom_Button_Matrix_Ch_15'], user_bottom_button_matrix_ch_16=self._midimap['User_Bottom_Button_Matrix_Ch_16'], user_arrow_button_matrix_ch_6=self._midimap['User_Arrow_Button_Matrix_Ch_6'], user_arrow_button_matrix_ch_7=self._midimap['User_Arrow_Button_Matrix_Ch_7'], user_arrow_button_matrix_ch_8=self._midimap['User_Arrow_Button_Matrix_Ch_8'], user_arrow_button_matrix_ch_14=self._midimap['User_Arrow_Button_Matrix_Ch_14'], user_arrow_button_matrix_ch_15=self._midimap['User_Arrow_Button_Matrix_Ch_15'], user_arrow_button_matrix_ch_16=self._midimap['User_Arrow_Button_Matrix_Ch_16']))
		self._user_matrix_component.set_enabled(True)


	def _setup_mod(self):

		self.monomodular = get_monomodular(self)
		self.monomodular.name = 'monomodular_switcher'
		#with inject(register_component = const(self._register_component), song = const(self.song)).everywhere():
		self.modhandler = LaunchModHandler(self) ## song = self.song, register_component = self._register_component)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer( priority = 6, 	grid = self._midimap['Main_Button_Matrix'],
																			Shift_button = self._midimap['Shift_Button'],
																			Alt_button = self._midimap['Note_Mode_Button'],
																			key_buttons = self._midimap['Scene_Launch_Button_Matrix'])
																			#lock_button = self.elements.note_mode_button,
		self.modhandler.legacy_shift_layer = AddLayerMode( self.modhandler, Layer(priority = 6,
																			nav_up_button = self._midimap['Arrow_Up_Button'],
																			nav_down_button = self._midimap['Arrow_Down_Button'],
																			nav_left_button = self._midimap['Arrow_Left_Button'],
																			nav_right_button = self._midimap['Arrow_Right_Button'],
																			channel_buttons = self._midimap['Main_Button_Matrix'].submatrix[:, 1:2],
																			nav_matrix = self._midimap['Main_Button_Matrix'].submatrix[4:8, 2:6] ))
		self.modhandler.shift_layer = AddLayerMode( self.modhandler, Layer( priority = 6,
																			device_selector_matrix = self._midimap['Main_Button_Matrix'].submatrix[:, :1],))
																			#lock_button = self.elements.master_select_button,))
		self.modhandler.alt_layer = AddLayerMode( self.modhandler, Layer( priority = 6,))


	@listens('drum_group')
	def _on_drum_group_changed(self):
		if self._note_modes.selected_mode == 'drum_mode':
			self._drum_group.set_drum_group_device(self._drum_group_finder.drum_group)
		if self._modes.selected_mode == 'note_mode':
			self._select_note_mode()
		else:
			self.release_controlled_track()
		self._update_note_mode_button(self._drum_group_finder.drum_group is not None)


	def _select_note_mode(self):
		"""
		Selects which note mode to use depending on the kind of
		current target track and its device chain.	Will also
		select the target if specified.
		"""
		track = self._target_track_component.target_track
		drum_device = self._drum_group_finder.drum_group
		debug('select_note_mode: ' + str(self.modhandler.active_mod()) + ' ' + str(len(track.devices)))
		if not (self._note_modes.selected_mode is 'mod' and self.modhandler.is_locked()):
			if track is None or track.is_foldable or track in self.song.return_tracks or track == self.song.master_track or track.is_frozen:
				self._note_modes.selected_mode = 'audio_mode'
			elif self.modhandler.active_mod():
				self._note_modes.selected_mode = 'mod'
			elif track.has_audio_input:
				self._note_modes.selected_mode = 'audio_mode'
			elif drum_device:
				self._note_modes.selected_mode = 'drum_mode'
			else:
				self._note_modes.selected_mode = 'chromatic_mode'
			self._modes.update()
			if self._note_modes.selected_mode == 'audio_mode' or self._note_modes.selected_mode == 'mod':
				self.release_controlled_track()
			else:
				self.set_controlled_track(self._target_track_component.target_track)
		debug('_select_note_mode:', self._note_modes.selected_mode)


	def set_highlighting_session_component(self, session_component):
		self._highlighting_session_component = session_component
		session_component and self._highlighting_session_component.set_highlighting_callback(self._set_session_highlight)


	def _select_target_track(self):
		track = self._target_track_component.target_track
		if track != self.song.view.selected_track:
			self.song.view.selected_track = track


	def _update_note_mode_button(self, focused_track_is_drum_track):
		button = self._midimap['Note_Mode_Button']
		if focused_track_is_drum_track:
			button.default_states = {True: 'Mode.Drum.On',
			 False: 'Mode.Drum.Off'}
		else:
			button.default_states = {True: 'Mode.Chromatic.On',
			 False: 'Mode.Chromatic.Off'}
		button.reset_state()
		self._modes.update()


	def _show_playing_clip(self):
		track = None
		if self._use_sel_track():
			track = self.song.view.selected_track
		else:
			track = self._target_track_component.target_track
		if track in self.song.tracks:
			slot_index = track.fired_slot_index
			if slot_index < 0:
				slot_index = track.playing_slot_index
			if slot_index >= 0:
				clip_slot = track.clip_slots[slot_index]
				self.song.view.highlighted_clip_slot = clip_slot


	def _set_clip_actions_type(self):
		self._clip_actions_component.use_selected_track(self._use_sel_track())
		self._clip_actions_component.update()


	def _use_sel_track(self):
		return self._modes.selected_mode == 'device_mode'


	def _should_arm_track(self):
		return self._modes.selected_mode == 'record_arm_mode'


	@listens('selected_mode')
	def _on_layout_changed(self, mode):
		if mode == 'note_mode':
			self.set_controlled_track(self._target_track_component.target_track)
		else:
			self.release_controlled_track()
		self._session_record.set_enabled(mode != 'user_mode')


	@listens('session_record')
	def _on_session_record_changed(self):
		status = self.song.session_record
		feedback_color = int(5 if status else 21)
		self._c_instance.set_feedback_velocity(feedback_color)


	def _clear_send_cache(self):
		with self.component_guard():
			for control in self.controls:
				control.clear_send_cache()


	def _update_hardware(self):
		self._clear_send_cache()
		self.update()


	def _update_global_components(self):
		self._actions_component.update()
		self._session_record.update()
		self._modifier_background_component.update()


	def _layout_setup(self, mode):
		self._layout_switch(mode)
		self._clear_send_cache()
		self._update_global_components()


	def _layout_switch(self, mode):
		prefix = consts.SYSEX_STANDARD_PREFIX + consts.SYSEX_PARAM_BYTE_LAYOUT
		suffix = consts.SYSEX_STANDARD_SUFFIX
		self._send_midi(prefix + mode + suffix)
		self._last_sent_mode_byte = mode


	def port_settings_changed(self):
		#self.set_highlighting_session_component(None)
		super(Launchpad_Pro, self).port_settings_changed()


	def on_identified(self, *a, **k):
		self._send_challenge()


	def _send_challenge(self, *a, **k):
		challenge_bytes = []
		for index in range(4):
			challenge_bytes.append(self._challenge >> 8 * index & 127)

		challenge = consts.CHALLENGE_PREFIX + tuple(challenge_bytes) + (247,)
		self._send_midi(challenge)


	def _on_handshake_successful(self):
		self._do_send_midi(consts.LIVE_MODE_SWITCH_REQUEST)
		with self.component_guard():
			self._modes.set_enabled(True)
			self._actions_component.set_enabled(True)
			self._session_record.set_enabled(True)
			self._modifier_background_component.set_enabled(True)
			self._shifted_background.set_enabled(True)
			self.release_controlled_track()
			self.set_feedback_channels(consts.FEEDBACK_CHANNELS)
		if self._last_sent_mode_byte is not None:
			self._layout_setup(self._last_sent_mode_byte)
		#self.set_highlighting_session_component(self._session)
		self.update()


	def _is_challenge_response(self, midi_bytes):
		return len(midi_bytes) == 10 and midi_bytes[:7] == consts.SYSEX_STANDARD_PREFIX + consts.SYSEX_CHALLENGE_RESPONSE_BYTE


	def _is_response_valid(self, midi_bytes):
		response = int(midi_bytes[7])
		response += int(midi_bytes[8] << 8)
		return response == Live.Application.encrypt_challenge2(self._challenge)


	def process_midi_bytes(self, midi_bytes, midi_processor):
		if len(midi_bytes) < 7:
			super(Launchpad_Pro, self).process_midi_bytes(midi_bytes, midi_processor)
		elif self._is_challenge_response(midi_bytes) and self._is_response_valid(midi_bytes):
			self._on_handshake_successful()
		elif midi_bytes[6] == consts.SYSEX_STATUS_BYTE_LAYOUT and midi_bytes[7] == consts.NOTE_LAYOUT_SYSEX_BYTE[0]:
			self._update_hardware()
		elif midi_bytes[6] in (consts.SYSEX_STATUS_BYTE_MODE, consts.SYSEX_STATUS_BYTE_LAYOUT):
			pass
		else:
			super(Launchpad_Pro, self).process_midi_bytes(midi_bytes, midi_processor)



class LaunchModHandler(ModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()

	def __init__(self, *a, **k):
		self._grid = None
		super(LaunchModHandler, self).__init__(*a, **k)
		self.nav_box = NavigationBox(self, 16, 16, 8, 8, self.set_offset,) # song = self.song, register_component = self.register_component, is_enabled = False))
		self._push_colors = list(range(128))
		self._push_colors[1:8] = [3, 85, 33, 95, 5, 21, 67]
		self._push_colors[127] = 67
		self._shifted = False


	def select_mod(self, mod):
		super(LaunchModHandler, self).select_mod(mod)
		self._script._select_note_mode()
		self.update()
		debug('modhandler select mod: ' + str(mod))


	def _receive_grid(self, x, y, value = -1, identifier = -1, channel = -1, *a, **k):
		#debug('_receive_base_grid:', x, y, value, identifier, channel)
		mod = self.active_mod()
		if mod and self._grid_value.subject:
			if mod.legacy:
				x = x-self.x_offset
				y = y-self.y_offset
			if x in range(8) and y in range(8):
				value > -1 and self._grid_value.subject.send_value(x, y, self._push_colors[self._colors[value]], True)
				button = self._grid_value.subject.get_button(y, x)
				if button:
					new_identifier = identifier if identifier > -1 else button._original_identifier
					new_channel = channel if channel > -1 else button._original_channel
					button._msg_identifier != new_identifier and button.set_identifier(new_identifier)
					button._msg_channel != new_channel and button.set_channel(new_channel)
					button.set_enabled((channel, identifier) == (-1, -1))


	def _receive_key(self, x, value):
		#debug('_receive_key:', x, value)
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._push_colors[self._colors[value]], True)


	def update_device(self):
		if self.is_enabled() and not self._device_component is None:
			self._device_component.update()
			self._device_component._update_parameters()


	@listens('value')
	def _shift_value(self, value, *a, **k):
		debug('mod shift value:', value)
		self._is_shifted = not value is 0
		mod = self.active_mod()
		if mod:
			mod.send('shift', value)
		if self._is_shifted:
			self.shift_layer and self.shift_layer.enter_mode()
			if mod and mod.legacy:
				self.legacy_shift_layer and self.legacy_shift_layer.enter_mode()

		else:
			self.legacy_shift_layer and self.legacy_shift_layer.leave_mode()
			self.shift_layer and self.shift_layer.leave_mode()
		self.update()


	@Shift_button.pressed
	def Shift_button(self, button):
		debug('shift_button.pressed')
		self._is_shifted = True
		mod = self.active_mod()
		if mod:
			mod.send('shift', 1)
		self.shift_layer and self.shift_layer.enter_mode()
		if mod and mod.legacy:
			self.legacy_shift_layer and self.legacy_shift_layer.enter_mode()
		self.update()


	@Shift_button.released
	def Shift_button(self, button):
		self._is_shifted = False
		mod = self.active_mod()
		if mod:
			mod.send('shift', 0)
		self.legacy_shift_layer and self.legacy_shift_layer.leave_mode()
		self.shift_layer and self.shift_layer.leave_mode()
		self.update()


	@Alt_button.pressed
	def Alt_button(self, button):
		debug('alt_button.pressed')
		self._is_alted = True
		mod = self.active_mod()
		if mod:
			mod.send('alt', 1)
			mod._device_proxy._alted = True
			mod._device_proxy.update_parameters()
		self.alt_layer and self.alt_layer.enter_mode()
		self.update()


	@Alt_button.released
	def Alt_button(self, button):
		self._is_alted = False
		mod = self.active_mod()
		if mod:
			mod.send('alt', 0)
			mod._device_proxy._alted = False
			mod._device_proxy.update_parameters()
		self.alt_layer and self.alt_layer.leave_mode()
		self.update()


	def update(self, *a, **k):
		mod = self.active_mod()
		if not mod is None:
			mod.restore()
		else:
			if not self._grid_value.subject is None:
				self._grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()



#
