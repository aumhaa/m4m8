
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
#from _Framework.ModeSelectorComponent import ModeSelectorComponent
from ableton.v2.control_surface.elements.button import ButtonElement
#from _Framework.ButtonElement import ButtonElement
from ableton.v2.control_surface.elements.button_matrix import ButtonMatrixElement
#from _Framework.ButtonMatrixElement import ButtonMatrixElement
from ableton.v2.control_surface.components.session import SessionComponent
from ableton.v2.base import task
#from _Framework.SessionComponent import SessionComponent
from ableton.v2.control_surface.defaults import *
from .SpecialMixerComponent import SpecialMixerComponent
from .PreciseButtonSliderElement import *
LED_OFF = 4
RED_FULL = 7
RED_HALF = 6
RED_THIRD = 5
RED_BLINK = 11
GREEN_FULL = 52
GREEN_HALF = 36
GREEN_THIRD = 20
GREEN_BLINK = 56
AMBER_FULL = RED_FULL + GREEN_FULL - 4
AMBER_HALF = RED_HALF + GREEN_HALF - 4
AMBER_THIRD = RED_THIRD + GREEN_THIRD - 4
AMBER_BLINK = AMBER_FULL - 4 + 8
PAN_VALUE_MAP = (-1.0, -0.634921, -0.31746, 0.0, 0.0, 0.31746, 0.634921, 1.0)
VOL_VALUE_MAP = (0.0, 0.142882, 0.302414, 0.4, 0.55, 0.7, 0.85, 1.0)
SEND_VALUE_MAP = (0.0, 0.103536, 0.164219, 0.238439, 0.343664, 0.55, 0.774942, 1.0)

from aumhaa.v2.base.debug import *
debug = initialize_debug()

class MomentaryModeObserver(object):
	u""" Listens to the changes of a given set of controls and decides which mode to use """

	def __init__(self):
		object.__init__(self)
		self._controls = None
		self._mode_callback = None
		self._reset()

	def disconnect(self):
		self._reset()

	def set_mode_details(self, base_mode, controls, mode_callback = None):
		assert isinstance(base_mode, int)
		assert isinstance(controls, (type(None), tuple))
		assert mode_callback == None or callable(mode_callback)
		self._reset()
		self._controls = controls if controls != None else []
		for control in self._controls:
			control.add_value_listener(self._control_changed)

		self._base_mode = base_mode
		self._mode_callback = mode_callback

	def is_mode_momentary(self):
		debug('is_mode_momentary:', 2, self._controls_changed or self._timer_count >= 2)
		return self._controls_changed or self._timer_count >= 2
		#return True

	def on_timer(self):
		self._timer_count += 1

	def _control_changed(self, value):
		debug('control_changed', value)
		if self._mode_callback == None or self._mode_callback() == self._base_mode:
			self._controls_changed = True
		debug('self._controls_changed:', self._controls_changed)

	def _release_controls(self):
		if self._controls != None:
			for control in self._controls:
				control.remove_value_listener(self._control_changed)

			self._controls = None

	def _reset(self):
		self._base_mode = -1
		self._controls_changed = False
		self._mode_callback = None
		self._timer_count = 0
		self._release_controls()


