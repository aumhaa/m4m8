# by amounra 0217 : http://www.aumhaa.com
# written against Live 10.0.5 on 102318

import Live
from itertools import chain, starmap
from functools import partial
from ableton.v2.control_surface import Component, ClipCreator, Layer
from ableton.v2.control_surface.components import SessionRingComponent, SessionComponent, ViewControlComponent, PlayableComponent, DrumGroupComponent
from ableton.v2.base import listens, listens_group, forward_property, find_if, first, in_range, product, clamp, listenable_property, liveobj_changed
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement, DisplayDataSource
from ableton.v2.control_surface.mode import ModesComponent, AddLayerMode, LayerMode, ModeButtonBehaviour
from ableton.v2.base.task import *
from ableton.v2.control_surface.components.session_recording import *
from ableton.v2.base import task
from ableton.v2.control_surface.control import control_list, ButtonControl, StepEncoderControl, ToggleButtonControl, control_color, PlayableControl, control_matrix
from ableton.v2.control_surface.percussion_instrument_finder import PercussionInstrumentFinder as DrumGroupFinderComponent, find_drum_group_device
from pushbase.step_seq_component import StepSeqComponent
#from pushbase.percussion_instrument_finder import PercussionInstrumentFinder as DrumGroupFinderComponent, find_drum_group_device
from pushbase.note_editor_component import NoteEditorComponent
from pushbase.loop_selector_component import LoopSelectorComponent
from pushbase.playhead_component import PlayheadComponent
from pushbase.grid_resolution import GridResolution
from pushbase.pad_control import PadControl


from aumhaa.v2.control_surface.mono_modes import CancellableBehaviour, CancellableBehaviourWithRelease
from aumhaa.v2.control_surface.components.channelized_settings import ChannelizedSettingsBase, ScrollingChannelizedSettingsComponent, ToggledChannelizedSettingsComponent, TaggedSettingsComponent
from aumhaa.v2.control_surface.components.mono_keygroup import MonoKeyGroupComponent
from aumhaa.v2.control_surface.components.mono_drumgroup import MonoDrumGroupComponent
from aumhaa.v2.control_surface.instrument_consts import *
from aumhaa.v2.base import initialize_debug

debug = initialize_debug()


def is_triplet_quantization(triplet_factor):
	return triplet_factor == 0.75



def song():
	return Live.Application.get_application().get_document()



def get_instrument_type(track, scale, settings):
	instrument_type = 'keypad'
	if scale is 'Auto':
		for device in track.devices:
			if isinstance(device, Live.Device.Device):
				if device.class_name == 'DrumGroupDevice':
					instrument_type = 'drumpad'
					break
	elif scale is 'DrumPad' or settings['DefaultAutoScale'] is 'DrumPad':
		instrument_type = 'drumpad'
	return instrument_type



class ShiftCancellableBehaviourWithRelease(CancellableBehaviour):


	def release_delayed(self, component, mode):
		component.pop_mode(mode)


	def update_button(self, component, mode, selected_mode):
		pass



class OffsetTaggedSetting(TaggedSettingsComponent, ScrollingChannelizedSettingsComponent):


	_set_attribute_tag_model = lambda self, a: int(a)


class ScaleTaggedSetting(TaggedSettingsComponent, ScrollingChannelizedSettingsComponent):


	_set_attribute_tag_model = lambda self, a: str(a)


class ToggledTaggedSetting(TaggedSettingsComponent, ChannelizedSettingsBase):


	_set_attribute_tag_model = lambda self, a: str(a)

	split_toggle = ToggleButtonControl(toggled_color = 'MonoInstrument.SplitModeOnValue', untoggled_color = 'DefaultButton.Off')
	seq_toggle = ToggleButtonControl(toggled_color = 'MonoInstrument.SequencerModeOnValue', untoggled_color = 'DefaultButton.Off')

	def __init__(self, *a, **k):
		super(ToggledTaggedSetting, self).__init__(value_dict = ['none', 'seq', 'split',], *a, **k)


	@split_toggle.toggled
	def split_toggle(self, toggled, button):
		self.value = 'none' if self.value == 'split' else 'split'
		self.update()


	@seq_toggle.toggled
	def seq_toggle(self, toggled, button):
		self.value = 'none' if self.value == 'seq' else 'seq'
		self.update()


	def _update_controls(self):
		self.split_toggle.is_toggled = bool(self.value is 'split')
		self.seq_toggle.is_toggled = bool(self.value is 'seq')



