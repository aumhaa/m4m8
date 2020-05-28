
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import capabilities as caps
from .aum256 import Aum256

def get_capabilities():
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10996, product_ids=[2304], model_name=[u'Aum256', u'AUM256']),
     caps.PORTS_KEY: [caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]), caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])],
     caps.TYPE_KEY: u'aum256'}


def create_instance(c_instance):
    return Aum256(c_instance=c_instance)
