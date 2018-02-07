# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516

from __future__ import with_statement
import sys
import os
import copy
import Live
import contextlib
from re import *
from itertools import chain, imap, izip_longest, izip

from ableton.v2.base import clamp, flatten, depends, listenable_property, listens, listens_group, liveobj_changed, liveobj_valid, EventObject
from ableton.v2.control_surface import ControlSurface, Component, CompoundComponent, ControlElement, NotifyingControlElement, InputSignal
from ableton.v2.control_surface.device_provider import DeviceProvider
from ableton.v2.control_surface.elements import ButtonMatrixElement
from ableton.v2.control_surface.control import ControlManager
from ableton.v2.base.task import *
from ableton.v2.base import Event, listens, listens_group, Signal, in_range, Disconnectable, listenable_property

from aumhaa.v2.control_surface.components import DeviceSelectorComponent, MonoParamComponent, MonoDeviceComponent
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.base.debug import initialize_debug
from aumhaa.v2.control_surface.elements import generate_strip_string

INITIAL_SCROLLING_DELAY = 5
INTERVAL_SCROLLING_DELAY = 1

CS_LIST_KEY = 'control_surfaces'

debug = initialize_debug()

def hascontrol(handler, control):
	return control in handler._controls.keys()


def unpack_values(values):
	values = [int(i) for i in str(values).split('^')]
	if len(values)<2:
		return values[0]
	else:
		return values
	


def unpack_items(values):
	to_convert = str(values).split('^')
	converted = []
	for i in to_convert:
		try:
			converted.append(int(i))
		except:
			converted.append(str(i))
	#if len(converted)<2:
	#	return converted[0]
	#else:
	return converted


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


def get_monomodular(host):
		if isinstance(__builtins__, dict):
			if not 'monomodular' in __builtins__.keys() or not isinstance(__builtins__['monomodular'], ModRouter):
				__builtins__['monomodular'] = ModRouter()
		else:
			if not hasattr(__builtins__, 'monomodular') or not isinstance(__builtins__['monomodular'], ModRouter):
				setattr(__builtins__, 'monomodular', ModRouter())
		monomodular = __builtins__['monomodular']
		if not monomodular.has_host():
			monomodular.set_host(host)
		return monomodular


def get_control_surfaces():
	if isinstance(__builtins__, dict):
		if CS_LIST_KEY not in __builtins__.keys():
			__builtins__[CS_LIST_KEY] = []
		return __builtins__[CS_LIST_KEY]
	else:
		if not hasattr(__builtins__, CS_LIST_KEY):
			setattr(__builtins__, CS_LIST_KEY, [])
		return getattr(__builtins__, CS_LIST_KEY)


def return_empty():
	return []


def appointed_device():
	return Live.song().appointed_device



class SpecialInputSignal(Signal):


	def __init__(self, sender = None, *a, **k):
		super(SpecialInputSignal, self).__init__(sender=sender, *a, **k)
		self._input_control = sender
	

	@contextlib.contextmanager
	def _listeners_update(self):
		old_count = self.count
		yield
		diff_count = self.count - old_count
		self._input_control._input_signal_listener_count += diff_count
		listener_count = self._input_control._input_signal_listener_count
	

	def connect(self, *a, **k):
		with self._listeners_update():
			super(SpecialInputSignal, self).connect(*a, **k)
	

	def disconnect(self, *a, **k):
		with self._listeners_update():
			super(SpecialInputSignal, self).disconnect(*a, **k)
	

	def disconnect_all(self, *a, **k):
		with self._listeners_update():
			super(SpecialInputSignal, self).disconnect_all(*a, **k)
	


class ElementTranslation(object):


	def __init__(self, name, script):
		self._script = script
		self._name = name
		self._targets = {}
		self._last_received = None
	

	def set_enabled(self, name, enabled):
		try:
			self._targets[name]['Enabled'] = enabled > 0
			if enabled and not self._last_received is None:
				target = self._targets[name]
				value_list = [i for i in target['Arguments']] + [j for j in self._last_received]
				try:
					getattr(target['Target'], method)(*value_list)
				except:
					pass
		except:
			pass
	

	def is_enabled(self, name):
		try:
			return self._targets[name]['Enabled']
		except:
			return False
	

	def target(self, name):
		try:
			return self._targets[name]['Target']
		except:
			return None
	

	def add_target(self, name, target, *args, **k):
		self._targets[name] = {'Target':target, 'Arguments':args, 'Enabled':True}
	

	def receive(self, method, *values):
		#debug(str(self._name) + ' receive: ' + str(method) + ' ' + str(values))
		for entry in self._targets.keys():
			target = self._targets[entry]
			if target['Enabled'] == True:
				value_list = [i for i in target['Arguments']] + [j for j in values]
				try:
					getattr(target['Target'], method)(*value_list)
				except:
					pass
		self._last_received = values
	


class StoredElement(object):


	def __init__(self, active_handlers = return_empty, *a, **attributes):
		self._active_handlers = active_handlers
		self._value = 0
		for name, attribute in attributes.iteritems():
			setattr(self, name, attribute)
	

	def value(self, value):
		self._value = value
		self.update_element()
	

	def update_element(self):
		for handler in self._active_handlers():
			handler.receive_address(self._name, value = self._value)
	

	def restore(self):
		self.update_element()
	


