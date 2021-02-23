

from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, SYNC, REMOTE, controller_id, inport, outport

def create_instance(c_instance):
	from .Launchpad_Pro import Launchpad_Pro
	return Launchpad_Pro(c_instance)


def get_capabilities():
	from ableton.v2.control_surface import capabilities as caps
	return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[81], model_name='Launchpad Pro'),
	 PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]),
				 inport(props=[]),
				 outport(props=[NOTES_CC,
				  SYNC,
				  SCRIPT,
				  REMOTE]),
				 outport(props=[])]}