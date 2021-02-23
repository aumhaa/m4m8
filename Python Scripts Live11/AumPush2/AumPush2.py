# by amounra 1016 : http://www.aumhaa.com
# written against Live 10.0.4 100918


import Live
import Live.DrumPad
import logging
logger = logging.getLogger(__name__)

from contextlib import contextmanager
from functools import partial
from itertools import chain
import re

from ableton.v2.base import task, inject, clamp, nop, const, NamedTuple, listens, listens_group, find_if, mixin, forward_property, first, NamedTuple, in_range, flatten, liveobj_valid
from ableton.v2.control_surface import defaults, Component, BackgroundLayer, ClipCreator, ControlSurface, DeviceBankRegistry, Layer, midi, PrioritizedResource
from ableton.v2.control_surface.components import MixerComponent, TransportComponent, DeviceComponent
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.control_surface.elements import DisplayDataSource, adjust_string, ButtonElement, ButtonMatrixElement, ComboElement, DoublePressElement, DoublePressContext, MultiElement, OptionalElement, to_midi_value
from ableton.v2.control_surface.mode import CompoundMode, AddLayerMode, ReenterBehaviour, ModesComponent, SetAttributeMode, DelayMode
from ableton.v2.control_surface.input_control_element import ParameterSlot
from ableton.v2.control_surface.elements import ButtonElement

from Push2.push2 import Push2
from pushbase.value_component import ValueComponent
#from pushbase.configurable_button_element import ConfigurableButtonElement
from pushbase.device_chain_utils import is_simpler
from pushbase.touch_strip_element import TouchStripElement
from pushbase.touch_strip_controller import TouchStripControllerComponent, TouchStripEncoderConnection, TouchStripModes
from pushbase.control_element_factory import create_button
from pushbase.matrix_maps import *
from pushbase.consts import *

from Push2.routing import RoutingControlComponent, TrackOrRoutingControlChooserComponent
from Push2.browser_component import BrowserComponent
from Push2.actions import *
from Push2.device_component_provider import DeviceComponentProvider, DeviceComponentProvider as DeviceComponentBase
from Push2.mixer_control_component import MixerControlComponent
from Push2.track_mixer_control_component import TrackMixerControlComponent as TrackMixerControlComponentBase

from aumhaa.v2.control_surface.components import DeviceSelectorComponent, ResetSendsComponent
from aumhaa.v2.control_surface.elements.mono_encoder import MonoEncoderElement
from aumhaa.v2.control_surface.mod_devices import *
from aumhaa.v2.control_surface.components.mono_instrument import *
from aumhaa.v2.base.debug import *
from aumhaa.v2.control_surface.mod import *
from aumhaa.v2.control_surface.components.tagged_defaults import *
from .colors import make_default_skin
from .Map import *
from .ModDevices import *

debug = initialize_debug()


####post 9.5

def tracks_to_use_from_song(song):
	return tuple(song.visible_tracks) + tuple(song.return_tracks)



class CancellableBehaviourWithRelease(CancellableBehaviour):


	def press_immediate(self, component, mode):
		active_modes = component.active_modes
		groups = component.get_mode_groups(mode)
		if mode in active_modes:
			"""can_cancel_mode = any(imap(lambda other: groups & component.get_mode_groups(other), active_modes))
			debug('mode not in active_modes', can_cancel_mode)
			if can_cancel_mode:
				groups and component.pop_groups(groups)
			else:"""
			component.pop_mode(mode)
			self.restore_previous_mode(component)
		else:
			debug('mode in active_modes')
			self.remember_previous_mode(component)
			component.push_mode(mode)


	def release_delayed(self, component, mode):
		if len(component.active_modes) > 1:
			component.pop_mode(mode)



