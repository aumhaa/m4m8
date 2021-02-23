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
from _Framework.ModesComponent import tomode
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import initialize_debug
from Launchpad_MK2 import Launchpad_MK2

debug = initialize_debug()

# def override_launchpad_mk2(script, lp2script):
#
# 	# with inject(register_component = const(lp2script._register_component), song = const(lp2script.song)).everywhere():
# 	lp2script.modhandler = LaunchpadMk2ModHandler(script = lp2script, modrouter = script.monomodular,  song = lp2script.song(), register_component = lp2script._register_component, is_enabled=False)
# 	lp2script.modhandler.name = 'ModHandler'
# 	lp2script.modhandler.layer = Layer(
# 		grid = lp2script._session_matrix,
# 		key_buttons = lp2script._scene_launch_matrix,
# 		nav_up_button = lp2script._up_button,
# 		nav_down_button = lp2script._down_button,
# 		nav_left_button = lp2script._left_button,
# 		nav_right_button = lp2script._right_button,
# 		Shift_button = lp2script._user_1_button,)
# 		# nav_matrix = lp2script._session_matrix.submatrix[2:6, 2:6])
# 	# lp2script.modhandler.legacy_shift_layer = AddLayerMode( lp2script.modhandler, Layer( nav_matrix = lp2script._session_matrix.submatrix[2:6, 2:6]))
# 																		# device_selector_matrix = lp2script._session_matrix.submatrix[:, :1],
# 																		# channel_buttons = lp2script._session_matrix.submatrix[:, 1:2],
#
# 	script._device_provider.restart_mod()
#
# 	lp2script._modes.add_mode(u'mod_mode', [lp2script.modhandler], layout_byte=0)
# 	lp2script._modes.layer = Layer(session_mode_button=lp2script._session_button,
# 											mod_mode_button=lp2script._user_1_button,
# 											user_2_mode_button=lp2script._user_2_button,
# 											mixer_mode_button=lp2script._mixer_button,
# 											volume_mode_button=lp2script._volume_button,
# 											pan_mode_button=lp2script._pan_button,
# 											send_a_mode_button=lp2script._send_a_button,
# 											send_b_mode_button=lp2script._send_b_button)
# 	lp2script._modified = True



def _Launchpad_MK2_setup_mod(args):
	# debug('args:', args)
	lp2script = args[0];
	script = args[1]
	if not hasattr(lp2script, '_modified') or (hasattr(lp2script, '_modified') and not lp2script._modified):
		lp2script.modhandler = LaunchpadMk2ModHandler(script = lp2script, modrouter = script.monomodular,  song = lp2script.song(), register_component = lp2script._register_component, is_enabled=False)
		lp2script.modhandler.name = 'ModHandler'
		lp2script.modhandler.layer = Layer(
			grid = lp2script._session_matrix,
			key_buttons = lp2script._scene_launch_matrix,
			nav_up_button = lp2script._up_button,
			nav_down_button = lp2script._down_button,
			nav_left_button = lp2script._left_button,
			nav_right_button = lp2script._right_button,
			Shift_button = lp2script._user_1_button,)
		lp2script.modhandler.legacy_shift_layer = AddLayerMode( lp2script.modhandler, Layer( nav_matrix = lp2script._session_matrix.submatrix[2:6, 2:6]))
		script.schedule_message(1, script._device_provider.restart_mod)


		lp2script._modes.add_mode('mod_mode', [lp2script.modhandler], layout_byte=0)

		lp2script._modes._original_layer = lp2script._modes.layer
		lp2script._modes.layer = Layer(session_mode_button=lp2script._session_button,
												mod_mode_button=lp2script._user_1_button,
												user_2_mode_button=lp2script._user_2_button,
												mixer_mode_button=lp2script._mixer_button,
												volume_mode_button=lp2script._volume_button,
												pan_mode_button=lp2script._pan_button,
												send_a_mode_button=lp2script._send_a_button,
												send_b_mode_button=lp2script._send_b_button)


		def make_lp2script_disconnect_mod():
			def _disconnect_mod():
				if hasattr(lp2script._modes, '_original_layer'):
					if lp2script._modes.selected_mode == 'mod_mode':
						lp2script._modes.selected_mode = 'user_2_mode'
					lp2script._modes.layer = lp2script._modes._original_layer
				if 'mod_mode' in lp2script._modes._mode_list:
					del lp2script._modes._mode_list[lp2script._modes._mode_list.index('mod_mode')]
				if 'mod_mode' in list(lp2script._modes._mode_map.keys()):
					del lp2script._modes._mode_map['mod_mode']
				lp2script.modhandler.select_mod = nop
				if hasattr(lp2script, '_original_disconnect'):
					lp2script.disconnect = lp2script._original_disconnect
				lp2script._modified = False
			return _disconnect_mod
		lp2script._disconnect_mod = make_lp2script_disconnect_mod()

		lp2script._original_disconnect = lp2script.disconnect

		def make_lp2script_disconnect():
			def disconnect():
				lp2script.modhandler.select_mod = nop
				lp2script.modhandler.disconnect()
				Launchpad_MK2.disconnect(lp2script)
			return disconnect
		lp2script.disconnect = make_lp2script_disconnect()

		lp2script._modified = True



