# written against Live 10.0.4 100918

import Live

from functools import partial
from ableton.v2.control_surface.components import SessionRecordingComponent
from ableton.v2.base import forward_property, listens, liveobj_valid
from ableton.v2.base.task import Task
from pushbase.action_with_options_component import ToggleWithOptionsComponent


_Q = Live.Song.Quantization
LAUNCH_QUANTIZATION = (_Q.q_quarter,
 _Q.q_half,
 _Q.q_bar,
 _Q.q_2_bars,
 _Q.q_4_bars,
 _Q.q_8_bars,
 _Q.q_8_bars,
 _Q.q_8_bars)

LENGTH_VALUES = [2, 3, 4]
LENGTH_OPTION_NAMES = ('1 Beat', '2 Beats', '1 Bar', '2 Bars', '4 Bars', '8 Bars', '16 Bars', '32 Bars')
LENGTH_LABELS = ('Recording length:', '', '', '')

def song_selected_slot(song):
	view = song.view
	scene = view.selected_scene
	track = view.selected_track
	scene_index = list(song.scenes).index(scene)
	try:
		slot = track.clip_slots[scene_index]
	except IndexError:
		slot = None

	return slot


def track_can_overdub(track):
	return not track.has_audio_input



class FixedLengthSessionRecordingComponent(SessionRecordingComponent):


	_length_buttons = []

	def __init__(self, clip_creator, length_values = LENGTH_VALUES, *a, **k):
		super(FixedLengthSessionRecordingComponent, self).__init__(*a, **k)
		self._clip_creator = clip_creator
		self._length_value = 1
		self._length_values = length_values
		self._fixed_length = ToggleWithOptionsComponent()
		self._length_selector = self._fixed_length.options
		self._length_selector.option_names = LENGTH_OPTION_NAMES
		self._length_selector.selected_option = 3
		self._length_selector.labels = LENGTH_LABELS
		self._on_selected_fixed_length_option_changed.subject = self._length_selector
		length, _ = self._get_selected_length()
		self._clip_creator.fixed_length = length

	length_layer = forward_property('_length_selector')('layer')

	def _length_should_be_fixed(self):
		return self._fixed_length.is_active


	def _original_get_selected_length(self):
		song = self.song
		length = 2.0 ** self._length_selector.selected_option
		quant = LAUNCH_QUANTIZATION[self._length_selector.selected_option]
		if self._length_selector.selected_option > 1:
			length = length * song.signature_numerator / song.signature_denominator
		return (length, quant)


	def _get_selected_length(self):
		song = self.song
		length = 2.0 ** (self._length_values[self._length_value])
		quant = LAUNCH_QUANTIZATION[(self._length_values[self._length_value])]
		length = length * song.signature_numerator / song.signature_denominator
		return (length, quant)


	def set_length_button(self, button):
		self._fixed_length.action_button.set_control_element(button)
		self._on_length_value.subject = button
		self._length_press_state = None


	def set_length_buttons(self, buttons):
		self._on_length_buttons_value.subject = buttons
		self.update_length_buttons()


	@listens('value')
	def _on_length_buttons_value(self, value, x, y, *a, **k):
		if value > 0:
			self._length_value = x
			self.update_length_buttons()


	def _start_recording(self):
		song = self.song
		song.overdub = True
		selected_scene = song.view.selected_scene
		scene_index = list(song.scenes).index(selected_scene)
		track = self.song.view.selected_track
		if track.can_be_armed and (track.arm or track.implicit_arm):
			self._record_in_slot(track, track.clip_slots[scene_index])
			self._ensure_slot_is_visible(track, scene_index)
		if not song.is_playing:
			song.is_playing = True


	def _record_in_slot(self, track, clip_slot):
		if self._length_should_be_fixed() and not clip_slot.has_clip:
			length, quant = self._get_selected_length()
			if track_can_overdub(track):
				self._clip_creator.create(clip_slot, length)
			else:
				clip_slot.fire(record_length=length, launch_quantization=quant)
		elif not clip_slot.is_playing:
			if clip_slot.has_clip:
				clip_slot.fire(force_legato=True, launch_quantization=_Q.q_no_q)
			else:
				clip_slot.fire()


	def _ensure_slot_is_visible(self, track, scene_index):
		song = self.song
		if song.view.selected_track == track:
			song.view.selected_scene = song.scenes[scene_index]
		self._view_selected_clip_detail()


	@listens('selected_option')
	def _on_selected_fixed_length_option_changed(self, _):
		length, _ = self._get_selected_length()
		self._clip_creator.fixed_length = length


	@listens('value')
	def _on_length_value(self, value):
		if value:
			self._on_length_press()
		else:
			self._on_length_release()


	def _on_length_press(self):
		song = self.song
		slot = song_selected_slot(song)
		if slot == None:
			return
		clip = slot.clip
		if slot.is_recording and not clip.is_overdubbing:
			self._length_press_state = (slot, clip.playing_position)


	def _on_length_release(self):
		song = self.song
		slot = song_selected_slot(song)
		if slot == None:
			return
		clip = slot.clip
		if self._length_press_state is not None:
			press_slot, press_position = self._length_press_state
			if press_slot == slot and self._length_should_be_fixed() and slot.is_recording and not clip.is_overdubbing:
				length, _ = self._get_selected_length()
				one_bar = 4.0 * song.signature_numerator / song.signature_denominator
				loop_end = int(press_position / one_bar) * one_bar
				loop_start = loop_end - length
				if loop_start >= 0.0:
					clip.loop_end = loop_end
					clip.end_marker = loop_end
					clip.loop_start = loop_start
					clip.start_marker = loop_start
					self._tasks.add(Task.sequence(Task.delay(0), Task.run(partial(slot.fire, force_legato=True, launch_quantization=_Q.q_no_q))))
					self.song.overdub = False
				self._fixed_length.is_active = False
		self._length_press_state = None


	def _handle_limitation_error_on_scene_creation(self):
		pass



	def update(self, *a, **k):
		super(FixedLengthSessionRecordingComponent, self).update(*a, **k)
		if self.is_enabled():
			self.update_length_buttons()


	def update_length_buttons(self):
		buttons = self._on_length_buttons_value.subject
		if buttons:
			for button, (x, y) in buttons.iterbuttons():
				if button:
					if x == self._length_value:
						button.set_light('Recorder.FixedAssigned')
					else:
						button.set_light('Recorder.FixedNotAssigned')


	def _update_new_button(self):
		self._update_generic_new_button(self._new_button)

	def _update_generic_new_button(self, new_button):
		if new_button and self.is_enabled():
			song = self.song
			selected_track = song.view.selected_track
			clip_slot = song.view.highlighted_clip_slot
			can_new = liveobj_valid(clip_slot) and clip_slot.clip or selected_track.can_be_armed and selected_track.playing_slot_index >= 0
			new_button.set_light('Recorder.NewOn' if can_new else 'Recorder.NewOff')


#a
