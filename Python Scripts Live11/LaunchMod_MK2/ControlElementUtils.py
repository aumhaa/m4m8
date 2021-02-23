

#from _Framework.Dependency import depends
from ableton.v2.base.dependency import depends
#from _Framework.Resource import PrioritizedResource
from ableton.v2.control_surface.resource import PrioritizedResource
#from _Framework.InputControlElement import MIDI_NOTE_TYPE
from ableton.v2.control_surface.input_control_element import MIDI_NOTE_TYPE
#from _Framework.ComboElement import ComboElement, MultiElement as MultiElementBase
from ableton.v2.control_surface.elements.combo import ComboElement, MultiElement as MultiElementBase
#from _Framework.ButtonElement import ButtonElement
from ableton.v2.control_surface.elements.button import ButtonElement as ButtonElementBase
from ableton.v2.control_surface import SkinColorMissingError

class ButtonElement(ButtonElementBase):


	def _set_skin_light(self, value):
		#debug(self.name, '_set_skin_light', value, self.default_states, self.states, self.states.get(value, value))
		try:
			color = self._skin[value]
			self._do_draw(color)
		except SkinColorMissingError:
			if isinstance(value, int) and value in range(127):
				super(ButtonElement, self).send_value(value)
	

@depends(skin=None)
def make_button(identifier, channel, name, msg_type = MIDI_NOTE_TYPE, skin = None, is_modifier = False):
    return ButtonElement(is_momentary = True, msg_type = msg_type, channel = channel, identifier = identifier, skin=skin, name=name, resource_type=PrioritizedResource if is_modifier else None)


def with_modifier(modifier, button):
    return ComboElement(control = button, modifier=[modifier])


class MultiElement(MultiElementBase):

    def __init__(self, *a, **k):
        super(MultiElement, self).__init__(*a, **k)
        self._is_pressed = False

    def is_pressed(self):
        return self._is_pressed

    def on_nested_control_element_value(self, value, control):
        self._is_pressed = bool(value)
        super(MultiElement, self).on_nested_control_element_value(value, control)


class FilteringMultiElement(MultiElement):

    def __init__(self, controls, feedback_channels = None, **k):
        super(MultiElement, self).__init__(*controls, **k)
        self._feedback_channels = feedback_channels

    def send_value(self, value):
        for control in self.owned_control_elements():
            if control.message_channel() in self._feedback_channels:
                control.send_value(value)

    def set_light(self, value):
        for control in self.owned_control_elements():
            if control.message_channel() in self._feedback_channels:
                control.set_light(value)