
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Skin
from .Colors import Rgb

class Colors:

	class DefaultButton:
		On = Rgb.GREEN
		Off = Rgb.GREEN_THIRD
		Disabled = Rgb.BLACK

	class MainModes:
		SelectedOn = Rgb.AMBER
		SelectedPressed = Rgb.AMBER_BLINK
		SelectedOff = Rgb.BLACK
	

	class SubModes:
		SelectedOn = Rgb.GREEN
		SelectedPressed = Rgb.GREEN_BLINK
		SelectedOff = Rgb.GREEN_THIRD
	

	"""
	self._session.set_stop_clip_value(AMBER_THIRD)
	self._session.set_stop_clip_triggered_value(AMBER_BLINK)
	for scene_index in range(self._matrix.height()):
		scene = self._session.scene(scene_index)
		scene.set_triggered_value(GREEN_BLINK)
		scene.name = u'Scene_' + str(scene_index)
		for track_index in range(self._matrix.width()):
			clip_slot = scene.clip_slot(track_index)
			clip_slot.set_triggered_to_play_value(GREEN_BLINK)
			clip_slot.set_triggered_to_record_value(RED_BLINK)
			clip_slot.set_stopped_value(AMBER_FULL)
			clip_slot.set_started_value(GREEN_FULL)
			clip_slot.set_recording_value(RED_FULL)
			clip_slot.name = str(track_index) + u'_Clip_Slot_' + str(scene_index)
			self._all_buttons.append(self._matrix.get_button(track_index, scene_index))

	self._zooming.set_stopped_value(RED_FULL)
	self._zooming.set_selected_value(AMBER_FULL)
	self._zooming.set_playing_value(GREEN_FULL)
	"""

	class Session:
		SceneTriggered = Rgb.GREEN_BLINK
		NoScene = Rgb.BLACK
		ClipStarted = Rgb.GREEN
		ClipRecording = Rgb.RED
		ClipTriggeredPlay = Rgb.GREEN_BLINK
		ClipTriggeredRecord = Rgb.RED_BLINK
		ClipEmpty = Rgb.BLACK
		RecordButton = Rgb.RED_HALF
		StopClip = Rgb.AMBER_THIRD
		StopClipTriggered = Rgb.AMBER_BLINK
		StoppedClip = Rgb.RED_HALF
		ClipStopped = Rgb.AMBER
		Enabled = Rgb.GREEN
		Off = Rgb.GREEN_HALF
		Scene = Rgb.BLACK
		NavigationButtonOn = Rgb.GREEN
		NavigationButtonOff = Rgb.GREEN_THIRD
		PageNavigationButtonOn = Rgb.RED
		PageNavigationButtonOff = Rgb.RED_THIRD
		StopAllClips = Rgb.RED_THIRD
		StopSingleClip = Rgb.RED
		StopClipButton = Rgb.RED_THIRD
		StopSingleClipTriggered = Rgb.RED_BLINK
	

	class Zooming:
		Selected = Rgb.AMBER
		Stopped = Rgb.RED
		Playing = Rgb.GREEN
		Empty = Rgb.BLACK

	class Mixer:
		ArmOn = Rgb.RED
		ArmOff = Rgb.RED_THIRD
		SoloOn = Rgb.RED
		SoloOff = Rgb.RED_THIRD
		MuteOn = Rgb.AMBER
		MuteOff = Rgb.AMBER_THIRD
		Selected = Rgb.AMBER_HALF
		Unselected = Rgb.AMBER_THIRD
		Volume = Rgb.GREEN
		Pan = Rgb.AMBER
		Sends = Rgb.RED
		DefaultValueOn = Rgb.GREEN_THIRD
		DefaultValueOff = Rgb.GREEN
		UnArmAll = Rgb.RED_HALF
		UnArmAllPressed = Rgb.RED
		UnMuteAll = Rgb.AMBER_HALF
		UnMuteAllPressed = Rgb.AMBER
		UnSoloAll = Rgb.RED_HALF
		UnSoloAllPressed = Rgb.RED

	class Scrolling:
		Enabled = Rgb.AMBER_HALF
		Pressed = Rgb.AMBER
		Disabled = Rgb.BLACK

	class Misc:
		UserMode = Rgb.GREEN
		Shift = Rgb.GREEN_THIRD
		ShiftOn = Rgb.AMBER_THIRD


def make_default_skin():
	return Skin(Colors)