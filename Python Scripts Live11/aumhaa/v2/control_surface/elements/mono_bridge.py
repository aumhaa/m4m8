# by amounra 0915 : http://www.aumhaa.com


import contextlib
from ableton.v2.base import Event, Signal, in_range
from ableton.v2.control_surface import NotifyingControlElement, InputSignal

from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()

def generate_strip_string(display_string):
	NUM_CHARS_PER_DISPLAY_STRIP = 12
	if (not display_string):
		return (' ' * NUM_CHARS_PER_DISPLAY_STRIP)
	else:
		display_string = str(display_string)
	if ((len(display_string.strip()) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)) and (display_string.endswith('dB') and (display_string.find('.') != -1))):
		display_string = display_string[:-2]
	if (len(display_string) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)):
		for um in [' ',
		 'i',
		 'o',
		 'u',
		 'e',
		 'a']:
			while ((len(display_string) > (NUM_CHARS_PER_DISPLAY_STRIP - 1)) and (display_string.rfind(um, 1) != -1)):
				um_pos = display_string.rfind(um, 1)
				display_string = (display_string[:um_pos] + display_string[(um_pos + 1):])
	else:
		display_string = display_string.center((NUM_CHARS_PER_DISPLAY_STRIP - 1))
	ret = ''
	for i in range((NUM_CHARS_PER_DISPLAY_STRIP - 1)):
		if ((ord(display_string[i]) > 127) or (ord(display_string[i]) < 0)):
			ret += ' '
		else:
			ret += display_string[i]
	ret += ' '
	ret = ret.replace(' ', '_')
	assert (len(ret) == NUM_CHARS_PER_DISPLAY_STRIP)
	return ret


class ModInputSignal(Signal):
	"""
	Special signal type that makes sure that interaction with input
	works properly. Special input control elements that define
	value-dependent properties should use this kind of signal.
	"""


	def __init__(self, sender = None, *a, **k):
		super(ModInputSignal, self).__init__(sender=sender, *a, **k)
		self._input_control = sender


	@contextlib.contextmanager
	def _listeners_update(self):
		old_count = self.count
		yield
		diff_count = self.count - old_count
		self._input_control._input_signal_listener_count += diff_count
		listener_count = self._input_control._input_signal_listener_count
		if diff_count > 0 and listener_count == diff_count or diff_count < 0 and listener_count == 0:
			self._input_control._request_rebuild()


	@contextlib.contextmanager
	def _listeners_update(self):
		try:
			control = self._input_control
			old_count = self.count
			old_wants_forwarding = control.script_wants_forwarding()
			yield
		finally:
			diff_count = self.count - old_count
			control._input_signal_listener_count += diff_count
			if old_wants_forwarding != control.script_wants_forwarding():
				self._input_control._request_rebuild()


	def connect(self, *a, **k):
		with self._listeners_update():
			super(ModInputSignal, self).connect(*a, **k)


	def disconnect(self, *a, **k):
		with self._listeners_update():
			super(ModInputSignal, self).disconnect(*a, **k)


	def disconnect_all(self, *a, **k):
		with self._listeners_update():
			super(ModInputSignal, self).disconnect_all(*a, **k)



class MonoBridgeElement(NotifyingControlElement):
	__module__ = __name__
	__doc__ = ' Class representing a 2-dimensional set of buttons '
	__subject_events__ = (Event(name='value', signal=InputSignal, override=True),)
	_input_signal_listener_count = 0



	def __init__(self, script, *a, **k):
		self._script = script
		super(MonoBridgeElement, self).__init__(*a, **k)


	def refresh_state(self, *a, **k):
		#self._script.schedule_message(2, self._script.update)
		#self._script.log_message('refresh_state')
		self._script.refresh_state()


	def _send(self, args1 = None, args2 = None, args3 = None, *a):
		self.notify_value(args1, args2, args3)


	def script_wants_forwarding(self):
		return True


	def reset(self):
		pass


	def notification_to_bridge(self, name = None, value = None, sender = None):
		if hasattr(sender, 'name'):
			#debug('has name:',  sender.name)
			self._send(sender.name, 'lcd_name', str(generate_strip_string(name)))
			self._send(sender.name, 'lcd_value', str(generate_strip_string(value)))
		else:
			#debug('missing name:',  sender, name)
			self._send(name, 'lcd_name', str(generate_strip_string(name)))
			self._send(name, 'lcd_value', str(generate_strip_string(value)))



class OSCMonoBridgeElement(MonoBridgeElement):


	def __init__(self, script, osc_display = None, *a, **k):
		self._osc_display = osc_display
		super(OSCMonoBridgeElement, self).__init__(script, *a, **k)
		#self._osc_display = k['osc_display'] if 'osc_display' in k else None


	def _send(self, args1 = None, args2 = None, args3 = None, args4 = None):
		super(OSCMonoBridgeElement, self)._send(args1, args2, args3, args4)
		self._osc_display and self._osc_display.sendOSC(str(args1 + '/' + args2), args3)



class MonoBridgeProxy(object):


	def __init__(self, *a, **k):
		super(MonoBridgeProxy, self).__init__()


	def notification_to_bridge(self, *a, **k):
		# debug('proxy bridge call:', a)
		pass


	def _send(self, *a, **k):
		debug('proxy send call:', a)
		#pass
