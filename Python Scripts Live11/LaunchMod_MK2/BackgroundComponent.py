

#from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase
from ableton.v2.control_surface.components import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(self._on_value_listener)
        super(BackgroundComponent, self)._clear_control(name, control)

    def _on_value_listener(self, *a, **k):
        pass


class TranslatingBackgroundComponent(BackgroundComponent):

    def __init__(self, translation_channel = 0, *a, **k):
        super(TranslatingBackgroundComponent, self).__init__(*a, **k)
        self._translation_channel = translation_channel

    def _clear_control(self, name, control):
        if control:
            control.set_channel(self._translation_channel)
        super(TranslatingBackgroundComponent, self)._clear_control(name, control)