# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516



import Live
from ableton.v2.base import listens, forward_property, clamp, listenable_property, depends, task, liveobj_valid, liveobj_changed
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl, ToggleButtonControl, control_color
from aumhaa.v2.base import initialize_debug

debug = initialize_debug()


"""A component to store and recall individual values in registers corresponding to the currently selected tracks Channel assignment"""

CHANNELS = ['Ch. 2', 'Ch. 3', 'Ch. 4', 'Ch. 5', 'Ch. 6', 'Ch. 7', 'Ch. 8', 'Ch. 9', 'Ch. 10', 'Ch. 11', 'Ch. 12', 'Ch. 13', 'Ch. 14']



class ChannelizedSettingsBase(Component):


	@depends(parent_task_group = None)
	def __init__(self, value_dict = [False, True], parent_task_group = None, number_channels = 16, default_value_index = 0, default_channel = 0, channel_list = CHANNELS, *a, **k):
		self._value_dict = value_dict
		self._range = len(value_dict)
		self._number_channels = number_channels
		self._channel = default_channel
		self._values = [default_value_index for x in range(number_channels)]
		self._channel_list = channel_list
		self._parent_task_group = parent_task_group
		super(ChannelizedSettingsBase, self).__init__(*a, **k)
		self._on_selected_track_changed.subject = self.song.view
		self._update_task = parent_task_group.add(task.sequence(task.wait(.01), task.run(self.update)))
		self._update_task.kill()
	

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
		self._channel = self._get_current_channel()
		self._update_task.restart()
	

	@property
	def channel(self):
		return self._channel
	

	@channel.setter
	def channel(self, channel):
		self._channel = clamp(channel, 0, self._number_channels)
		self.update()
	

	"""self._values is array of indexes, they must be converted to actual values before reporting"""
	@listenable_property
	def value(self):
		return self._value_dict[self.index]
	

	@value.setter
	def value(self, value):
		if value in self._value_dict:
			self._values[self._channel] = self._value_dict.index(value)
			self.update()
	

	def set_value(self, value):
		if value in self._value_dict:
			self._values[self._channel] = self._value_dict.index(value)
	

	@listenable_property
	def index(self):
		return self._values[self._channel]
	

	@index.setter
	def index(self, index):
		if index in range(self._range):
			self._values[self._channel] = index
			self.update()
	

	def set_index(self, index):
		if index in range(self._range):
			self._values[self._channel] = index
	

	def _update_controls(self):
		pass
	

	def update(self):
		if self.is_enabled():
			self.notify_index(self.index)
			self.notify_value(self.value)
			self._update_controls()
	

	def on_enabled_changed(self):
		self._update_task.restart()
	


class ToggledChannelizedSettingsComponent(ChannelizedSettingsBase):


	toggle_button = ToggleButtonControl()

	def __init__(self, toggled_color = 'DefaultButton.On', untoggled_color = 'DefaultButton.Off', *a, **k):
		super(ToggledChannelizedSettingsComponent, self).__init__(value_dict = [False, True], *a, **k)
		self.toggle_button.toggled_color = toggled_color
		self.toggle_button.untoggled_color = untoggled_color
	

	@toggle_button.toggled
	def toggle_button(self, toggled, button):
		self.index = int(toggled)
		self.update()
	

	def _update_controls(self):
		self.toggle_button.is_toggled = bool(self._values[self._channel])
	


