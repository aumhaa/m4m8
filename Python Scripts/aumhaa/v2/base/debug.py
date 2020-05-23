# by amounra 0915 : http://www.aumhaa.com

#for debugging connection:
#install telnet with brew install telnet
#terminal:telnet localhost 23

import Live
import logging

import os, __builtin__, __main__, _ast, _codecs, _functools, _md5, _random, _sha, _sha256, _sha512, _socket, _sre, _ssl, _struct, _symtable, _weakref, binascii, cStringIO, collections, datetime, errno, exceptions, gc, imp, itertools, marshal, math, sys, time

#modules = [__builtin__, __main__, _ast, _codecs, _functools, _md5, _random, _sha, _sha256, _sha512, _socket, _sre, _ssl, _struct, _symtable, _types, _weakref, binascii, cStringIO, collections, datetime, errno, exceptions, fcntl, gc, imp, itertools, marshal, math, operator, posix, pwd, select, signal, sys, thread, time, unicodedata, xxsubtype, zipimport, zlib]

modules = []

DIRS_TO_REBUILD = ['Debug', 'AumPC20_b995_9', 'AumPC40_b995_9', 'AumPush_b995', 'AumTroll_b995_9', 'AumTroll_b995_9_G', 'Base_9_LE', 'BlockMod_b995_9', 'Codec_b995_9', 'Codex', 'LaunchMod_b995_9', 'Lemur256_b995_9', 'LemurPad_b995_9', 'Livid_Alias8', 'Livid_Base', 'Livid_Block', 'Livid_CNTRLR', 'Livid_CodeGriid', 'Livid_CodeRemoteScriptLinked', 'Livid_Ohm64', 'Livid_OhmModes', 'MonOhm_b995_9', 'Monomodular_b995_9']

MODS_TO_REBUILD = ['Debug', 'AumPC20', 'AumPC40', 'AumPush', 'AumTroll', 'AumTroll_G', 'Base', 'BlockMod', 'Codec', 'LaunchMod', 'Lemur256', 'LemurPad', 'Alias8', 'Block', 'CNTRLR', 'CodeGriid', 'Ohm64', 'MonOhm', 'Monomodular']

from re import *

from ableton.v2.control_surface.control_surface import *
from ableton.v2.control_surface.component import Component as ControlSurfaceComponent

logger = logging.getLogger(__name__)


CS_LIST_KEY = 'control_surfaces'

def publish_control_surface(control_surface):
	get_control_surfaces().append(control_surface)


def get_control_surfaces():
	if isinstance(__builtins__, dict):
		if CS_LIST_KEY not in __builtins__.keys():
			__builtins__[CS_LIST_KEY] = []
		return __builtins__[CS_LIST_KEY]
	else:
		if not hasattr(__builtins__, CS_LIST_KEY):
			setattr(__builtins__, CS_LIST_KEY, [])
		return getattr(__builtins__, CS_LIST_KEY)


DEBUG = True

def _normalize_filename(filename):
	if filename is not None:
		if filename.endswith('.pyc') or filename.endswith('.pyo'):
			filename = filename[:-1]
		elif filename.endswith('$py.class'):
			filename = filename[:-9] + '.py'
	return filename


def rebuild_sys():
	modnames = []
	for module in get_control_surfaces():
		if isinstance(module, Debug):
			#module._reimport_loaded_modules()
			module.rebuild_sys()
			break
	return modnames


def list_new_modules():
	modnames = []
	for module in get_control_surfaces():
		if isinstance(module, Debug):
			#modnames.append['debug found:']
			modnames = module.rollbackImporter.newModules
			break
	return modnames


def rollback_is_enabled():
	control_surfaces = get_control_surfaces()
	if 'Debug' in control_surfaces:
		debug = control_surfaces['Debug']
		modnames = debug.rollbackImporter.newModules.keys()
	return modnames


def log_sys_modules():
	modnames = []
	for module in get_control_surfaces():
		if isinstance(module, Debug):
			#modnames.append['debug found:']
			module._log_sys_modules()
			break


def print_debug(message):
	for module in get_control_surfaces():
		if isinstance(module, Debug):
			#modnames.append['debug found:']
			module.log_message(message)
			break


def no_debug(*a, **k):
	pass


def initialize_debug():
	debug = no_debug
	for module in get_control_surfaces():
		#logger.info('module is:' + str(module))
		if isinstance(module, Debug):
			debug = log_flattened_arguments
	return debug