"""
Playhead notes must be set for .note and .triplet to the ids of the buttons on the controller in the PlayheadComponent, as well as Feedback Channels (must be list).
Feedback channels for playhead are locked to Ch.15, we overloaded NoteEditor to get it there instead of the default Ch.2 so Playhead feedback needs to be set to that channel as well.
Feedback channels for track notes are set via control_surface.set_feedback channels and control_surface.set_controlled_track
"""

class SpecialPlayheadComponent(PlayheadComponent):

	def update(self):
		super(SpecialPlayheadComponent, self).update()
		debug('SpecialPlayheadComponent.update()')
		debug('self._playhead:', self._playhead)
		debug('enabled:', self.is_enabled())
		#debug('liveobj_valid:', liveobj_valid(self._clip))
		if self.is_enabled() and self.song.is_playing and liveobj_valid(self._clip):
			if self._clip.is_arrangement_clip or self._clip.is_playing:
				clip = self._clip
				is_triplet = self._grid_resolution.clip_grid[1]
				notes = self._triplet_notes if is_triplet else self._notes
				debug('clip:', clip.name if hasattr(clip, 'name') else None)
				debug('notes:', notes)
				debug('wrap_around:', self._follower.is_following and self._paginator.can_change_page)
				debug('start_time:', self._paginator.page_length * self._paginator.page_index)
				debug('step_length:', self._paginator.page_length / len(notes))
				debug('feedback_channels:', self._feedback_channels)



	def set_clip(self, clip):
		debug('*******************Playhead.set_clip:', clip.name if clip and hasattr(clip, 'name') else None)
		super(SpecialPlayheadComponent, self).set_clip(clip)

	@listens('page')
	def _on_page_changed(self):
		debug('*******************Playhead._on_page_changed()')
		self.update()

	@listens('playing_status')
	def _on_playing_status_changed(self):
		debug('*******************Playhead._on_page_changed()')
		self.update()

	@listens('is_playing')
	def _on_song_is_playing_changed(self):
		debug('*******************Playhead._on_playing_status_changed()')
		self.update()

	@listens('is_following')
	def _on_follower_is_following_changed(self, value):
		debug('*******************Playhead._on_follower_is_following_changed()')
		self.update()



class MonoStepSeqComponent(StepSeqComponent):


	def __init__(self, *a, **k):
		super(MonoStepSeqComponent, self).__init__(*a, **k)
		self._playhead_component = PlayheadComponent(parent=self, grid_resolution=self._grid_resolution, paginator=self.paginator, follower=self._loop_selector, notes=chain(*starmap(range, ((92, 100),
		 (84, 92),
		 (76, 84),
		 (68, 76)))), triplet_notes=chain(*starmap(range, ((92, 98),
		 (84, 90),
		 (76, 82),
		 (68, 74)))), feedback_channels=[15])
		self._loop_selector.follow_detail_clip = True
		self._loop_selector._on_detail_clip_changed.subject = self.song.view
		self._update_delay_task = self._tasks.add(task.sequence(task.wait(.1), task.run(self._update_delayed)))
		self._update_delay_task.kill()


	def update(self):
		"""We need to delay the update task, as on_detail_clip_changed (triggering set_detail_clip() in loopselector) causes all stored sequencer states to zero out while modes are switching"""
		super(StepSeqComponent, self).update()
		self._update_delay_task.restart()


	def _update_delayed(self):
		self._on_detail_clip_changed()
		self._update_playhead_color()
		self._update_delay_task.kill()


	def set_follow_button(self, button):
		#self._loop_selector.set_follow_button(button)
		pass


	def set_solo_button(self, button):
		debug('set_solo_button:', button, hasattr(self._instrument, 'set_solo_button'))
		hasattr(self._instrument, 'set_solo_button') and self._instrument.set_solo_button(button)



