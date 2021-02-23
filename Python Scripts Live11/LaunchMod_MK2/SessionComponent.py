

#from _Framework.Util import in_range
from ableton.v2.base.util import in_range
#from _Framework.SubjectSlot import subject_slot_group
from ableton.v2.base.event import listens_group
#from _Framework.SessionComponent import SessionComponent as SessionComponentBase
from ableton.v2.control_surface.components.session import SessionComponent as SessionComponentBase
from .ComponentUtils import skin_scroll_component

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

class SessionComponent(SessionComponentBase):

	def __init__(self, *a, **k):
		self._stopped_clip_value = 0
		super(SessionComponent, self).__init__(*a, **k)

	def _enable_skinning(self):
		super(SessionComponent, self)._enable_skinning()
		self.set_stopped_clip_value('Session.StoppedClip')
		scroll_components = (self._horizontal_banking,
		 self._horizontal_paginator,
		 self._vertical_banking,
		 self._vertical_paginator)
		list(map(skin_scroll_component, scroll_components))

	def set_stopped_clip_value(self, value):
		self._stopped_clip_value = value

	def set_stop_all_clips_button(self, button):
		if button:
			button.reset_state()
		super(SessionComponent, self).set_stop_all_clips_button(button)

	def _update_stop_clips_led(self, index):
		tracks_to_use = self._session_ring.tracks_to_use()
		track_index = index + self._session_ring.track_offset
		if self.is_enabled() and self._stop_track_clip_buttons is not None and index < len(self._stop_track_clip_buttons):
			button = self._stop_track_clip_buttons[index]
			if button is not None:
				value_to_send = None
				if track_index < len(tracks_to_use) and tracks_to_use[track_index].clip_slots:
					track = tracks_to_use[track_index]
					if track.fired_slot_index == -2:
						value_to_send = self._stop_clip_triggered_value
					elif track.playing_slot_index >= 0:
						value_to_send = self._stop_clip_value
					else:
						value_to_send = self._stopped_clip_value
				if value_to_send is None:
					# button.turn_off()
					button.set_light(False)
				elif in_range(value_to_send, 0, 128):
					button.send_value(value_to_send)
				else:
					button.set_light(value_to_send)

	def _update_stop_clips_led(self, index):
		tracks_to_use = self._session_ring.tracks_to_use()
		track_index = index + self._session_ring.track_offset
		if self.is_enabled() and self._stop_track_clip_buttons != None and index < len(self._stop_track_clip_buttons):
			button = self._stop_track_clip_buttons[index]
			if button != None:
				value_to_send = None
				if track_index < len(tracks_to_use) and tracks_to_use[track_index].clip_slots:
					track = tracks_to_use[track_index]
					if track.fired_slot_index == -2:
						value_to_send = self._stop_clip_triggered_value
					elif track.playing_slot_index >= 0:
						value_to_send = self._stop_clip_value
				if value_to_send == None:
					# button.turn_off()
					button.set_light(False)
				elif in_range(value_to_send, 0, 128):
					#debug('in_range:', value_to_send)
					button.send_value(value_to_send)
				else:
					#debug('not_in_range:', value_to_send)
					button.set_light(value_to_send)

	def _update_stop_all_clips_button(self):
		#debug('_update_stop_all_clips_button')
		button = self._stop_all_button
		if button:
			if button.is_pressed():
				button.set_light(self._stop_clip_value)
			else:
				button.set_light(self._stopped_clip_value)