class AumPushResetSendsComponent(ResetSendsComponent):


	def __init__(self, *a, **k):
		super(AumPushResetSendsComponent, self).__init__(*a, **k)
		self._buttons = []


	def set_buttons(self, buttons):
		self._buttons = buttons
		self._on_button_value.replace_subjects(buttons)
		#debug('send reset, set buttons:', buttons)
		if buttons:
			for button in buttons:
				button and button.set_light('ResetSendsColor')


	def set_send_a_button(self, button):
		self._on_send_a_button_value.subject = button
		button and button.send_value(1)


	def set_send_b_button(self, button):
		self._on_send_b_button_value.subject = button
		button and button.send_value(1)


	def set_send_c_button(self, button):
		self._on_send_c_button_value.subject = button
		button and button.send_value(1)


	def set_send_d_button(self, button):
		self._on_send_d_button_value.subject = button
		button and button.send_value(1)


	@listens('value')
	def _on_send_a_button_value(self, value):
		value and self.reset_send(0)


	@listens('value')
	def _on_send_b_button_value(self, value):
		value and self.reset_send(1)


	@listens('value')
	def _on_send_c_button_value(self, value):
		value and self.reset_send(2)


	@listens('value')
	def _on_send_d_button_value(self, value):
		value and self.reset_send(3)



class TrollMixerControlComponent(TrackMixerControlComponentBase):


	def __init__(self, script = None, troll_submodes = None, *a, **k):
		self._script = script
		self._troll_submodes = troll_submodes
		self._main_offset = 0
		self._troll_offset = 1
		self._mode_on_troll_entrance = 'global'
		super(TrollMixerControlComponent, self).__init__(*a, **k)
		self._on_troll_submode_changed.subject = self._troll_submodes


	def find_inputs(self):
		found_device = None
		tracks = self.song.tracks
		for track in tracks:
			if track.name == 'Inputs':
				for device in track.devices:
					if bool(device.can_have_chains) and device.name.endswith('Inputs'):
						found_device = device
		return found_device


	def find_perc_crossfader(self):
		found_parameter = None
		tracks = self.song.tracks
		for track in tracks:
			if track.name == 'Perc':
				for device in track.devices:
					if bool(device.can_have_chains) and device.name == 'Perc':
						for parameter in device.parameters:
							if parameter.name == 'XFade':
								found_parameter = parameter
		return found_parameter


	def _troll_mode(self):
		val = False
		if hasattr(self._script, '_troll_modes'):
			val = self._script._troll_modes.selected_mode is 'enabled'
		#debug('mixer._troll_mode():', val)
		return val


	def _get_track_mixer_parameters(self):
		if self._troll_mode():
			if self._troll_submodes.selected_mode == 'Strip':
				mixer_params = []
				if self._tracks_provider.selected_item:
					mixer = self._tracks_provider.selected_item.mixer_device
					rets = list(self.song.return_tracks)[:4]
					returns = [ret.mixer_device.volume for ret in rets]
					mixer_params = [mixer.volume] + list(mixer.sends[:4]) + returns[:4]
				return mixer_params
			elif self._troll_submodes.selected_mode == 'FX1':
				mixer_params = []
				if self._tracks_provider.selected_item:
					if len(self.song.return_tracks) and len(self.song.return_tracks[0].devices):
						mixer_params = [None] + list(self.song.return_tracks[0].devices[0].parameters[1:9])
			elif self._troll_submodes.selected_mode == 'FX2':
				mixer_params = []
				if self._tracks_provider.selected_item:
					if len(self.song.return_tracks)>1 and len(self.song.return_tracks[0].devices):
						mixer_params = [None] + list(self.song.return_tracks[1].devices[0].parameters[1:9])
			elif self._troll_submodes.selected_mode == 'Inputs':
				mixer_params = [None]
				if self._tracks_provider.selected_item:
					inputs = self.find_inputs()
					if inputs:
						mixer_params += list(inputs.parameters[1:5])
					returns = self.song.return_tracks
					if len(returns) >= 2:
						mixer_params += [returns[0].mixer_device.sends[1], returns[1].mixer_device.sends[0]]
					mixer_params += [self.find_perc_crossfader()]
			return mixer_params
		else:
			return TrackMixerControlComponentBase._get_track_mixer_parameters(self)


	def _update_scroll_buttons(self):
		if self.is_enabled():
			if self._troll_mode():
				num_return_tracks = self._number_sends()
				self.scroll_right_button.enabled = self._number_sends() and self._scroll_offset < 2
				self.scroll_left_button.enabled = self._scroll_offset > 0
				self._update_view_slots()
			else:
				return TrackMixerControlComponentBase._update_scroll_buttons(self)


	def _update_scroll_offset(self):
		if self._troll_mode():
			new_number_return_tracks = self._number_sends()
			self._update_controls()
			self._update_scroll_buttons()
			self._number_return_tracks = new_number_return_tracks
		else:
			return TrackMixerControlComponentBase._update_scroll_offset(self)


	def _scroll_controls(self, delta):
		if self._troll_mode():
			num_return_tracks = self._number_sends()
			self._scroll_offset = clamp(self._scroll_offset + delta, 0, 2)
			self.notify_scroll_offset()
			self._update_controls()
			self._update_scroll_buttons()
		else:
			return TrackMixerControlComponentBase._scroll_controls(self, delta)


	@listens('selected_mode')
	def _on_troll_submode_changed(self, mode):
		#debug('_on_troll_submode_changed:', mode)
		self._update_controls()