class MonoNoteEditorComponent(NoteEditorComponent):


	"""Custom function for displaying triplets for different grid sizes, called by _visible steps"""
	_visible_steps_model = lambda self, indices: [k for k in indices if k % 4 != 3]
	#_matrix = None
	matrix = control_matrix(PadControl, channel=15, sensitivity_profile='loop', mode=PlayableControl.Mode.listenable)

	"""First we need to reset the state (chan, id) of each button of the matrix that was previously grabbed so that it doesn't display the playhead when it's given to something else"""
	"""Next we need to override the channel that each control is set to in this function, as it is hardcoded from a header definition in the module"""
	"""def set_button_matrix(self, matrix):
		if self._matrix:
			for button, _ in filter(first, self._matrix.iterbuttons()):
				button.reset_state()
		super(MonoNoteEditorComponent, self).set_button_matrix(matrix)
		if matrix:
			for button, _ in filter(first, matrix.iterbuttons()):
				button.set_channel(15)"""

	"""
	def set_matrix(self, matrix):
		if self._matrix:
			for button, _ in filter(first, self._matrix.iterbuttons()):
				button.reset_state()
		self._matrix = matrix
		super(MonoNoteEditorComponent, self).set_matrix(matrix)
		if matrix:
			for button, _ in filter(first, matrix.iterbuttons()):
				button.set_channel(15)
	"""

	@matrix.pressed
	def matrix(self, button):
		super(MonoNoteEditorComponent, self)._on_pad_pressed(button.coordinate)

	@matrix.released
	def matrix(self, button):
		super(MonoNoteEditorComponent, self)._on_pad_released(button.coordinate)

	def _on_pad_pressed(self, coordinate):
		y, x = coordinate
		debug('MonoNoteEditorComponent._on_pad_pressed:', y, x)
		super(MonoNoteEditorComponent, self)._on_pad_pressed(coordinate)


	def _visible_steps(self):
		first_time = self.page_length * self._page_index
		steps_per_page = self._get_step_count()
		step_length = self._get_step_length()
		indices = list(range(steps_per_page))
		if is_triplet_quantization(self._triplet_factor):
			indices = self._visible_steps_model(indices)
		return [ (self._time_step(first_time + k * step_length), index) for k, index in enumerate(indices) ]



class ScaleSessionComponent(SessionComponent):


	_clip_launch_buttons = None

	def __init__(self, *a, **k):
		super(ScaleSessionComponent, self).__init__(*a, **k)
		self._session_ring._update_highlight = lambda : None


	def set_clip_launch_buttons(self, matrix):
		self._clip_launch_buttons = matrix
		if matrix:
			for button, (x,y) in matrix.iterbuttons():
				debug('session button is:', button)
				if button:
					button.display_press = False
					button.set_off_value('DefaultButton.Off')
					button.reset()
					index = x + (y*matrix.width())
					scene = self.scene(index)
					slot = scene.clip_slot(0)
					slot.set_launch_button(button)
			#self._session_ring.update_highlight(ring.tracks_to_use(), ring.song.return_tracks)
		else:
			for x, y in product(range(self._session_ring.num_tracks), range(self._session_ring.num_scenes)):
				scene = self.scene(y)
				slot = scene.clip_slot(x)
				slot.set_launch_button(None)
		self._reassign_tracks()
		self._reassign_scenes()
		self.update()


	def update_current_track(self):
		#for some reason Live returns our tracks in reversed order....
		if self.is_enabled():
			track = self.song.view.selected_track
			track_list = [track for track in reversed(self._session_ring._tracks_to_use())]
			if track in track_list:
				self._session_ring.track_offset = abs(track_list.index(self.song.view.selected_track)-(len(track_list)-1))
			self.update()


	def update(self):
		super(ScaleSessionComponent, self).update()



