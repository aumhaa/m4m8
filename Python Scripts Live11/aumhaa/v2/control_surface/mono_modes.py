# by amounra 0216 : http://www.aumhaa.com

# from itertools import imap
from ableton.v2.control_surface.mode import *

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()


class SendSysexMode(Mode):


	def __init__(self, script = None, sysex = None, *a, **k):
		super(SendSysexMode, self).__init__(*a, **k)
		self._send_midi = script._send_midi
		self._sysex = sysex


	def enter_mode(self):
		self._send_midi and self._send_midi(self._sysex)


	def leave_mode(self):
		pass



class DisplayMessageMode(Mode):


	def __init__(self, script = None, message = None, *a, **k):
		super(DisplayMessageMode, self).__init__(*a, **k)
		self._show_message = script.show_message
		self._message = message


	def enter_mode(self):
		self._show_message and self._message and self._show_message(self._message)


	def leave_mode(self):
		pass



class SendLividSysexMode(Mode):


	def __init__(self, livid_settings = None, call = None, message = None, *a, **k):
		super(SendLividSysexMode, self).__init__(*a, **k)
		self._send = livid_settings.send if hasattr(livid_settings, 'send') else self.fallback_send
		self._call = call
		self._message = message


	def fallback_send(self, call = 'no call', message = 'no message', *a, **k):
		debug('sysex call made to invalid livid_settings object:', call, message)


	def enter_mode(self):
		self._send(self._call, self._message)


	def leave_mode(self):
		pass



class MomentaryBehaviour(ModeButtonBehaviour):


	def press_immediate(self, component, mode):
		debug('momentary press')
		component.push_mode(mode)


	def release_immediate(self, component, mode):
		debug('momentary release immediate')
		if len(component.active_modes) > 1:
			component.pop_mode(mode)


	def release_delayed(self, component, mode):
		debug('momentary release delayed')
		if len(component.active_modes) > 1:
			component.pop_mode(mode)



class BicoloredMomentaryBehaviour(MomentaryBehaviour):


	def __init__(self, color = 'DefaultButton.On', off_color = 'DefaultButton.Off', *a, **k):
		super(BicoloredMomentaryBehaviour, self).__init__(*a, **k)
		self._color = color
		self._off_color = off_color


	def update_button(self, component, mode, selected_mode):
		button = component.get_mode_button(mode)
		groups = component.get_mode_groups(mode)
		selected_groups = component.get_mode_groups(selected_mode)
		if mode == selected_mode:
			#button.set_light(self._color)
			button.mode_selected_color = self._color
		else:
			#button.set_light(self._off_color)
			button.mode_unselected_color = self._off_color



class ExcludingBehaviourMixin(ModeButtonBehaviour):


	def __init__(self, excluded_groups = set(), *a, **k):
		super(ExcludingBehaviourMixin, self).__init__(*a, **k)
		self._excluded_groups = set(excluded_groups)


	def is_excluded(self, component, selected):
		return bool(component.get_mode_groups(selected) & self._excluded_groups)


	def press_immediate(self, component, mode):
		if not self.is_excluded(component, component.selected_mode):
			super(ExcludingBehaviourMixin, self).press_immediate(component, mode)


	def release_delayed(self, component, mode):
		if not self.is_excluded(component, component.selected_mode):
			super(ExcludingBehaviourMixin, self).release_delayed(component, mode)


	def press_delayed(self, component, mode):
		if not self.is_excluded(component, component.selected_mode):
			super(ExcludingBehaviourMixin, self).press_delayed(component, mode)


	def release_immediate(self, component, mode):
		if not self.is_excluded(component, component.selected_mode):
			super(ExcludingBehaviourMixin, self).release_immediate(component, mode)


	def update_button(self, component, mode, selected_mode):
		component.get_mode_button(mode).enabled = not self.is_excluded(component, selected_mode)



class ExcludingMomentaryBehaviour(ExcludingBehaviourMixin, MomentaryBehaviour):


	def update_button(self, component, mode, selected_mode):
		pass



class DelayedExcludingMomentaryBehaviour(ExcludingMomentaryBehaviour):


	def press_immediate(self, component, mode):
		pass


	def press_delayed(self, component, mode):
		if not self.is_excluded(component, component.selected_mode):
			component.push_mode(mode)