class AumPush2DeviceComponent(DeviceComponentBase):


	def __init__(self, script = None, *a, **k):
		self._script = script
		self._alt_pressed = False
		super(AumPush2DeviceComponent, self).__init__(*a, **k)


	#our new device_proxy messes up realtimedata, its looking for an actual LiveDeviceObject in C code.  We need to tell the realtimechannel where our ACTUAL device is.
	def _set_device(self, device):
		super(AumPush2DeviceComponent, self)._set_device(device)
		if hasattr(device, '_mod_device'):
			device = device._mod_device
			self._playhead_real_time_data.set_data(device)
			self._waveform_real_time_data.set_data(device)
			self.notify_options()



class AumPush2DeviceProvider(ModDeviceProvider):


	allow_update_callback = const(True)

	def update_device_selection(self):
		if self.allow_update_callback():
			super(AumPush2DeviceProvider, self).update_device_selection()



"""A bug in original implemenation prevents touchstrip from releasing parameter correctly so we have to delay it"""
class AumPushCrossfader(Component):


	def __init__(self, strip_controller, task_group, *a, **k):
		super(AumPushCrossfader, self).__init__(*a, **k)
		self._strip_controller = strip_controller
		self._task_group = task_group


	def update(self):
		if self.is_enabled():
			self._strip_controller.set_parameter(self.song.master_track.mixer_device.crossfader)
			self._strip_controller.set_enabled(True)
		else:
			self._strip_controller.set_parameter(None)
			self._task_group.add(sequence(delay(1), self.delayed_disable))


	def delayed_disable(self, *a, **k):
		self._strip_controller.set_enabled(False)