class MonoScaleComponent(Component):


	_offset_settings_component_class = OffsetTaggedSetting

	def __init__(self, parent, control_surface, skin, grid_resolution, parent_task_group, settings = DEFAULT_INSTRUMENT_SETTINGS, *a, **k):
		super(MonoScaleComponent, self).__init__(*a, **k)
		debug('grid resolution is:', grid_resolution)
		self._settings = settings
		self._parent = parent
		self._control_surface = control_surface
		self._skin = skin
		self._grid_resolution = grid_resolution

		#self._vertical_offset_component = self.register_component(self._offset_settings_component_class(name = 'VerticalOffset', attribute_tag = 'vert_offset', parent_task_group = parent_task_group, value_dict = range(24), default_value_index = self._settings['DefaultVertOffset'], default_channel = 0, on_color = 'MonoInstrument.VerticalOffsetOnValue', off_color = 'MonoInstrument.VerticalOffsetOffValue'))
		self._vertical_offset_component = self._offset_settings_component_class(parent = self, name = 'VerticalOffset', attribute_tag = 'vert_offset', parent_task_group = parent_task_group, value_dict = list(range(24)), default_value_index = self._settings['DefaultVertOffset'], default_channel = 0, on_color = 'MonoInstrument.VerticalOffsetOnValue', off_color = 'MonoInstrument.VerticalOffsetOffValue')
		self._vertical_offset_value.subject = self._vertical_offset_component

		#self._offset_component = self.register_component(self._offset_settings_component_class(name = 'NoteOffset', attribute_tag = 'drum_offset', parent_task_group = parent_task_group, value_dict = range(112), default_value_index = self._settings['DefaultOffset'], default_channel = 0, bank_increment = 12, on_color = 'MonoInstrument.OffsetOnValue', off_color = 'MonoInstrument.OffsetOffValue'))
		self._offset_component = self._offset_settings_component_class(parent = self, name = 'NoteOffset', attribute_tag = 'drum_offset', parent_task_group = parent_task_group, value_dict = list(range(112)), default_value_index = self._settings['DefaultOffset'], default_channel = 0, bank_increment = 12, on_color = 'MonoInstrument.OffsetOnValue', off_color = 'MonoInstrument.OffsetOffValue')
		self._offset_value.subject = self._offset_component
		self.set_offset_shift_toggle = self._offset_component.shift_toggle.set_control_element

		self._keygroup = MonoKeyGroupComponent(settings = self._settings, channel_list = self._settings['Channels'])
		self.set_keypad_matrix = self._keygroup.set_matrix
		self.set_keypad_select_matrix = self._keygroup.set_select_matrix

		scale_clip_creator = ClipCreator()
		scale_note_editor = MonoNoteEditorComponent(clip_creator=scale_clip_creator, grid_resolution=grid_resolution)
		self._note_sequencer = MonoStepSeqComponent(parent = self, clip_creator=scale_clip_creator, skin=skin, grid_resolution=self._grid_resolution, name='Note_Sequencer', note_editor_component=scale_note_editor, instrument_component=self._keygroup )
		#self._note_sequencer._playhead_component._follower = self._note_sequencer._loop_selector  ##########pull this if everything works, it was a test
		self._note_sequencer._playhead_component._notes=tuple(chain(*starmap(range, ((60, 68), (52, 60)))))
		self._note_sequencer._playhead_component._triplet_notes=tuple(chain(*starmap(range, ((60, 66), (52, 58)))))
		self._note_sequencer._playhead_component._feedback_channels = [15]
		self._note_sequencer._note_editor._visible_steps_model = lambda indices: [k for k in indices if k % 8 not in (6, 7)]
		self.set_playhead = self._note_sequencer.set_playhead
		self.set_loop_selector_matrix = self._note_sequencer.set_loop_selector_matrix
		self.set_quantization_buttons = self._note_sequencer.set_quantization_buttons
		self.set_follow_button = self._note_sequencer.set_follow_button
		self.set_sequencer_matrix = self._note_sequencer.set_button_matrix
		#self.register_component(self._note_sequencer)

		self.set_split_matrix = self._parent._selected_session.set_clip_launch_buttons


	@listens('value')
	def _vertical_offset_value(self, value):
		#debug('_vertical_offset_value', value)
		self._keygroup.vertical_offset = value
		#self._set_device_attribute(self._top_device(), 'vertoffset', value)
		self._vertical_offset_component.buttons_are_pressed() and self._control_surface.show_message('New vertical offset is ' + str(value))


	@listens('value')
	def _offset_value(self, value):
		#debug('offset_value', value)
		self._keygroup.offset = value
		#self._set_device_attribute(self._top_device(), 'offset', offset)
		self._offset_component.buttons_are_pressed() and self._control_surface.show_message('New root is Note# ' + str(value) + ', ' + str(NOTENAMES[value]))


	def update(self):
		super(MonoScaleComponent, self).update()
		#debug('monoscale enabled:', self.is_enabled())