def log_flattened_arguments(*a, **k):
	args = ''
	for item in a:
		args = args + str(item) + ' '
	logger.info(args)


debug = log_flattened_arguments


try:
	import builtins
except ImportError:
	import __builtin__ as builtins

try:
	sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python')
	
	import StringIO, socket, code
except:
	debug('couldnt append path')





# import debugpy


class Debug(ControlSurface):


	def __init__(self, c_instance, *a, **k):
		super(Debug, self).__init__(c_instance, *a, **k)
		self._LiveTelnet__c_instance = c_instance
		self.originalstdin = sys.stdin
		self.originalstdout = sys.stdout
		self.originalstderr = sys.stderr

		self.stdin = StringIO.StringIO()
		self.stdout = StringIO.StringIO()
		self.stderr = StringIO.StringIO()

		self.telnetSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.telnetSocket.bind( ('', 23) )
		self.telnetSocket.setblocking(False)
		self.telnetSocket.listen(1)
		self.telnetConnection = None

		self.interpreter = code.InteractiveConsole(globals())

		self.telnetBuffer = ""
		self.lastData = ""
		self.commandBuffer = []

		# import pydevd_pycharm

		# pydevd_pycharm.settrace('localhost', port=2334, stdoutToServer=True, stderrToServer=True)

		# pydevd_pycharm.settrace(<host name>, port=<port number>)
		# import pydevd

		# pydevd.settrace('localhost', port=63342, stdoutToServer=True, stderrToServer=True)

		# debugpy.listen(5678);

		# self._log_version_data()
		# self._log_sys_modules()
		# self._log_dirs()
		# self._log_C_modules()
		# self.log_filenames()
		self.log_message('_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_ DEBUG ON _^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_')
		self._scripts = []
		#self._scan()

	def connect_script_instances(self, instanciated_scripts):
		return

	# def application(self):
	# 	return Live.Application.get_application()
	#
	# def song(self):
	# 	return self._LiveTelnet__c_instance.song

	def handle(self):
		return self._LiveTelnet__c_instance.handle()

	def refresh_state(self):
		return

	def is_extension(self):
		return False

	def request_rebuild_midi_map(self):
		return

	def build_midi_map(self, midi_map_handle):
		return

	def update_display(self):
		#Keep trying to accept a connection until someone actually connects
		if not self.telnetConnection:
			try:
				#Does anyone want to connect?
				self.telnetConnection, self.addr = self.telnetSocket.accept()
			except:
				#No one connected in this iteration
				pass
			else:
				#Yay! Someone connected! Send them the banner and first prompt.
				self.telnetConnection.send("Welcome to the Ableton Live Python Interpreter (Python 2.2.1)\r\n")
				self.telnetConnection.send("Brought to by LiveAPI.org\r\n")
				self.telnetConnection.send(">>> ")
		else:
			#Someone's connected, so lets interact with them.
			try:
				#If the client has typed anything, get it
				data = self.telnetConnection.recv(1)
			except:
				#Nope they haven't typed anything yet
				data = "" #

			#If return is pressed, process the command (This if statement is so ugly because ableton python doesn't have universal newlines)
			if (data == "\n" or data == "\r") and (self.lastData != "\n" and self.lastData != "\r"):
				continues = self.interpreter.push(self.telnetBuffer.rstrip()) #should be strip("/r/n") but ableton python throws an error
				self.commandBuffer.append(self.telnetBuffer.rstrip())
				self.telnetBuffer = ""

				#if the user input is multi-line, continue, otherwise return the results

				if continues:
					self.telnetConnection.send("... ")
				else:
					#return stdout to the client
					self.telnetConnection.send(self.stdout.getvalue().replace("\n","\r\n"))
					#return stderr to the client
					self.telnetConnection.send(self.stderr.getvalue().replace("\n","\r\n"))
					self.telnetConnection.send(">>> ")

				#Empty buffers by creating new stringIO objects
				#There's probably a better way to empty these
				self.stdin.close()
				self.stdout.close()
				self.stderr.close()
				self.stdin = StringIO.StringIO()
				self.stdout = StringIO.StringIO()
				self.stderr = StringIO.StringIO()
				#re-redirect the stdio
				sys.stdin = self.stdin
				sys.stdout = self.stdout
				sys.stderr = self.stderr


			elif data == "\b": #deals with backspaces
				if len(self.telnetBuffer):
					self.telnetBuffer = self.telnetBuffer[:-1]
					self.telnetConnection.send(" \b") #deletes the character on the console
				else:
					self.telnetConnection.send(" ")
			elif data != "\n" and data != "\r":
				self.telnetBuffer = self.telnetBuffer + data
			self.lastData = data

	def send_midi(self, midi_event_bytes):
		pass

	def receive_midi(self, midi_bytes):
		return

	def can_lock_to_devices(self):
		return False

	def suggest_input_port(self):
		return ''

	def suggest_output_port(self):
		return ''

	def suggest_map_mode(self, cc_no):
		result = Live.MidiMap.MapMode.absolute
		if (cc_no in range(FID_PANNING_BASE, (FID_PANNING_BASE + NUM_CHANNEL_STRIPS))):
			result = Live.MidiMap.MapMode.relative_signed_bit
		return result

	def __handle_display_switch_ids(self, switch_id, value):
		pass


	def log_filenames(self):
		modules = [m.__file__ for m in sys.modules.values() if m and getattr(m, '__file__', None)]
		for mod in modules:
			self.log_message('module:' + str(mod))


	def _log_dirs(self):
		self.log_message(str(sys.path))
		#self.log_message(str(__file__) + ' working dir: ' + str(os.listdir(sys.path[5])))


	def _log_version_data(self):
		self.log_message('modules: ' + str(sys.builtin_module_names))
		self.log_message('version: ' + str(sys.version))
		self.log_message('sys.path: ' + str(sys.path))


	def _log_builtins(self):
		for item in dir(module):
			self.log_message('---   %s' %(item))


	def _log_C_modules(self):
		for item in modules:
			self.log_message('Module Name:   %s' %(item.__name__))
			self.log_message('---   %s' %(item.__doc__))


	def _log_sys_modules(self):
		pairs = ((v, k) for (v, k) in sys.modules.iteritems())
		for module in sorted(pairs):
			self.log_message('---' + str(module))
		for mod in sys.modules.keys():
			self.log_message('---------path' + str(sys.modules[mod]))
		#for item in dir(gc):
		#	self.log_message(str(item))
		#looks_at = gc.get_referrers(self)
		#for item in looks_at:
		#	self.log_message(str(item))


	def _clean_sys(self):
		for key, value in sys.modules.items():
			if value == None:
				del sys.modules[key]
		for path in sys.path:
			if 'MIDI Remote Scripts' in path:
				name_list = os.listdir(path)
				for name in name_list:
					if name[0] != '_' or '_Mono_Framework' == name[:15]:
						for key in sys.modules.keys():
							if name == key[:len(name)]:
								del sys.modules[key]
								#self.log_message('deleting key---' + str(key))
		#self._log_sys_modules()


	def log_message(self, *a):
		logger.info(a)


	def disconnect(self):

		#Be nice and return stdio to their original owners
		sys.stdin = self.originalstdin
		sys.stdout = self.originalstdout
		sys.stderr = self.originalstderr
		self.telnetSocket.close()
		self.log_message('_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_ DEBUG OFF _v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_')
		super(Debug, self).disconnect()