class LaunchpadMk2ModHandler(FrameworkModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'LaunchpadMk2ModHandler'

	def __init__(self, register_component=None, *a, **k):
		self._color_type = 'Push'
		self._grid = None
		super(LaunchpadMk2ModHandler, self).__init__(register_component = register_component, *a, **k)
		self.nav_box = self.register_component(FrameworkNavigationBox(parent=self,height=16,width=16,window_x=8,window_y=8,callback=self.set_offset,register_component = register_component, song = self._song))
		self.nav_box._on_off_values = ('Mixer.Solo.Off', 'Mixer.Arm.On')
		self._launchmodColors = list(range(128))
		launchmod_colors = [3, 13, 37, 53, 5, 21, 49]
		self._launchmodColors[1:127] = [launchmod_colors[x%7] for x in range(126)]
		self._launchmodColors[127] = 49
		self._shifted = False


	def select_mod(self, mod):
		super(LaunchpadMk2ModHandler, self).select_mod(mod)
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
		hasattr(self, 'shift_layer') and self.shift_layer.enter_mode()
		if mod and mod.legacy:
			hasattr(self, 'legacy_shift_layer') and self.legacy_shift_layer.enter_mode()
		self.update()


	@Shift_button.released
	def Shift_button(self, button):
		self._is_shifted = False
		mod = self.active_mod()
		if mod:
			mod.send('shift', 0)
		hasattr(self, 'legacy_shift_layer') and self.legacy_shift_layer.leave_mode()
		hasattr(self, 'shift_layer') and self.shift_layer.leave_mode()
		self.update()
	#
	#
	# @Alt_button.pressed
	# def Alt_button(self, button):
	# 	debug('alt_button.pressed')
	# 	self._is_alted = True
	# 	mod = self.active_mod()
	# 	if mod:
	# 		mod.send('alt', 1)
	# 		mod._device_proxy._alted = True
	# 		mod._device_proxy.update_parameters()
	# 	self.alt_layer and self.alt_layer.enter_mode()
	# 	self.update()
	#
	#
	# @Alt_button.released
	# def Alt_button(self, button):
	# 	self._is_alted = False
	# 	mod = self.active_mod()
	# 	if mod:
	# 		mod.send('alt', 0)
	# 		mod._device_proxy._alted = False
	# 		mod._device_proxy.update_parameters()
	# 	self.alt_layer and self.alt_layer.leave_mode()
	# 	self.update()


	def update(self, *a, **k):
		mod = self.active_mod()
		if not mod is None:
			mod.restore()
		else:
			if not self._grid_value.subject is None:
				self._grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()
