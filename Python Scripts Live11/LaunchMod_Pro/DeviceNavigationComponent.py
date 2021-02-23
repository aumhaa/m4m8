

import Live
from ableton.v2.control_surface import Component
#from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from ableton.v2.control_surface.control import ButtonControl
#from _Framework.Control import ButtonControl
NavDirection = Live.Application.Application.View.NavDirection

class DeviceNavigationComponent(Component):
    device_nav_left_button = ButtonControl(color='Device.Off', pressed_color='Device.On')
    device_nav_right_button = ButtonControl(color='Device.Off', pressed_color='Device.On')

    @device_nav_left_button.pressed
    def device_nav_left_button(self, value):
        self._scroll_device_chain(NavDirection.left)

    @device_nav_right_button.pressed
    def device_nav_right_button(self, value):
        self._scroll_device_chain(NavDirection.right)

    def _scroll_device_chain(self, direction):
        view = self.application.view
        if not view.is_view_visible('Detail') or not view.is_view_visible('Detail/DeviceChain'):
            view.show_view('Detail')
            view.show_view('Detail/DeviceChain')
        else:
            view.scroll_view(direction, 'Detail/DeviceChain', False)