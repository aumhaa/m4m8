# by amounra 1017 : http://www.aumhaa.com
# written against Live 10.0.3b8 RC on 083018


import Live
import math
import sys
from re import *
from itertools import chain, starmap

import logging
logger = logging.getLogger(__name__)

from ableton.v2.base import inject, listens, listens_group
from ableton.v2.control_surface import ControlSurface, ControlElement, Layer, Skin, PrioritizedResource, Component, ClipCreator, DeviceBankRegistry, midi
from ableton.v2.control_surface.elements import ButtonMatrixElement, DoublePressElement, MultiElement, DisplayDataSource, SysexElement
from ableton.v2.control_surface.components import BackgroundComponent, ViewControlComponent, PlayableComponent
from ableton.v2.control_surface.components.mixer import SimpleTrackAssigner
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
from aumhaa.v2.control_surface.components.m4l_interface import M4LInterfaceComponent

from pushbase.auto_arm_component import AutoArmComponent

from ableton.v2.control_surface.elements.color import Color
from aumhaa.v2.livid.colors import *

from Launchpad_MK2 import Launchpad_MK2
from .launchpad_mk2_mod import _Launchpad_MK2_setup_mod

from Launchpad_Pro import Launchpad_Pro
from .launchpad_pro_mod import _Launchpad_Pro_setup_mod

from Launchpad import Launchpad
from .launchpad_mod import _Launchpad_setup_mod

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


#COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]
COLOR_MAP = list(range(7))

class Aum256Colors:


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


class SpecialMonoButtonElement(MonoButtonElement):

	def __init__(self, *a, **k):
		self._text = ''
		super(SpecialMonoButtonElement, self).__init__(*a, **k)

	@listenable_property
	def text(self):
		return str(self._text)

	def set_text(self, text = ''):
		# debug('button text:', self._text)
		# self._text = text.encode('utf-8', 'ignore')
		self._text = str(text)
		self.notify_text(self._text)

	def reset(self):
		super(SpecialMonoButtonElement, self).reset()
		self._text = ''
		self.notify_text(self._text)


class TextGrid(Grid):

	def __init__(self, name, width, height, active_handlers = return_empty, *a, **k):
		super(TextGrid, self).__init__(name, width, height, active_handlers, *a, **k)
		self._cell = [[StoredElement(active_handlers, _name = self._name + '_' + str(x) + '_' + str(y), _x = x, _y = y , _value = '', *a, **k) for y in range(height)] for x in range(width)]


class TextArray(Array):

	def __init__(self, name, size, active_handlers = return_empty, *a, **k):
		super(TextArray, self).__init__(name, size, active_handlers, *a, **k)
		self._cell = [StoredElement(self._name + '_' + str(num), _num = num, _value = '', *a, **k) for num in range(size)]


class Aum256ModHandler(ModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'Aum256ModHandler'

	def __init__(self, *a, **k):
		self._color_type = 'Push'
		self._grid = None
		addresses = {'key_text': {'obj':TextArray('key_text', 8), 'method':self._receive_key_text},
					'grid_text': {'obj':TextGrid('grid_text', 16, 16), 'method':self._receive_grid_text}}
		super(Aum256ModHandler, self).__init__(*a, **k)
		self.nav_box = Aum256NavigationBox(self, 16, 16, 16, 16, self.set_offset,)
		self._push_colors = list(range(128))
		self._push_colors[1:127] = [(x%7)+1 for x in range(127)]
		self._push_colors[127] = 7
		self._shifted = False


	def select_mod(self, mod):
		super(Aum256ModHandler, self).select_mod(mod)
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
			if x in range(16) and y in range(16):
				value > -1 and self._grid_value.subject.send_value(x, y, self._push_colors[self._colors[value]], True)
				button = self._grid_value.subject.get_button(y, x)
				if button:
					new_identifier = identifier if identifier > -1 else button._original_identifier
					new_channel = channel if channel > -1 else button._original_channel
					button._msg_identifier != new_identifier and button.set_identifier(new_identifier)
					button._msg_channel != new_channel and button.set_channel(new_channel)
					button._report_input = True
					button.set_enabled((channel, identifier) == (-1, -1))


	def _receive_grid_text(self, x, y, value = '', *a, **k):
		# debug('_receive_grid_text:', x, y, value)
		mod = self.active_mod()
		if mod and self._grid_value.subject:
			if mod.legacy:
				x = x-self.x_offset
				y = y-self.y_offset
			if x in range(8) and y in range(4):
				button = self._grid_value.subject.get_button(y, x)
				if button:
					# debug('setting button')
					button.set_text(value)


	def _receive_key(self, x, value):
		#debug('_receive_key:', x, value)
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._push_colors[self._colors[value]], True)


	def _receive_key_text(self, x, value = '', *a, **k):
		#debug('_receive_key:', x, value)
		if not self._keys_value.subject is None:
			button = self._keys_value.subject.get_button(0, x)
			if button:
				button.set_text(value)


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


class Aum256NavigationBox(NavigationBox):


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