class AumPush2(Push2):


	device_component_class = AumPush2DeviceComponent
	device_provider_class = ModDeviceProvider

	def __init__(self, c_instance, model):
		self._monomod_version = 'b996'
		self._cntrlr_version = 'b996'
		self._host_name = 'AumPush2'
		self._color_type = 'Push'
		self._auto_arm_calls = 0
		self.log_message = logger.warning
		super(AumPush2, self).__init__(c_instance, model)
		with self.component_guard():
			self._hack_stuff()
		#self._on_selected_track_changed.subject = self.song.view
		#self._on_main_mode_changed.subject = self._main_modes
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<< AumPush2 ' + str(self._monomod_version) + ' log opened >>>>>>>>>>>>>>>>>>>>>>>>')


	def _create_components(self):
		self._remove_pedal()
		super(AumPush2, self)._create_components()


	def _create_skin(self):
		return self.register_disconnectable(make_default_skin())


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
		with inject(register_component = const(self._register_component), song = const(self.song)).everywhere():
			self.modhandler = PushModHandler(self) ## song = self.song, register_component = self._register_component)
		self.modhandler.name = 'ModHandler'
		self.modhandler.layer = Layer( priority = 6, lock_button = self.elements.note_mode_button, grid = self.elements.matrix,
																			nav_up_button = self.elements.octave_up_button,
																			nav_down_button = self.elements.octave_down_button,
																			nav_left_button = self.elements.in_button,
																			nav_right_button = self.elements.out_button,
																			key_buttons = self.elements.side_buttons,
																			)
		self.modhandler.alt_shift_layer = AddLayerMode( self.modhandler, Layer(Shift_button = self.elements.shift_button,
																			Alt_button = self.elements.select_button))
		self.modhandler.legacy_shift_layer = AddLayerMode( self.modhandler, Layer(priority = 7,
																			device_selector_matrix = self.elements.matrix.submatrix[:, :1],
																			channel_buttons = self.elements.matrix.submatrix[:, 1:2],
																			nav_matrix = self.elements.matrix.submatrix[4:8, 2:6],
																			))
		self.modhandler.shift_layer = AddLayerMode( self.modhandler, Layer( priority = 7,
																			device_selector_matrix = self.elements.matrix.submatrix[:, :1],
																			))
																			#lock_button = self.elements.master_select_button,
																			#))
		self.modhandler.alt_layer = AddLayerMode( self.modhandler, Layer( priority = 7,
																			))
																			#key_buttons = self.elements.select_buttons))
																			#key_buttons = self.elements.track_state_buttons))
		self._device_provider.restart_mod()


	def _init_matrix_modes(self):
		super(AumPush2, self)._init_matrix_modes()
		#self._setup_monoinstrument()
		self._setup_mod()
		self._note_modes.add_mode('mod', [self.modhandler, self.modhandler.alt_shift_layer, DelayMode(delay = .1, mode = self.modhandler.nav_update)])
		self._note_modes.add_mode('looperhack', [self._audio_loop])


	"""
	def _create_device_component(self):
		return self.device_component_class(script = self, device_decorator_factory=self._device_decorator_factory, device_bank_registry=self._device_bank_registry, banking_info=self._banking_info, name='DeviceComponent', is_enabled=True, is_root=True)

	"""


	def _create_device_component(self):
		device_component_layer = Layer(parameter_touch_buttons=ButtonMatrixElement(rows=[self.elements.global_param_touch_buttons_raw]), shift_button='shift_button')
		return DeviceComponentProvider(device_component_layer=device_component_layer, device_decorator_factory=self._device_decorator_factory, device_bank_registry=self._device_bank_registry, banking_info=self._banking_info, name='DeviceComponent', is_enabled=False, delete_button=self.elements.delete_button)


	def _create_main_mixer_modes(self):

		self._mixer_control = MixerControlComponent(name='Global_Mix_Component', view_model=self._model.mixerView, tracks_provider=self._session_ring, is_enabled=False, layer=Layer(controls='fine_grain_param_controls', volume_button='track_state_buttons_raw[0]', panning_button='track_state_buttons_raw[1]', send_slot_one_button='track_state_buttons_raw[2]', send_slot_two_button='track_state_buttons_raw[3]', send_slot_three_button='track_state_buttons_raw[4]', send_slot_four_button='track_state_buttons_raw[5]', send_slot_five_button='track_state_buttons_raw[6]', cycle_sends_button='track_state_buttons_raw[7]'))
		self._model.mixerView.realtimeMeterData = self._mixer_control.real_time_meter_handlers
		track_mixer_control = TrollMixerControlComponent(script = self, troll_submodes = self._troll_submodes, name='Track_Mix_Component', is_enabled=False, tracks_provider=self._session_ring, layer=Layer(controls='fine_grain_param_controls', scroll_left_button='track_state_buttons_raw[6]', scroll_right_button='track_state_buttons_raw[7]'))
		self._track_mixer_control = track_mixer_control
		#track_mixer_control = TrackMixerControlComponent(name='Track_Mix_Component', is_enabled=False, tracks_provider=self._session_ring, layer=Layer(controls='fine_grain_param_controls', scroll_left_button='track_state_buttons_raw[6]', scroll_right_button='track_state_buttons_raw[7]'))
		routing_control = RoutingControlComponent(is_enabled=False, layer=Layer(monitor_state_encoder='parameter_controls_raw[0]'))
		track_mix_or_routing_chooser = TrackOrRoutingControlChooserComponent(tracks_provider=self._session_ring, track_mixer_component=track_mixer_control, routing_control_component=routing_control, is_enabled=False, layer=Layer(mix_button='track_state_buttons_raw[0]', routing_button='track_state_buttons_raw[1]'))
		self._model.mixerView.trackControlView = track_mix_or_routing_chooser
		self._mix_modes = ModesComponent(is_enabled=False)
		self._mix_modes.add_mode('global', self._mixer_control)
		self._mix_modes.add_mode('track', track_mix_or_routing_chooser)
		self._mix_modes.selected_mode = 'global'
		self._model.mixerSelectView = self._mixer_control
		self._model.trackMixerSelectView = track_mixer_control

		class MixModeBehaviour(ReenterBehaviour):

			def press_immediate(behaviour_self, component, mode):
				if self._is_on_master() and self._mix_modes.selected_mode != 'track':
					self._mix_modes.selected_mode = 'track'
				super(MixModeBehaviour, behaviour_self).press_immediate(component, mode)


			def on_reenter(behaviour_self):
				if not self._is_on_master():
					self._mix_modes.cycle_mode()




		self._main_modes.add_mode('mix', [self._mix_modes, SetAttributeMode(obj=self._note_editor_settings_component, attribute='parameter_provider', value=self._track_parameter_provider)], behaviour=MixModeBehaviour())


	def _with_select(self, button):
		return ComboElement(button, [self.elements.select_button])


	def _hack_stuff(self):
		crossfader_strip = TouchStripControllerComponent()
		crossfader_strip.layer = Layer(touch_strip = self.elements.touch_strip_control)
		crossfader_strip.set_enabled(False)
		self._crossfader_control = AumPushCrossfader(strip_controller = crossfader_strip, task_group = self._task_group)
		self._crossfader_control.set_enabled(False)

		self._device_selector = DeviceSelectorComponent(self)
		self._device_selector._off_value = 64
		self._device_selector.layer = Layer(priority = 9, matrix = self.elements.matrix.submatrix[:, :4])
		self._device_selector.set_enabled(False)

		self._send_reset = AumPushResetSendsComponent(self)
		self._send_reset.layer = Layer(priority = 9, send_a_button = self._with_select(self.elements.track_state_buttons_raw[4]), send_b_button = self._with_select(self.elements.track_state_buttons_raw[5]), send_c_button = self._with_select(self.elements.track_state_buttons_raw[6]), send_d_button = self._with_select(self.elements.track_state_buttons_raw[7]))
		self._send_reset.set_enabled(False)

		self._tagged_defaults = TaggedDefaultsComponent(self)
		self._tagged_defaults.layer = Layer(priority = 9, reset_button = 'side_buttons_raw[7]')
		self._tagged_defaults.set_enabled(False)

		self._troll_submodes = ModesComponent()
		self._troll_submodes.add_mode('Strip', [])
		self._troll_submodes.add_mode('FX1', [])
		self._troll_submodes.add_mode('FX2', [])
		self._troll_submodes.add_mode('Inputs', [])
		self._troll_submodes.layer = Layer(priority = 8, Strip_button = 'side_buttons_raw[0]', FX1_button = 'side_buttons_raw[1]', FX2_button = 'side_buttons_raw[2]', Inputs_button = 'side_buttons_raw[3]')
		self._troll_submodes.selected_mode = 'Strip'
		self._troll_submodes.set_enabled(False)

		static_modes = CompoundMode(self._crossfader_control, self._device_selector, self._send_reset, self._troll_submodes, self._tagged_defaults)

		self._troll_modes = ModesComponent()
		self._troll_modes.add_mode('disabled', [], cycle_mode_button_color = 'DefaultButton.Off')
		self._troll_modes.add_mode('enabled', [static_modes, tuple([self._grab_track_mode, self._release_track_mode, ])], cycle_mode_button_color = 'DefaultButton.Alert')
		self._troll_modes.layer = Layer(cycle_mode_button = 'master_select_button')
		self._troll_modes.selected_mode = 'disabled'


	@listens('selected_mode')
	def _on_main_mode_changed(self, mode):
		debug('main_mode selected mode is now:', mode)
		#if self._troll_modes.selected_mode is 'enabled' and not mode is 'device':
		#	self._troll_modes.selected_mode = 'disabled'


	def _init_main_modes(self):
		super(AumPush2, self)._init_main_modes()
		self._on_main_mode_changed.subject = self._main_modes


	def _grab_track_mode(self):
		debug('grab device mode')
		"""self._main_modes.pop_unselected_modes()
		if not self._main_modes.selected_mode is 'device':
			self._main_modes.push_mode('device')
		self._device_component._update_parameters()"""

		self._track_mixer_control._mode_on_troll_entrance = self._mix_modes.selected_mode
		self._track_mixer_control._main_offset = self._track_mixer_control.scroll_offset
		self._track_mixer_control._scroll_offset = self._track_mixer_control._troll_offset
		if self._main_modes.selected_mode is 'mix':
			self._check_track_mixer_entry()


	def _release_track_mode(self):
		debug('release device mode')
		"""if self._troll_modes.selected_mode is 'enabled':
			self._troll_modes.selected_mode = 'disabled'
		if len(self._main_modes.active_modes) > 1:
			self._main_modes.pop_mode('device')
		self._device_component._update_parameters()"""

		self._track_mixer_control._troll_offset = self._track_mixer_control.scroll_offset
		self._track_mixer_control._scroll_offset = self._track_mixer_control._main_offset
		if self._main_modes.selected_mode is 'mix':
			self._mix_modes.selected_mode = self._track_mixer_control._mode_on_troll_entrance
			if self._track_mixer_control._mode_on_troll_entrance is 'track':
				self._track_mixer_control.notify_scroll_offset()
				self._track_mixer_control.update()


	def _check_track_mixer_entry(self):
		debug('_check_track_mixer_entry')
		if self._troll_modes.selected_mode is 'enabled':
			if not self._mix_modes.selected_mode is 'track':
				#self._mix_modes.push_mode('track')
				self._mix_modes.selected_mode = 'track'
			self._track_mixer_control.notify_scroll_offset()
			self._track_mixer_control.update()


	def _check_track_mixer_exit(self):
		debug('_check_track_mixer_exit')


	def _disable_troll(self):
		#self._troll_modes.selected_mode = 'disabled'
		debug('disable troll')


	def _init_mute_solo_stop(self):
		super(AumPush2, self)._init_mute_solo_stop()
		self._master_selector.layer = Layer(toggle_button=self._with_select('master_select_button'))


	def _grab_crossfader(self):
		self._crossfader_strip.set_parameter(self.song.master_track.mixer_device.crossfader)


	def _release_crossfader(self):
		self._crossfader_strip.set_parameter(None)


	def _remove_pedal(self):

		#self.real_foot_pedal_button = self.elements.foot_pedal_button
		self.elements.foot_pedal_button = DoublePressElement(create_button(127, name = 'Foot_Pedal', skin = self._skin, is_rgb=True))
		for control in self.controls:
			if isinstance(control, ButtonElement) and control._original_identifier is 69:
				self.log_message('found control: ' + str(control))
				self.controls.remove(control)
				break
		self.request_rebuild_midi_map()


	#in progress: this will allow viewing returns on right side of channel selectors when trollmode is engaged.
	def right_align_return_tracks_track_assigner(song, tracks_provider):
		if self._troll_modes.selected_mode == 'disabled':
			offset = tracks_provider.track_offset
			tracks = tracks_provider.tracks_to_use()
			return_tracks = list(song.return_tracks)
			size = tracks_provider.num_tracks
			num_empty_tracks = max(0, size + offset - len(tracks))
			track_list = size * [None]
			for i in range(size):
				track_index = i + offset
				if len(tracks) > track_index:
					track = tracks[track_index]
					empty_offset = 0 if tracks[track_index] not in return_tracks else num_empty_tracks
					track_list[i + empty_offset] = track
		else:
			offset = tracks_provider.track_offset
			tracks = tracks_provider.tracks_to_use()
			return_tracks = list(song.return_tracks)
			size = tracks_provider.num_tracks
			num_empty_tracks = max(0, size + offset - len(tracks))
			track_list = size * [None]
			for i in range(size):
				track_index = i + offset
				if len(tracks) > track_index:
					track = tracks[track_index]
					empty_offset = 0 if tracks[track_index] not in return_tracks else num_empty_tracks
					track_list[i + empty_offset] = track

		return track_list


	"""
	@listens('device')
	def _on_device_changed(self):
		debug('_on_device_changed')
		#self.schedule_message(1, self._select_note_mode)
		#self._select_note_mode()


	@listens('selected_track')
	def _on_selected_track_changed(self):
		#if self._troll_modes.selected_mode is 'enabled':
		#	self._device_component._update_parameters()
		pass

	"""

	def _select_note_mode(self, mod_device = None):
		track = self.song.view.selected_track
		drum_device, sliced_simpler = self._percussion_instruments_for_track(track)
		self._drum_component.set_drum_group_device(drum_device)
		self._slicing_component.set_simpler(sliced_simpler)
		debug('select_note_mode: ', self.modhandler.is_locked(), self.modhandler.active_mod(), len(track.devices))
		if not (self._note_modes.selected_mode is 'mod' and self.modhandler.is_locked()):
			if track == None or track.is_frozen:
				self._note_modes.selected_mode = 'disabled'
			elif self.modhandler.active_mod():
				self._note_modes.selected_mode = 'mod'
			elif track.is_foldable or track in self.song.return_tracks or track == self.song.master_track:
				self._note_modes.selected_mode = 'disabled'
			elif track and track.has_audio_input:
				self._note_modes.selected_mode = 'looperhack'
			elif drum_device:
				self._note_modes.selected_mode = 'drums'
			elif sliced_simpler:
				self._note_modes.selected_mode = 'slicing'
			else:
				self._note_modes.selected_mode = 'instrument'
			self.reset_controlled_track()


	def disconnect(self):
		self.log_message('<<<<<<<<<<<<<<<<<<<<<<<< AumPush2 ' + str(self._monomod_version) + ' log closed >>>>>>>>>>>>>>>>>>>>>>>>')
		super(AumPush2, self).disconnect()


	def _can_auto_arm_track(self, track):
		routing = track.current_input_routing
		return routing == 'Ext: All Ins' or routing == 'All Ins' or routing.startswith('AumPush2')



