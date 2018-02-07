# by amounra 1017 : http://www.aumhaa.com
# written against Live 9.75 release on 102717

from __future__ import absolute_import, print_function, unicode_literals
import Live
import math
import sys
from re import *
from itertools import imap, chain, starmap

import logging
logger = logging.getLogger(__name__)

from ableton.v2.base import inject, listens, listens_group
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry, midi
from ableton.v2.control_surface.elements import ButtonMatrixElement, DoublePressElement, MultiElement, DisplayDataSource, SysexElement
from ableton.v2.control_surface.components import M4LInterfaceComponent, BackgroundComponent, ViewControlComponent, PlayableComponent
from ableton.v2.control_surface.components.mixer import simple_track_assigner
from ableton.v2.control_surface.mode import AddLayerMode, ModesComponent, DelayMode
from ableton.v2.control_surface.elements.physical_display import PhysicalDisplayElement
from ableton.v2.control_surface.components.session_recording import *
from ableton.v2.control_surface.percussion_instrument_finder import PercussionInstrumentFinder, find_drum_group_device
from ableton.v2.control_surface.control import PlayableControl, ButtonControl, control_matrix

from aumhaa.v2.base import initialize_debug
from aumhaa.v2.control_surface import MomentaryBehaviour, ExcludingMomentaryBehaviour, DelayedExcludingMomentaryBehaviour, ShiftedBehaviour, LatchingShiftedBehaviour, FlashingBehaviour
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.elements import MonoBridgeElement, generate_strip_string
from aumhaa.v2.control_surface.elements.mono_button import *
from aumhaa.v2.control_surface.components import MonoDeviceComponent, DeviceNavigator, TranslationComponent

from pushbase.auto_arm_component import AutoArmComponent

from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

debug = initialize_debug()

SYSEX_HEADER = (240, 0, 33, 16)
MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224

CHANNEL = 0

BLOCKS_PADS = [x%8 + (abs(int(x/8)-7)*8) + 36 for x in range(64)]

COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]

class MonoBlocksColors:


	class DefaultButton:
		On = LividRGB.WHITE
		Off = LividRGB.OFF
		Disabled = LividRGB.OFF
		Alert = LividRGB.BlinkFast.WHITE
	

	class DrumGroup:
		PadAction = LividRGB.WHITE
		PadFilled = LividRGB.GREEN
		PadFilledAlt = LividRGB.MAGENTA
		PadSelected = LividRGB.WHITE
		PadSelectedNotSoloed = LividRGB.WHITE
		PadEmpty = LividRGB.OFF
		PadMuted = LividRGB.YELLOW
		PadSoloed = LividRGB.CYAN
		PadMutedSelected = LividRGB.BLUE
		PadSoloedSelected = LividRGB.BLUE
		PadInvisible = LividRGB.OFF
		PadAction = LividRGB.RED
	

	class Mod:
		class Nav:
			OnValue = LividRGB.RED
			OffValue = LividRGB.WHITE
		
	