class Grid(object):


	def __init__(self, name, width, height, active_handlers = return_empty, *a, **k):
		self._active_handlers = active_handlers
		self._name = name
		self._width = width
		self._height = height
		self._cell = [[StoredElement(active_handlers, _name = self._name + '_' + str(x) + '_' + str(y), _x = x, _y = y , *a, **k) for y in range(height)] for x in range(width)]
	

	def restore(self):
		for column in self._cell:
			for element in column:
				self.update_element(element)
	

	def update_element(self, element):
		for handler in self._active_handlers():
			handler.receive_address(self._name, element._x, element._y, value = element._value)
	

	def value(self, x, y, value, *a):
		element = self._cell[x][y]
		element._value = value
		self.update_element(element)
	

	def row(self, row, value, *a):
		for column in range(len(self._cell)):
			self.value(column, row, value)
	

	def column(self, column, value, *a):
		for row in range(len(self._cell[column])):
			self.value(column, row, value)
	

	def clear(self, value, *a):
		self.all(0)
	

	def all(self, value, *a):
		for column in range(len(self._cell)):
			for row in range(len(self._cell[column])):
				self.value(column, row, value)
	

	def batch_row(self, row, *values):
		width = len(self._cell)
		for index in range(len(values)):
			self.value(index%width, row + int(index/width), values[index])
	

	def batch_column(self, column, *values):
		for row in range(len(self._cell[column])):
			if values[row]:
				self.value(column, row, values[row])
	

	def batch_all(self, *values):
		for column in range(len(self._cell)):
			for row in range(len(self._cell[column])):
				if values[column + (row*self._width)]:
					self.value(column, row, values[column + (row*len(self._cell))])
	

	def mask(self, x, y, value, *a):
		element = self._cell[x][y]
		if value > -1:
			for handler in self._active_handlers():
				handler.receive_address(self._name, element._x, element._y, value = value)
		else:
			self.update_element(element)
	

	def mask_row(self, row, value, *a):
		for column in range(len(self._cell[row])):
			self.mask(column, row, value)
	

	def mask_column(self, column, value, *a):
		for row in range(len(self._cell)):
			self.mask(column, row, value)
	

	def mask_all(self, value, *a):
		for column in range(len(self._cell)):
			for row in range(len(self._cell[column])):
				self.mask(column, row, value)
	

	def batch_mask_row(self, row, *values):
		width = len(self._cell)
		for index in range(len(values)):
			self.mask(index%width, row + int(index/width), values[index])
	

	def batch_mask_column(self, column, *values):
		for row in range(len(self._cell[column])):
			if values[row]:
				self.mask(column, row, values[row])
	

	def batch_mask_all(self, *values):
		for column in range(len(self._cell)):
			for row in range(len(self._cell[column])):
				if values[column + (row*len(self._cell))]:
					self.mask(column, row, values[column + (row*self._width)])
	

	def batch_row_fold(self, row, end, *values):
		width = min(len(self._cell), end)
		for index in range(len(values)):
			self.value(index%width, row + int(index/width), values[index])
	

	def batch_column_fold(self, column, end, *values):
		height = min(len(self._cell[0] if hasattr(self._cell, len) else 0, end))
		for index in range(len(values)):
			self.value(column + int(index/height), index%height, values[index])
	

	def map(self, x_offset, y_offset, *values):
		if len(values) is 8:
			if x_offset % 8 is 0 and y_offset % 8 is 0:
				for row in range(8):
					for column in range(8):
						self.value(x_offset+column, y_offset+row, (values[row]>>column)&1)
	

	def monome_row(self, x_offset, y, value = 0, *a):
		if x_offset % 8 is 0:
			for column in range(8):
				self.value(x_offset+column, y, (value>>column)&1)
	

	def monome_col(self, y_offset, x, value = 0, *a):
		if y_offset % 8 is 0:
			for row in range(8):
				self.value(x, y_offset+row, (value>>row)&1)
	

	def mask_next_empty_x(self, x, y, value, *a):
		debug('mask_next_empty_x', x, y, value)
		for handler in self._active_handlers():
			x_off = handler.x_offset
			y_off = handler.y_offset
			next_empty_x = None
			for column in range(x_off, x_off+8):
				debug('column:', column, 'sum:', sum([self._cell[column][y_off+row]._value for row in range(8)]))
				if not sum([self._cell[column][y_off+row]._value for row in range(8)]):
					next_empty_x = column
					break
			if next_empty_x:
				if value:
					debug('sending:', self._name, next_empty_x + x + x_off, y + y_off, value)
					handler.receive_address(self._name, next_empty_x + x + x_off, y + y_off, value = value)
				else:
					element = self._cell[next_empty_x + x + x_off][y + y_off]
					handler.receive_address(self._name, element._x, element._y, value = element._value)
	

	def mask_next_empty_y(self, x, y, value, *a):
		for handler in self._active_handlers():
			x_off = handler.x_offset
			y_off = handler.y_offset
			next_empty_y = None
			for row in range(y_off, y_off+8):
				if not sum([self._cell[x_off+column][y_off+row]._value for column in range(8)]):
					next_empty_y = row
					break
			if next_empty_y:
				if value:
					handler.receive_address(self._name, x + x_off, next_empty_y + y + y_off, value = value)
				else:
					element = self._cell[x + x_off][next_empty_y + y + y_off]
					handler.receive_address(self._name, element._x, element._y, value = element._value)
	


class ButtonGrid(Grid):


	def __init__(self, name, width, height, active_handlers = return_empty, *a, **k):
		self._active_handlers = active_handlers
		self._name = name
		self._cell = [[StoredElement(active_handlers, _name = self._name + '_' + str(x) + '_' + str(y), _x = x, _y = y, _identifier = -1, _channel = -1 ) for y in range(height)] for x in range(width)]
	

	def identifier(self, x, y, identifier = -1, *a):
		element = self._cell[x][y]
		element._identifier = min(127, max(-1, identifier))
		self.update_element(element)
	

	def channel(self, x, y, channel = -1, *a):
		element = self._cell[x][y]
		element._channel = min(15, max(-1, channel))
		self.update_element(element)
	

	def update_element(self, element):
		for handler in self._active_handlers():
			handler.receive_address(self._name, element._x, element._y, value = element._value, identifier = element._identifier, channel = element._channel)
	


class Array(object):


	def __init__(self, name, size, active_handlers = return_empty, *a, **k):
		self._active_handlers = active_handlers
		self._name = name
		self._cell = [StoredElement(self._name + '_' + str(num), _num = num, *a, **k) for num in range(size)]
	

	def restore(self):
		for element in self._cell:
			self.update_element(element)
	

	def update_element(self, element):
		for handler in self._active_handlers():
			handler.receive_address(self._name, element._num, value = element._value)
	

	def value(self, num, value):
		element = self._cell[num]
		element._value = value
		self.update_element(element)
	

	def all(self, value):
		for num in range(len(self.cell)):
			self.value(num, value)
	

	def mask(self, num, value):
		control = self.cell[num]
		if value > 0:
			for handler in self._active_handlers():
				handler.receive_address(self.name, element._num, value)
		else:
			self._update_element(element)
	

	def mask_all(self, value):
		for num in range(len(self.cell)):
			self.mask(num, value)
	


class RadioArray(Array):


	def value(self, num):
		for element in self._cell:
			element._value = int(element is self._cell[num])
			self.update_element(element)
	


class RingedStoredElement(StoredElement):


	def __init__(self, active_handlers = return_empty, *a, **attributes):
		self._green = 0
		self._mode = 0
		self._custom = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		super(RingedStoredElement, self).__init__(active_handlers, *a, **attributes)
	

	def mode(self, value):
		self._mode = value
		self.update_element()
	

	def green(self, value):
		self._green = value
		self.update_element()
	

	def custom(self, *values):
		self._custom = values
		self.update_element()
	

	def update_element(self):
		for handler in self._active_handlers():
			handler.receive_address(self._name, value = self._value)
			handler.receive_address(self._name, green = self._green)
			handler.receive_address(self._name, mode = self._mode)
			handler.receive_address(self._name, custom = self._custom)	
	


class RingedGrid(Grid):


	def __init__(self, name, width, height, active_handlers = return_empty, *a, **k):
		self._active_handlers = active_handlers
		self._name = name
		self._width = width
		self._height = height
		self._relative = False
		self._local = True
		self._cell = [[RingedStoredElement(active_handlers, _name = self._name + '_' + str(x) + '_' + str(y), _x = x, _y = y , *a, **k) for y in range(height)] for x in range(width)]
	

	def green(self, x, y, value):
		element = self._cell[x][y]
		element._green = value
		self.update_element(element)
	

	def led(self, x, y, value):
		element = self._cell[x][y]
		element._led = value
		self.update_element(element)
	

	def mode(self, x, y, value):
		element = self._cell[x][y]
		element._mode = value
		self.update_element(element)
	

	def custom(self, x, y, *values):
		element = self._cell[x][y]
		element._custom = values
		self.update_element(element)
	

	def relative(self, value):
		#if not self._relative == value:
		self._relative = bool(value)
		self.restore()
	

	def local(self, value):
		#if not self._local == bool(value):
		#debug(self._name, 'internal receive local', value)
		self._local = bool(value)
		self.restore()
	

	def restore(self):
		for handler in self._active_handlers():
			#handler.receive_address(str(self._name+'_relative'), self._relative)
			#handler.receive_address(str(self._name+'_local'), self._local)
			handler.receive_address(self._name, 0, 0, relative = self._relative)
			handler.receive_address(self._name, 0, 0, local = self._local)
		super(RingedGrid, self).restore()
	

	def update_element(self, element):
		for handler in self._active_handlers():
			handler.receive_address(self._name, element._x, element._y, value = element._value, green = element._green, mode = element._mode, custom = element._custom)
	


