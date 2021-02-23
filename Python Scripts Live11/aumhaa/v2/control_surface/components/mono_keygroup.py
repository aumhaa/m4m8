# by amounra 0218 : http://www.aumhaa.com
# written against Live 10.b110

import Live

#from ableton.v2.control_surface import CompoundComponent
from ableton.v2.control_surface.components import PlayableComponent
from ableton.v2.base import listens, forward_property, clamp, listenable_property
from ableton.v2.base.task import *
from ableton.v2.base import task
from ableton.v2.control_surface.control import PlayableControl, control_matrix
from aumhaa.v2.control_surface.instrument_consts import *
from aumhaa.v2.base import initialize_debug

from pushbase.instrument_component import SelectedNotesProvider

debug = initialize_debug()

#CompoundComponent, Messenger, Slidable

class MonoKeyGroupComponent(PlayableComponent):

	_scales = SCALES
	_scale = DEFAULT_AUTO_SCALE
	_vertoffset = DEFAULT_VERTOFFSET
	_offset = DEFAULT_OFFSET
	_translation_channel = 0
	_selected_note = 0
	_selected_notes = tuple([0])
	select_matrix = control_matrix(PlayableControl)

	def __init__(self, channel_list = CHANNELS, settings = DEFAULT_INSTRUMENT_SETTINGS, *a, **k):
		self._channel_list = channel_list
		self._settings = settings
		self._scales = settings['Scales']
		super(MonoKeyGroupComponent, self).__init__(*a, **k)
		self.selected_notes_provider = self
		self.select_button._send_current_color = lambda : None
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
		self.translation_channel = self._get_current_channel()
		self.update_matrix()
	

	@property
	def translation_channel(self, translation_channel):
		return self._translation_channel
	

	@translation_channel.setter
	def translation_channel(self, channel):
		self._translation_channel = channel
		self.update_matrix()
	

	@property
	def scale(self):
		return self._scale
	

	@scale.setter
	def scale(self, scale):
		self._scale = scale
		self.update_matrix()
	

	@property
	def vertical_offset(self):
		return self._vertoffset
	

	@vertical_offset.setter
	def vertical_offset(self, offset):
		self._vertoffset = offset
		self.update_matrix()
	

	@property
	def offset(self):
		return self._offset
	

	@offset.setter
	def offset(self, offset):
		self._offset = offset
		self.update_matrix()
	

	def update_matrix(self):
		self._reset_selected_pads()
		self._update_led_feedback()
		self._update_note_translations()
	

	def _update_led_feedback(self):
		super(MonoKeyGroupComponent, self)._update_led_feedback()
		for button in self.select_matrix:
			self._update_button_color(button)
	

	def set_select_matrix(self, matrix):
		self.select_matrix.set_control_element(matrix)
		for button in self.select_matrix:
			#button.set_playable(False)
			button.set_mode(PlayableControl.Mode.listenable)
		self._update_led_feedback()
	

	def _note_translation_for_button(self, button):
		y, x = button.coordinate
		scale_len = len(self._scales[self._scale])
		note_pos = x + (abs((self.height-1)-y)*self._vertoffset)
		note = self._offset + self._scales[self._scale][note_pos%scale_len] + (12*int(note_pos/scale_len))
		return (note, self._translation_channel)
	

	def set_matrix(self, matrix):
		self._set_matrix_special_attributes(False)
		super(MonoKeyGroupComponent, self).set_matrix(matrix)
		self._set_matrix_special_attributes(True)
	

	def _set_matrix_special_attributes(self, enabled):
		for button in self.matrix:
			if button._control_element:
				button._control_element.display_press = enabled
				button._control_element._last_flash = 0 
				not enabled and button._control_element.reset_state()
	

	def _update_button_color(self, button):
		y, x = button.coordinate
		scale_len = len(self._scales[self._scale])
		note_pos = x + (abs((self.height-1)-y)*self._vertoffset)
		note = self._offset + self._scales[self._scale][note_pos%scale_len] + (12*int(note_pos/scale_len))
		if note is self.selected_note:
			button.color = SELECTED_NOTE
		else:
			button.color = KEYCOLORS[(note%12 in WHITEKEYS) + (((note_pos%scale_len)==0)*2)]
		if button._control_element:
			button._control_element.scale_color = button.color

	

	@select_matrix.pressed
	def select_matrix(self, button):
		self._on_matrix_pressed(button)
	

	def _on_matrix_pressed(self, button):
		super(MonoKeyGroupComponent, self)._on_matrix_pressed(button)
		self._selected_note = self._note_translation_for_button(button)[0]
		self.notify_selected_note()
		self.selected_notes = [int(self._selected_note)]
		self._update_led_feedback()
	

	@listenable_property
	def selected_note(self):
		return int(self._selected_note)
	

	@listenable_property
	def selected_notes(self):
		return tuple([int(self._selected_note)])
	

	@selected_notes.setter
	def selected_notes(self, notes):
		self._selected_notes = tuple(notes)
		self.notify_selected_notes(self._selected_notes)
	