class Aum256(ControlSurface):


	_rgb = 0
	_color_type = 'Push'
	_timer = 0
	_touched = 0
	flash_status = False
	_model_name = 'Aum256'
	_host_name = 'Aum256'
	_version_check = 'b996'
	monomodular = None
	device_provider_class = ModDeviceProvider

	def __init__(self, *a, **k):
		super(Aum256, self).__init__(*a, **k)
		self.log_message = logger.info
		self._skin = Skin(Aum256Colors)
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


	@listenable_property
	def pipe(self):
		return None


	def _send(self, **a):
		notify_pipe(a)



	def _setup_controls(self):
		is_momentary = True
		optimized = True
		resource = PrioritizedResource
		#self._pads_raw = [ ButtonElement(True, MIDI_NOTE_TYPE, 0, identifier, name=u'Pad_{}'.format(identifier), skin=skin) for identifier in xrange(100) ]
		self._pad = [SpecialMonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = int(math.floor(index/128)), identifier = index%128, name = 'Pad_' + str(index), script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for index in range(256)]
		for button in self._pad:
			button.set_color_map(tuple(range(128)))
		self._matrix = ButtonMatrixElement(name = 'Matrix', rows = [self._pad[(index*16):(index*16)+16] for index in range(16)])
		self._key = [SpecialMonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = 2, identifier = index, name = 'Key_' + str(index), script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource) for index in range(8)]
		for button in self._pad:
			button.set_color_map(tuple(range(128)))
		self._key_matrix = ButtonMatrixElement(name = 'KeyMatrix', rows = [self._key])

		self._shift = SpecialMonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = 2, identifier = 8, name = 'Shift', script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource)
		self._shift.set_color_map(tuple(range(128)))
		self._alt = SpecialMonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = 2, identifier = 9, name = 'Alt', script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource)
		self._alt.set_color_map(tuple(range(128)))
		self._lock = SpecialMonoButtonElement(is_momentary = is_momentary, msg_type = MIDI_NOTE_TYPE, channel = 2, identifier = 10, name = 'Lock', script = self, monobridge = self._monobridge, skin = self._skin, color_map = COLOR_MAP, optimized_send_midi = optimized, resource_type = resource)
		self._lock.set_color_map(tuple(range(128)))

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
					if not 'monomodular' in list(__builtins__.keys()) or not isinstance(__builtins__['monomodular'], ModRouter):
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
		# with inject(register_component = const(self._register_component), song = const(self.song)).everywhere():
		self.modhandler = Aum256ModHandler(self) ## song = self.song, register_component = self._register_component)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer( priority = 6, grid = self._matrix,
																			Shift_button = self._shift,
																			Alt_button = self._alt,
																			key_buttons = self._key_matrix)
		self.modhandler.alt_shift_layer = AddLayerMode( self.modhandler, Layer())
		self.modhandler.legacy_shift_layer = AddLayerMode( self.modhandler, Layer(priority = 7,
																			device_selector_matrix = self._matrix.submatrix[:, :1],
																			channel_buttons = self._matrix.submatrix[:, 1:2],
																			))
																			#nav_matrix = self._matrix.submatrix[4:8, 2:6],
																			#))
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
		self._modHandle = ModControl(modscript = self, monomodular = self.monomodular, name = 'ModHandle')


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
		debug('Aum256 on_device_changed')
		#self._update_modswitcher()


	def _on_selected_track_changed(self):
		super(Aum256, self)._on_selected_track_changed()
		if not len(self.song.view.selected_track.devices):
			self._update_modswitcher()
		#self.schedule_message(1, self._update_modswitcher)


	def disconnect(self):
		for script in self._connected_scripts:
			if hasattr(script, '_disconnect_mod'):
				script._disconnect_mod()
		super(Aum256, self).disconnect()
		self._close_log()


	def restart_monomodular(self):
		#self.log_message('restart monomodular')
		self.modhandler.disconnect()
		with self.component_guard():
			self._setup_mod()


	def _do_send_midi(self, midi_event_bytes):
		super(Aum256, self)._do_send_midi(midi_event_bytes)
		bytes = list(midi_event_bytes)
		self.notify_pipe('midi', *bytes)


	def receive_note(self, num, val, chan=0):
		# debug('receive_note', num, val)
		self.receive_midi(tuple([144+chan, num, val]))


	def receive_cc(self, num, val, chan=0):
		# debug('receive_cc', num, val)
		self.receive_midi(tuple([176+chan, num, val]))


	def process_midi_bytes(self, midi_bytes, midi_processor):
		"""
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


	def connect_script_instances(self, instanciated_scripts):
		debug('connect_script_instances', instanciated_scripts)
		self._connected_scripts = []
		for script in instanciated_scripts:
			# debug(script)
			if  isinstance (script, Launchpad_MK2):
				self._connected_scripts.append(script)
				self._on_lp2_mode_changed.subject = script._modes
				if not hasattr(script, '_modified') or (hasattr(script, '_modified') and not script._modified):
					script.setup_mod = _Launchpad_MK2_setup_mod
					script.schedule_message(1, script.setup_mod, [script, self])
			elif  isinstance (script, Launchpad_Pro):
				self._connected_scripts.append(script)
				self._on_lppro_mode_changed.subject = script._note_modes
				if not hasattr(script, '_modified') or (hasattr(script, '_modified') and not script._modified):
					script.setup_mod = _Launchpad_Pro_setup_mod
					script.schedule_message(1, script.setup_mod, [script, self])
			elif  isinstance (script, Launchpad):
				self._connected_scripts.append(script)
				# self._on_lppro_mode_changed.subject = script._note_modes
				if not hasattr(script, '_modified') or (hasattr(script, '_modified') and not script._modified):
					script.setup_mod = _Launchpad_setup_mod
					script.schedule_message(1, script.setup_mod, [script, self])
		debug('connected_scripts:', self._connected_scripts)




	@listens('selected_mode')
	def _on_lp2_mode_changed(self, mode):
		debug('_on_lp2_mode_changed', mode)

	@listens('selected_mode')
	def _on_lppro_mode_changed(self, mode):
		debug('_on_lppro_mode_changed', mode)
