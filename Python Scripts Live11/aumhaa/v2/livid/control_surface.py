# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


import Live
import math
import sys

import logging
logger = logging.getLogger(__name__)

from ableton.v2.control_surface import midi
from ableton.v2.control_surface.profile import profile
from ableton.v2.control_surface.control_surface import *
from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, MIDI_SYSEX_TYPE

from aumhaa.v2.control_surface.elements import MonoButtonElement, MonoBridgeElement
from aumhaa.v2.livid.utilities import LividSettings
from aumhaa.v2.base.debug import initialize_debug

debug = initialize_debug()


class LividControlSurface(ControlSurface):


	_rgb = 0
	_color_type = 'OhmRGB'
	_timer = 0
	_touched = 0
	flash_status = 1
	_connected = False
	_sysex_id = 0
	_model_name = 'Livid Control Surface'
	_version_check = 'Mod_Disabled'

	def __init__(self, *a, **k):
		self.log_message = logger.info
		super(LividControlSurface, self).__init__(*a, **k)
		with self.component_guard():
			self._setup_monobridge()
			self._livid_settings = LividSettings(model = self._sysex_id, control_surface = self)
		self.schedule_message(1, self._open_log)
		#self._connection_routine = self._tasks.add(task.sequence(task.wait(10), task.run(self._check_connection)))
		#self._connection_routine.restart()
		self.schedule_message(2, self._check_connection)


	def _open_log(self):
		self.log_message("<<<<<<<<<<<<<<<<<<<<= " + str(self._model_name) + " " + str(self._version_check) + " log opened =>>>>>>>>>>>>>>>>>>>")
		self.show_message(str(self._model_name) + ' Control Surface Loaded')


	def _close_log(self):
		self.log_message("<<<<<<<<<<<<<<<<<<<<= " + str(self._model_name) + " " + str(self._version_check) + " log closed =>>>>>>>>>>>>>>>>>>>")


	def _setup_monobridge(self):
		self._monobridge = MonoBridgeElement(self)
		self._monobridge.name = 'MonoBridge'


	def port_settings_changed(self):
		debug('port settings changed!')
		self._connected = False
		self._check_connection()


	def _check_connection(self):
		if not self._connected:
			#debug(self._model_name, '_check_connection')
			self._livid_settings.query_surface()
			#self._connection_routine.restart()
			self.schedule_message(5, self._check_connection)


	def _initialize_hardware(self):
		debug(self._model_name, 'initialize_hardware()')


	def _initialize_script(self):
		self.refresh_state()
		debug(self._model_name, 'initialize_script()')


	def set_appointed_device(self, device):
		self.song.appointed_device = device


	def flash(self):
		if(self.flash_status > 0):
			for control in self.controls:
				if isinstance(control, MonoButtonElement):
					control.flash(self._timer)



	def update_display(self):
		super(LividControlSurface, self).update_display()
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



	def process_midi_bytes(self, midi_bytes, midi_processor):
		if midi.is_sysex(midi_bytes):
			result = self.get_registry_entry_for_sysex_midi_message(midi_bytes)
			if result is not None:
				identifier, recipient = result
				midi_processor(recipient, midi_bytes[len(identifier):-1])
			else:
				try:
					self.handle_sysex(midi_bytes)
				except:
					pass
		else:
			recipient = self.get_recipient_for_nonsysex_midi_message(midi_bytes)
			if recipient is not None:
				midi_processor(recipient, midi.extract_value(midi_bytes))
			else:
				logger.warning('Got unknown message: ' + midi.pretty_print_bytes(midi_bytes))


	def handle_sysex(self, midi_bytes):
		#debug('sysex: ', str(midi_bytes))
		#debug('matching:', midi_bytes[3:11], 'to', tuple([6, 2, 0, 1, 97, 1, 0]  + [self._sysex_id]))
		if midi_bytes[3:11] == tuple([6, 2, 0, 1, 97, 1, 0]  + [self._sysex_id]):
			if not self._connected:
				debug('connecting from sysex...')
				#self._connection_routine.kill()
				self._connected = True
				#self._livid_settings.set_model(midi_bytes[11])
				self._initialize_hardware()
				self._initialize_script()


	def disconnect(self):
		super(LividControlSurface, self).disconnect()
		self._close_log()