class MonoBlocksModHandler(ModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'MonoBlocksModHandler'

	def __init__(self, *a, **k):
		self._color_type = 'Push'
		self._grid = None
		super(MonoBlocksModHandler, self).__init__(*a, **k)
		self.nav_box = self.register_component(MonoBlocksNavigationBox(self, 16, 16, 8, 8, self.set_offset,)) # song = self.song, register_component = self.register_component, is_enabled = False))
		self._push_colors = range(128)
		self._push_colors[1:8] = [120, 30, 12, 20, 65, 11, 125]
		self._push_colors[127] = 125
		self._shifted = False
		#debug(BLOCKS_PADS)
	

	def select_mod(self, mod):
		super(MonoBlocksModHandler, self).select_mod(mod)
		#self._script._select_note_mode()
		self.update()
		debug('modhandler select mod: ' + str(mod))
	

	def _receive_grid(self, x, y, value = -1, identifier = -1, channel = -1, *a, **k):
		#debug('_receive_ blocks_grid:', x, y, value, identifier, channel)
		mod = self.active_mod()
		if mod and self._grid_value.subject:
			if mod.legacy:
				x = x-self.x_offset
				y = y-self.y_offset
			if x in range(8) and y in range(8):
				value > -1 and self._grid_value.subject.send_value(x, y, self._push_colors[self._colors[value]], True)
				button = self._grid_value.subject.get_button(y, x)
				if button:
					new_identifier = identifier if identifier > -1 else button._original_identifier
					new_channel = channel if channel > -1 else button._original_channel
					button._msg_identifier != new_identifier and button.set_identifier(new_identifier)
					button._msg_channel != new_channel and button.set_channel(new_channel)
					button._report_input = True
					button.set_enabled((channel, identifier) == (-1, -1))
					
	

	def _receive_key(self, x, value):
		#debug('_receive_key:', x, value)
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._push_colors[self._colors[value]], True)
	

	def nav_update(self):
		self.nav_box and self.nav_box.update()
	

	def set_modifier_colors(self):
		shiftbutton = self._shift_value.subject
		shiftbutton and shiftbutton.set_on_off_values('Mod.ShiftOn', 'Mod.ShiftOff')
		altbutton = self._alt_value.subject
		altbutton and altbutton.set_on_off_values('Mod.AltOn', 'Mod.AltOff')
	

	@Shift_button.pressed
	def Shift_button(self, button):
		debug('shift_button.pressed')
		self._is_shifted = True
		mod = self.active_mod()
		if mod:
			mod.send('shift', 1)
		self.shift_layer and self.shift_layer.enter_mode()
		if mod and mod.legacy:
			self.legacy_shift_layer and self.legacy_shift_layer.enter_mode()
		self.update()
	

	@Shift_button.released
	def Shift_button(self, button):
		self._is_shifted = False
		mod = self.active_mod()
		if mod:
			mod.send('shift', 0)
		self.legacy_shift_layer and self.legacy_shift_layer.leave_mode()
		self.shift_layer and self.shift_layer.leave_mode()
		self.update()
	

	@Alt_button.pressed
	def Alt_button(self, button):
		debug('alt_button.pressed')
		self._is_alted = True
		mod = self.active_mod()
		if mod:
			mod.send('alt', 1)
			mod._device_proxy._alted = True
			mod._device_proxy.update_parameters()
		self.alt_layer and self.alt_layer.enter_mode()
		self.update()
	

	@Alt_button.released
	def Alt_button(self, button):
		self._is_alted = False
		mod = self.active_mod()
		if mod:
			mod.send('alt', 0)
			mod._device_proxy._alted = False
			mod._device_proxy.update_parameters()
		self.alt_layer and self.alt_layer.leave_mode()
		self.update()
	

	def update(self, *a, **k):
		mod = self.active_mod()
		if not mod is None:
			mod.restore()
		else:
			if not self._grid_value.subject is None:
				self._grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()
	


class MonoBlocksNavigationBox(NavigationBox):


	def update(self):
		debug('nav_box.update()')
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
		left_button and left_button.set_light('DefaultButton.On' if (xoff>0) else 'DefaultButton.Off')
		right_button and right_button.set_light('DefaultButton.On' if (xoff<(self.width()-self._window_x)) else 'DefaultButton.Off')
		up_button and up_button.set_light('DefaultButton.On' if (yoff>0) else 'DefaultButton.Off')
		down_button and down_button.set_light('DefaultButton.On' if (yoff<(self.height()-self._window_y)) else 'DefaultButton.Off')
	