class MonoDrumpadComponent(Component):

	_offset_settings_component_class = OffsetTaggedSetting

	def __init__(self, parent, control_surface, skin, grid_resolution, parent_task_group, settings = DEFAULT_INSTRUMENT_SETTINGS, *a, **k):
		super(MonoDrumpadComponent, self).__init__(*a, **k)
		self._settings = settings
		self._parent = parent
		self._control_surface = control_surface
		self._skin = skin
		self._grid_resolution = grid_resolution

		#self._drum_offset_component = self.register_component(self._offset_settings_component_class(attribute_tag = 'drum_offset', name = 'DrumPadOffset', parent_task_group = parent_task_group, value_dict = range(28), default_value_index = self._settings['DefaultDrumOffset'], default_channel = 0, bank_increment = 4, on_color = 'MonoInstrument.OffsetOnValue', off_color = 'MonoInstrument.OffsetOffValue'))
		self._drum_offset_component = self._offset_settings_component_class(parent = self, attribute_tag = 'drum_offset', name = 'DrumPadOffset', parent_task_group = parent_task_group, value_dict = list(range(28)), default_value_index = self._settings['DefaultDrumOffset'], default_channel = 0, bank_increment = 4, on_color = 'MonoInstrument.OffsetOnValue', off_color = 'MonoInstrument.OffsetOffValue')
		self._drum_offset_value.subject = self._drum_offset_component
		self.set_offset_shift_toggle = self._drum_offset_component.shift_toggle.set_control_element

		self._drumgroup = MonoDrumGroupComponent(translation_channel = 3, set_pad_translations = self._control_surface.set_pad_translations, channel_list = self._settings['Channels'], settings = self._settings)
		self._drumpad_position_value.subject = self._drumgroup
		self.set_drumpad_matrix = self._drumgroup.set_matrix
		self.set_drumpad_select_matrix = self._drumgroup.set_select_matrix

		drum_clip_creator = ClipCreator()
		drum_note_editor = MonoNoteEditorComponent(clip_creator=drum_clip_creator, grid_resolution=grid_resolution)
		self._step_sequencer = MonoStepSeqComponent(parent = self, clip_creator=drum_clip_creator, skin=skin, grid_resolution=grid_resolution, name='Drum_Sequencer', note_editor_component=drum_note_editor, instrument_component=self._drumgroup)
		self._step_sequencer._playhead_component._notes=tuple(chain(*starmap(range, ((64, 68), (56, 60), (48, 52), (40, 44)))))
		self._step_sequencer._playhead_component._triplet_notes=tuple(chain(*starmap(range, ((64, 67), (56, 59), (48, 51), (40, 43)))))
		self._step_sequencer._playhead_component._feedback_channels = [15]
		self._step_sequencer._note_editor._visible_steps_model = lambda indices: [k for k in indices if k % 4 != 3]
		self.set_sequencer_matrix = self._step_sequencer.set_button_matrix
		self.set_playhead = self._step_sequencer.set_playhead
		self.set_loop_selector_matrix = self._step_sequencer.set_loop_selector_matrix
		self.set_quantization_buttons = self._step_sequencer.set_quantization_buttons
		self.set_follow_button = self._step_sequencer.set_follow_button
		self.set_follow_button = self._step_sequencer.set_follow_button
		self.set_mute_button = self._step_sequencer.set_mute_button
		self.set_solo_button = self._step_sequencer.set_solo_button
		#self.register_component(self._step_sequencer)

		self.set_split_matrix = self._parent._selected_session.set_clip_launch_buttons


	@listens('value')
	def _drum_offset_value(self, value):
		self._drumgroup.position = value
		self._drum_offset_component.buttons_are_pressed() and self._control_surface.show_message('New drum root is ' + str(value))
		#debug('_drum_offset_value', value)


	@listens('position')
	def _drumpad_position_value(self):
		self._drum_offset_component.set_index(self._drumgroup.position)


	def update(self):
		self._drumgroup._update_assigned_drum_pads()
		self._drumgroup._create_and_set_pad_translations()
		super(MonoDrumpadComponent, self).update()
		#debug('monodrum is enabled:', self.is_enabled())



