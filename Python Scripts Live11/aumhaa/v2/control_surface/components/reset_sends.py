# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


import Live 

from ableton.v2.control_surface.component import Component
from ableton.v2.base.event import listens

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

class ResetSendsComponent(Component):
	' Special Component to reset all track sends to zero for the first four returns '
	__module__ = __name__


	def __init__(self, script, *a, **k):
		super(ResetSendsComponent, self).__init__(*a, **k)
		self._script = script
	

	def set_buttons(self, buttons):
		self._on_button_value.subject = buttons
		if buttons:
			for button, _ in buttons.iterbuttons():
				button and button.set_light('ResetSendsColor')
	

	def update(self):
		pass
	
	
	@listens('value')
	def _on_button_value(self, value, x, y, *a, **k):
		if value:
			self._on_button_value.subject and self.reset_send(x)
	

	def reset_send(self, send_number):
		if send_number < len(self.returns_to_use()):
			for track in self.tracks_to_use():
				track.mixer_device.sends[send_number].value = 0
			for track in self.returns_to_use():
				track.mixer_device.sends[send_number].value = 0
	

	def tracks_to_use(self):
		return self.song.tracks
	

	def returns_to_use(self):
		return self.song.return_tracks
	

