# by amounra 0520 : http://www.aumhaa.com
# written against Live 10.1.14 on 051620


import sys
import os
import copy
import Live
import contextlib
import re

from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.CompoundComponent import CompoundComponent
from _Framework.Task import *
from _Framework.SubjectSlot import subject_slot, subject_slot_group, SlotManager
from _Framework.ScrollComponent import *

from aumhaa.v2.base.debug import initialize_debug

# from ableton.v2.control_surface import ControlSurface as ControlSurface_v2

from aumhaa.v2.control_surface.mod import *

INITIAL_SCROLLING_DELAY = 5
INTERVAL_SCROLLING_DELAY = 1

CS_LIST_KEY = 'control_surfaces'

debug = initialize_debug()


class FrameworkModHandler(CompoundComponent):


	def __init__(self, script, addresses = None, device_selector = None, modrouter = None, *a, **k):
		super(FrameworkModHandler, self).__init__(*a, **k)
		self._script = script
		#self._device_selector = device_selector or DeviceSelectorComponent(script)
		self._color_type = 'RGB'
		self.log_message = script.log_message
		self.modrouter = modrouter
		self._active_mod = None
		self._parameter_controls = None
		self._device_component = None
		self._colors = list(range(128))
		self._is_enabled = False
		self._is_connected = False
		self._is_locked = False
		self._is_alted = False
		self._is_shifted = False
		self._is_shiftlocked = False
		self._receive_methods = {}
		self._addresses = {'grid': {'obj':ButtonGrid('grid', 16, 16), 'method':self._receive_grid},
							'key': {'obj':Array('key', 8), 'method':self._receive_key},
							'shift': {'obj':StoredElement(_name = 'shift'), 'method':self._receive_shift},
							'alt': {'obj':StoredElement(_name = 'alt'), 'method':self._receive_alt},
							'channel': {'obj':RadioArray('channel', 16), 'method':self._receive_channel}}
		self._addresses.update(addresses or {})
		self._grid = None
		self._mod_nav_buttons = None
		self.x_offset = 0
		self.y_offset = 0
		self.navbox_selected = 3
		self.navbox_unselected = 5
		self.navbox = None
		self._initialize_receive_methods()
		self.modrouter.register_handler(self)
		self._on_device_changed.subject = self.song()
		# self.modrouter._task_group.add(sequence(delay(5), self.select_appointed_device))


	def disconnect(self, *a, **k):
		self._active_mod = None
		debug('modhandler disconnect')
		self.modrouter.unregister_handler(self._script, self)
		super(FrameworkModHandler, self).disconnect(*a, **k)


	def _initialize_receive_methods(self):
		addresses = self._addresses
		for address, Dict in addresses.items():
			if not address in list(self._receive_methods.keys()):
				self._receive_methods[address] = Dict['method']


	def _register_addresses(self, client):
		addresses = self._addresses
		for address, Dict in addresses.items():
			if not address in list(client._addresses.keys()):
				client._addresses[address] = copy.deepcopy(Dict['obj'])
				client._addresses[address]._active_handlers = client.active_handlers


	def receive_address(self, address_name, *a, **k):
		#debug('receive_address ' + str(address_name) + str(a))
		if address_name in list(self._receive_methods.keys()):
			self._receive_methods[address_name](*a, **k)


	def update(self, *a, **k):
		if self._active_mod:
			self._active_mod.restore()
		self.update_buttons()


	def select_mod(self, mod = None):
		self._active_mod = mod
		self._colors = list(range(128))
		debug('new mod is:--------------------------------', mod)
		for mod in self.modrouter._mods:
			if self in mod._active_handlers:
				mod._active_handlers.remove(self)
		if not self._active_mod is None:
			self._active_mod._active_handlers.append(self)
			if self._color_type in list(self._active_mod._color_maps.keys()):
				self._colors = self._active_mod._color_maps[self._color_type]
			self._active_mod.restore()
		self.update()


	def active_mod(self, *a, **k):
		return self._active_mod


	@subject_slot('appointed_device')
	def _on_device_changed(self):
		#debug('modhandler on_device_changed')
		if not self.is_locked() or self.active_mod() is None:
			#self.modrouter._task_group.add(sequence(delay(2), self.select_appointed_device))
			self.select_appointed_device()


	def on_selected_track_changed(self):
		#debug('modhandler on_device_changed')
		if not self.is_locked() or self.active_mod() is None:
			#self.modrouter._task_group.add(sequence(delay(2), self.select_appointed_device))
			self.select_appointed_device()


	def select_appointed_device(self, *a):
		debug('select_appointed_device' + str(a))
		track = self.song().view.selected_track
		device_to_select = track.view.selected_device
		if device_to_select == None and len(track.devices) > 0:
			device_to_select = track.devices[0]
		self.select_mod(self.modrouter.is_mod(device_to_select))


	def set_parameter_controls(self, controls):
		debug('setting parameter controls', controls)
		self._parameter_controls = None
		if not controls is None:
			self._parameter_controls = [control for control, _ in controls.iterbuttons()]
		if not self._active_mod is None:
			debug('updating param component')
			self._active_mod._param_component.update()


	def set_device_component(self, device_component):
		self._device_component = device_component


	def update_device(self):
		#debug('update device')
		#self.update_parameter_controls()
		#if self.is_enabled() and not self._device_component is None:
		#	self.update_device()
		pass


	def update_buttons(self):
		self._shift_value.subject and self._shift_value.subject.send_value(7 + self.is_shifted()*7)
		self._on_shiftlock_value.subject and self._on_shiftlock_value.subject.send_value(3 + self.is_shiftlocked()*7)
		self._on_lock_value.subject and self._on_lock_value.subject.send_value(1 + self.is_locked()*7)
		self._alt_value.subject and self._alt_value.subject.send_value(2 + self.is_alted()*7)


	def set_mod_nav_buttons(self, buttons):
		self._mod_nav_buttons = buttons
		self._on_mod_nav_button_value.replace_subjects(buttons)
		self._update_mod_nav_buttons()


	@subject_slot_group('value')
	def _on_mod_nav_button_value(self, value, sender):
		if value and not self._mod_nav_buttons is None:
			direction = self._mod_nav_buttons.index(sender)
			if direction:
				self.nav_mod_up()
			else:
				self.nav_mod_down()


	def _update_mod_nav_buttons(self):
		if not self._mod_nav_buttons is None:
			for button in self._mod_nav_buttons:
				if not button is None:
					button.turn_on()


	def nav_mod_down(self):
		new_mod = self.modrouter.get_previous_mod(self.active_mod())
		debug('new_mod: ' + str(new_mod))
		if isinstance(new_mod, ModClient):
			device = new_mod.linked_device()
			#debug('device: ' + str(device))
			if isinstance(device, Live.Device.Device):
				self.song().view.select_device(device)
				#debug('selected: ' + str(device))
				self.select_mod(new_mod)


	def nav_mod_up(self):
		new_mod = self.modrouter.get_next_mod(self.active_mod())
		debug('new_mod: ' + str(new_mod))
		if isinstance(new_mod, ModClient):
			device = new_mod.linked_device()
			if isinstance(device, Live.Device.Device):
				self.song().view.select_device(device)
				self.select_mod(new_mod)


	def show_mod_in_live(self):
		if isinstance(self.active_mod(), Live.Device.Device):
			self.song().view.select_device(self.active_mod().linked_device())


	def set_grid(self, grid):
		#debug('set grid:' + str(grid))
		self._grid = grid
		self._grid_value.subject = grid
		if not self._grid is None:
			for button, _ in grid.iterbuttons():
				if not button == None:
					button.use_default_message()
					button.suppress_script_forwarding = False
		self.update()


	def _receive_grid(self, *a, **k):
		debug('receive grid:  this should be overridden')


	@subject_slot('value')
	def _grid_value(self, value, x, y, *a, **k):
		# debug('_grid_value ', str(x), str(y), str(value))
		if self.active_mod():
			if self.active_mod().legacy:
				x += self.x_offset
				y += self.y_offset
			self._active_mod.send('grid', x, y, value)


	def set_key_buttons(self, keys):
		self._keys_value.subject = keys
		if self.active_mod():
			self.active_mod()._addresses['key'].restore()


	def _receive_key(self, x, value):
		#debug('_receive_key: %s %s' % (x, value))
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._colors[value], True)


	@subject_slot('value')
	def _keys_value(self, value, x, y, *a, **k):
		if self._active_mod:
			self._active_mod.send('key', x, value)



	def set_channel_buttons(self, buttons):
		self._channel_value.subject = buttons
		if self.active_mod():
			self.active_mod()._addresses['channel'].restore()


	def _receive_channel(self, x, value):
		#debug('_receive_channel:', x, value)
		if not self._channel_value.subject is None and x < self._channel_value.subject.width():
			self._channel_value.subject.send_value(x, 0, self._colors[value], True)


	@subject_slot('value')
	def _channel_value(self, value, x, y, *a, **k):
		#debug('_channel_value: %s %s' % (x, value))
		if value and self._active_mod:
			self._active_mod.send('channel', x)



	def set_shift_button(self, button):
		self._shift_value.subject = button
		if button:
			button.send_value(self.is_shifted())


	def is_shifted(self):
		return self._is_shifted


	def _receive_shift(self, value):
		if not self._shift_value.subject is None:
			self._shift_value.subject.send_value(value)


	@subject_slot('value')
	def _shift_value(self, value, *a, **k):
		self._is_shifted = not value is 0
		if self.active_mod():
			self._active_mod.send('shift', value)
		self.update()



	def set_alt_button(self, button):
		self._alt_value.subject = button
		if button:
			button.send_value(self.is_alted())


	def is_alted(self):
		return self._is_alted


	def _receive_alt(self, value):
		if not self._alt_value.subject is None:
			self._alt_value.subject.send_value(value)


	@subject_slot('value')
	def _alt_value(self, value, *a, **k):
		self._is_alted = not value is 0
		mod = self.active_mod()
		if mod:
			mod.send('alt', value)
			mod._param_component._is_alted = bool(value)
			mod._param_component.update()
			#self.update_device()
		self.update()



	def set_lock_button(self, button):
		self._on_lock_value.subject = button
		self.update()


	def is_locked(self):
		return self._is_locked


	def set_lock(self, value):
		self._is_locked = value > 0
		self.select_appointed_device()


	@subject_slot('value')
	def _on_lock_value(self, value):
		if value>0:
			self.set_lock(not self.is_locked())
		self.update()



	def set_shiftlock_button(self, button):
		self._on_shiftlock_value.subject = button


	def is_shiftlocked(self):
		return self._is_shiftlocked


	@subject_slot('value')
	def _on_shiftlock_value(self, value):
		#debug('shiftlock value ' + str(value))
		if value>0:
			self._is_shiftlocked = not self.is_shiftlocked()
			self.update()



	def set_offset(self, x, y):
		debug('setting offset:', str(x), str(y))
		self.x_offset = x
		self.y_offset = y
		if self._active_mod and self._active_mod.legacy:
			self._active_mod.send('offset', self.x_offset, self.y_offset)
			self.update()


	def _display_nav_box(self):
		pass


	# def set_device_selector_matrix(self, matrix):
	# 	self._device_selector and self._device_selector.set_matrix(matrix)


	def set_nav_matrix(self, matrix):
		self.nav_box and self.nav_box.set_matrix(matrix)


	def set_nav_buttons(self, buttons):
		assert buttons is None or len(buttons)==4
		if buttons is None:
			buttons = [None for index in range(4)]
		self.set_nav_up_button(buttons[0])
		self.set_nav_down_button(buttons[1])
		self.set_nav_left_button(buttons[2])
		self.set_nav_right_button(buttons[3])


	def set_nav_up_button(self, button):
		if not self.nav_box is None:
			self.nav_box.set_nav_up_button(button)


	def set_nav_down_button(self, button):
		if not self.nav_box is None:
			self.nav_box.set_nav_down_button(button)


	def set_nav_left_button(self, button):
		if not self.nav_box is None:
			self.nav_box.set_nav_left_button(button)


	def set_nav_right_button(self, button):
		if not self.nav_box is None:
			self.nav_box.set_nav_right_button(button)


	def on_enabled_changed(self):
		super(FrameworkModHandler, self).on_enabled_changed()
		#if not self.is_enabled():
		#	self._instrument and self._instrument.set_enabled(False)



