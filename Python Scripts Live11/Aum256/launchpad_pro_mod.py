# by amounra 0520 : http://www.aumhaa.com
# written against Live 10.1.14 on 051620


from functools import partial
import Live
import math
import sys
from re import *
from itertools import chain, starmap


from .framework_mod_handler import *
from _Framework.Layer import Layer
from _Framework.ModesComponent import AddLayerMode, DelayMode
from _Framework.SubjectSlot import SlotManager
from _Framework.Control import ButtonControl
from _Framework.ModesComponent import tomode, CompoundMode
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.base.debug import initialize_debug
from ableton.v2.base.util import nop
from Launchpad_Pro.Launchpad_Pro import Launchpad_Pro
from Launchpad_Pro import consts
from Launchpad_Pro.TranslationComponent import TranslationComponent

debug = initialize_debug()

def _Launchpad_Pro_setup_mod(args):
	lpproscript = args[0]
	modscript = args[1]
	if not hasattr(lpproscript, '_modified') or (hasattr(lpproscript, '_modified') and not lpproscript._modified):
		with lpproscript.component_guard():
			lpproscript.modhandler = LaunchpadProModHandler(script = lpproscript, modrouter = modscript.monomodular,  song = lpproscript.song(), register_component = lpproscript._register_component, is_enabled=False)
		lpproscript.modhandler.name = 'ModHandler'
		lpproscript.modhandler.layer = Layer(grid = lpproscript._midimap['Main_Button_Matrix'].submatrix[:,:],
			key_buttons = lpproscript._midimap['Scene_Launch_Button_Matrix'],
			nav_up_button = lpproscript._midimap['Arrow_Up_Button'],
			nav_down_button = lpproscript._midimap['Arrow_Down_Button'],
			nav_left_button = lpproscript._midimap['Arrow_Left_Button'],
			nav_right_button = lpproscript._midimap['Arrow_Right_Button'],
			Shift_button = lpproscript._midimap['Shift_Button'],
			Alt_button = lpproscript._midimap['Note_Mode_Button'])
		lpproscript.modhandler.legacy_shift_layer = AddLayerMode(lpproscript.modhandler, Layer(nav_matrix = lpproscript._midimap['Main_Button_Matrix'].submatrix[2:6, 2:6]))

		modscript.schedule_message(1, modscript._device_provider.restart_mod)

		lpproscript._note_modes.add_mode('mod_mode', [ partial(lpproscript._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE), lpproscript.modhandler])

		lpproscript._original_select_note_mode = lpproscript._select_note_mode

		def create_note_mode_override(lpproscript):
			def _select_note_mode():
				track = lpproscript._target_track_component.target_track
				drum_device = lpproscript._drum_group_finder.drum_group
				if lpproscript.modhandler.active_mod():
					lpproscript._note_modes.selected_mode = 'mod_mode'
				elif track is None or track.is_foldable or track in lpproscript.song().return_tracks or track == lpproscript.song().master_track or track.is_frozen or track.has_audio_input:
					lpproscript._note_modes.selected_mode = 'audio_mode'
				elif drum_device:
					lpproscript._note_modes.selected_mode = 'drum_mode'
				else:
					lpproscript._note_modes.selected_mode = 'chromatic_mode'
				lpproscript._modes.update()
				if lpproscript._note_modes.selected_mode == 'audio_mode' or lpproscript._note_modes.selected_mode == 'mod_mode':
					lpproscript.release_controlled_track()
				else:
					lpproscript.set_controlled_track(lpproscript._target_track_component.target_track)
			return _select_note_mode

		lpproscript._select_note_mode = create_note_mode_override(lpproscript)

		def make_lpproscript_disconnect_mod():
			def _disconnect_mod():
				if hasattr(lpproscript, '_original_select_note_mode'):
					if lpproscript._note_modes.selected_mode == 'mod_mode':
						lpproscript._note_modes.selected_mode = 'audio_mode'
					lpproscript._select_note_mode = lpproscript._original_select_note_mode
					lpproscript._select_note_mode()
				if 'mod_mode' in lpproscript._note_modes._mode_list:
					del lpproscript._note_modes._mode_list[lpproscript._note_modes._mode_list.index('mod_mode')]
				if 'mod_mode' in list(lpproscript._note_modes._mode_map.keys()):
					del lpproscript._note_modes._mode_map['mod_mode']
				lpproscript.modhandler.select_mod = nop
				if hasattr(lpproscript, '_original_disconnect'):
					lpproscript.disconnect = lpproscript._original_disconnect
				lpproscript._modified = False
			return _disconnect_mod
		lpproscript._disconnect_mod = make_lpproscript_disconnect_mod()

		lpproscript._original_disconnect = lpproscript.disconnect

		def make_lpproscript_disconnect():
			def disconnect():
				lpproscript.modhandler.select_mod = nop
				# modscript.schedule_message(1, modscript._device_provider.restart_mod)
				lpproscript.modhandler.disconnect()
				Launchpad_Pro.disconnect(lpproscript)
			return disconnect
		lpproscript.disconnect = make_lpproscript_disconnect()

		lpproscript._modified = True



class LaunchpadProModHandler(FrameworkModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'LaunchpadProModHandler'

	def __init__(self, register_component=None, *a, **k):
		self._color_type = 'LaunchpadPro'
		self._grid = None
		super(LaunchpadProModHandler, self).__init__(register_component = register_component, *a, **k)
		self.nav_box = self.register_component(FrameworkNavigationBox(parent=self,height=16,width=16,window_x=8,window_y=8,callback=self.set_offset,register_component = register_component, song = self._song))
		self.nav_box._on_off_values = ('Mixer.SoloOff', 'Mixer.ArmOn')
		self._launchmodColors = list(range(128))
		launchmod_colors = [3, 13, 37, 53, 5, 21, 49]
		self._launchmodColors[1:127] = [launchmod_colors[x%7] for x in range(126)]
		self._launchmodColors[127] = 49
		self._shifted = False


	def select_mod(self, mod):
		super(LaunchpadProModHandler, self).select_mod(mod)
		self._script._select_note_mode()
		self.update()
		debug('lppromodhandler select mod: ' + str(mod))

	def set_grid(self, grid):
		debug('set grid:' + str(grid))
		self._grid = grid
		self._grid_value.subject = grid
		if not self._grid is None:
			for button, _ in grid.iterbuttons():
				if not button == None:
					# debug('button:', button, 'suprress_forwarding?', button.suppress_script_forwarding )
					# button.use_default_message()
					# button.suppress_script_forwarding = False
					button.set_enabled(True)
		self.update()

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
			# if not self._grid_value.subject is None:
			# 	for button in self._grid_value.subject:
			# 		button.set_enabled(True)
		else:
			if not self._grid_value.subject is None:
				self._grid_value.subject.reset()
			if not self._keys_value.subject is None:
				self._keys_value.subject.reset()
