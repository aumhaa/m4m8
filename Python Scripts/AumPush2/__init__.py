# by amounra 1215 : http://www.aumhaa.com

#from __future__ import absolute_import, print_function

def get_capabilities():
	from ableton.v2.control_surface import capabilities as caps
	return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10626, product_ids=[6503], model_name='Ableton Push 2'),
	 caps.PORTS_KEY: [caps.inport(props=[caps.HIDDEN, caps.NOTES_CC, caps.SCRIPT]),
					  caps.inport(props=[]),
					  caps.outport(props=[caps.HIDDEN,
					   caps.NOTES_CC,
					   caps.SYNC,
					   caps.SCRIPT]),
					  caps.outport(props=[])],
	 caps.TYPE_KEY: 'push2',
	 caps.AUTO_LOAD_KEY: True}


def create_instance(c_instance):
	from AumPush2 import AumPush2
	from Push2.push2 import Push2
	from Push2.push2_model import Sender, Root
	#from _model import Root
	root = Root(sender=Sender(message_sink=c_instance.send_model_update, process_connected=c_instance.process_connected))
	return AumPush2(c_instance=c_instance, model=root)
