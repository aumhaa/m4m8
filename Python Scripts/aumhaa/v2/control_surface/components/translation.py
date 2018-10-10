# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.4 100918

from ableton.v2.control_surface.elements.button_matrix import ButtonMatrixElement
from ableton.v2.control_surface.component import Component
from ableton.v2.base.event import Event, listens, listens_group

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

class TranslationComponent(Component):


	def __init__(self, controls = [], user_channel_offset = 1, channel = 0, *a, **k):
		super(TranslationComponent, self).__init__()
		self._controls = controls
		self._user_channel_offset = user_channel_offset
		self._channel = channel or 0
		self._color = 0


	def set_controls(self, controls):
		self._controls = controls


	def add_control(self, control):
		if control:
			self._controls.append(control)


	def set_channel_selector_buttons(self, buttons):
		self._on_channel_selector_button_value.subject = buttons
		self.update_channel_selector_buttons()


	def set_channel_selector_control(self, control):
		if self._on_channel_selector_control_value.subject:
			self._on_channel_selector_control_value.subject.send_value(0)
		self._on_channel_selector_control_value.subject = control
		self.update_channel_selector_control()


	def update_channel_selector_control(self):
		control = self._on_channel_selector_control_value.subject
		if control:
			chan_range = 14 - self._user_channel_offset
			value =  ((self._channel-self._user_channel_offset)*127)/chan_range
			control.send_value(  int(value)  )


	def update_channel_selector_buttons(self):
		buttons = self._on_channel_selector_button_value.subject
		#debug('update_channel_selector_buttons:', buttons)
		if buttons:
			channel = self._channel - self._user_channel_offset
			#debug('channel:', channel)
			for button, coords in buttons.iterbuttons():
				#debug('coords:', coords)
				if button:
					selected = coords[0] + (coords[1]*buttons.width())
					if channel == selected:
						button.set_light('Translation.SelectorOn')
						#debug('turning on:', channel, button)
					else:
						button.set_light('Translation.SelectorOff')


	@listens('value')
	def _on_channel_selector_control_value(self, value, *a, **k):
		if self.is_enabled():
			chan_range = 14 - self._user_channel_offset
			channel = int((value*chan_range)/127)+self._user_channel_offset
			if channel != self._channel:
				self._channel = channel
				self.update()


	@listens('value')
	def _on_channel_selector_button_value(self, value, x, y, *a, **k):
		if self.is_enabled():
			if value:
				x = x + (y*self._on_channel_selector_button_value.subject.width())
				self._channel = min(x+self._user_channel_offset, 14)
			self.update()


	def update(self):
		if self.is_enabled():
			for control in self._controls:
				if control:
					control.clear_send_cache()
					control.release_parameter()
					try:
						control.set_light('Translation.Channel_'+str(self._channel)+'.'+str(control.name))
					except:
						control.send_value(self._color, True)
					control.set_channel(self._channel)
					control.set_enabled(False)
		else:
			for control in self._controls:
				if control:
					control.use_default_message()
					control.set_enabled(True)
		self.update_channel_selector_buttons()
		self.update_channel_selector_control()