class MonoBlocks(ControlSurface):


	_rgb = 0
	_color_type = 'Push'
	_timer = 0
	_touched = 0
	flash_status = False
	_model_name = 'MonoBlocks'
	_host_name = 'MonoBlocks'
	_version_check = 'b996'
	monomodular = None
	device_provider_class = ModDeviceProvider

	def __init__(self, *a, **k):
		super(MonoBlocks, self).__init__(*a, **k)
		self.log_message = logger.info
		self._skin = Skin(MonoBlocksColors)
		with self.component_guard():
			self._setup_monobridge()
			self._setup_controls()
			#self._setup_device()
			self._setup_mod()
			#self._setup_modes()
			self._setup_modswitcher()
		self._on_device_changed.subject = self._device_provider
		self.schedule_message(1, self._open_log)
	

	def _open_log(self):
		#self.log_message("<<<<<<<<<<<<<<<<<<<<= " + str(self._model_name) + " " + str(self._version_check) + " log opened =>>>>>>>>>>>>>>>>>>>") 
		self.show_message(str(self._model_name) + ' Control Surface Loaded')
	

	def _close_log(self):
		#self.log_message("<<<<<<<<<<<<<<<<<<<<= " + str(self._model_name) + " " + str(self._version_check) + " log closed =>>>>>>>>>>>>>>>>>>>") 
		pass
	

	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		#self._pads_raw = [ ButtonElement(True, MIDI_NOTE_TYPE, 0, identifier, name=u'Pad_{}'.format(identifier), skin=skin) for identifier in xrange(100) ]
		self._pad = [MonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = CHANNEL, identifier = BLOCKS_PADS[index], name = 'Pad_' + str(index), script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for index in range(64)]
		for button in self._pad:
			button.set_color_map(tuple(range(128))) 
		self._matrix = ButtonMatrixElement(name = 'Matrix', rows = [self._pad[(index*8):(index*8)+8] for index in range(8)])
	

	#def _setup_device(self):
	#	self._device_selection_follows_track_selection = True 
	#	self._device = DeviceComponent(name = 'Device_Component', device_bank_registry = DeviceBankRegistry(), device_provider = self._device_provider)
	#	self._device.set_enabled(True)
	

	def _setup_monobridge(self):
		self._monobridge = MonoBridgeElement(self)
		self._monobridge.name = 'MonoBridge'
	

	def _setup_mod(self):

		def get_monomodular(host):
				if isinstance(__builtins__, dict):
					if not 'monomodular' in __builtins__.keys() or not isinstance(__builtins__['monomodular'], ModRouter):
						__builtins__['monomodular'] = ModRouter(song = self.song, register_component = self._register_component)
				else:
					if not hasattr(__builtins__, 'monomodular') or not isinstance(__builtins__['monomodular'], ModRouter):
						setattr(__builtins__, 'monomodular', ModRouter(song = self.song, register_component = self._register_component))
				monomodular = __builtins__['monomodular']
				if not monomodular.has_host():
					monomodular.set_host(host)
				return monomodular
		

		self.monomodular = get_monomodular(self)
		self.monomodular.name = 'monomodular_switcher'
		with inject(register_component = const(self._register_component), song = const(self.song)).everywhere():
			self.modhandler = MonoBlocksModHandler(self) ## song = self.song, register_component = self._register_component)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer( priority = 6, grid = self._matrix)
		self.modhandler.alt_shift_layer = AddLayerMode( self.modhandler, Layer())
		#																	Shift_button = self.elements.shift_button,
		#																	Alt_button = self.elements.select_button))
		self.modhandler.legacy_shift_layer = AddLayerMode( self.modhandler, Layer(priority = 7, 
																			device_selector_matrix = self._matrix.submatrix[:, :1],
																			channel_buttons = self._matrix.submatrix[:, 1:2], 
																			nav_matrix = self._matrix.submatrix[4:8, 2:6],
																			))
		self.modhandler.shift_layer = AddLayerMode( self.modhandler, Layer( priority = 7, 
																			device_selector_matrix = self._matrix.submatrix[:, :1],
																			))
																			#lock_button = self.elements.master_select_button,
																			#))
		self.modhandler.alt_layer = AddLayerMode( self.modhandler, Layer( priority = 7, 
																			))
																			#key_buttons = self.elements.select_buttons))
																			#key_buttons = self.elements.track_state_buttons))
		self._device_provider.restart_mod()
	

	def _setup_modswitcher(self):
		self._modswitcher = ModesComponent(name = 'ModSwitcher')
		self._modswitcher.add_mode('mod', [self.modhandler])
		self._modswitcher.selected_mode = 'mod'
		self._modswitcher.set_enabled(True)
	

	def flash(self):
		if(self.flash_status > 0):
			for control in self.controls:
				if isinstance(control, MonoButtonElement):
					control.flash(self._timer)
	

	def update_display(self):
		super(ControlSurface, self).update_display()
		self._timer = (self._timer + 1) % 256
		self.flash()
	

	def touched(self):
		if self._touched is 0:
			self._monobridge._send('touch', 'on')
			self.schedule_message(2, self.check_touch)
		self._touched +=1
	

	def check_touch(self):
		if self._touched > 5:
			self._touched = 5
		elif self._touched > 0:
			self._touched -= 1
		if self._touched is 0:
			self._monobridge._send('touch', 'off')
		else:
			self.schedule_message(2, self.check_touch)
	

	@listens('device')
	def _on_device_changed(self):
		#self.schedule_message(1, self._update_modswitcher)
		debug('base on_device_changed')
		#self._update_modswitcher()
	

	def _on_selected_track_changed(self):
		super(MonoBlocks, self)._on_selected_track_changed()
		if not len(self.song.view.selected_track.devices):
			self._update_modswitcher()
		#self.schedule_message(1, self._update_modswitcher)
	

	def disconnect(self):
		super(MonoBlocks, self).disconnect()
		self._close_log()
	

	def restart_monomodular(self):
		#self.log_message('restart monomodular')
		self.modhandler.disconnect()
		with self.component_guard():
			self._setup_mod()
	

	def process_midi_bytes(self, midi_bytes, midi_processor):
		u"""
		Finds the right recipient for the MIDI message and translates it into the
		expected format. The result is forwarded to the midi_processor.
		"""
		if midi.is_sysex(midi_bytes):
			result = self.get_registry_entry_for_sysex_midi_message(midi_bytes)
			if result is not None:
				identifier, recipient = result
				midi_processor(recipient, midi_bytes[len(identifier):-1])
			#elif self.received_midi_listener_count() == 0:
			#	logger.warning(u'Got unknown sysex message: ' + midi.pretty_print_bytes(midi_bytes))
		else:
			recipient = self.get_recipient_for_nonsysex_midi_message(midi_bytes)
			if recipient is not None:
				midi_processor(recipient, midi.extract_value(midi_bytes))
			#elif self.received_midi_listener_count() == 0:
			#	logger.warning(u'Got unknown message: ' + midi.pretty_print_bytes(midi_bytes))
	