class FrameworkNavigationBox(CompoundComponent):


	def __init__(self, parent = None, width = None, height = None, window_x = None, window_y = None, callback = None,  *a, **k):
		super(FrameworkNavigationBox, self).__init__(*a, **k)
		self._parent = parent
		self._width = width
		self._height = height
		self._window_x = window_x
		self._window_y = window_y
		self._callback = callback
		self._x_inc = 0
		self._y_inc = 0
		self.on_value = 5
		self.off_value = 1
		self.x_offset = 0
		self.y_offset = 0
		self._vertical_nav, self._horizontal_nav = self.register_components(ScrollComponent(), ScrollComponent())
		self._vertical_nav.can_scroll_up = self._can_scroll_up
		self._vertical_nav.can_scroll_down = self._can_scroll_down
		self._vertical_nav.scroll_up = self._scroll_up
		self._vertical_nav.scroll_down = self._scroll_down
		self._horizontal_nav.can_scroll_up = self._can_scroll_left
		self._horizontal_nav.can_scroll_down = self._can_scroll_right
		self._horizontal_nav.scroll_up = self._scroll_left
		self._horizontal_nav.scroll_down = self._scroll_right
		self.set_nav_down_button = self._vertical_nav.set_scroll_down_button
		self.set_nav_up_button = self._vertical_nav.set_scroll_up_button
		self.set_nav_left_button = self._horizontal_nav.set_scroll_down_button
		self.set_nav_right_button = self._horizontal_nav.set_scroll_up_button
		self._on_off_values = ('DefaultButton.Off', 'DefaultButton.On')


	def width(self):
		return self._width


	def height(self):
		return self._height


	def set_matrix(self, matrix):
		if matrix:
			for button, _ in matrix.iterbuttons():
				# button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
				pass
		self._on_navigation_value.subject = matrix
		if not matrix is None:
			self._x_inc = int(self.width()/matrix.width())
			self._y_inc = int(self.height()/matrix.height())
		else:
			self._x_inc = 0
			self._y_inc = 0
		#debug('incs: ' + str(self._x_inc) + ' ' + str(self._y_inc))
		self.update()

	def _can_scroll_up(self):
		return self.y_offset > 0

	def _can_scroll_down(self):
		return self.y_offset < (self.height() - self._window_y)

	def _scroll_up(self):
		self.set_offset(self.x_offset, self.y_offset -1)

	def _scroll_down(self):
		self.set_offset(self.x_offset, self.y_offset +1)

	def _can_scroll_left(self):
		return self.x_offset < (self.width() - self._window_x)

	def _can_scroll_right(self):
		return self.x_offset > 0

	def _scroll_left(self):
		self.set_offset(self.x_offset +1, self.y_offset)

	def _scroll_right(self):
		self.set_offset(self.x_offset -1, self.y_offset)

	def set_nav_buttons(self, buttons):
		assert buttons is None or len(buttons)==4
		if buttons is None:
			buttons = [None for index in range(4)]
		self.set_nav_up_button(buttons[0])
		self.set_nav_down_button(buttons[1])
		self.set_nav_left_button(buttons[2])
		self.set_nav_right_button(buttons[3])

	@subject_slot('value')
	def _on_navigation_value(self, value, x, y, *a, **k):
		nav_grid = self._on_navigation_value.subject
		if value>0 and nav_grid:
			new_x = self.x_offset
			new_y = self.y_offset
			xinc = self._x_inc
			yinc = self._y_inc
			newx = x*xinc
			newy = y*yinc
			xoff = self.x_offset
			yoff = self.y_offset
			xmax = xoff+self._window_x
			ymax = yoff+self._window_y
			if newx < xoff:
				new_x = newx
			elif newx >= xmax:
				new_x = (newx+xinc)-self._window_x
			if newy < yoff:
				new_y = newy
			elif newy >= ymax:
				new_y = (newy+yinc)-self._window_y
			#new_x = x * self._x_inc
			#new_y = y * self._y_inc
			debug('new offsets:', new_x, new_y)
			self.set_offset(new_x, new_y)

	def update(self):
		if self.is_enabled():
			debug('Nav update')
			nav_grid = self._on_navigation_value.subject
			xinc = self._x_inc
			yinc = self._y_inc
			xoff = self.x_offset
			yoff = self.y_offset
			xmax = xoff+self._window_x
			ymax = yoff+self._window_y
			if nav_grid:
				for button, coord in nav_grid.iterbuttons():
					x = coord[0]
					y = coord[1]
					# debug(x, y, (((x*xinc) in range(xoff, xmax)) and ((y*yinc) in range(yoff, ymax))) )
					button.set_light( self._on_off_values[int(((x*xinc) in range(xoff, xmax)) and ((y*yinc) in range(yoff, ymax)))]  )

	def set_offset(self, x, y):
		self.x_offset = min(x, self.width() - self._window_x)
		self.y_offset = min(y, self.height() - self._window_y)
		self.update()
		if self._callback:
			self._callback(x, y)
