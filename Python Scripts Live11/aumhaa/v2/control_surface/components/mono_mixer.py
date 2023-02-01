# by amounra 0216 : http://www.aumhaa.com
# written against Live 10.0.5 on 102318


import Live
import math
from itertools import zip_longest, product, chain
from ableton.v2.base import listens, listens_group, EventObject, liveobj_valid, nop, clamp, listenable_property, liveobj_changed
import ableton.v2.base.task as Task
from ableton.v2.control_surface import DeviceBankRegistry
from ableton.v2.control_surface.components import ChannelStripComponent as ChannelStripComponentBase, MixerComponent as MixerComponentBase
from ableton.v2.control_surface import ParameterSlot

from _Generic.Devices import *

from aumhaa.v2.control_surface.components.device import DeviceComponent
from aumhaa.v2.base.debug import *

debug = initialize_debug()

EQ_DEVICES = {'Eq8': {'Gains': [ '%i Gain A' % (index + 1) for index in range(8) ]},
 'FilterEQ3': {'Gains': ['GainHi', 'GainMid', 'GainLo'],
			   'Cuts': ['LowOn', 'MidOn', 'HighOn']}}

TRACK_FOLD_DELAY = 0.5


def release_control(control):
	if control != None:
		control.release_parameter()


class TrackArmState(EventObject):
	__events__ = ('arm',)


	def __init__(self, track = None, *a, **k):
		super(TrackArmState, self).__init__(*a, **k)
		self.set_track(track)


	def set_track(self, track):
		self._track = track
		self._arm = track and track.can_be_armed and (track.arm or track.implicit_arm)
		subject = track if track and track.can_be_armed else None
		self._on_explicit_arm_changed.subject = subject
		self._on_implicit_arm_changed.subject = subject


	@listens('arm')
	def _on_explicit_arm_changed(self):
		self._on_arm_changed()


	@listens('implicit_arm')
	def _on_implicit_arm_changed(self):
		self._on_arm_changed()


	def _on_arm_changed(self):
		if not self._track.arm:
			new_state = self._track.implicit_arm
			self._arm = self._arm != new_state and new_state
			self.notify_arm()


	def _get_arm(self):
		return self._arm if self._track.can_be_armed else False


	def _set_arm(self, new_state):
		if self._track.can_be_armed:
			self._track.arm = new_state
			if not new_state:
				self._track.implicit_arm = False
		self._arm = new_state


	arm = property(_get_arm, _set_arm)


def turn_button_on_off(button, on = True):
	if button != None:
		if on:
			button.turn_on()
		else:
			button.turn_off()




class ChannelStripStaticDeviceProvider(EventObject):


	device_selection_follows_track_selection = False
	_device = None

	def __init__(self, *a, **k):
		super(ChannelStripStaticDeviceProvider, self).__init__(*a, **k)


	@listenable_property
	def device(self):
		#debug('returning:', self._device)
		return self._device


	@device.setter
	def device(self, device):
		#debug('provider device_setter:', device)
		if liveobj_changed(self._device, device):
			self._device = device
			self.notify_device()



class ChannelStripDeviceComponent(DeviceComponent):


	def show_message(self, *a, **k):
		pass


