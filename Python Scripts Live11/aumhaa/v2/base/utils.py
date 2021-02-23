# by amounra 0216 : http://www.aumhaa.com
# written against Live 9.6 release on 021516


import Live
import math
import sys
from re import *
from itertools import chain, starmap

from aumhaa.v2.base import initialize_debug

debug = initialize_debug()


def get_devices(track):

	def dig(container_device):
		contained_devices = []
		if container_device.can_have_chains:
			for chain in container_device.chains:
				for chain_device in chain.devices:
					for item in dig(chain_device):
						contained_devices.append(item)
		else:
			contained_devices.append(container_device)
		return contained_devices


	devices = []
	for device in track.devices:
		for item in dig(device):
			devices.append(item)
			#self.log_message('appending ' + str(item))
	return devices