# _baseimport = builtins.__import__
# _blacklist = None
# _dependencies = dict()
# _parent = None

# # Jython doesn't have imp.reload().
# if not hasattr(imp, 'reload'):
# 	imp.reload = reload

# # PEP 328 changed the default level to 0 in Python 3.3.
# _default_level = -1 if sys.version_info < (3, 3) else 0


# class Reloader(object):


# 	def enable(self, blacklist=None):
# 		"""Enable global module dependency tracking.

# 		A blacklist can be specified to exclude specific modules (and their import
# 		hierachies) from the reloading process.	 The blacklist can be any iterable
# 		listing the fully-qualified names of modules that should be ignored.  Note
# 		that blacklisted modules will still appear in the dependency graph; they
# 		will just not be reloaded.
# 		"""
# 		global _blacklist
# 		_blacklist = ['Debug']
# 		builtins.__import__ = self._import
# 		if blacklist is not None:
# 			_blacklist = frozenset(blacklist)


# 	def disable(self):
# 		"""Disable global module dependency tracking."""
# 		global _blacklist, _parent
# 		builtins.__import__ = _baseimport
# 		_blacklist = None
# 		_dependencies.clear()
# 		_parent = None


# 	def get_dependencies(self, m):
# 		"""Get the dependency list for the given imported module."""
# 		try:
# 			name = m.__name__
# 		except:
# 			name = m
# 		#name = m.__name__ if isinstance(m, _types.ModuleType) else m
# 		return _dependencies.get(name, None)


