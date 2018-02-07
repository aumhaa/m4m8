
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components.session import SessionComponent
#from _Framework.SessionComponent import SessionComponent

class SpecialSessionComponent(SessionComponent):
	u""" Special session subclass that handles ConfigurableButtons """

	def _update_stop_clips_led(self, index):
		if self.is_enabled() and self._stop_track_clip_buttons != None and index < len(self._stop_track_clip_buttons):
			button = self._stop_track_clip_buttons[index]
			if not button is None:
				tracks_to_use = self._session_ring.tracks_to_use()
				track_index = index + self._session_ring.track_offset
				if 0 <= track_index < len(tracks_to_use):
					track = tracks_to_use[track_index]
					if track.fired_slot_index == -2:
						button.set_light(u'Session.StopSingleClipTriggered')
					elif track.playing_slot_index >= 0:
						button.set_light(u'Session.StopSingleClip')
					else:
						button.set_light(u'Session.StopClipButton')
				else:
					button.send_value(4)
	

	def _update_stop_all_clips_button(self):
		self._stop_all_button and self._stop_all_button.set_light(u'Session.StopAllClips')
	