class ModeSelectorComponent(Component):
	u""" Class for switching between modes, handle several functions with few controls """

	def __init__(self, *a, **k):
		super(ModeSelectorComponent, self).__init__(*a, **k)
		self._modes_buttons = []
		self._mode_toggle = None
		self._mode_listeners = []
		self.__mode_index = -1
		self._modes_observers = {}
		self._modes_heap = []
		#self._task_group = task.TaskGroup(auto_kill=False)
		self._register_timer_callback(self._on_timer)

	def _get_protected_mode_index(self):
		return self.__mode_index

	def _set_protected_mode_index(self, mode):
		assert isinstance(mode, int)
		self.__mode_index = mode
		for listener in self._mode_listeners:
			listener()

	_mode_index = property(_get_protected_mode_index, _set_protected_mode_index)

	def _get_public_mode_index(self):
		return self.__mode_index

	def _set_public_mode_index(self, mode):
		assert False

	mode_index = property(_get_public_mode_index, _set_public_mode_index)

	def disconnect(self):
		self._clean_heap()
		if self._mode_toggle != None:
			self._mode_toggle.remove_value_listener(self._toggle_value)
			self._mode_toggle = None
		self._modes_buttons = None
		self._mode_listeners = None
		super(ModeSelectorComponent, self).disconnect()

	def on_enabled_changed(self):
		self.update()

	def set_mode_toggle(self, button):
		assert (button == None or isinstance(button, ButtonElement))
		if self._mode_toggle != None:
			self._mode_toggle.remove_value_listener(self._toggle_value)
		self._mode_toggle = button
		self._mode_toggle != None and self._mode_toggle.add_value_listener(self._toggle_value)
		self.set_mode(0)

	def set_mode_buttons(self, buttons):
		assert buttons != None
		assert isinstance(buttons, tuple)
		assert len(buttons) - 1 in range(16)
		for button in buttons:
			assert isinstance(button, ButtonElement)
			identify_sender = True
			button.add_value_listener(self._mode_value, identify_sender)
			self._modes_buttons.append(button)

		self.set_mode(0)

	def set_mode(self, mode):
		debug(self.name, '-----------------set_mode:', mode)
		self._clean_heap()
		self._modes_heap = [(mode, None, None)]
		if self._mode_index != mode:
			self._update_mode()

	def _update_mode(self):
		debug(self.name, '_____________________update_mode:', self._modes_heap)
		mode = self._modes_heap[-1][0]
		assert mode in range(self.number_of_modes())
		self._mode_index = self._mode_index if self._mode_index != mode else mode
		self.update()

	def _clean_heap(self):
		debug(self.name, '______________________clean_heap:', self._modes_heap)
		for _, _, observer in self._modes_heap:
			if observer != None:
				observer.disconnect()

		self._modes_heap = []

	def number_of_modes(self):
		raise NotImplementedError

	def mode_index_has_listener(self, listener):
		return listener in self._mode_listeners

	def add_mode_index_listener(self, listener):
		assert listener not in self._mode_listeners
		self._mode_listeners.append(listener)

	def remove_mode_index_listener(self, listener):
		assert listener in self._mode_listeners
		self._mode_listeners.remove(listener)

	def _mode_value(self, value, sender):
		assert len(self._modes_buttons) > 0
		assert isinstance(value, int)
		assert sender in self._modes_buttons
		new_mode = self._modes_buttons.index(sender)
		if sender.is_momentary():
			if value > 0:
				mode_observer = MomentaryModeObserver()
				mode_observer.set_mode_details(new_mode, self._controls_for_mode(new_mode), self._get_public_mode_index)
				self._modes_heap.append((new_mode, sender, mode_observer))
				self._update_mode()
			elif self._modes_heap[-1][1] == sender and not self._modes_heap[-1][2].is_mode_momentary():
				self.set_mode(new_mode)
			else:
				for mode, button, observer in self._modes_heap:
					if button == sender:
						self._modes_heap.remove((mode, button, observer))
						break

				self._update_mode()
		else:
			self.set_mode(new_mode)

	def _toggle_value(self, value):
		assert self._mode_toggle != None
		assert isinstance(value, int)
		(value is not 0 or not self._mode_toggle.is_momentary()) and self.set_mode((self._mode_index + 1) % self.number_of_modes())

	def _controls_for_mode(self, mode):
		return None

	def _on_timer(self):
		for _, _, mode_observer in self._modes_heap:
			if mode_observer != None:
				mode_observer.on_timer()
	



