# by amounra 0719 : http://www.aumhaa.com
# written against Live 10.1 release on 070119


import Live

from ableton.v2.control_surface.component import Component
from ableton.v2.control_surface.control import ButtonControl, control_color
from ableton.v2.base.event import listens

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

def enumerate_track_device(track):
	devices = []
	if hasattr(track, 'devices'):
		for device in track.devices:
			devices.append(device)
			if device.can_have_chains:
				for chain in device.chains:
					for chain_device in enumerate_track_device(chain):
						devices.append(chain_device)
	return devices


class TaggedDefaultsComponent(Component):

	reset_button = ButtonControl(color = 'TaggedDefaults.ResetOff', pressed_color = 'TaggedDefaults.ResetOn')

	def __init__(self, parent, prefix = '@def', *a, **k):
		super(TaggedDefaultsComponent, self).__init__(*a, **k)
		self._parent = parent
		self._prefix = prefix
		self._button = None
		self._defaults_registry = []


	def disconnect(self, *a, **k):
		super(TaggedDefaultsComponent, self).disconnect()


	@reset_button.pressed
	def reset_button(self, button):
		if self.is_enabled():
			self.set_defaults()


	def set_defaults(self):
		for track in self.song.tracks:
			for device in enumerate_track_device(track):
				if device.class_name.endswith('GroupDevice'):
					self.scan_device(device)
		for return_track in self.song.return_tracks:
			for device in enumerate_track_device(return_track):
				if device.class_name.endswith('GroupDevice'):
					self.scan_device(device)
		for device in enumerate_track_device(self.song.master_track):
			if device.class_name.endswith('GroupDevice'):
				self.scan_device(device)


	def scan_device(self, device):
		prefix = str(self._prefix)+':'
		for param in device.parameters:
			for item in param.name.split(' '):
				if item.startswith(prefix):
					vals = item.split(':')
					self.set_param_to_default(param, vals[1])


	def set_param_to_default(self, param, val):
		rst_val = float(val)/100
		newval = float(rst_val * (param.max - param.min)) + param.min
		param.value = newval