class MonoChannelStripComponent(ChannelStripComponentBase):

	_mute_on_color = 'DefaultButton.On'
	_mute_off_color = 'DefaultButton.Off'
	_solo_on_color = 'DefaultButton.On'
	_solo_off_color = 'DefaultButton.Off'
	_arm_on_color = 'DefaultButton.On'
	_arm_selected_color = 'DefaultButton.On'
	_arm_implicit_color = 'DefaultButton.On'
	_arm_off_color = 'DefaultButton.Off'
	_selected_on_color = 'DefaultButton.On'
	_selected_off_color = 'DefaultButton.Off'
	_clip_stop_color = 'DefaultButton.On'
	_xfade_off_color = 'DefaultButton.Off'
	_xfade_a_color = 'DefaultButton.On'
	_xfade_b_color = 'DefaultButton.On'
	empty_color = 'DefaultButton.Off'
	_eq_gain_controls = None
	_eq_device = None
	_record_button_value = 0
	_arming_select_button = None
	_output_meter_level_control = None
	_output_meter_left_control = None
	_output_meter_right_control = None
	_device_component = None
	_device_provider = None

	def __init__(self, *a, **k):
		super(MonoChannelStripComponent, self).__init__(*a, **k)
		def make_property_slot(name, alias = None):
			alias = alias or name
			return self.register_slot(None, getattr(self, '_on_%s_changed' % alias), name)
		self._track_property_slots.append(make_property_slot('output_meter_level'))
		self._track_property_slots.append(make_property_slot('output_meter_left'))
		self._track_property_slots.append(make_property_slot('output_meter_right'))

		self._playing_clip = None

		# def make_control_slot(name):
		#     return self.register_slot(None, getattr(self, u'_%s_value' % name), u'value')
		self.register_slot(None, getattr(self, '_output_meter_level_value'), 'value')
		self.register_slot(None, getattr(self, '_output_meter_left_value'), 'value')
		self.register_slot(None, getattr(self, '_output_meter_right_value'), 'value')

		self._device_provider = ChannelStripStaticDeviceProvider()
		self._device_component = self._create_device(device_provider=self._device_provider)
		self._track_state = self.register_disconnectable(TrackArmState())
		self._fold_task = self._tasks.add(Task.sequence(Task.wait(TRACK_FOLD_DELAY), Task.run(self._do_fold_track))).kill()
		self._on_arm_state_changed.subject = self._track_state
		self._ChannelStripComponent__on_selected_track_changed.subject = None
		self._ChannelStripComponent__on_selected_track_changed = self.__on_selected_track_changed
		self.__on_selected_track_changed.subject = self.song.view
		self.__on_selected_track_changed()
		self._update_playing_clip()


	def _create_device(self, device_provider):
		device_component = ChannelStripDeviceComponent(device_provider = device_provider, device_bank_registry = DeviceBankRegistry())
		device_component._show_msg_callback = lambda message: None
		return device_component


	@listens('playing_slot_index')
	def __on_playing_slot_index_changed(self):
		debug('channelstrip.__on_playing_slot_index_changed')
		self._update_playing_clip()

	def _update_playing_clip(self):
		if liveobj_valid(self._track) and self._track.can_be_armed:
			clip = self._track.clip_slots[self._track.playing_slot_index].clip
			self._playing_clip = clip if liveobj_valid(clip) else None
		self.notify_playing_clip(self._playing_clip)

	@listenable_property
	def playing_clip(self):
		return self._playing_clip

	@listens('selected_track')
	def __on_selected_track_changed(self):
		if liveobj_valid(self._track) or self.empty_color == None:
			if self.song.view.selected_track == self._track:
				self.select_button.color = self._selected_on_color
			else:
				self.select_button.color = self._selected_off_color
		else:
			self.select_button.color = self.empty_color
		self._update_track_button()
		self._update_device_selection()



	def set_track(self, track):
		assert(isinstance(track, (type(None), Live.Track.Track)))
		self._on_devices_changed.subject = track
		self.__on_playing_slot_index_changed.subject = track
		self._update_device_selection()
		self._detect_eq(track)
		self._update_playing_clip()
		super(MonoChannelStripComponent,self).set_track(track)


	def set_output_meter_level_control(self, control):
		if control != self._output_meter_level_control:
			release_control(self._output_meter_level_control)
			self._output_meter_level_control = control
			self.update()


	def set_output_meter_left_control(self, control):
		if control != self._output_meter_left_control:
			release_control(self._output_meter_left_control)
			self._output_meter_left_control = control
			self.update()

	def set_output_meter_right_control(self, control):
		if control != self._output_meter_right_control:
			release_control(self._output_meter_right_control)
			self._output_meter_right_control = control
			self.update()

	def _scaled_value(self, pos, minp = 0, maxp= 1):
		minv = 0
		maxv = math.log(127)
		scale = (maxv-minv) / (maxp-minp)
		return math.exp(minv + scale*(pos-minp))


	def _on_output_meter_level_changed(self):
		if self.is_enabled() and self._output_meter_level_control != None:
			if liveobj_valid(self._track):
				level = self._track.output_meter_level
				# debug('level is:', level)
				maxp = 1 if self._track.has_audio_output else 8
				scaled_level = self._scaled_value(level, 0, maxp)
				# debug('scaled_level is:', scaled_level)
				self._output_meter_level_control.send_value(scaled_level)

	def _on_output_meter_left_changed(self):
		if self.is_enabled() and self._output_meter_left_control != None:
			if liveobj_valid(self._track) and self._track.has_audio_output:
				level = self._track.output_meter_left
				# debug('level is:', level)
				# maxp = 1 if self._track.has_audio_output else 8
				scaled_level = self._scaled_value(level, 0, 1)
				# debug('scaled_left_level is:', scaled_level)
				self._output_meter_left_control.send_value(scaled_level)


	def _on_output_meter_right_changed(self):
		if self.is_enabled() and self._output_meter_right_control != None:
			if liveobj_valid(self._track) and self._track.has_audio_output:
				level = self._track.output_meter_right
				# debug('level is:', level)
				# maxp = 1 if self._track.has_audio_output else 8
				scaled_level = self._scaled_value(level, 0, 1)
				# debug('scaled_right_level is:', scaled_level)
				self._output_meter_right_control.send_value(scaled_level)


	def _on_mute_changed(self):
		if self.is_enabled() and self._mute_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in chain(self.song.tracks, self.song.return_tracks) and self._track.mute != self._invert_mute_feedback:
					self._mute_button.set_light(self._mute_on_color)
				else:
					self._mute_button.set_light(self._mute_off_color)
			else:
				self._mute_button.set_light(self.empty_color)


	def _on_solo_changed(self):
		if self.is_enabled() and self._solo_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in chain(self.song.tracks, self.song.return_tracks) and self._track.solo:
					self._solo_button.set_light(self._solo_on_color)
				else:
					self._solo_button.set_light(self._solo_off_color)
			else:
				self._solo_button.set_light(self.empty_color)


	def _on_arm_changed(self):
		if self.is_enabled() and self._arm_button != None:
			if liveobj_valid(self._track) or self.empty_color == None:
				if self._track in self.song.tracks and self._track.can_be_armed and self._track.arm:
					self._arm_button.set_light(self._arm_on_color)
				else:
					self._arm_button.set_light(self._arm_off_color)
			else:
				self._arm_button.set_light(self.empty_color)
		self._update_track_button()


	def _on_cf_assign_changed(self):
		if self.is_enabled() and self._crossfade_toggle != None:
			if liveobj_valid(self._track) and self._track in chain(self.song.tracks, self.song.return_tracks):
				val = self._track.mixer_device.crossfade_assign
				if val == 0:
					self._crossfade_toggle.set_light(self._xfade_a_color)
				elif val == 2:
					self._crossfade_toggle.set_light(self._xfade_b_color)
				else:
					self._crossfade_toggle.set_light(self._xfade_off_color)
			else:
				self._crossfade_toggle.turn_off()
			#debug('xfade toggle is:', self._track.mixer_device.crossfade_assign)


	def set_stop_button(self, button):
		#debug('setting stop button:', button)
		button and button.reset()
		self._on_stop_value.subject = button
		button and button.set_light(self._clip_stop_color)


	@listens('value')
	def _on_stop_value(self, value):
		if self._track:
			self._track.stop_all_clips()


	def update(self, *a, **k):
		super(MonoChannelStripComponent, self).update()
		self._update_device_selection()


	def set_invert_mute_feedback(self, invert_feedback):
		assert(isinstance(invert_feedback, type(False)))
		self._invert_mute_feedback = invert_feedback
		self.update()


	def set_eq_gain_controls(self, controls):
		for control in list(self._eq_gain_controls or []):
			release_control(control)
		self._eq_gain_controls = controls
		self.update()


	def set_parameter_controls(self, controls):
		self._device_component.set_parameter_controls(controls)


	@listens('devices')
	def _on_devices_changed(self):
		#debug(self.name, 'on devices changed')
		self._update_device_selection()
		self._detect_eq(self._track)
		self.update()


	def _detect_eq(self, track = None):
		self._eq_device = None
		if not track is None:
			for index in range(len(track.devices)):
				device = track.devices[-1 * (index + 1)]
				if device.class_name in list(EQ_DEVICES.keys()):
					self._eq_device = device
					break


	def _connect_parameters(self):
		super(MonoChannelStripComponent, self)._connect_parameters()
		if not self._eq_device is None:
			device_dict = EQ_DEVICES[self._eq_device.class_name]
			if self._eq_gain_controls != None:
				gain_names = device_dict['Gains']
				index = 0
				for eq_gain_control in self._eq_gain_controls:
					if eq_gain_control != None:
						if len(gain_names) > index:
							parameter = get_parameter_by_name(self._eq_device, gain_names[index])
							if parameter != None:
								eq_gain_control.connect_to(parameter)
							else:
								eq_gain_control.release_parameter()
								self._empty_control_slots.register_slot(eq_gain_control, nop, 'value')
						else:
							eq_gain_control.release_parameter()
							self._empty_control_slots.register_slot(eq_gain_control, nop, 'value')
					index += 1


	def _all_controls(self):
		return [self._pan_control, self._volume_control] + list(self._send_controls or []) + list(self._eq_gain_controls or [])


	def _update_device_selection(self):
		track = self._track
		device_to_select = None
		if track and device_to_select == None and len(track.devices) > 0:
			device_to_select = track.devices[0]
		self._device_provider.device = device_to_select


	@listens('arm')
	def _on_arm_state_changed(self):
		if self.is_enabled() and self._track:
			self._update_track_button()


	def set_arming_select_button(self, button):
		button and button.reset()
		self._arming_select_button = button
		self._arming_select_value.subject = button
		self._update_track_button()


	@listens('value')
	def _arming_select_value(self, value):
		if value and self.song.view.selected_track == self._track:
			self._do_toggle_arm(exclusive=self.song.exclusive_arm)
		else:
			if liveobj_valid(self._track) and self.song.view.selected_track != self._track:
				self.song.view.selected_track = self._track
		if value and liveobj_valid(self._track) and self._track.is_foldable and self._arming_select_button and self._arming_select_button.is_momentary():
			self._fold_task.restart()
		else:
			self._fold_task.kill()

	@listens('value')
	def _output_meter_level_value(self, value):
		pass

	@listens('value')
	def _output_meter_left_value(self, value):
		pass

	@listens('value')
	def _output_meter_right_value(self, value):
		pass

	def _do_toggle_arm(self, exclusive = False):
		if self._track.can_be_armed:
			self._track.arm = not self._track.arm
			if exclusive and (self._track.implicit_arm or self._track.arm):
				for track in self.song.tracks:
					if track.can_be_armed and track != self._track:
						track.arm = False


	def _do_fold_track(self):
		if self.is_enabled() and self._track != None and self._track.is_foldable:
			self._track.fold_state = not self._track.fold_state


	def _do_select_track(self, track):
		pass


	def _update_track_button(self):
		if self.is_enabled():
			if self._arming_select_button != None:
				if not liveobj_valid(self._track):
					self._arming_select_button.set_light(self.empty_color)
				elif self._track.can_be_armed and (self._track.arm or self._track.implicit_arm):
					if self._track == self.song.view.selected_track:
						if self._track.arm:
							self._arming_select_button.set_light(self._arm_selected_color)
						else:
							self._arming_select_button.set_light(self._arm_selected_implicit_color)
					else:
						self._arming_select_button.set_light(self._arm_on_color)
				elif self._track == self.song.view.selected_track:
					self._arming_select_button.set_light(self._selected_on_color)
				else:
					self._arming_select_button.set_light(self._selected_off_color)


	def disconnect(self):
		self._device_component._get_device = lambda: None
		super(MonoChannelStripComponent, self).disconnect()