class SubSelectorComponent(ModeSelectorComponent):
	u""" Class that handles different mixer modes """

	def __init__(self, matrix, side_buttons, session):
		assert isinstance(matrix, ButtonMatrixElement)
		assert matrix.width() == 8 and matrix.height() == 8
		assert isinstance(side_buttons, tuple)
		assert len(side_buttons) == 8
		assert isinstance(session, SessionComponent)
		ModeSelectorComponent.__init__(self)
		self._session = session
		self._mixer = SpecialMixerComponent(self._session._session_ring)
		self._matrix = matrix
		self._sliders = []
		self._mixer.name = u'Mixer'
		self._mixer.master_strip().name = u'Master_Channel_strip'
		self._mixer.selected_strip().name = u'Selected_Channel_strip'
		for column in range(matrix.width()):
			self._mixer.channel_strip(column).name = u'Channel_Strip_' + str(column)
			self._sliders.append(PreciseButtonSliderElement(buttons = tuple([ matrix._orig_buttons[column][7 - row] for row in range(8) ])))
			self._sliders[-1].name = u'Button_Slider_' + str(column)

		self._side_buttons = side_buttons[4:]
		self._update_callback = None
		#self._session.set_mixer(self._mixer)
		self.set_modes_buttons(side_buttons[:4])

	def disconnect(self):
		for button in self._modes_buttons:
			button.remove_value_listener(self._mode_value)

		self._session = None
		self._mixer = None
		for slider in self._sliders:
			slider.release_parameter()
			slider.set_disabled(True)

		self._sliders = None
		self._matrix = None
		self._side_buttons = None
		self._update_callback = None
		ModeSelectorComponent.disconnect(self)

	def set_update_callback(self, callback):
		assert dir(callback).count(u'im_func') is 1
		self._update_callback = callback

	def set_modes_buttons(self, buttons):
		assert buttons == None or isinstance(buttons, tuple) or len(buttons) == self.number_of_modes()
		identify_sender = True
		for button in self._modes_buttons:
			button.remove_value_listener(self._mode_value)

		self._modes_buttons = []
		if buttons != None:
			for button in buttons:
				assert isinstance(button, ButtonElement)
				self._modes_buttons.append(button)
				button.add_value_listener(self._mode_value, identify_sender)

	def set_mode(self, mode):
		assert isinstance(mode, int)
		assert mode in range(-1, self.number_of_modes())
		self._mode_index = (self._mode_index != mode or mode == -1) and mode
		self.update()

	def mode(self):
		result = 0
		if self.is_enabled():
			result = self._mode_index + 1
		return result

	def number_of_modes(self):
		return 4

	def on_enabled_changed(self):
		enabled = self.is_enabled()
		for index in range(self._matrix.width()):
			self._sliders[index].set_disabled(not enabled)

		self._mixer.set_enabled(enabled)
		self.set_mode(-1)

	def release_controls(self):
		for track in range(self._matrix.width()):
			#for row in range(self._matrix.height()):
			#	self._matrix.get_button(track, row).set_on_off_values(127, LED_OFF)

			strip = self._mixer.channel_strip(track)
			strip.set_default_buttons(None, None, None, None)
			strip.set_mute_button(None)
			strip.set_solo_button(None)
			strip.set_arm_button(None)
			strip.set_send_controls((None, None))
			strip.set_pan_control(None)
			strip.set_volume_control(None)

		self._session.set_stop_track_clip_buttons(None)
		self._mixer.set_global_buttons(None, None, None)
		self._session.set_stop_all_clips_button(None)

	def update(self):
		super(SubSelectorComponent, self).update()
		if not self._modes_buttons != None:
			debug('SubSelectorComponent.update:', self.is_enabled(), self._mode_index)
			if self.is_enabled():
				if self._modes_buttons != None:
					for index in range(len(self._modes_buttons)):
						self._modes_buttons[index].set_on_off_values(GREEN_FULL, GREEN_THIRD)
						if index == self._mode_index:
							self._modes_buttons[index].turn_on()
						else:
							self._modes_buttons[index].turn_off()

				for button in self._side_buttons:
					button.set_on_off_values(127, LED_OFF)
					button.turn_off()

				for index in range(self._matrix.width()):
					self._sliders[index].set_disabled(self._mode_index == -1)

				self._mixer.set_allow_update(False)
				self._session.set_allow_update(False)
				if self._mode_index == -1:
					self._setup_mixer_overview()
				elif self._mode_index == 0:
					self._setup_volume_mode()
				elif self._mode_index == 1:
					self._setup_pan_mode()
				elif self._mode_index == 2:
					self._setup_send1_mode()
				elif self._mode_index == 3:
					self._setup_send2_mode()
				else:
					raise False or AssertionError
				self._update_callback != None and self._update_callback()
			self._mixer.set_allow_update(True)
			self._session.set_allow_update(True)
		else:
			self.release_controls()

	def _setup_mixer_overview(self):
		trkon_index = 5
		stop_buttons = []
		for track in range(self._matrix.width()):
			strip = self._mixer.channel_strip(track)
			strip.set_send_controls((None, None))
			strip.set_pan_control(None)
			strip.set_volume_control(None)
			self._sliders[track].release_parameter()
			for row in range(self._matrix.height()):
				full_value = GREEN_THIRD
				third_value = GREEN_FULL
				if row == trkon_index:
					full_value = AMBER_FULL
					third_value = AMBER_THIRD
				elif row > 3:
					full_value = RED_FULL
					third_value = RED_THIRD
				self._matrix.get_button(track, row).set_on_off_values(full_value, third_value)

			strip.set_default_buttons(self._matrix.get_button(track, 0), self._matrix.get_button(track, 1), self._matrix.get_button(track, 2), self._matrix.get_button(track, 3))
			stop_buttons.append(self._matrix.get_button(track, 4))
			strip.set_mute_button(self._matrix.get_button(track, 5))
			strip.set_solo_button(self._matrix.get_button(track, 6))
			strip.set_arm_button(self._matrix.get_button(track, 7))

		for button in self._side_buttons:
			if list(self._side_buttons).index(button) == trkon_index - 4:
				button.set_on_off_values(AMBER_FULL, AMBER_THIRD)
			else:
				button.set_on_off_values(RED_FULL, RED_THIRD)
			button.set_force_next_value()
			button.turn_off()

		self._session.set_stop_track_clip_buttons(tuple(stop_buttons))
		self._session.set_stop_all_clips_button(self._side_buttons[0])
		self._mixer.set_global_buttons(self._side_buttons[3], self._side_buttons[2], self._side_buttons[1])

	def _setup_volume_mode(self):
		for track in range(self._matrix.width()):
			strip = self._mixer.channel_strip(track)
			strip.set_default_buttons(None, None, None, None)
			strip.set_mute_button(None)
			strip.set_solo_button(None)
			strip.set_arm_button(None)
			strip.set_send_controls((None, None))
			strip.set_pan_control(None)
			for row in range(self._matrix.height()):
				self._matrix.get_button(track, row).set_on_off_values(GREEN_FULL, LED_OFF)

			self._sliders[track].set_mode(SLIDER_MODE_VOLUME)
			self._sliders[track].set_value_map(VOL_VALUE_MAP)
			strip.set_volume_control(self._sliders[track])

		self._session.set_stop_track_clip_buttons(None)
		self._session.set_stop_all_clips_button(None)
		self._mixer.set_global_buttons(None, None, None)

	def _setup_pan_mode(self):
		for track in range(self._matrix.width()):
			strip = self._mixer.channel_strip(track)
			strip.set_default_buttons(None, None, None, None)
			strip.set_mute_button(None)
			strip.set_solo_button(None)
			strip.set_arm_button(None)
			strip.set_send_controls((None, None))
			strip.set_volume_control(None)
			for row in range(self._matrix.height()):
				self._matrix.get_button(track, row).set_on_off_values(AMBER_FULL, LED_OFF)

			self._sliders[track].set_mode(SLIDER_MODE_PAN)
			self._sliders[track].set_value_map(PAN_VALUE_MAP)
			strip.set_pan_control(self._sliders[track])

		self._session.set_stop_track_clip_buttons(None)
		self._session.set_stop_all_clips_button(None)
		self._mixer.set_global_buttons(None, None, None)

	def _setup_send1_mode(self):
		for track in range(self._matrix.width()):
			strip = self._mixer.channel_strip(track)
			strip.set_default_buttons(None, None, None, None)
			strip.set_mute_button(None)
			strip.set_solo_button(None)
			strip.set_arm_button(None)
			strip.set_volume_control(None)
			strip.set_pan_control(None)
			for row in range(self._matrix.height()):
				self._matrix.get_button(track, row).set_on_off_values(RED_FULL, LED_OFF)

			self._sliders[track].set_mode(SLIDER_MODE_VOLUME)
			self._sliders[track].set_value_map(SEND_VALUE_MAP)
			strip.set_send_controls((self._sliders[track], None))

		self._session.set_stop_track_clip_buttons(None)
		self._session.set_stop_all_clips_button(None)
		self._mixer.set_global_buttons(None, None, None)

	def _setup_send2_mode(self):
		for track in range(self._matrix.width()):
			strip = self._mixer.channel_strip(track)
			strip.set_default_buttons(None, None, None, None)
			strip.set_mute_button(None)
			strip.set_solo_button(None)
			strip.set_arm_button(None)
			strip.set_volume_control(None)
			strip.set_pan_control(None)
			for row in range(self._matrix.height()):
				self._matrix.get_button(track, row).set_on_off_values(RED_FULL, LED_OFF)

			self._sliders[track].set_mode(SLIDER_MODE_VOLUME)
			self._sliders[track].set_value_map(SEND_VALUE_MAP)
			strip.set_send_controls((None, self._sliders[track]))

		self._session.set_stop_track_clip_buttons(None)
		self._session.set_stop_all_clips_button(None)
		self._mixer.set_global_buttons(None, None, None)