class ModDisplayComponent(Component):


	def __init__(self, parent, display_strings, value_strings, *a, **k):
		assert len(display_strings) == len(value_strings)
		super(ModDisplayComponent, self).__init__(*a, **k)
		self.num_segments = len(display_strings)
		self._parent = parent
		self._name_display_line = None
		self._value_display_line = None
		self._name_data_sources = [ DisplayDataSource(string) for string in display_strings ]
		self._value_data_sources = [ DisplayDataSource(string) for string in value_strings ]


	def set_name_display_line(self, display_line):
		self._name_display_line = display_line
		if self._name_display_line:
			self._name_display_line.set_data_sources(self._name_data_sources)


	def set_value_display_line(self, display_line):
		self._value_display_line = display_line
		if self._value_display_line:
			self._value_display_line.set_data_sources(self._value_data_sources)


	def set_name_string(self, value, source = 0):
		if source in range(len(self._name_data_sources)):
			self._name_data_sources[source].set_display_string(str(value))


	def set_value_string(self, value, source = 0):
		if source in range(len(self._value_data_sources)):
			self._value_data_sources[source].set_display_string(str(value))


	def update(self):
		pass



class ModShiftBehaviour(ModeButtonBehaviour):


	def press_immediate(self, component, mode):
		component.push_mode(mode)


	def release_immediate(self, component, mode):
		if len(component.active_modes) > 1:
			component.pop_mode(mode)


	def release_delayed(self, component, mode):
		if len(component.active_modes) > 1:
			component.pop_mode(mode)