class MonoMixerComponent(MixerComponentBase):


	_channel_strip_class = MonoChannelStripComponent

	def __init__(self, num_returns = 4, enable_skinning = False, *a, **k):
		self._return_strips = []
		self._return_controls = None
		super(MonoMixerComponent, self).__init__(*a, **k)
		for index in range(num_returns):
			self._return_strips.append(self._create_strip())
			#self.register_components(self._return_strips[index])
		enable_skinning and self._assign_skin_colors()
		self._reassign_tracks()


	def _create_strip(self):
		return self._channel_strip_class()


	def _assign_skin_colors(self):
		for strip in self._channel_strips + self._return_strips + [self._master_strip, self._selected_strip]:
			strip._mute_on_color = 'Mixer.MuteOn'
			strip._mute_off_color = 'Mixer.MuteOff'
			strip._solo_on_color = 'Mixer.SoloOn'
			strip._solo_off_color = 'Mixer.SoloOff'
			strip._arm_on_color = 'Mixer.ArmUnselected'
			strip._arm_selected_color = 'Mixer.ArmSelected'
			strip._arm_selected_implicit_color = 'Mixer.ArmSelectedImplicit'
			strip._arm_off_color = 'Mixer.ArmOff'
			strip._selected_on_color = 'Mixer.SelectedOn'
			strip._selected_off_color = 'Mixer.SelectedOff'
			strip._clip_stop_color = 'Mixer.StopClip'
			strip._xfade_off_color = 'Mixer.XFadeOff'
			strip._xfade_a_color = 'Mixer.XFadeAOn'
			strip._xfade_b_color = 'Mixer.XFadeBOn'


	def return_strip(self, index):
		assert(index in range(len(self._return_strips)))
		return self._return_strips[index]


	def _reassign_tracks(self):
		super(MonoMixerComponent, self)._reassign_tracks()
		for track, channel_strip in zip(self.song.return_tracks, self._return_strips):
			channel_strip.set_track(track)


	def set_output_meter_level_controls(self, controls):
		for strip, control in zip_longest(self._channel_strips, controls or []):
			strip.set_output_meter_level_control(control)


	def set_output_meter_left_controls(self, controls):
		for strip, control in zip_longest(self._channel_strips, controls or []):
			strip.set_output_meter_left_control(control)


	def set_output_meter_right_controls(self, controls):
		for strip, control in zip_longest(self._channel_strips, controls or []):
			strip.set_output_meter_right_control(control)


	def set_send_controls(self, controls):
		self._send_controls and self._send_controls.reset()
		self._send_controls = controls
		if controls:
			for index in range(len(self._channel_strips)):
				send_controls = [controls.get_button(row, index) for row in range(controls.height())]
				if self.send_index > controls.height():
					send_controls = send_controls + [None for _ in range(self.send_index - controls.height())]
				self._channel_strips[index].set_send_controls(send_controls)
		else:
			for strip in self._channel_strips:
				if self.send_index is None:
					strip.set_send_controls([None])
				else:
					strip.set_send_controls([None for _ in range(self.send_index)])


	def set_return_controls(self, controls):
		self._return_controls = controls
		for channel_strip, control in zip_longest(self._return_strips, controls or []):
			if channel_strip:
				channel_strip.set_volume_control(control)
				channel_strip.update()


	def set_crossfade_toggles(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_crossfade_toggle(button)


	def set_stop_clip_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_stop_button(button)


	def set_arming_track_select_buttons(self, buttons):
		for strip, button in zip_longest(self._channel_strips, buttons or []):
			strip.set_arming_select_button(button)


	def set_eq_gain_controls(self, controls):
		self._eq_controls = controls
		if controls:
			for index in range(len(self._channel_strips)):
				eq_controls = [controls.get_button(row, index) for row in range(controls.height())]
				self._channel_strips[index].set_eq_gain_controls(eq_controls)
		else:
			for strip in self._channel_strips:
				strip.set_eq_gain_controls(None)


	def set_parameter_controls(self, controls):
		self._parameter_controls = controls
		if controls:
			for index in range(len(self._channel_strips)):
				parameter_controls = [controls.get_button(row, index) for row in range(controls.height())]
				self._channel_strips[index].set_parameter_controls(parameter_controls)
		else:
			for strip in self._channel_strips:
				strip.set_parameter_controls(None)


	def tracks_to_use(self):
		return tuple(self.song.visible_tracks) + tuple(self.song.return_tracks)


	def set_track_select_dial(self, dial):
		self._on_track_select_dial_value.subject = dial


	@listens('value')
	def _on_track_select_dial_value(self, value):
		#debug('_on_track_select_dial_value', value)
		if value > 64:
			self.select_prev_track()
		else:
			self.select_next_track()


	def select_next_track(self):
		if self.is_enabled():
			selected_track = self.song.view.selected_track
			all_tracks = tuple(self.song.visible_tracks) + tuple(self.song.return_tracks) + (self.song.master_track,)
			assert(selected_track in all_tracks)
			if selected_track != all_tracks[-1]:
				index = list(all_tracks).index(selected_track)
				self.song.view.selected_track = all_tracks[index + 1]


	def select_prev_track(self):
		if self.is_enabled():
			selected_track = self.song.view.selected_track
			all_tracks = tuple(self.song.visible_tracks) + tuple(self.song.return_tracks) + (self.song.master_track,)
			assert(selected_track in all_tracks)
			if selected_track != all_tracks[0]:
				index = list(all_tracks).index(selected_track)
				self.song.view.selected_track = all_tracks[index - 1]
#a
