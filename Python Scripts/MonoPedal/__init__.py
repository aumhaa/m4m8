# by amounra 0216 : http://www.aumhaa.com

from __future__ import absolute_import, print_function
from ableton.v2.control_surface.capabilities import *
from .MonoPedal import MonoPedal

from .MonoPedal import MonoPedal

def create_instance(c_instance):
	""" Creates and returns the MonoPedal script """
	return MonoPedal(c_instance)


def get_capabilities():
	return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[115], model_name='aumhaa MonoPedal'),
	 PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT, REMOTE])]}