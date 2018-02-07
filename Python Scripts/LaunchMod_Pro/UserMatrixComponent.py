
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
#from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

def _disable_control(control):
    for button in control:
        button.set_enabled(False)


class UserMatrixComponent(Component):
    u"""
    "Component" that expects ButtonMatrixElements that hold
    ConfigurableButtonElements, to then turn them off. This
    is done so the buttons' messages can be forwarded to Live's Tracks.
    """

    def __getattr__(self, name):
        if len(name) > 4 and name[:4] == u'set_':
            return _disable_control
        raise AttributeError(name)