# by amounra 0520 : http://www.aumhaa.com
# written against Live 10.1.14 on 051620


import Live
import math
import sys
from re import *
from itertools import chain, starmap



from .framework_mod_handler import *
from _Framework.Layer import Layer
from _Framework.ModesComponent import AddLayerMode
from _Framework.SubjectSlot import SlotManager
from _Framework.Control import ButtonControl
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from ableton.v2.base.util import nop
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import initialize_debug

from Launchpad.MainSelectorComponent import *
from Launchpad.Launchpad import Launchpad

debug = initialize_debug()


def _Launchpad_setup_mod(args):
	debug('args:', args)
	lpscript = args[0];
	script = args[1]
	if not hasattr(lpscript, '_modified') or (hasattr(lpscript, '_modified') and not lpscript._modified):
		with lpscript.component_guard():
			lpscript._sidebuttons = ButtonMatrixElement(name = 'SideButtons', rows = [lpscript._selector._side_buttons], register_control = lpscript._register_control, send_midi = lpscript._send_midi)
			lpscript.modhandler = LaunchpadModHandler(script = lpscript, modrouter = script.monomodular,  song = lpscript.song(), register_component = lpscript._register_component, is_enabled=False)
			lpscript.modhandler.name = 'ModHandler'
		script.schedule_message(1, script._device_provider.restart_mod)

		lpscript._selector._original_setup_user = lpscript._selector._setup_user
		lpscript._selector._original_update = lpscript._selector.update

		def make_setup_user():
			def _setup_user(release_buttons):
				MainSelectorComponent._setup_user(lpscript._selector, release_buttons)
				if not release_buttons:
					lpscript.modhandler.set_enabled(True)
					lpscript.modhandler.set_grid(lpscript._selector._matrix)
					lpscript.modhandler.set_key_buttons(lpscript._sidebuttons)
					lpscript.modhandler.set_nav_up_button(lpscript._selector._nav_buttons[0])
					lpscript.modhandler.set_nav_down_button(lpscript._selector._nav_buttons[1])
					lpscript.modhandler.set_nav_left_button(lpscript._selector._nav_buttons[2])
					lpscript.modhandler.set_nav_right_button(lpscript._selector._nav_buttons[3])
					lpscript.modhandler.set_shift_button(lpscript._selector._modes_buttons[2])
				else:
					lpscript.modhandler.set_enabled(False)
					lpscript.modhandler.set_grid(None)
					lpscript.modhandler.set_key_buttons(None)
					lpscript.modhandler.set_nav_up_button(None)
					lpscript.modhandler.set_nav_down_button(None)
					lpscript.modhandler.set_nav_left_button(None)
					lpscript.modhandler.set_nav_right_button(None)
					lpscript.modhandler.set_shift_button(None)
			return _setup_user

		lpscript._selector._setup_user = make_setup_user()

		def make_lppro_update():
			def update():
				lpscript.modhandler.set_grid(None)
				lpscript.modhandler.set_key_buttons(None)
				lpscript.modhandler.set_nav_up_button(None)
				lpscript.modhandler.set_nav_down_button(None)
				lpscript.modhandler.set_nav_left_button(None)
				lpscript.modhandler.set_nav_right_button(None)
				lpscript.modhandler.set_shift_button(None)
				lpscript.modhandler.set_enabled(False)
				MainSelectorComponent.update(lpscript._selector)
			return update

		lpscript._selector.update = make_lppro_update()

		def make_lppro_disconnect_mod():
			def _disconnect_mod():
				if lpscript._selector._mode_index == 2:
					lpscript._selector.set_mode(0)
				if hasattr(lpscript._selector, '_original_update'):
					lpscript._selector.update = lpscript._selector._original_update
				if hasattr(lpscript._selector, '_original_setup_user'):
					lpscript._setup_user = lpscript._selector._original_setup_user
				lpscript.modhandler.select_mod = nop
				if hasattr(lpscript, '_original_disconnect'):
					lpscript.disconnect = lpscript._original_disconnect
				lpscript._modified = False

			return _disconnect_mod

		lpscript._disconnect_mod = make_lppro_disconnect_mod()

		lpscript._original_disconnect = lpscript.disconnect

		def make_lpscript_disconnect():
			def disconnect():
				lpscript.modhandler.select_mod = nop
				lpscript.modhandler.disconnect()
				Launchpad.disconnect(lpscript)
			return disconnect

		lpscript.disconnect = make_lpscript_disconnect()

		lpscript._modified = True






class LaunchpadModHandler(FrameworkModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'LaunchpadModHandler'

	def __init__(self, register_component=None, *a, **k):
		self._color_type = 'Push'
		self._grid = None
		super(LaunchpadModHandler, self).__init__(register_component = register_component, *a, **k)
		self.nav_box = self.register_component(FrameworkNavigationBox(parent=self,height=16,width=16,window_x=8,window_y=8,callback=self.set_offset,register_component = register_component, song = self._song))
		self.nav_box._on_off_values = ('Mixer.Solo.Off', 'Mixer.Arm.On')
		self._launchmodColors = list(range(128))
		launchmod_colors = [3, 13, 37, 53, 5, 21, 49]
		self._launchmodColors[1:127] = [launchmod_colors[x%7] for x in range(126)]
		self._launchmodColors[127] = 49
		self._shifted = False


	def select_mod(self, mod):
		super(LaunchpadModHandler, self).select_mod(mod)
		#self._script._select_note_mode()
		self.update()
		debug('lp2modhandler select mod: ' + str(mod))


	def _receive_grid(self, x, y, value = -1, identifier = -1, channel = -1, *a, **k):
		# debug('lp2modhandler._receive_grid:', x, y, value, identifier, channel)
		mod = self.active_mod()
		if mod and self._grid_value.subject:
			if mod.legacy:
				x = x-self.x_offset
				y = y-self.y_offset
			if x in range(8) and y in range(8):
				value > -1 and self._grid_value.subject.send_value(x, y, self._launchmodColors[self._colors[value]], True)
				button = self._grid_value.subject.get_button(y, x)
				if button:
					new_identifier = identifier if identifier > -1 else button._original_identifier
					new_channel = channel if channel > -1 else button._original_channel
					button._msg_identifier != new_identifier and button.set_identifier(new_identifier)
					button._msg_channel != new_channel and button.set_channel(new_channel)
					button._report_input = True
					button.suppress_script_forwarding = ((channel, identifier) != (-1, -1))


	def _receive_key(self, x, value):
		# debug('lp2modhandler._receive_key:', x, value)
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._launchmodColors[self._colors[value]], True)


	def nav_update(self):
		self.nav_box and self.nav_box.update()


	def set_shift_button(self, button):
		self._shift_value.subject = button
		if button:
			button.send_value(127)


	def update(self, *a, **k):
		if not self._shift_value.subject is None:
			self._shift_value.subject.send_value(127)
		mod = self.active_mod()
		if not mod is None:
			mod.restore()
		else:
			if not self._grid_value.subject is None:
				self._grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()
