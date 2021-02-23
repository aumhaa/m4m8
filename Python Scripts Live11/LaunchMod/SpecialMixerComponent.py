

import Live
from itertools import zip_longest
from ableton.v2.control_surface.components.mixer import MixerComponent
from .DefChannelStripComponent import DefChannelStripComponent
from ableton.v2.control_surface.elements.button import ButtonElement
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.base import EventObject, nop, listens, liveobj_valid

"""
class SpecialMixerComponent(MixerComponent):

	def __init__(self, *a, **k):
		MixerComponent.__init__(self, *a, **k)
		self._unarm_all_button = None
		self._unsolo_all_button = None
		self._unmute_all_button = None
	

	def disconnect(self):
		if self._unarm_all_button != None:
			self._unarm_all_button.remove_value_listener(self._unarm_all_value)
			self._unarm_all_button = None
		if self._unsolo_all_button != None:
			self._unsolo_all_button.remove_value_listener(self._unsolo_all_value)
			self._unsolo_all_button = None
		if self._unmute_all_button != None:
			self._unmute_all_button.remove_value_listener(self._unmute_all_value)
			self._unmute_all_button = None
		MixerComponent.disconnect(self)
	

	def set_global_buttons(self, unarm_all, unsolo_all, unmute_all):
		assert isinstance(unarm_all, (ButtonElement, type(None)))
		assert isinstance(unsolo_all, (ButtonElement, type(None)))
		assert isinstance(unmute_all, (ButtonElement, type(None)))
		if self._unarm_all_button != None:
			self._unarm_all_button.remove_value_listener(self._unarm_all_value)
		self._unarm_all_button = unarm_all
		if self._unarm_all_button != None:
			self._unarm_all_button.add_value_listener(self._unarm_all_value)
			self._unarm_all_button.turn_off()
		if self._unsolo_all_button != None:
			self._unsolo_all_button.remove_value_listener(self._unsolo_all_value)
		self._unsolo_all_button = unsolo_all
		if self._unsolo_all_button != None:
			self._unsolo_all_button.add_value_listener(self._unsolo_all_value)
			self._unsolo_all_button.turn_off()
		if self._unmute_all_button != None:
			self._unmute_all_button.remove_value_listener(self._unmute_all_value)
		self._unmute_all_button = unmute_all
		if self._unmute_all_button != None:
			self._unmute_all_button.add_value_listener(self._unmute_all_value)
			self._unmute_all_button.turn_off()
	

	def _create_strip(self):
		return DefChannelStripComponent()
	

	def _unarm_all_value(self, value):
		assert self.is_enabled()
		assert self._unarm_all_button != None
		assert value in range(128)
		if value != 0 or not self._unarm_all_button.is_momentary():
			for track in self.song().tracks:
				if track.can_be_armed and track.arm:
					track.arm = False
	

	def _unsolo_all_value(self, value):
		assert self.is_enabled()
		assert self._unsolo_all_button != None
		assert value in range(128)
		if value != 0 or not self._unsolo_all_button.is_momentary():
			for track in tuple(self.song().tracks) + tuple(self.song().return_tracks):
				if track.solo:
					track.solo = False
	

	def _unmute_all_value(self, value):
		assert self.is_enabled()
		assert self._unmute_all_button != None
		assert value in range(128)
		if value != 0 or not self._unmute_all_button.is_momentary():
			for track in tuple(self.song().tracks) + tuple(self.song().return_tracks):
				if track.mute:
					track.mute = False
	
"""

class SpecialMixerComponent(MixerComponent):
	""" Class encompassing several defaultable channel strips to form a mixer """


	unarm_all_button = ButtonControl(color = 'Mixer.UnArmAll', pressed_color = 'Mixer.UnArmAllPressed')
	unsolo_all_button = ButtonControl(color = 'Mixer.UnSoloAll', pressed_color = 'Mixer.UnSoloAllPressed')
	unmute_all_button = ButtonControl(color = 'Mixer.UnMuteAll', pressed_color = 'Mixer.UnMuteAllPressed')

	def __init__(self, *a, **k):
		super(SpecialMixerComponent, self).__init__(*a, **k)
	

	def disconnect(self):
		self._unarm_all_button = None
		self._unsolo_all_button = None
		self._unmute_all_button = None
		super(SpecialMixerComponent, self).disconnect()
	

	def set_default_volume_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_default_volume_button(button)
	

	def set_default_panning_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_default_panning_button(button)
	

	def set_default_send1_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_default_send1_button(button)
		

	def set_default_send2_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_default_send2_button(button)
	

	def _create_strip(self):
		return DefChannelStripComponent()
	

	def set_unarm_all_button(self, button):
		self.unarm_all_button.set_control_element(button)
		self.update()
	

	def set_unsolo_all_button(self, button):
		self.unsolo_all_button.set_control_element(button)
		self.update()
	

	def set_unmute_all_button(self, button):
		self.unmute_all_button.set_control_element(button)
		self.update()
	

	@unarm_all_button.pressed
	def unarm_all_button(self, button):
		self._unarm_all_value(button)
	

	@unmute_all_button.pressed
	def unmute_all_button(self, button):
		self._unmute_all_value(button)
	

	@unsolo_all_button.pressed
	def unsolo_all_button(self, button):
		self._unsolo_all_value(button)
	

	def _unarm_all_value(self, value):
		assert self.is_enabled()
		for track in self.song.tracks:
			if track.can_be_armed and track.arm:
				track.arm = False
	

	@listens('value')
	def _unsolo_all_value(self, value):
		assert self.is_enabled()
		for track in tuple(self.song.tracks) + tuple(self.song.return_tracks):
			if track.solo:
				track.solo = False
	

	@listens('value')
	def _unmute_all_value(self, value):
		assert self.is_enabled()
		for track in tuple(self.song.tracks) + tuple(self.song.return_tracks):
			if track.mute:
				track.mute = False
	