class ScrollingChannelizedSettingsComponent(ChannelizedSettingsBase):


	up_button = ButtonControl(repeat=True)
	down_button = ButtonControl(repeat=True)
	bank_up_button = ButtonControl(repeat=True)
	bank_down_button = ButtonControl(repeat=True)
	shift_toggle = ToggleButtonControl()

	def __init__(self, bank_increment = 16, on_color = 'DefaultButton.On', off_color = 'DefaultButton.Off', bank_on_color = 'DefaultButton.On', bank_off_color = 'DefaultButton.Off', *a, **k):
		super(ScrollingChannelizedSettingsComponent, self).__init__(*a, **k)
		self._bank_increment = bank_increment
		self.up_button.color = on_color
		self.up_button.disabled_color = off_color
		self.down_button.color = on_color
		self.down_button.disabled_color = off_color
		self.shift_toggle.toggled_color = on_color
		self.shift_toggle.untoggled_color = off_color
	

	@up_button.pressed
	def up_button(self, button):
		if self.shift_toggle.is_toggled:
			value = self._values[self._channel]
			self.index = clamp(value+self._bank_increment, 0, (self._range-1))
		else:
			value = self._values[self._channel]
			self.index = clamp(value+1, 0, (self._range-1))
	

	@down_button.pressed
	def down_button(self, button):
		if self.shift_toggle.is_toggled:
			value = self._values[self._channel]
			self.index = clamp(value-self._bank_increment, 0, (self._range-1))
		else:
			value = self._values[self._channel]
			self.index = clamp(value-1, 0, (self._range-1))
	

	@bank_up_button.pressed
	def bank_up_button(self, button):
		value = self._values[self._channel]
		self.index = clamp(value+self._bank_increment, 0, (self._range-1))
	

	@bank_down_button.pressed
	def bank_down_button(self, button):
		value = self._values[self._channel]
		self.index = clamp(value-self._bank_increment, 0, (self._range-1))
	

	def _update_controls(self):
		at_beginning = self.index == 0
		at_end = self.index == (self._range - 1)
		self.up_button.enabled = not at_end
		self.down_button.enabled = not at_beginning
		self.bank_up_button.enabled = not at_end
		self.bank_down_button.enabled = not at_beginning
	

	def buttons_are_pressed(self):
		return self.up_button.is_pressed or self.down_button.is_pressed or self.bank_up_button.is_pressed or self.bank_down_button.is_pressed
	


class TaggedSettingsComponent(ScrollingChannelizedSettingsComponent):


	_set_attribute_tag_model = lambda self, a: int(a)
	_track_has_tagged_attribute = False
	_last_track = None

	def __init__(self, attribute_tag = None, *a, **k):
		self._attribute_tag = '@'+attribute_tag+':'
		super(TaggedSettingsComponent, self).__init__(*a, **k)
		self._read_tag_task = self._parent_task_group.add(task.sequence(task.wait(.1), task.run(self._read_attribute_tag)))
		self._read_tag_task.kill()
		self._set_tag_task = self._parent_task_group.add(task.sequence(task.wait(.1), task.run(self._set_attribute_tag)))
		self._set_tag_task.kill()
	

	@listens('selected_track')
	def _on_selected_track_changed(self):
		super(TaggedSettingsComponent, self)._on_selected_track_changed()
		#debug('setting tagged to False')
		if liveobj_changed(self.song.view.selected_track, self._last_track):
			self._last_track = self.song.view.selected_track
			self._track_has_tagged_attribute = False
			self._read_attribute_tag()
		
	

	def _read_attribute_tag(self):
		devices = self.song.view.selected_track.devices
		device = len(devices) and devices[0] or None
		if liveobj_valid(device):
			name = device.name
			for item in name.split(' '):
				if item.startswith(self._attribute_tag):
					entry = self._set_attribute_tag_model(item[len(self._attribute_tag):])
					try:
						self._values[self._channel] = self._value_dict.index(entry)
					except:
						debug('cant read attribute error for:', device.name, entry)
					#debug('setting tagged to True')
					self._track_has_tagged_attribute = True
	

	def _set_attribute_tag(self):
		devices = self.song.view.selected_track.devices
		device = len(devices) and devices[0] or None
		if liveobj_valid(device):
			name = device.name.split(' ')
			for item in name:
				if item.startswith(self._attribute_tag):
					entry = self._attribute_tag+str(self._value_dict[self._values[self._channel]])
					try:
						name[name.index(item)] = str(entry)
						device.name = ' '.join(name)
					except:
						debug('cant set attribute error for:', device.name, entry, ''.join(name))
	

	def update(self):
		super(TaggedSettingsComponent, self).update()
		if self._track_has_tagged_attribute:
			self._set_tag_task.restart()
	










