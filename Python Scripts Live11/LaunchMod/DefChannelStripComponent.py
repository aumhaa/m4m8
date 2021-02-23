

import Live
from ableton.v2.base import listens, liveobj_valid
from ableton.v2.control_surface.components.channel_strip import ChannelStripComponent
from .ConfigurableButtonElement import ConfigurableButtonElement
from itertools import chain

from aumhaa.v2.base.debug import *
debug = initialize_debug()

class DefChannelStripComponent(ChannelStripComponent):
	""" Subclass of channel strip component offering defaultbuttons for the timeables """


	empty_color = 'DefaultButton.Disabled'

	def __init__(self):
		super(DefChannelStripComponent, self).__init__()
		self._default_volume_button = None
		self._default_panning_button = None
		self._default_send1_button = None
		self._default_send2_button = None
		self._invert_mute_feedback = True

		def make_property_slot(name, alias = None):
			alias = alias or name
			return self.register_slot(None, getattr(self, '_on_%s_changed' % alias), name)
	

		def make_button_slot(name):
			return self.register_slot(None, getattr(self, '_%s_value' % name), 'value')
	
		self._default_volume_button_slot = make_button_slot('default_volume')
		self._default_panning_button_slot = make_button_slot('default_panning')
		self._default_send1_button_slot = make_button_slot('default_send1')
		self._default_send2_button_slot = make_button_slot('default_send2')
	

	def disconnect(self):
		self._default_volume_button = None
		self._default_panning_button = None
		self._default_send1_button = None
		self._default_send2_button = None
		super(DefChannelStripComponent, self).disconnect()
	

	def set_track(self, track):
		super(DefChannelStripComponent, self).set_track(track)
		self._on_volume_changed.subject = track.mixer_device.volume if liveobj_valid(track) else None
		self._on_panning_changed.subject = track.mixer_device.panning if liveobj_valid(track) else None
		self._on_send1_changed.subject = track.mixer_device.sends[0] if liveobj_valid(track) and len(track.mixer_device.sends) else None
		self._on_send2_changed.subject = track.mixer_device.sends[1] if liveobj_valid(track) and len(track.mixer_device.sends) > 1 else None
	

	def set_default_buttons(self, volume, panning, send1, send2):
		if not (volume == None or isinstance(volume, ConfigurableButtonElement)):
			raise AssertionError
			if not (panning == None or isinstance(panning, ConfigurableButtonElement)):
				raise AssertionError
				if not (send1 == None or isinstance(send1, ConfigurableButtonElement)):
					raise AssertionError
					if not (send2 == None or isinstance(send2, ConfigurableButtonElement)):
						raise AssertionError
						if volume != self._default_volume_button:
							if self._default_volume_button != None:
								self._default_volume_button.remove_value_listener(self._default_volume_value)
							self._default_volume_button = volume
							if self._default_volume_button != None:
								self._default_volume_button.add_value_listener(self._default_volume_value)
						if panning != self._default_panning_button:
							if self._default_panning_button != None:
								self._default_panning_button.remove_value_listener(self._default_panning_value)
							self._default_panning_button = panning
							if self._default_panning_button != None:
								self._default_panning_button.add_value_listener(self._default_panning_value)
						if send1 != self._default_send1_button:
							if self._default_send1_button != None:
								self._default_send1_button.remove_value_listener(self._default_send1_value)
							self._default_send1_button = send1
							self._default_send1_button != None and self._default_send1_button.add_value_listener(self._default_send1_value)
					send2 != self._default_send2_button and self._default_send2_button != None and self._default_send2_button.remove_value_listener(self._default_send2_value)
				self._default_send2_button = send2
				self._default_send2_button != None and self._default_send2_button.add_value_listener(self._default_send2_value)
		self.update()

	def set_default_panning_button(self, button):
		if button != self._default_panning_button:
			self.reset_button_on_exchange(self._default_panning_button)
			self._default_panning_pressed = False
			self._default_panning_button = button
			self._default_panning_button_slot.subject = button
			self.update()
	

	def set_default_volume_button(self, button):
		if button != self._default_volume_button:
			self.reset_button_on_exchange(self._default_volume_button)
			self._default_volume_pressed = False
			self._default_volume_button = button
			self._default_volume_button_slot.subject = button
			self.update()
	

	def set_default_send1_button(self, button):
		if button != self._default_send1_button:
			self.reset_button_on_exchange(self._default_send1_button)
			self._default_send1_pressed = False
			self._default_send1_button = button
			self._default_send1_button_slot.subject = button
			self.update()
	

	def set_default_send2_button(self, button):
		if button != self._default_send2_button:
			self.reset_button_on_exchange(self._default_send2_button)
			self._default_send2_pressed = False
			self._default_send2_button = button
			self._default_send2_button_slot.subject = button
			self.update()
	

	def update(self):
		super(DefChannelStripComponent, self).update()
		if self._allow_updates:
			if self.is_enabled():
				self._on_volume_changed()
				self._on_panning_changed()
				self._on_send1_changed()
				self._on_send2_changed()
	

		"""
		if self._allow_updates:
			if self.is_enabled():
				if self._track != None:
					volume = self._track.mixer_device.volume
					panning = self._track.mixer_device.panning
					sends = self._track.mixer_device.sends
					if not volume.value_has_listener(self._on_volume_changed):
						volume.add_value_listener(self._on_volume_changed)
					if not panning.value_has_listener(self._on_panning_changed):
						panning.add_value_listener(self._on_panning_changed)
					if len(sends) > 0:
						if not sends[0].value_has_listener(self._on_send1_changed):
							sends[0].add_value_listener(self._on_send1_changed)
						self._on_send1_changed()
					elif self._default_send1_button != None:
						self._default_send1_button.turn_off()
					if len(sends) > 1:
						if not sends[1].value_has_listener(self._on_send2_changed):
							sends[1].add_value_listener(self._on_send2_changed)
						self._on_send2_changed()
					elif self._default_send2_button != None:
						self._default_send2_button.turn_off()
					self._on_volume_changed()
					self._on_panning_changed()
				else:
					if self._default_volume_button != None:
						self._default_volume_button.reset()
					if self._default_panning_button != None:
						self._default_panning_button.reset()
					if self._default_send1_button != None:
						self._default_send1_button.reset()
					if self._default_send2_button != None:
						self._default_send2_button.reset()
					if self._mute_button != None:
						self._mute_button.reset()
					if self._arm_button != None:
						self._arm_button.reset()
					if self._solo_button != None:
						self._solo_button.reset()
					if self._volume_control != None:
						self._volume_control.reset()
					if self._pan_control != None:
						self._pan_control.reset()
					if self._send_controls != None:
						for send_control in self._send_controls:
							if send_control != None:
								send_control.reset()
		"""

	def _default_volume_value(self, value):
		debug('_default_volume_value', value)
		assert self._default_volume_button != None
		assert value in range(128)
		if self.is_enabled() and self._track != None:
			if (value != 0 or not self._default_volume_button.is_momentary()) and self._track.mixer_device.volume and self._track.mixer_device.volume.is_enabled:
				self._track.mixer_device.volume.value = self._track.mixer_device.volume.default_value
	

	def _default_panning_value(self, value):
		assert self._default_panning_button != None
		assert value in range(128)
		if self.is_enabled() and self._track != None:
			if (value != 0 or not self._default_panning_button.is_momentary()) and self._track.mixer_device.panning and self._track.mixer_device.panning.is_enabled:
				self._track.mixer_device.panning.value = self._track.mixer_device.panning.default_value
	

	def _default_send1_value(self, value):
		assert self._default_send1_button != None
		assert value in range(128)
		if self.is_enabled() and self._track != None and len(self._track.mixer_device.sends) > 0:
			if (value != 0 or not self._default_send1_button.is_momentary()) and self._track.mixer_device.sends[0] and self._track.mixer_device.sends[0].is_enabled:
				self._track.mixer_device.sends[0].value = self._track.mixer_device.sends[0].default_value
	

	def _default_send2_value(self, value):
		assert self._default_send2_button != None
		assert value in range(128)
		if self.is_enabled() and self._track != None and len(self._track.mixer_device.sends) > 0:
			if (value != 0 or not self._default_send1_button.is_momentary()) and self._track.mixer_device.sends[1] and self._track.mixer_device.sends[1].is_enabled:
				self._track.mixer_device.sends[1].value = self._track.mixer_device.sends[1].default_value
	

	@listens('value')
	def _on_volume_changed(self):
		if not self._default_volume_button is None:
			if liveobj_valid(self._track):
				volume = self._track.mixer_device.volume
				if self.is_enabled() and self._default_volume_button != None and volume.value == volume.default_value:
					self._default_volume_button.set_light('Mixer.DefaultValueOn')
				else:
					self._default_volume_button.set_light('Mixer.DefaultValueOff')
			else:
				self._default_volume_button.set_light('DefaultButton.Disabled')
	

	@listens('value')
	def _on_panning_changed(self):
		if not self._default_panning_button is None:
			if liveobj_valid(self._track):
				panning = self._track.mixer_device.panning
				if self.is_enabled() and self._default_panning_button != None and panning.value == panning.default_value:
					self._default_panning_button.set_light('Mixer.DefaultValueOn')
				else:
					self._default_panning_button.set_light('Mixer.DefaultValueOff')
			else:
				self._default_panning_button.set_light('DefaultButton.Disabled')
	

	@listens('value')
	def _on_send1_changed(self):
		if not self._default_send1_button is None:
			if liveobj_valid(self._track):
				sends = self._track.mixer_device.sends
				assert len(sends) > 0
				if self.is_enabled() and self._default_send1_button != None and sends[0] and sends[0].value == sends[0].default_value:
					self._default_send1_button.set_light('Mixer.DefaultValueOn')
				else:
					self._default_send1_button.set_light('Mixer.DefaultValueOff')
			else:
				self._default_send1_button.set_light('DefaultButton.Disabled')
	

	@listens('value')
	def _on_send2_changed(self):
		if not self._default_send2_button is None:
			if liveobj_valid(self._track):
				sends = self._track.mixer_device.sends
				assert len(sends) > 0
				if self.is_enabled() and self._default_send2_button != None and sends[1] and sends[1].value == sends[1].default_value:
					self._default_send2_button.set_light('Mixer.DefaultValueOn')
				else:
					self._default_send2_button.set_light('Mixer.DefaultValueOff')
			else:
				self._default_send2_button.set_light('DefaultButton.Disabled')
	

	def _on_mute_changed(self):
		if self.is_enabled() and self._mute_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in chain(self.song.tracks, self.song.return_tracks) and self._track.mute != self._invert_mute_feedback:
					self._mute_button.set_light('Mixer.MuteOn')
				else:
					self._mute_button.set_light('Mixer.MuteOff')
			else:
				self._mute_button.set_light(self.empty_color)

	def _on_solo_changed(self):
		if self.is_enabled() and self._solo_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in chain(self.song.tracks, self.song.return_tracks) and self._track.solo:
					self._solo_button.set_light('Mixer.SoloOn')
				else:
					self._solo_button.set_light('Mixer.SoloOff')
			else:
				self._solo_button.set_light(self.empty_color)

	def _on_arm_changed(self):
		if self.is_enabled() and self._arm_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in self.song.tracks and self._track.can_be_armed and self._track.arm:
					self._arm_button.set_light('Mixer.ArmOn')
				else:
					self._arm_button.set_light('Mixer.ArmOff')
			else:
				self._arm_button.set_light(self.empty_color)

