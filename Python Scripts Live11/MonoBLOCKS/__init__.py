

from ableton.v2.control_surface import capabilities as caps
from .mono_blocks import MonoBlocks

def get_capabilities():
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10996, product_ids=[2304], model_name=['Lightpad BLOCK', 'BLOCKS']),
     caps.PORTS_KEY: [caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]), caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])],
     caps.TYPE_KEY: 'blocks'}


def create_instance(c_instance):
    return MonoBlocks(c_instance=c_instance)