class MonoInstrumentComponent(Component):


	_keypad_class = MonoScaleComponent
	_drumpad_class = MonoDrumpadComponent

	_scale_settings_component_class = ScaleTaggedSetting
	_toggle_settings_component_class = ToggledTaggedSetting

	_shifted = False

	def __init__(self, script, skin, grid_resolution, drum_group_finder, device_provider, parent_task_group, settings = DEFAULT_INSTRUMENT_SETTINGS, *a, **k):
		super(MonoInstrumentComponent, self).__init__(*a, **k)
		self._settings = settings
		self._parent_task_group = parent_task_group
		self._scalenames = settings['ScaleNames']
		self._device_provider = device_provider
		self._script = script
		self._skin = skin
		self._grid_resolution = grid_resolution
		self._drum_group_finder = drum_group_finder

		self._setup_selected_session_control()

		self._setup_shift_mode()

		#self._scale_offset_component = self.register_component(self._scale_settings_component_class(name = 'VerticalOffset', attribute_tag = 'scale', parent_task_group = parent_task_group, value_dict = self._scalenames, default_value_index = self._scalenames.index(DEFAULT_SCALE), default_channel = 0, on_color = 'MonoInstrument.ScaleOffsetOnValue', off_color = 'MonoInstrument.ScaleOffsetOffValue'))
		self._scale_offset_component = self._scale_settings_component_class(parent = self, name = 'VerticalOffset', attribute_tag = 'scale', parent_task_group = parent_task_group, value_dict = self._scalenames, default_value_index = self._scalenames.index(DEFAULT_SCALE), default_channel = 0, on_color = 'MonoInstrument.ScaleOffsetOnValue', off_color = 'MonoInstrument.ScaleOffsetOffValue')
		self._scale_offset_value.subject = self._scale_offset_component
		self.set_scale_up_button = self._scale_offset_component.up_button.set_control_element
		self.set_scale_down_button = self._scale_offset_component.down_button.set_control_element

		#self._mode_component = self.register_component(self._toggle_settings_component_class(name = 'SplitModeOffset', attribute_tag = 'mode', parent_task_group = parent_task_group,))
		self._mode_component = self._toggle_settings_component_class(parent = self, name = 'SplitModeOffset', attribute_tag = 'mode', parent_task_group = parent_task_group,)
		self._mode_value.subject = self._mode_component
		self.set_split_button = self._mode_component.split_toggle.set_control_element
		self.set_sequencer_button = self._mode_component.seq_toggle.set_control_element

		#self._keypad = self.register_component(self._keypad_class(parent = self, control_surface = script, skin = skin, grid_resolution = grid_resolution, parent_task_group = parent_task_group, settings = self._settings))
		self._keypad = self._keypad_class(parent = self, control_surface = script, skin = skin, grid_resolution = grid_resolution, parent_task_group = parent_task_group, settings = self._settings)
		self.set_vertical_offset_up_button = self._keypad._vertical_offset_component.up_button.set_control_element
		self.set_vertical_offset_down_button = self._keypad._vertical_offset_component.down_button.set_control_element
		self.set_offset_up_button = self._keypad._offset_component.up_button.set_control_element
		self.set_offset_down_button = self._keypad._offset_component.down_button.set_control_element
		self.set_octave_up_button = self._keypad._offset_component.bank_up_button.set_control_element
		self.set_octave_down_button = self._keypad._offset_component.bank_down_button.set_control_element

		#self._drumpad = self.register_component(self._drumpad_class(parent = self, control_surface = script, skin = skin, grid_resolution = grid_resolution, parent_task_group = parent_task_group, settings = self._settings))
		self._drumpad = self._drumpad_class(parent = self, control_surface = script, skin = skin, grid_resolution = grid_resolution, parent_task_group = parent_task_group, settings = self._settings)
		self.set_drum_offset_up_button = self._drumpad._drum_offset_component.up_button.set_control_element
		self.set_drum_offset_down_button = self._drumpad._drum_offset_component.down_button.set_control_element
		self.set_drum_octave_up_button = self._drumpad._drum_offset_component.bank_up_button.set_control_element
		self.set_drum_octave_down_button = self._drumpad._drum_offset_component.bank_down_button.set_control_element
		self.set_drumpad_mute_button = self._drumpad._drumgroup.mute_button.set_control_element
		self.set_drumpad_solo_button = self._drumpad._drumgroup.solo_button.set_control_element

		self._audio_loop = LoopSelectorComponent(follow_detail_clip=True, measure_length=1.0, name='Loop_Selector', default_size = 8)
		self.set_loop_selector_matrix = self._audio_loop.set_loop_selector_matrix

		#self._main_modes = self.register_component(ModesComponent())
		self._main_modes = ModesComponent()  #parent = self)
		self._main_modes.add_mode('disabled', [])
		self._main_modes.add_mode('audioloop', [self._audio_loop])
		self._main_modes.set_enabled(True)

		self._on_device_changed.subject = self._device_provider

		self.on_selected_track_changed.subject = self.song.view
		self.on_selected_track_changed()


	def _setup_selected_session_control(self):
		self._session_ring = SessionRingComponent(num_tracks=1, num_scenes=32)
		self._selected_session = ScaleSessionComponent(name = "SelectedSession", session_ring = self._session_ring, auto_name = True, is_enabled = False)
		self._selected_session.set_enabled(False)


	def _setup_shift_mode(self):
		self._shifted = False
		#self._shift_mode = self.register_component(ModesComponent())
		self._shift_mode = ModesComponent()  #parent = self)
		self._shift_mode.add_mode('disabled', [])
		self._shift_mode.add_mode('shift', tuple([lambda a: self._on_shift_value(True), lambda a: self._on_shift_value(False)]), behaviour = ShiftCancellableBehaviourWithRelease())


	def set_shift_button(self, button):
		debug('shift_button:', button)
		self._on_shift_value.subject = button
		self._shifted = 0


	def set_shift_mode_button(self, button):
		self._on_shift_value.subject = None
		self._shifted = 0
		self._shift_mode.shift_button.set_control_element(button)


	@listens('value')
	def _on_shift_value(self, value):
		#debug('on shift value:', value)
		self._shifted = bool(value)
		self.update()



	def set_octave_enable_button(self, button):
		self._keypad._offset_component.shift_button.set_control_element(button)
		self._drumpad._drum_offset_component.shift_button.set_control_element(button)


	@listens('value')
	def _on_octave_enable_value(self, value):
		value and self._keypad._offset_component.shift_button._press_button() or self._keypad._offset_component.shift_button._release_button()
		value and self._drumpad._drum_offset_component.shift_button._press_button() or self._drumpad._drum_offset_component.shift_button._release_button()


	@listens('value')
	def _mode_value(self, value):
		self.update()


	@listens('value')
	def _scale_offset_value(self, value):
		#debug('_scale_offset_value', value)
		value = self._settings['DefaultAutoScale'] if value is 'Auto' else value
		self._keypad._keygroup.scale = value
		self._scale_offset_component.buttons_are_pressed() and self._script.show_message('New scale is ' + str(value))
		self.update()


	@listens('instrument')
	def _on_drum_group_changed(self):
		drum_device = self._drum_group_finder.drum_group
		#debug('monoinstrument _on_drum_group_changed', drum_device)
		self._drumpad._step_sequencer.set_drum_group_device(drum_device)


	@listens('device')
	def _on_device_changed(self):
		#debug('monoinstrument _on_device_changed')
		self._script.schedule_message(1, self.update)
		#self.update()


	@listens('selected_track')
	def on_selected_track_changed(self):
		self._selected_session.update_current_track()
		self.update()


	def update(self):
		super(MonoInstrumentComponent, self).update()
		self._main_modes.selected_mode = 'disabled'
		#if self.is_enabled():
		new_mode = 'disabled'
		drum_device = find_drum_group_device(self.song.view.selected_track)
		#debug('instrument update, drum device:', drum_device.name if drum_device else None)
		self._drumpad._drumgroup.set_drum_group_device(drum_device)
		cur_track = self.song.view.selected_track
		if cur_track.has_audio_input and cur_track in self.song.visible_tracks:
			new_mode = 'audioloop'
		elif cur_track.has_midi_input:
			scale, mode = self._scale_offset_component.value, self._mode_component.value
			new_mode = get_instrument_type(cur_track, scale, self._settings)
			if mode is 'split':
				new_mode += '_split'
			elif mode is 'seq':
				new_mode +=  '_sequencer'
			if self._shifted:
				new_mode += '_shifted'
			self._script.set_feedback_channels([self._scale_offset_component.channel])
			self._script.set_controlled_track(self.song.view.selected_track)
		#debug('trying to set mode:', new_mode)
		if new_mode in self._main_modes._mode_map or new_mode is None:
			self._main_modes.selected_mode = new_mode
			self._script.set_controlled_track(self.song.view.selected_track)
		else:
			self._main_modes.selected_mode = 'disabled'
			self._script.set_controlled_track(self.song.view.selected_track)
		#debug('monoInstrument mode is:', self._main_modes.selected_mode, '  inst:', self.is_enabled(), '  modes:', self._main_modes.is_enabled(), '   key:', self._keypad.is_enabled(), '   drum:', self._drumpad.is_enabled())



#a