# 	def _deepcopy_module_dict(self, m):
# 		"""Make a deep copy of a module's dictionary."""
# 		import copy

# 		# We can't deepcopy() everything in the module's dictionary because some
# 		# items, such as '__builtins__', aren't deepcopy()-able.  To work around
# 		# that, we start by making a shallow copy of the dictionary, giving us a
# 		# way to remove keys before performing the deep copy.
# 		d = vars(m).copy()
# 		del d['__builtins__']
# 		return copy.deepcopy(d)


# 	def _reload(self, m, visited):
# 		"""Internal module reloading routine."""
# 		name = m.__name__

# 		#print_debug('reloading: ' + str(m))
# 		# If this module's name appears in our blacklist, skip its entire
# 		# dependency hierarchy.
# 		if _blacklist and name in _blacklist:
# 			return

# 		# Start by adding this module to our set of visited modules.  We use this
# 		# set to avoid running into infinite recursion while walking the module
# 		# dependency graph.
# 		visited.add(m)

# 		# Start by reloading all of our dependencies in reverse order.	Note that
# 		# we recursively call ourself to perform the nested reloads.
# 		deps = _dependencies.get(name, None)
# 		if deps is not None:
# 			for dep in reversed(deps):
# 				if dep not in visited:
# 					self._reload(dep, visited)

# 		# Clear this module's list of dependencies.	 Some import statements may
# 		# have been removed.  We'll rebuild the dependency list as part of the
# 		# reload operation below.
# 		try:
# 			del _dependencies[name]
# 		except KeyError:
# 			pass

# 		# Because we're triggering a reload and not an import, the module itself
# 		# won't run through our _import hook below.	 In order for this module's
# 		# dependencies (which will pass through the _import hook) to be associated
# 		# with this module, we need to set our parent pointer beforehand.
# 		global _parent
# 		_parent = name

# 		# If the module has a __reload__(d) function, we'll call it with a copy of
# 		# the original module's dictionary after it's been reloaded.
# 		callback = getattr(m, '__reload__', None)
# 		if callback is not None:
# 			d = self._deepcopy_module_dict(m)
# 			imp.reload(m)
# 			callback(d)
# 		else:
# 			imp.reload(m)

# 		# Reset our parent pointer now that the reloading operation is complete.
# 		_parent = None


# 	def reload(self, m):

# 		"""Reload an existing module.
# 		Any known dependencies of the module will also be reloaded.
# 		If a module has a __reload__(d) function, it will be called with a copy of
# 		the original module's dictionary after the module is reloaded."""

# 		self._reload(m, set())


# 	def _import(self, name, globals=None, locals=None, fromlist=None, level=_default_level):
# 		"""__import__() replacement function that tracks module dependencies."""
# 		# Track our current parent module.	This is used to find our current place
# 		# in the dependency graph.

# 		#print_debug('importing: ' + str(name))
# 		global _parent
# 		parent = _parent
# 		_parent = name

# 		# Perform the actual import work using the base import function.
# 		base = _baseimport(name, globals, locals, fromlist, level)

# 		if base is not None and parent is not None:
# 			m = base

# 			# We manually walk through the imported hierarchy because the import
# 			# function only returns the top-level package reference for a nested
# 			# import statement (e.g. 'package' for `import package.module`) when
# 			# no fromlist has been specified.  It's possible that the package
# 			# might not have all of its descendents as attributes, in which case
# 			# we fall back to using the immediate ancestor of the module instead.
# 			if fromlist is None:
# 				for component in name.split('.')[1:]:
# 					try:
# 						m = getattr(m, component)
# 					except AttributeError:
# 						m = sys.modules[m.__name__ + '.' + component]

# 			# If this is a nested import for a reloadable (source-based) module,
# 			# we append ourself to our parent's dependency list.
# 			if hasattr(m, '__file__'):
# 				l = _dependencies.setdefault(parent, [])
# 				l.append(m)

# 		# Lastly, we always restore our global _parent pointer.
# 		_parent = parent

# 		return base


# mod_path = "/Users/amounra/Documents/Max/Packages/mod/Python Scripts"
# livid_path = "/Users/amounra/monomodular_git/Livid Python Scripts"