class ModHandler(CompoundComponent):


	_name = 'DefaultModHandler'

	@depends(device_provider = None)
	def __init__(self, script, addresses = None, device_selector = None, device_provider = None, *a, **k):
		super(ModHandler, self).__init__(*a, **k)
		self._script = script
		self._device_selector = device_selector or DeviceSelectorComponent(script)
		self._device_provider = device_provider
		self._color_type = 'RGB'
		self.modrouter = script.monomodular
		self._active_mod = None
		self._colors = range(128)
		self._is_enabled = False
		self._is_connected = False
		self._is_locked = False
		self._is_alted = False
		self._is_shifted = False
		self._is_shiftlocked = False
		self._receive_methods = {}
		self._addresses =  {'grid': {'obj':ButtonGrid('grid', 16, 16), 'method':self._receive_grid},
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
		self._initialize_receive_methods()
		self.modrouter.register_handler(self)
		self._on_device_changed.subject = self._device_provider
		self.modrouter._task_group.add(sequence(delay(5), self.select_appointed_device))
	

	def disconnect(self, *a, **k):
		self._active_mod = None
		super(ModHandler, self).disconnect(*a, **k)
	

	def _initialize_receive_methods(self):
		addresses = self._addresses
		for address, Dict in addresses.iteritems():
			if not address in self._receive_methods.keys():
				self._receive_methods[address] = Dict['method']
	

	def _register_addresses(self, client):
		addresses = self._addresses
		for address, Dict in addresses.iteritems():
			if not address in client._addresses.keys():
				client._addresses[address] = copy.deepcopy(Dict['obj'])
				client._addresses[address]._active_handlers = client.active_handlers
	

	def receive_address(self, address_name, *a, **k):
		#debug('receive_address ' + str(address_name) + str(a))
		if address_name in self._receive_methods.keys():
			self._receive_methods[address_name](*a, **k)
	

	def update(self, *a, **k):
		if self._active_mod:
			self._active_mod.restore()
		self.update_buttons()
	

	def select_mod(self, mod = None):
		self._active_mod = mod
		self._colors = range(128)
		debug('select_mod(), new mod is:--------------------------------', mod)
		for mod in self.modrouter._mods:
			if self in mod._active_handlers:
				mod._active_handlers.remove(self)
				mod.report_active_handlers()
		if not self._active_mod is None:
			self._active_mod._active_handlers.append(self)
			if self._color_type in self._active_mod._color_maps.keys():
				self._colors = self._active_mod._color_maps[self._color_type]
			self._active_mod.report_active_handlers()
			self._active_mod.restore()
		self.update()
	

	def active_mod(self, *a, **k):
		return self._active_mod
	

	@listens('device')
	def _on_device_changed(self):
		#debug('modhandler on_device_changed')
		if not self.is_locked() or self.active_mod() is None:
			debug('ModHandler _on_device_changed()')
			self.select_appointed_device()
	

	def on_selected_track_changed(self):
		#debug('modhandler on_selected_track_changed()')
		if not self.is_locked() or self.active_mod() is None:
			self.select_appointed_device()
	

	def select_appointed_device(self, *a):
		debug('select_appointed_device' + str(a))
		self.select_mod(self.modrouter.is_mod(self._device_provider.device))
	

	def update_buttons(self):
		self._shift_value.subject and self._shift_value.subject.send_value(7 + self.is_shifted()*7)
		self._on_shiftlock_value.subject and self._on_shiftlock_value.subject.send_value(3 + self.is_shiftlocked()*7)
		self._on_lock_value.subject and self._on_lock_value.subject.send_value(1 + self.is_locked()*7)
		self._alt_value.subject and self._alt_value.subject.send_value(2 + self.is_alted()*7)
	

	def set_mod_nav_buttons(self, buttons):
		self._mod_nav_buttons = buttons
		self._on_mod_nav_button_value.replace_subjects(buttons)
		self._update_mod_nav_buttons()
	

	@listens_group('value')
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
			device = new_mod.linked_device
			#debug('device: ' + str(device))
			if isinstance(device, Live.Device.Device):
				self.song.view.select_device(device)
				#debug('selected: ' + str(device))
				self.select_mod(new_mod)
	

	def nav_mod_up(self):
		new_mod = self.modrouter.get_next_mod(self.active_mod())
		debug('new_mod: ' + str(new_mod))
		if isinstance(new_mod, ModClient):
			device = new_mod.linked_device
			if isinstance(device, Live.Device.Device):
				self.song.view.select_device(device)
				self.select_mod(new_mod)
	

	def show_mod_in_live(self):
		if isinstance(self.active_mod(), Live.Device.Device):
			self.song.view.select_device(self.active_mod().linked_device)
	

	def set_grid(self, grid):
		#debug('set grid:' + str(grid))
		self._grid = grid
		self._grid_value.subject = grid
		if not self._grid is None:
			for button, _ in grid.iterbuttons():
				if not button == None:
					button.use_default_message()
					button.set_enabled(True)
		self.update()
	

	def _receive_grid(self, *a, **k):
		debug('receive grid:  this should be overridden')
	

	@listens('value')
	def _grid_value(self, value, x, y, *a, **k):
		#debug('_grid_value ' + str(x) + str(y) + str(value))
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
	

	@listens('value')
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
	

	@listens('value')
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
	

	@listens('value')
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
	

	@listens('value')
	def _alt_value(self, value, *a, **k):
		self._is_alted = not value is 0
		mod = self.active_mod()
		if mod:
			mod.send('alt', value)
			mod._device_proxy._alted = bool(value)
			mod._device_proxy.update_parameters()
			#mod._param_component._is_alted = bool(value)
			#mod._param_component.update()
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
	

	@listens('value')
	def _on_lock_value(self, value):
		if value>0:
			self.set_lock(not self.is_locked())
		self.update()
	


	def set_shiftlock_button(self, button):
		self._on_shiftlock_value.subject = button
	

	def is_shiftlocked(self):
		return self._is_shiftlocked
	

	@listens('value')
	def _on_shiftlock_value(self, value):
		#debug('shiftlock value ' + str(value))
		if value>0:
			self._is_shiftlocked = not self.is_shiftlocked()
			self.update()
	


	def set_offset(self, x, y):
		debug('setting offset:' + str(x) + str(y))
		self.x_offset = max(0, min(x, 12))
		self.y_offset = max(0, min(y, 12))
		if self._active_mod and self._active_mod.legacy:
			self._active_mod.send('offset', self.x_offset, self.y_offset)
			self.update()
	

	def _display_nav_box(self):
		pass
	

	def set_device_selector_matrix(self, matrix):
		self._device_selector and self._device_selector.set_matrix(matrix)
	

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
		super(ModHandler, self).on_enabled_changed()
		#if not self.is_enabled():
		#	self._instrument and self._instrument.set_enabled(False)
	


class NavigationBox(Component):


	def __init__(self, parent, width, height, window_x, window_y, callback = None, *a, **k):
		super(NavigationBox, self).__init__(*a, **k)
		self._parent = parent
		self._width = width
		self._height = height
		self._window_x = window_x
		self._window_y = window_y
		self._callback = callback
		self._scroll_up_ticks_delay = -1
		self._scroll_down_ticks_delay = -1
		self._scroll_right_ticks_delay = -1
		self._scroll_left_ticks_delay = -1
		self._x_inc = 0
		self._y_inc = 0
		self.on_value = 5
		self.off_value = 1
		self.x_offset = 0
		self.y_offset = 0
		#debug('timer is callable:', callable(self._on_timer))
		self._task_group = TaskGroup(auto_kill=False)
		self._task_group.add(totask(self._on_timer))
		#self._register_timer_callback(self._on_timer)
	

	def width(self):
		return self._width
	

	def height(self):
		return self._height
	

	def set_matrix(self, matrix):
		#if matrix:
		#	for button, _ in matrix.iterbuttons():
		#		button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
		self._on_navigation_value.subject = matrix
		if not matrix is None:
			self._x_inc = int(self.width()/matrix.width())
			self._y_inc = int(self.height()/matrix.height())
		else:
			self._x_inc = 0
			self._y_inc = 0
		#debug('incs: ' + str(self._x_inc) + ' ' + str(self._y_inc))
		self.update()
	

	def set_nav_buttons(self, buttons):
		assert buttons is None or len(buttons)==4
		if buttons is None:
			buttons = [None for index in range(4)]
		self.set_nav_up_button(buttons[0])
		self.set_nav_down_button(buttons[1])
		self.set_nav_left_button(buttons[2])
		self.set_nav_right_button(buttons[3])
	

	def set_nav_up_button(self, button):
		#button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
		self._on_nav_up_value.subject = button
	

	def set_nav_down_button(self, button):
		#button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
		self._on_nav_down_value.subject = button
	

	def set_nav_left_button(self, button):
		#button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
		self._on_nav_left_value.subject = button
	

	def set_nav_right_button(self, button):
		#button and button.set_on_off_values('Mod.Nav.OnValue', 'Mod.Nav.OffValue')
		self._on_nav_right_value.subject = button
	

	@listens('value')
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
	

	@listens('value')
	def _on_nav_up_value(self, value):
		if value:
			self._scroll_up_ticks_delay = INITIAL_SCROLLING_DELAY
			if (not self._is_scrolling()):
				self.set_offset(self.x_offset, self.y_offset - 1)
				#self.update()
		else:
			self._scroll_up_ticks_delay = -1
	

	@listens('value')
	def _on_nav_down_value(self, value):
		if value:
			self._scroll_down_ticks_delay = INITIAL_SCROLLING_DELAY
			if (not self._is_scrolling()):
				self.set_offset(self.x_offset, self.y_offset + 1)
				#self.update()
		else:
			self._scroll_down_ticks_delay = -1
	

	@listens('value')
	def _on_nav_left_value(self, value):
		if value:
			self._scroll_left_ticks_delay = INITIAL_SCROLLING_DELAY
			if (not self._is_scrolling()):
				self.set_offset(self.x_offset - 1, self.y_offset)
				#self.update()
		else:
			self._scroll_left_ticks_delay = -1
	

	@listens('value')
	def _on_nav_right_value(self, value):
		if value:
			self._scroll_right_ticks_delay = INITIAL_SCROLLING_DELAY
			if (not self._is_scrolling()):
				self.set_offset(self.x_offset + 1, self.y_offset)
				#self.update()
		else:
			self._scroll_right_ticks_delay = -1
	

	def update(self):
		nav_grid = self._on_navigation_value.subject
		left_button = self._on_nav_left_value.subject
		right_button = self._on_nav_right_value.subject
		up_button = self._on_nav_up_value.subject
		down_button = self._on_nav_down_value.subject
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
				button and button.set_light('Mod.Nav.OnValue' if ((x*xinc) in range(xoff, xmax)) and ((y*yinc) in range(yoff, ymax)) else 'Mod.Nav.OffValue')
		left_button and left_button.set_light('Mod.Nav.OnValue' if xoff>0 else 'Mod.Nav.OffValue')
		right_button and right_button.set_light(xoff<(self.width()-self._window_x))
		up_button and up_button.set_light('Mod.Nav.OnValue' if yoff>0 else 'Mod.Nav.OffValue')
		down_button and down_button.set_light(yoff<(self.height()-self._window_y))
	

	def set_offset(self, x, y):
		self.x_offset = min(x, self.width() - self._window_x)
		self.y_offset = min(y, self.height() - self._window_y)
		self.update()
		if self._callback:
			self._callback(x, y)
	

	def _is_scrolling(self):
		return (0 in (self._scroll_up_ticks_delay, self._scroll_down_ticks_delay, self._scroll_right_ticks_delay, self._scroll_left_ticks_delay))
	

	def _on_timer(self):
		if self.is_enabled():
			scroll_delays = [self._scroll_up_ticks_delay,
							 self._scroll_down_ticks_delay,
							 self._scroll_right_ticks_delay,
							 self._scroll_left_ticks_delay]
			if (scroll_delays.count(-1) < 4):
				x_increment = 0
				y_increment = 0
				if (self._scroll_right_ticks_delay > -1):
					if self._is_scrolling():
						x_increment += 1
						self._scroll_right_ticks_delay = INTERVAL_SCROLLING_DELAY
					self._scroll_right_ticks_delay -= 1
				if (self._scroll_left_ticks_delay > -1):
					if self._is_scrolling():
						x_increment -= 1
						self._scroll_left_ticks_delay = INTERVAL_SCROLLING_DELAY
					self._scroll_left_ticks_delay -= 1
				if (self._scroll_down_ticks_delay > -1):
					if self._is_scrolling():
						y_increment += 1
						self._scroll_down_ticks_delay = INTERVAL_SCROLLING_DELAY
					self._scroll_down_ticks_delay -= 1
				if (self._scroll_up_ticks_delay > -1):
					if self._is_scrolling():
						y_increment -= 1
						self._scroll_up_ticks_delay = INTERVAL_SCROLLING_DELAY
					self._scroll_up_ticks_delay -= 1
				new_x_offset = max(0, (self.x_offset + x_increment))
				new_y_offset = max(0, (self.y_offset + y_increment))
				if ((new_x_offset != self.x_offset) or (new_y_offset != self.y_offset)):
					self.set_offset(new_x_offset, new_y_offset)
					self.update()
	


class ParamHolder(ControlManager, EventObject):
	
	__doc__ = ' Simple class to hold the owner of a Device.parameter and forward its value when receiving updates from Live, or update its value from a mod '


	_parameter = None
	_feedback = True
	_report = True

	def __init__(self, parent, index, control_prefix = 'Encoder'):
		self._index = index
		self._control_name = control_prefix+'_'+str(index)
		self._parent = parent
	

	def set_control_prefix(self, control_prefix):
		self._control_name = str(control_prefix)+'_'+str(self._index)
	

	@listenable_property
	def parameter(self):
		return self._parameter
	

	@parameter.setter
	def parameter(self, parameter, *a):
		#debug('parameter.setter:', parameter)
		if parameter != self._parameter:
			if not self._parameter == None and self._parameter.value_has_listener(self._value_change):
				self._parameter.remove_value_listener(self._value_change)
			self._parameter = parameter
			if not self._parameter == None:
				self._parameter.add_value_listener(self._value_change)
			self._value_change()

		#self._value_change.subject = parameter
		#self.notify_parameter()
	

	#@listens('value')
	def _value_change(self, *a):
		control_name = self._control_name
		self._parent._params_value_change(self._parameter, control_name, self._feedback)
		self._feedback = self._report
	

	def _change_value(self, value):
		if(self._parameter != None):
			if(self._parameter.is_enabled):
				self._feedback = False
				newval = float(float(float(value)/127) * float(self._parameter.max - self._parameter.min)) + self._parameter.min
				#debug('newval:', newval)
				self._parameter.value = newval
	


class NoDevice(object):
	__doc__ = 'Dummy Device with no parameters and custom class_name that is used when no device is selected, but parameter assignment is still necessary'	


	def __init__(self):
		self.class_name = 'NoDevice'
		self.parameters = []
		self.canonical_parent = None
		self.can_have_chains = False
		self.name = 'NoDevice'
	

	def add_name_listener(self, callback=None):
		pass
	

	def remove_name_listener(self, callback=None):
		pass
	

	def name_has_listener(self, callback=None):
		return False
	

	def add_parameters_listener(self, callback=None):
		pass
	

	def remove_parameters_listener(self, callback=None):
		pass
	

	def parameters_has_listener(self, callback=None):
		return False
	

	def store_chosen_bank(self, callback=None):
		pass
	


class ModParameterProxy(ControlManager, EventObject):


	_name = 'ModParameterProxy'
	_value = 0

	def __init__(self, parameter = None, *a, **k):
		super(ModParameterProxy, self).__init__(*a, **k)
	



class ModDeviceProxy(ControlManager, EventObject):


	class_name = 'ModDeviceProxy'
	_name = 'ModDeviceProxy'
	_parameters = []
	_alted = False

	def __init__(self, parent = None, mod_device = None, *a, **k):
		self._parent = parent
		self._mod_device = mod_device
		self._bank_dict = {}
		super(ModDeviceProxy, self).__init__(*a, **k)
		self.fill_parameters_from_device(mod_device)
	

	def fill_parameters_from_device(self, device):
		self._parameters = []
		if device:
			#self._parameters = [ModParameterProxy(parameter = parameter) for parameter in device.parameters]
			self._parameters = [parameter for parameter in device.parameters]
	

	def set_bank_dict_entry(self, bank_type, bank_num, *a):
		debug('set bank dict_entry for proxy:', self._name, 'type:', bank_type, 'num:', bank_num, 'contents:', *a)
		if not bank_type in self._bank_dict.keys():
			self._bank_dict[bank_type] = []
		self._bank_dict[bank_type].insert(bank_num, [item for item in a])
		#debug('new banks:', self._bank_dict)
	

	def update_parameters(self):
		self.notify_parameters()
	

	@property
	def bank_dict(self):
		return self._bank_dict
	

	@listenable_property
	def parameters(self):
		debug('notifying parameters:', self._parameters if not self._alted else [self._parameters[0]] + self._parameters[8:])
		return self._parameters if (not self._alted or len(self._parameters) < 9) else [self._parameters[0]] + self._parameters[9:]
	

	def current_parameters(self):
		return self._parameters
	

	@parameters.setter
	def parameters(self, parameters):
		self._parameters = parameters
		debug('parameters are now:', [parameter.name if hasattr(parameter, 'name') else None for parameter in self._parameters])
		self.notify_parameters()
	

	@listenable_property
	def name(self):
		return self._name
	

	def store_chosen_bank(self, callback=None):
		pass
	

	@property
	def canonical_parent(self):
		return self._mod_device.canonical_parent
	

	@property
	def can_have_chains(self):
		return self._mod_device.can_have_chains
	

	def test_dict(self):
		for bank_type in self._bank_dict.keys():
			debug('bank_type:', bank_type)
			for bank_num in range(len(self._bank_dict[bank_type])):
				debug('bank_num:', bank_num, self._bank_dict[bank_type][bank_num])
	


class LegacyModDeviceProxy(ModDeviceProxy):


	class_name = 'LegacyModDeviceProxy'
	_name = 'LegacyModDeviceProxy'
	_device_parent = None
	_chain = 0
	_device_chain = 0
	_params = []
	_bank_index = 0
	_assigned_device = None
	_nodevice = NoDevice()
	_custom_parameter = []
	_control_prefix = 'Encoder'

	def __init__(self, *a, **k):
		super(LegacyModDeviceProxy, self).__init__(*a, **k)
		self._params = [ParamHolder(self, index, self._control_prefix) for index in range(16)] 
	

	def fill_parameters_from_device(self, *a):
		self.set_mod_device(self._mod_device)
	

	def _set_device_parent(self, mod_device_parent, single = None):
		#debug('_set_device_parent', mod_device_parent, single)
		self._parent_device_changed.subject = None
		if isinstance(mod_device_parent, Live.Device.Device):
			if mod_device_parent.can_have_chains and single is None:
				self._device_parent = mod_device_parent
				if self._device_parent.canonical_parent != None:
					self._parent_device_changed.subject = self._device_parent.canonical_parent
				self._select_parent_chain(self._device_chain)
			else:
				self._device_parent = mod_device_parent
				self._assign_parameters(self._device_parent, True)
		elif 'NoDevice' in self._bank_dict.keys():
			#debug('_set_device_parent is NoDevice')
			self._device_parent = self._nodevice
			self._device_chain = 0
			self._assign_parameters(None, True)
		else:
			#debug('_set_device_parent is None')
			self._device_parent = None
			self._device_chain = 0
			self._assign_parameters(None, True)
	

	def _select_parent_chain(self, chain, force = False): 
		#debug('_select_parent_chain ', str(chain))
		self._device_chain = chain 
		if self._device_parent != None:
			if isinstance(self._device_parent, Live.Device.Device):
				if self._device_parent.can_have_chains:
					if len(self._device_parent.chains) > chain:
						if len(self._device_parent.chains[chain].devices) > 0:
							self._assign_parameters(self._device_parent.chains[chain].devices[0], force)
					elif 'NoDevice' in self._bank_dict.keys():
						self._assign_parameters(self._nodevice, True)
					else:
						self._assign_parameters(None)
	

	def _select_drum_pad(self, pad, force = False):
		#debug('_select_drum_pad', pad, force, 'parent:', self._device_parent)
		if self._device_parent != None:
			if isinstance(self._device_parent, Live.Device.Device):
				#debug('is device')
				if self._device_parent.can_have_drum_pads and self._device_parent.has_drum_pads:
					#debug('can and has drum_pads')
					pad = self._device_parent.drum_pads[pad]
					#debug('pad is: ', str(pad))
					if pad.chains and pad.chains[0] and pad.chains[0].devices and isinstance(pad.chains[0].devices[0], Live.Device.Device):
						self._assign_parameters(pad.chains[0].devices[0], force)
					elif 'NoDevice' in self._bank_dict.keys():
						self._assign_parameters(self._nodevice, True)
					else:
						self._assign_parameters(None)
	

	@listens('devices')
	def _parent_device_changed(self):
		debug('parent_device_changed')
		self._set_device_parent(None)
		self._parent.send('lcd', 'parent', 'check')
	

	@listens('devices')
	def _device_changed(self):
		debug('device_changed')
		self._assign_parameters(None)
		self._parent.send('lcd', 'device', 'check')
	

	def _assign_parameters(self, device, force = False, *a):
		debug('_assign_parameters:', device, device.class_name if device and hasattr(device, 'class_name') else 'no name')
		self._assigned_device = device
		new_parameters = [self._mod_device.parameters[0]]
		for param in self._params:
			param.parameter = None
		if device is None:
			class_name = 'NoDevice'
		elif (device and device.class_name in self._bank_dict.keys()):
			class_name = device.class_name
		else:
			class_name = 'Other'
		debug('class name is:', class_name, 'keys:', self._bank_dict.keys());
		if (class_name in self._bank_dict.keys()):
			debug('class name in keys...')
			bank_index = clamp(self._bank_index, 0, len(self._bank_dict[class_name]))
			#debug('bank index is:', bank_index)
			bank = [name for name in self._bank_dict[class_name][bank_index]]
			#debug('bank is:', bank)
			for parameter_name in bank:
			 	new_parameters.append(self.get_parameter_by_name(device, parameter_name))
		elif device is self._mod_device:
			new_parameters = [parameter for parameter in self._mod_device.parameters]
		for param, parameter in izip(self._params, new_parameters[1:]):
			param.parameter = parameter
		self.parameters = new_parameters
		self._parent.send('lcd', 'device_name', 'lcd_name', generate_strip_string(str(device.name)) if hasattr(device, 'name') else ' ')
		debug('params are now:', [param.parameter.name if hasattr(param.parameter, 'name') else None for param in self._params])
	

	def get_parameter_by_name(self, device, name):
		debug('get parameter: device-', device, 'name-', name)
		result = None
		if device:
			for i in device.parameters:
				if (i.original_name == name):
					result = i
					break
			if result == None:
				if name == 'Mod_Chain_Pan':
					if device.canonical_parent.mixer_device != None:
						if device.canonical_parent.mixer_device.panning != None:
							result = device.canonical_parent.mixer_device.panning
				elif name == 'Mod_Chain_Vol':
					if device.canonical_parent.mixer_device !=None:
						if device.canonical_parent.mixer_device.panning != None:
							result = device.canonical_parent.mixer_device.volume
				elif(match('Mod_Chain_Send_', name)):
					#debug('match Mod_Chain_Send_')
					send_index = int(name.replace('Mod_Chain_Send_', ''))
					if device.canonical_parent != None:
						if device.canonical_parent.mixer_device != None:
							if device.canonical_parent.mixer_device.sends != None:
								if len(device.canonical_parent.mixer_device.sends)>send_index:
									result = device.canonical_parent.mixer_device.sends[send_index]
		if result == None:
			#debug('checking for ModDevice...')
			if match('ModDevice_', name) and self._mod_device != None:
				name = name.replace('ModDevice_', '')
				debug('modDevice with name:', name)
				for i in self._mod_device.parameters:
					if (i.name == name):
						result = i
						break
			elif match('CustomParameter_', name):
				index = int(name.replace('CustomParameter_', ''))
				if len(self._custom_parameter)>index:
					if isinstance(self._custom_parameter[index], Live.DeviceParameter.DeviceParameter):
						result = self._custom_parameter[index]
		return result
	

	def rebuild_parameters(self):
		self._assign_parameters(device = self._assigned_device, force = True)
	

	def set_params_report_change(self, value):
		for param in self._params:
			param._report = bool(value)
	

	def set_params_control_prefix(self, prefix):
		self._control_prefix = prefix
		for param in self._params:
			param.set_control_prefix(prefix)
	

	def set_number_params(self, number, *a):
		debug('set number params', number)
		for param in self._params:
			param.parameter = None
		self._params = [ParamHolder(self, index) for index in range(number)]
		#self._assign_parameters(self._assigned_device)
	

	def set_mod_device_type(self, mod_device_type, *a):
		debug('set type ' + str(mod_device_type))
	

	def set_mod_device(self, mod_device, *a):
		debug('set_mod_device:', mod_device)
		self._assign_parameters(mod_device)
	

	def set_mod_device_parent(self, mod_device_parent, single=None, *a):
		debug('set_mod_device_parent:', mod_device_parent, single)
		self._set_device_parent(mod_device_parent, single)
	

	def set_mod_device_chain(self, chain, *a):
		debug('set_mod_device_chain:', chain)
		self._select_parent_chain(chain, True)
	

	def set_mod_drum_pad(self, pad, *a):
		debug('set_mod_drum_pad:', pad)
		self._select_drum_pad(pad, True)
	

	def set_mod_device_bank(self, bank_index, *a):
		debug('set_mod_device_bank:', bank_index)
		if bank_index != self._bank_index:
			self._bank_index = bank_index
			self.rebuild_parameters()
	

	def set_mod_parameter_value(self, num, val, *a):
		num < len(self._params) and self._params[num]._change_value(val)
	

	def _params_value_change(self, sender, control_name, feedback = True):
		#debug('params change', sender, control_name)
		pn = ' '
		pv = ' '
		val = 0
		if(sender != None):
			pn = str(generate_strip_string(str(sender.name)))
			if sender.is_enabled:
				try: 
					value = str(sender)
				except:
					value = ' '
				pv = str(generate_strip_string(value))
			else:
				pv = '-bound-'
			val = ((sender.value - sender.min) / (sender.max - sender.min))  * 127
		self._parent.send('lcd', control_name, 'lcd_name', pn)
		self._parent.send('lcd', control_name, 'lcd_value', pv)
		if feedback == True:
			self._parent.send('lcd', control_name, 'encoder_value', val)
	

	def set_number_custom(self, number, *a):
		self._custom_parameter = [None for index in range(number)]
	

	def set_custom_parameter(self, number, parameter, rebuild = True, *a):
		if number < len(self._custom_parameter):
			debug('custom=', parameter)
			if isinstance(parameter, Live.DeviceParameter.DeviceParameter) or parameter is None:
				debug('custom is device:', parameter)
				self._custom_parameter[number] = parameter
				rebuild and self.rebuild_parameters()
	

	def set_custom_parameter_value(self, num, value, *a):
		if num < len(self._custom_parameter):
			parameter = self._custom_parameter[num]
			if parameter != None:
				newval = float(float(float(value)/127) * float(parameter.max - parameter.min)) + parameter.min
				parameter.value = newval
	


class ModClient(NotifyingControlElement):


	__subject_events__ = (Event(name='value', signal=InputSignal, override=True),)
	_input_signal_listener_count = 0

	def __init__(self, parent, device, name, *a, **k):
		super(ModClient, self).__init__(*a, **k)
		self.name = name
		self._device = device
		self._device_parent = device.canonical_parent
		self._parent = parent
		self._active_handlers = []
		self._addresses = {}
		self._translations = {}
		self._translation_groups = {}
		self._color_maps = {}
		self.legacy = False
		self._device_proxy = LegacyModDeviceProxy(parent = self, mod_device = device)
		self._proxied_devices = [self._device_proxy]
		self.register_addresses()
		if self._device_parent.devices_has_listener(self._device_listener):
			self._device_parent.remove_devices_listener(self._device_listener)
		self._device_parent.add_devices_listener(self._device_listener)
	

	@property
	def proxied_devices(self):
		return self._proxied_devices
	

	@property
	def device(self):
		return self._device
	

	def register_addresses(self):
		for handler in self._parent._handlers:
			handler._register_addresses(self)
			self.send('register_handler', handler.name)
	

	def addresses(self):
		return self._addresses
	

	def translations(self):
		return self._translations
	

	def active_handlers(self):
		return self._active_handlers
	

	def report_active_handlers(self):
		args = ['active_handlers'] + [handler._name for handler in self.active_handlers()]
		self.send(*args)
	

	def receive(self, address_name, method = 'value', values = 0, *a, **k):
		if address_name in self._addresses.keys():
			address = self._addresses[address_name]
			value_list = unpack_items(values)
			#debug('address: ' + str(address) + ' value_list: ' + str(value_list))
			try:
				getattr(address, method)(*value_list)
			except:
				debug('receive method exception', address_name, method, values)
	

	def Receive(self, address_name, method = 'value', *value_list):
		if address_name in self._addresses.keys():
			address = self._addresses[address_name]
			#debug('address: ' + str(address) + ' value_list: ' + str(value_list))
			try:
				getattr(address, method)(*value_list)
			except:
				debug('Receive method exception', address_name, method, value_list)
	

	def distribute(self, function_name, values = 0, *a, **k):
		if hasattr(self, function_name):
			value_list = unpack_items(values)
			#debug('distribute: ' + str(function_name) + ' ' + str(values) + ' ' + str(value_list))
			try:
				getattr(self, function_name)(*value_list)
			except:
				debug('distribute method exception', function_name, value_list)
	

	def Distribute(self, function_name, *value_list):
		if hasattr(self, function_name):
			#value_list = unpack_items(values)
			#debug('distribute: ' + str(function_name) + ' ' + str(values) + ' ' + str(value_list))
			try:
				getattr(self, function_name)(*value_list)
			except:
				debug('Distribute method exception', function_name, value_list)
	

	def receive_translation(self, translation_name, method = 'value', *values):
		#value_list = unpack_items(values)
		#debug('receive_translation: ' + str(translation_name) + ' ' + str(method) + ' ' + str(values))
		try:
			self._translations[translation_name].receive(method, *values)
		except:
			debug('receive_translation method exception', translation_name, method, values)
	

	def trans(self, translation_name, method = 'value', *values):
		#value_list = unpack_items(values)
		#debug('receive_translation: ' + str(translation_name) + 'is avail: ' + str(translation_name in self._translations.keys()) + ' ' + str(method) + ' ' + str(values))# + ' ' + str(value_list))
		try:
			self._translations[translation_name].receive(method, *values)
		except:
			debug('receive_translation method exception', translation_name, method, values)
	

	def send(self, control_name, *a):
		#with self._parent._host.component_guard():
		self.notify_value(control_name, *a)
	

	def is_active(self):
		return (len(self._active_host) > 0)
	

	def set_enabled(self, val):
		self._enabled = bool(val)
	

	def reset(self):
		pass
	

	def restore(self):
		for address_name, address in self._addresses.iteritems():
			address.restore()
		#self._param_component.update()
	

	#@listens('devices')
	def _device_listener(self, *a, **k):
		debug('devices listener....', liveobj_valid(self.device))
		liveobj_valid(self.device) or self._disconnect_client()
	

	def _disconnect_client(self, reconnect = False):
		#self._device_listener.subject = None
		self._device = None
		self.send('disconnect')
		for handler in self.active_handlers():
			handler.select_mod(None)
		self._parent.remove_mod(self)
		self.disconnect()
	

	def disconnect(self):
		self._active_handlers = []
		if self._device_parent.devices_has_listener(self._device_listener):
			self._device_parent.remove_devices_listener(self._device_listener)
		#self._device_listener.subject = None
		super(ModClient, self).disconnect()
	

	@property
	def linked_device(self):
		return self.device
	

	def script_wants_forwarding(self):
		return True
	

	def add_translation(self, name, target, group=None, *args, **k):
		#debug('name: ' + str(name) + ' target: ' + str(target) + ' args: ' + str(args))
		if target in self._addresses.keys():
			if not name in self._translations.keys():
				self._translations[name] = ElementTranslation(name, self)
			#debug('adding new target')
			self._translations[name].add_target(target, self._addresses[target], *args)
			if not group is None:
				if not group in self._translation_groups.keys():
					self._translation_groups[group] = []
				self._translation_groups[group].append([name, target])
				#debug('added to group ' + str(group) + ' : ' + str(self._translation_groups[group]))
	

	def enable_translation(self, name, target, enabled = True):
		if name in self._translations.keys():
			self._translations[name].set_enabled(target, enabled)
	

	def enable_translation_group(self, group, enabled = True):
		if group in self._translation_groups.keys():
			for pair in self._translation_groups[group]:
				#debug('enabling for ' + str(pair))
				self.enable_translation(pair[0], pair[1], enabled)
	

	def receive_device(self, command, *args):
		#debug('receive_device_proxy', 'command:', command, 'args:', args)
		#for arg in args:
		#	debug('type of:', arg, type(arg))
		try:
			getattr(self._device_proxy, command)(*args)
		except:
			debug('receive_device_proxy exception: %(c)s %(a)s' % {'c':command, 'a':args})
	

	def receive_device_proxy(self, command, *args):
		try:
			getattr(self._device_proxy, command)(*args)
		except:
			debug('receive_device_proxy exception: %(c)s %(a)s' % {'c':command, 'a':args})
	

	def receive_alt_device_proxy(self, proxy_name, command, *args):
		if hasattr(self, proxy_name):
			device_proxy = getattr(self, proxy_name)
			try:
				getattr(device_proxy, command)(*args)
			except:
				debug('receive_device_proxy exception: %(c)s %(a)s' % {'c':command, 'a':args})
	

	def create_alt_device_proxy(self, proxy_name):
		if not hasattr(self, proxy_name):
			device_proxy = LegacyModDeviceProxy(parent = self, mod_device = self.device)
			device_proxy._name = proxy_name
			setattr(self, proxy_name, device_proxy)
			self._proxied_devices.append(getattr(self, proxy_name))
		else:
			debug('proxy already exists:', proxy_name)
	

	def update_device(self):
		for handler in self.active_handlers():
			handler.update_device()
	

	def set_legacy(self, value):
		#debug('set_legacy: ' + str(value))
		self.legacy = value > 0
		for handler in self.active_handlers():
			handler.update()
	

	def select_device_from_key(self, key):
		key = str(key)
		preset = None
		for track in self._parent.song.tracks:
			for device in enumerate_track_device(track):
				if(match(key, str(device.name)) != None):
					preset = device
					break
		for return_track in self._parent.song.return_tracks:
			for device in enumerate_track_device(return_track):
				if(match(key, str(device.name)) != None):
					preset = device
					break
		for device in enumerate_track_device(self._parent.song.master_track):
			if(match(key, str(device.name)) != None):
				preset = device
				break
		if preset != None:
			self._parent.song.view.select_device(preset)
	

	def fill_color_map(self, color_type = None, *color_map):
		#debug('fill color map: ' + str(color_type) + ' ' + str(color_map))
		if not color_type is None:
			self._color_maps[color_type] = [color_map[index%(len(color_map))] for index in range(128)]
			self._color_maps[color_type][0:0] = [0]
			for handler in self.active_handlers():
				if handler._color_type is color_type:
					handler._colors = self._color_maps[color_type]
				handler.update()
	

	def set_color_map(self, color_type, *color_map):
		#debug('set color map: ' + str(color_type) + ' ' + str(color_map))
		if not color_type is None:
			for index in xrange(color_map):
				self._color_maps[color_type][index] = color_map[index]
			for handler in self.active_handlers():
				if handler._color_type is color_type:
					handler._colors = self._color_maps[color_type]
				handler.update()
	

	def get_handler_offsets(self):
		debug('get handler offsets')
		offsets = (0, 0)
		if len(self.active_handlers())==1:
			debug('theres one handler, getting offsets...')
			handler = self.active_handlers()[0]
			offsets = (handler.x_offset, handler.y_offset)
		return offsets
	

	@property
	def parameters(self):
		return self._device_proxy.parameters
	

	def Forward(self, method = None, *value_list):
		if not method is None:
			for handler in self.active_handlers():
				try:
					getattr(handler, method)(*value_list)
				except:
					debug('Forward method exception', method, value_list)
	


class ModRouter(CompoundComponent):


	def __init__(self, *a, **k):
		super(ModRouter, self).__init__(*a, **k)
		self._host = None
		self._task_group = TaskGroup(auto_kill=False)
		self._handlers = []
		self._mods = []
		self.log_message = self._log_message
		return None
	

	def set_host(self, host):
		assert isinstance(host, ControlSurface)
		self._host = host
		#self._task_group = host._task_group
		self._host.log_message('host registered: ' + str(host))
		self.log_message = host.log_message
	

	def has_host(self):
		return not self._host is None
	

	def _log_message(self, *a, **k):
		pass
	

	def register_handler(self, handler):
		if handler not in self._handlers:
			self._handlers.append(handler)
		for mod in self._mods:
			mod.register_addresses()
			mod.send('disconnect')
	

	def unregister_handler(self, cs, handler):
		debug('unregistering handler ' + str(cs) + ' ' + str(handler))
		for mod in self._mods:
			mod.send('disconnect')
		for index in range(len(self._handlers)):
			if self._handlers[index] is handler:
				self._host = None
				self._task_group = None
				debug('deleting from handlers: ' + str(self._handlers[index]))
				del self._handlers[index]
				for surface in get_control_surfaces():
					if not surface is cs:
						if hasattr(surface, 'monomodular'):
							debug('reconnecting router to ' + str(surface))
							self.set_host(surface)
							break
				self._log_message = self._log_message
				break

	

	@listenable_property
	def mods(self):
		return self._mods
	

	@mods.setter
	def mods(self, mods):
		self._mods = mods
		self.notify_mods()
	

	def update_handlers(self, *a, **k):
		self.notify_mods()
		for handler in self._handlers:
			handler._on_device_changed()
	

	@property
	def devices(self):
		return [mod.device for mod in self.mods]
	

	def get_mod(self, device):
		debug('getting mod...')
		mod_client = None
		for mod in self.mods:
			if mod.device == device:
				mod_client = mod
		return mod_client
	

	def get_next_mod(self, active_mod):
		if not active_mod is None:
			return self._mods[(self._mods.index(active_mod) +1) % len(self._mods)]
		elif not len(self._mods) is 0:
			return self._mods[0]
		else:
			return None
	

	def get_previous_mod(self, active_mod):
		if not active_mod is None:
			return self._mods[(self._mods.index(active_mod) + len(self._mods) -1) % len(self._mods)]
		elif not len(self._mods) is 0:
			return self._mods[-1]
		else:
			return active_mod
	

	def add_mod(self, device):
		mod_client = self.get_mod(device)
		debug('add_mod', device)
		#debug('devices:', self.devices)
		if mod_client is None:
			#debug('device not in self.mods')
			with self._host.component_guard():
				mod_client = ModClient(parent = self, device = device, name = 'modClient'+str(len(self.mods))) 
				self._mods.append( mod_client )
		debug('add mod device:', device.name, mod_client)
		self._host.schedule_message(1, self.update_handlers)
		return mod_client
	

	def remove_mod(self, mod):
		if mod in self._mods:
			debug('removing mod:', mod)
			self._mods.remove(mod)
	

	def timer(self, *a, **k):
		pass
	

	def update(self):
		pass
	

	def disconnect(self):
		for surface in get_control_surfaces():
			if hasattr(surface, 'monomodular'):
				debug('deleting monomodular for ' + str(surface))
				del surface.monomodular
		old_host = self._host
		self._host = None
		self._handlers = []
		if hasattr(__builtins__, 'monomodular') or 'monomodular' in __builtins__.keys():
			debug('deleting monomodular from builtins')
			del __builtins__['monomodular']
		for surface in get_control_surfaces():
			if not surface is old_host:
				if hasattr(surface, 'restart_monomodular'):
					surface.schedule_message(2, surface.restart_monomodular)
		for mod in self._mods:
			mod.disconnect()
		self._mods = []
		debug('monomodular is disconnecting....')
		super(ModRouter, self).disconnect()
	

	def is_mod(self, device):
		#debug('is mod(', device, ')')
		mod_device = None
		if isinstance(device, Live.Device.Device):
			try:
				if device.can_have_chains and not device.can_have_drum_pads and len(device.view.selected_chain.devices)>0:
					device = device.view.selected_chain.devices[0]
			except:
				pass
		#debug('pass device: ' + str(device))
		if not device is None:
			for mod in self._mods:
				#debug('mod in mods: ' + str(mod.device))
				#if mod.device == device or mod._device_proxy == device:
				if mod.device == device or device in mod.proxied_devices:
					mod_device = mod
					break
		#debug('modrouter is_mod() returned device: ' + str(mod_device))
		return mod_device
	

	def is_mod(self, device):
		debug('is mod(', device, ')')
		mod_device = None
		if isinstance(device, Live.Device.Device):
			try:
				if device.can_have_chains and not device.can_have_drum_pads and len(device.view.selected_chain.devices)>0:
					device = device.view.selected_chain.devices[0]
			except:
				pass
			debug('---------------device name is:', device.name)
			debug('---------------device startswith @modAlias:', device.name.startswith('@modAlias'))
			if device.name.startswith('@modAlias:'):
				alias_name = device.name.split('@modAlias:')[1]
				debug('---------------alias name is:', alias_name)
				for mod in self._mods:
					name = mod.device.name if mod.device else None
					debug('mod device name is:', name)
					debug('name == alias_name:', str(name) == str(alias_name))
					if str(name) == str(alias_name):
						device = mod.device
						break
		#debug('pass device: ' + str(device))
		if not device is None:
			for mod in self._mods:
				#debug('mod in mods: ' + str(mod.device))
				#if mod.device == device or mod._device_proxy == device:
				if mod.device == device or device in mod.proxied_devices:
					mod_device = mod
					break
		#debug('modrouter is_mod() returned device: ' + str(mod_device))
		return mod_device
	


def original_device_to_appoint(device):
	appointed_device = device
	if liveobj_valid(device) and device.can_have_drum_pads and not device.has_macro_mappings and len(device.chains) > 0 and liveobj_valid(device.view.selected_chain) and len(device.view.selected_chain.devices) > 0:
		appointed_device = device_to_appoint(device.view.selected_chain.devices[0])
	return appointed_device


def device_to_appoint(device):
	appointed_device = device
	#if liveobj_valid(device) and device.can_have_drum_pads and not device.has_macro_mappings and len(device.chains) > 0 and liveobj_valid(device.view.selected_chain) and len(device.view.selected_chain.devices) > 0:
	#	appointed_device = device_to_appoint(device.view.selected_chain.devices[0])
	return appointed_device


def select_and_appoint_device(song, device_to_select, ignore_unmapped_macros = True):
	appointed_device = device_to_select
	if ignore_unmapped_macros:
		appointed_device = device_to_appoint(device_to_select)
	song.view.select_device(device_to_select, False)
	song.appointed_device = appointed_device


def get_modrouter():
	modrouter = None
	if hasattr(__builtins__, 'monomodular') or 'monomodular' in __builtins__.keys():
		modrouter = __builtins__['monomodular']
	return modrouter


def livedevice(device):
	return device._mod_device if hasattr(device, '_mod_device') else device


class ModDeviceProvider(EventObject):


	device_selection_follows_track_selection = True

	def __init__(self, song = None, *a, **k):
		super(ModDeviceProvider, self).__init__(*a, **k)
		self._device = None
		self._locked_to_device = False
		self.song = song
		self.__on_appointed_device_changed.subject = song
		self.__on_selected_track_changed.subject = song.view
		self.__on_selected_device_changed.subject = song.view.selected_track.view
		#self.__on_mod_device_added.subject = get_modrouter()
	

	@listenable_property
	def device(self):
		#debug('delivering device:', self._device)
		return self._device
	

	@device.setter
	def device(self, device):
		device = self.mod_device_from_device(device)
		if liveobj_changed(self._device, device) and not self.is_locked_to_device:
			#self._device = device
			self._device = device
			#debug('setting device:', self._device)
			self.notify_device()
	

	@listenable_property
	def is_locked_to_device(self):
		return self._locked_to_device
	

	def lock_to_device(self, device):
		self.device = device
		self._locked_to_device = True
		self.notify_is_locked_to_device()
	

	def unlock_from_device(self):
		self._locked_to_device = False
		self.notify_is_locked_to_device()
		self.update_device_selection()
	

	@listens('appointed_device')
	def __on_appointed_device_changed(self):
		self.device = device_to_appoint(self.song.appointed_device)
	

	@listens('has_macro_mappings')
	def __on_has_macro_mappings_changed(self):
		self.song.appointed_device = device_to_appoint(self.song.view.selected_track.view.selected_device)
	

	@listens('selected_track')
	def __on_selected_track_changed(self):
		self.__on_selected_device_changed.subject = self.song.view.selected_track.view
		if self.device_selection_follows_track_selection:
			self.update_device_selection()
	

	@listens('selected_device')
	def __on_selected_device_changed(self):
		self._update_appointed_device()
	

	@listens('chains')
	def __on_chains_changed(self):
		self._update_appointed_device()
	

	@listens('mods')
	def __on_mod_device_added(self):
		debug('__on_mod_device_added')
		self.update_device_selection()
	

	def restart_mod(self):
		self.__on_mod_device_added.subject = get_modrouter()
	

	def _update_appointed_device(self):
		song = self.song
		device = song.view.selected_track.view.selected_device
		if liveobj_valid(device):
			self.song.appointed_device = device_to_appoint(device)
		rack_device = device if isinstance(device, Live.RackDevice.RackDevice) else None
		self.__on_has_macro_mappings_changed.subject = rack_device
		self.__on_chains_changed.subject = rack_device
	

	def mod_device_from_device(self, device):
		modrouter = get_modrouter()
		if modrouter:
			mod_device = modrouter.is_mod(device)
			if mod_device:
				device = mod_device._device_proxy
		return device
	

	def update_device_selection(self):
		debug('--------------update_device_selection')
		view = self.song.view
		track_or_chain = view.selected_chain if view.selected_chain else view.selected_track
		device_to_select = None
		if isinstance(track_or_chain, Live.Track.Track):
			device_to_select = track_or_chain.view.selected_device
		if device_to_select == None and len(track_or_chain.devices) > 0:
			device_to_select = track_or_chain.devices[0]
		if liveobj_valid(device_to_select):
			appointed_device = device_to_appoint(device_to_select)
			self.song.view.select_device(device_to_select, False)
			self.song.appointed_device = appointed_device
			#appointed_device = self.mod_device_from_device(appointed_device)
			self.device = appointed_device
		else:
			self.song.appointed_device = None
			self.device = None
	

	def reevaluate_device(self):
		debug('reevaluate_device')
		if isinstance(self.device, ModDeviceProxy):
			self.notify_device()
		else:
			device = self.mod_device_from_device(self.device)
			self._device = device
			self.notify_device()
	

#a