class PushModHandler(ModHandler):


	Shift_button = ButtonControl()
	Alt_button = ButtonControl()
	_name = 'AumPush2ModHandler'

	def __init__(self, *a, **k):
		self._color_type = 'Push'
		self._grid = None
		super(PushModHandler, self).__init__(*a, **k)
		self.nav_box = AumPushNavigationBox(self, 16, 16, 8, 8, self.set_offset,) # song = self.song, register_component = self.register_component, is_enabled = False))
		self._push_colors = list(range(128))
		self._push_colors[1:8] = [120, 30, 12, 20, 65, 11, 125]
		self._push_colors[127] = 125
		self._shifted = False


	def select_mod(self, mod):
		super(PushModHandler, self).select_mod(mod)
		self._script._select_note_mode()
		self.update()
		debug('modhandler select mod: ' + str(mod))


	def _receive_grid(self, x, y, value = -1, identifier = -1, channel = -1, *a, **k):
		#debug('_receive_base_grid:', x, y, value, identifier, channel)
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
					button.suppress_script_forwarding = not ((channel, identifier) == (-1, -1))



	def _receive_key(self, x, value):
		#debug('_receive_key:', x, value)
		if not self._keys_value.subject is None:
			self._keys_value.subject.send_value(x, 0, self._push_colors[self._colors[value]], True)


	def _receive_push_name_display(self, x, value):
		if not self._shift_display is None:
			self._shift_display.set_name_string(str(value), x)


	def _receive_push_value_display(self, x, value):
		if not self._shift_display is None:
			self._shift_display.set_value_string(str(value), x)


	def _receive_push_alt_name_display(self, x, value):
		if not self._alt_display is None:
			self._alt_display.set_name_string(str(value), x)


	def _receive_push_alt_value_display(self, x, value):
		if not self._alt_display is None:
			self._alt_display.set_value_string(str(value), x)


	def set_name_display_line(self, display):
		if self._shift_display:
			self._shift_display.set_name_display_line(display)


	def set_value_display_line(self, display):
		if self._shift_display:
			self._shift_display.set_value_display_line(display)


	def set_alt_name_display_line(self, display):
		if self._alt_display:
			self._alt_display.set_name_display_line(display)
			self.log_message('setting alt display')


	def set_alt_value_display_line(self, display):
		if self._alt_display:
			self._alt_display.set_value_display_line(display)


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
		#self.shift_layer and self.shift_layer.enter_mode()
		debug('legacy:', mod.legacy)
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
		#self.shift_layer and self.shift_layer.leave_mode()
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



class AumPushNavigationBox(NavigationBox):


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


#a