class ShiftedBehaviour(ModeButtonBehaviour):


	def __init__(self, color = 1, *a, **k):
		super(ShiftedBehaviour, self).__init__(*a, **k)
		self._color = color
		self._chosen_mode = None


	def press_immediate(self, component, mode):
		if mode is component.selected_mode and not component.get_mode(mode+'_shifted') is None:
			self._chosen_mode = mode+'_shifted'
		else:
			self._chosen_mode = mode
		component.push_mode(self._chosen_mode)


	def release_immediate(self, component, mode):
		if component.selected_mode.endswith('_shifted'):
			component.pop_groups(['shifted'])
		elif len(component.active_modes) > 1:
			component.pop_unselected_modes()


	def release_delayed(self, component, mode):
		component.pop_mode(self._chosen_mode)


	def update_button(self, component, mode, selected_mode):
		if not mode.endswith('_shifted'):
			button = component.get_mode_button(mode)
			groups = component.get_mode_groups(mode)
			selected_groups = component.get_mode_groups(selected_mode)
			#debug('--------mode:', mode, 'selected:', selected_mode, 'chosen:', self._chosen_mode)
			if mode == selected_mode:
				button.mode_selected_color = self._color
			elif mode+'_shifted' == selected_mode:
				button.mode_unselected_color = self._color+'_shifted'
			else:
				button.mode_unselected_color = 'DefaultButton.Disabled'
			button.update()



class LatchingShiftedBehaviour(ShiftedBehaviour):


	def press_immediate(self, component, mode):
		if mode is component.selected_mode and component.get_mode(mode+'_shifted'):
			self._chosen_mode = mode+'_shifted'
		else:
			self._chosen_mode = mode
		component.push_mode(self._chosen_mode)


	def release_immediate(self, component, mode):
		if len(component.active_modes) > 1:
			component.pop_unselected_modes()


	def release_delayed(self, component, mode):
		if not mode is self._chosen_mode is mode + '_shifted':
			if len(component.active_modes) > 1:
				component.pop_mode(component.selected_mode)




class CancellableBehaviour(ModeButtonBehaviour):


	_previous_mode = None

	def press_immediate(self, component, mode):
		active_modes = component.active_modes
		groups = component.get_mode_groups(mode)
		can_cancel_mode = mode in active_modes or any(list([groups & component.get_mode_groups(other) for other in active_modes]))
		if can_cancel_mode:
			if groups:
				component.pop_groups(groups)
			else:
				component.pop_mode(mode)
			self.restore_previous_mode(component)
		else:
			self.remember_previous_mode(component)
			component.push_mode(mode)


	def remember_previous_mode(self, component):
		self._previous_mode = component.active_modes[0] if component.active_modes else None


	def restore_previous_mode(self, component):
		if len(component.active_modes) == 0 and self._previous_mode is not None:
			component.push_mode(self._previous_mode)



"""
class CancellableBehaviourWithRelease(CancellableBehaviour):


	def release_delayed(self, component, mode):
		component.pop_mode(mode)


"""
class CancellableBehaviourWithRelease(CancellableBehaviour):


	def release_delayed(self, component, mode):
		component.pop_mode(mode)


	def update_button(self, component, mode, selected_mode):
		button = component.get_mode_button(mode)
		groups = component.get_mode_groups(mode)
		selected_groups = component.get_mode_groups(selected_mode)
		value = (mode == selected_mode or bool(groups & selected_groups))*32 or 1
		#if mode == selected_mode:
		#	button.mode_selected_color = self.color
		#elif (groups & selected_groups):
		#	button.mode_unselected_color = self.color
		#else:
		#	button.mode_unselected_color = self.off_color
		button.mode_selected_color = value
		button.update()


class FlashingBehaviour(CancellableBehaviourWithRelease):


	def __init__(self, color = 1, *a, **k):
		super(FlashingBehaviour, self).__init__(*a, **k)
		self._color = color


	def update_button(self, component, mode, selected_mode):
		button = component.get_mode_button(mode)
		groups = component.get_mode_groups(mode)
		selected_groups = component.get_mode_groups(selected_mode)
		if mode == selected_mode or bool(groups & selected_groups):
			button.send_value(self._color + 7, True)
		else:
			button.send_value(self._color, True)



class ColoredCancellableBehaviourWithRelease(CancellableBehaviourWithRelease):


	def __init__(self, color = 'DefaultButton.On', off_color = 'DefaultButton.Off', *a, **k):
		super(ColoredCancellableBehaviourWithRelease, self).__init__(*a, **k)
		self._color = color
		self._off_color = off_color


	def update_button(self, component, mode, selected_mode):
		button = component.get_mode_button(mode)
		groups = component.get_mode_groups(mode)
		selected_groups = component.get_mode_groups(selected_mode)
		if mode == selected_mode:
			#button.set_light(self._color)
			button.mode_selected_color = self._color
		else:
			#button.set_light(self._off_color)
			button.mode_unselected_color = self._off_color
		button.update()



class DefaultedBehaviour(ColoredCancellableBehaviourWithRelease):


	def __init__(self, default_mode = 'disabled', *a, **k):
		super(DefaultedBehaviour, self).__init__(*a, **k)
		self._default_mode = default_mode


	def press_immediate(self, component, mode):
		if mode is component.selected_mode:
			mode = self._default_mode
		component.push_mode(mode)


	def release_immediate(self, component, mode):
		if len(component.active_modes) > 1:
			component.pop_unselected_modes()


	def release_delayed(self, component, mode):
		component.pop_mode(mode)
