
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import ButtonControl
#from _Framework.Control import ButtonControl
from ableton.v2.control_surface import Component
#from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class LedLightingComponent(Component):
    button = ButtonControl(color=u'Misc.Shift', pressed_color=u'Misc.ShiftOn')