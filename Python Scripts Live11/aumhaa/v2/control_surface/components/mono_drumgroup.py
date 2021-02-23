# by amounra 0218 : http://www.aumhaa.com
# written against Live 10.b110

import Live

from ableton.v2.control_surface.components import DrumGroupComponent
from ableton.v2.base import listens, forward_property, clamp, listenable_property, liveobj_valid, first, find_if
from ableton.v2.base.task import *
from ableton.v2.base import task
from ableton.v2.control_surface.control import PlayableControl, control_matrix, ButtonControl

from aumhaa.v2.control_surface.instrument_consts import *
from aumhaa.v2.base import initialize_debug

debug = initialize_debug()


class MonoDrumGroupComponent(DrumGroupComponent):

	mute_button = ButtonControl(color='DrumGroup.PadMuted')
	solo_button = ButtonControl(color='DrumGroup.PadSoloed')
	_raw_position = 0
	_selected_note = DEFAULT_DRUMOFFSET*4
	_selected_notes = tuple([DEFAULT_DRUMOFFSET*4])
	select_matrix = control_matrix(PlayableControl)
	create_translation_entry = lambda self, button: (button.coordinate[1], button.coordinate[0], button.identifier, button.channel)

	def __init__(self, channel_list = CHANNELS, settings = DEFAULT_INSTRUMENT_SETTINGS, *a, **k):
		self._channel_list = channel_list
		self._settings = settings
		super(MonoDrumGroupComponent, self).__init__(*a, **k)
		self.selected_notes_provider = self
		self._on_selected_track_changed.subject = self.song.view


	def _get_current_channel(self):
		cur_track = self.song.view.selected_track
		cur_chan = cur_track.current_input_sub_routing
		if len(cur_chan) == 0:
			cur_chan = 'All Channels'
		if cur_chan == 'All Channels':
			cur_chan = 1
		if cur_chan in self._channel_list:
			cur_chan = (self._channel_list.index(cur_chan)%15)+1
		else:
			cur_chan = 14
		return cur_chan


	@listens('selected_track')
	def _on_selected_track_changed(self):
		#debug('keys settings track changed')
		self.translation_channel = self._get_current_channel()
		self.update_matrix()


	@property
	def translation_channel(self, translation_channel):
		return self._translation_channel


	@translation_channel.setter
	def translation_channel(self, channel):
		debug('drumpad set_translation_channel', channel)
		self._translation_channel = channel
		self.update_matrix()


	@property
	def position(self):
		if liveobj_valid(self._drum_group_device):
			return self._drum_group_device.view.drum_pads_scroll_position
		return 0


	@position.setter
	def position(self, index):
		if not 0 <= index <= 28:
			raise AssertionError
		self._raw_position = index
		if liveobj_valid(self._drum_group_device):
			self._drum_group_device.view.drum_pads_scroll_position = index
			self.update_matrix()
		else:
			self.update_matrix()


	def update_matrix(self):
		self._reset_selected_pads()
		self._update_led_feedback()
		self._update_note_translations()


	def set_translation_channel(self, translation_channel):
		self._translation_channel = translation_channel
		self._update_assigned_drum_pads()
		self._create_and_set_pad_translations()


	def _create_and_set_pad_translations(self):
		debug('_create_and_set_pad_translations')
		def create_translation_entry(button):
			row, col = button.coordinate
			return (col,
			 row,
			 button.identifier,
			 button.channel)

		if self._can_set_pad_translations():
			translations = []
			for button in self.matrix:
				button.channel = self._translation_channel
				button.identifier = self._button_coordinates_to_pad_index(self._raw_position*4, button.coordinate)
				button.enabled = True
				translations.append(create_translation_entry(button))

			self._set_pad_translations(tuple(translations))
		else:
			self._update_note_translations()
			self._set_pad_translations(None)


	def _button_coordinates_to_pad_index(self, first_note, coordinates):
		y, x = coordinates
		y = self.height - y - 1
		if x < 4 and y >= 4:
			first_note += 32
		elif x >= 4 and y < 4:
			first_note += 2 * self.width
		elif x >= 4 and y >= 4:
			first_note += 4 * self.width + 16
		index = x % 4 + y % 4 * 4 + first_note
		return index


	def _note_translation_for_button(self, button):
		if liveobj_valid(self._drum_group_device):
			identifier = None
			channel = None
			if self.has_assigned_pads:
				identifier = self._button_coordinates_to_pad_index(first(self._assigned_drum_pads).note, button.coordinate)
				channel = self._translation_channel
			return (identifier, channel)
		else:
			identifier = self._button_coordinates_to_pad_index(self._raw_position*4, button.coordinate)
			channel = self._translation_channel
			return (identifier, channel)


	def _update_led_feedback(self):
		if liveobj_valid(self._drum_group_device):
			super(MonoDrumGroupComponent, self)._update_led_feedback()
		else:
			super(DrumGroupComponent, self)._update_led_feedback()
		for button in self.select_matrix:
			self._update_button_color(button)


	def _update_button_color(self, button):
		if liveobj_valid(self._drum_group_device):
			super(MonoDrumGroupComponent, self)._update_button_color(button)
		elif button._control_element:
			note = self._button_coordinates_to_pad_index(self._raw_position*4, button.coordinate)
			register = (note-4)%32
			if note is self._selected_note:
				button.color = 'MonoInstrument.Drums.SelectedNote'
			else:
				button.color = 'MonoInstrument.Drums.EvenValue' if (0 <= register <16) else 'MonoInstrument.Drums.OddValue'
			#debug('button color:', button.color)
		if button._control_element:
			button._control_element.scale_color = button.color


	def _color_for_pad(self, pad):
		has_soloed_pads = bool(find_if(lambda pad: pad.solo, self._all_drum_pads))
		button_color = 'DrumGroup.PadEmpty'
		if pad == self._selected_drum_pad:
			button_color = 'DrumGroup.PadSelected'
			if has_soloed_pads and not pad.solo and not pad.mute:
				button_color = 'DrumGroup.PadSelectedNotSoloed'
			elif pad.mute and not pad.solo:
				button_color = 'DrumGroup.PadMutedSelected'
			elif has_soloed_pads and pad.solo:
				button_color = 'DrumGroup.PadSoloedSelected'
		elif pad.chains:
			register = (pad.note-4)%32
			button_color = 'DrumGroup.PadFilled' if (0 <= register <16) else 'DrumGroup.PadFilledAlt'
			if has_soloed_pads and not pad.solo:
				button_color = 'DrumGroup.PadFilled' if not pad.mute else 'DrumGroup.PadMuted'
			elif not has_soloed_pads and pad.mute:
				button_color = 'DrumGroup.PadMuted'
			elif has_soloed_pads and pad.solo:
				button_color = 'DrumGroup.PadSoloed'
		return button_color


	def set_drum_group_device(self, *a, **k):
		super(MonoDrumGroupComponent,self).set_drum_group_device(*a, **k)
		self.update_matrix()


	def _update_selected_drum_pad(self):
		super(MonoDrumGroupComponent, self)._update_selected_drum_pad()
		self.notify_selected_note()
		selected_drum_pad = self._drum_group_device.view.selected_drum_pad if liveobj_valid(self._drum_group_device) else None
		if liveobj_valid(selected_drum_pad):
			self.notify_selected_notes(tuple([selected_drum_pad.note]))
		else:
			self.notify_selected_notes(tuple([int(self._selected_note)]))


	@listenable_property
	def selected_note(self):
		selected_drum_pad = self._drum_group_device.view.selected_drum_pad if liveobj_valid(self._drum_group_device) else None
		if liveobj_valid(selected_drum_pad):
			#debug('selected note:', selected_drum_pad.note)
			return selected_drum_pad.note
		else:
			#debug('selected note:', self._selected_note)
			return int(self._selected_note)



	@listenable_property
	def selected_notes(self):
		selected_drum_pad = self._drum_group_device.view.selected_drum_pad if liveobj_valid(self._drum_group_device) else None
		if liveobj_valid(selected_drum_pad):
			return tuple([selected_drum_pad.note])
		else:
			return tuple([int(self._selected_note)])
		return self._selected_notes


	@selected_notes.setter
	def selected_notes(self, note):
		self._selected_notes = tuple(note)
		self.notify_selected_notes(self._selected_notes)


	def set_matrix(self, matrix):
		self._set_matrix_special_attributes(False)
		super(MonoDrumGroupComponent, self).set_matrix(matrix)
		self._set_matrix_special_attributes(True)


	def _set_matrix_special_attributes(self, enabled):
		for button in self.matrix:
			if button._control_element:
				button._control_element.display_press = enabled
				button._control_element._last_flash = 0
				not enabled and button._control_element.reset_state()


	def _on_matrix_pressed(self, button):
		debug('DrumGroup._on_matrix_pressed: mute:', self.mute_button.is_pressed, 'solo:', self.solo_button.is_pressed)
		super(MonoDrumGroupComponent, self)._on_matrix_pressed(button)


	@select_matrix.pressed
	def select_matrix(self, button):
		debug('on select matrix pressed:', button)
		if liveobj_valid(self._drum_group_device):
			if self.mute_button.is_pressed or self.solo_button.is_pressed:
				super(MonoDrumGroupComponent, self)._on_matrix_pressed(button)
			else:
				self._drum_group_device.view.selected_drum_pad = self._pad_for_button(button)
		else:
			self._selected_note = self._button_coordinates_to_pad_index(self._raw_position*4, button.coordinate)
		self.notify_selected_note()
		selected_drum_pad = self._drum_group_device.view.selected_drum_pad if liveobj_valid(self._drum_group_device) else None
		if liveobj_valid(selected_drum_pad):
			self.notify_selected_notes(tuple([selected_drum_pad.note]))
		else:
			self.notify_selected_notes(tuple([int(self._selected_note)]))
		self._update_led_feedback()


	def select_drum_pad(self, drum_pad):
		pass


	def set_select_matrix(self, matrix):
		debug('set select matrix:', matrix)
		self.select_matrix.set_control_element(matrix)
		for button in self.select_matrix:
			#not button is None and hasattr(button, 'set_playable') and button.set_playable(False)
			button.set_mode(PlayableControl.Mode.listenable)
		self._update_led_feedback()


	def _update_note_translations(self):
		debug('_update_note_translations')
		"""if liveobj_valid(self._drum_group_device):
			debug('MONO')
			super(MonoDrumGroupComponent, self)._update_note_translations()
		else:
			debug('VANILLA')"""
		super(DrumGroupComponent, self)._update_note_translations()


	def _button_should_be_enabled(self, button):
		#this was throwing an error so I overrode, sometimes drumcomponent sends a non-iterable
		identifier = 128
		if button:
			identifier, _ = self._note_translation_for_button(button)
		return identifier < 128


	def _on_selected_drum_pad_changed(self):
		#debug('on selected drumpad changed')
		self.notify_selected_note()
		selected_drum_pad = self._drum_group_device.view.selected_drum_pad if liveobj_valid(self._drum_group_device) else None
		if liveobj_valid(selected_drum_pad):
			self.notify_selected_notes(tuple([selected_drum_pad.note]))
		else:
			self.notify_selected_notes(tuple([int(self._selected_note)]))

	@mute_button.value
	def mute_button(self, value, button):
		debug('mute_button.value:', value)
		self._set_control_pads_from_script(bool(value))

	@solo_button.value
	def solo_button(self, value, button):
		debug('solo_button.value:', value)
		self._set_control_pads_from_script(bool(value))


#a
