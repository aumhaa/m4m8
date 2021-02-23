# by amounra 0915 : http://www.aumhaa.com

#for debugging connection:
#install telnet with brew install telnet
#terminal:telnet localhost 23

import Live
import logging
import sys
import builtins
import functools

import os #, __builtin__, __main__, _ast, _codecs, _functools, _md5, _random, _sha, _sha256, _sha512, _socket, _sre, _ssl, _struct, _symtable, _weakref, binascii, cStringIO, collections, datetime, errno, exceptions, gc, imp, itertools, marshal, math, sys, time

#modules = [__builtin__, __main__, _ast, _codecs, _functools, _md5, _random, _sha, _sha256, _sha512, _socket, _sre, _ssl, _struct, _symtable, _types, _weakref, binascii, cStringIO, collections, datetime, errno, exceptions, fcntl, gc, imp, itertools, marshal, math, operator, posix, pwd, select, signal, sys, thread, time, unicodedata, xxsubtype, zipimport, zlib]

modules = []

from re import *

from ableton.v2.base import old_hasattr
from ableton.v2.control_surface.control_surface import *
from ableton.v2.control_surface.component import Component as ControlSurfaceComponent

logger = logging.getLogger(__name__)

CS_LIST_KEY = 'control_surfaces'

def publish_control_surface(control_surface):
	get_control_surfaces().append(control_surface)


def get_control_surfaces():
	if isinstance(__builtins__, dict):
		if CS_LIST_KEY not in list(__builtins__.keys()):
			__builtins__[CS_LIST_KEY] = []
		return __builtins__[CS_LIST_KEY]
	else:
		if not old_hasattr(__builtins__, CS_LIST_KEY):
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
		modnames = list(debug.rollbackImporter.newModules.keys())
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


def log_flattened_arguments(*a, **k):
	args = ''
	for item in a:
		args = args + str(item) + ' '
	logger.info(args)


def initialize_debug():
	debug = no_debug
	logger.info('getting control_surfaces:')
	for module in get_control_surfaces():
		logger.info('module is:' + str(module))
		logger.info('isinstance:' + str(isinstance(module, Debug)) + ' ' + str(Debug))
		if isinstance(module, Debug):
			logger.info('setting to flattened_arguments')
			debug = log_flattened_arguments
			break
	return debug


def initialize_debug():
	return log_flattened_arguments if DEBUG else no_debug


debug = log_flattened_arguments






def nop(*a, **k):
	pass

#telnet localhost

class TelnetDebugger(object):

	def __init__(self, script, c_instance, port=23):
		self._script = script
		self._LiveTelnet__c_instance = c_instance
		self._port = port
		# debug('Telnet port is:', port)
		try:
			import builtins
		except ImportError:
			import builtins as builtins

		try:
			sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
			# sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python')

			import io, socket, code
		except:
			debug('couldnt append path')
		# self.originalstdin = sys.stdin
		# self.originalstdout = sys.stdout
		# self.originalstderr = sys.stderr

		self.stdin = io.StringIO()
		self.stdout = io.StringIO()
		self.stderr = io.StringIO()

		self.telnetSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# debug('base port:', 25, 'is in use', self.is_port_in_use(25))
		self.telnetSocket.bind( ('', int(port) ))
		self.telnetSocket.setblocking(False)
		self.telnetSocket.listen(1)
		self.telnetConnection = None

		self.interpreter = code.InteractiveConsole(globals())

		self.telnetBuffer = ""
		self.lastData = ""
		self.commandBuffer = []

		self._script.handle = self.handle

	def is_port_in_use(self, port):
	    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	        return s.connect_ex(('localhost', port)) == 0

	def handle(self):
		return self._LiveTelnet__c_instance.handle()

	def update(self):
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
				self.telnetConnection.send(("Welcome to the Ableton Live Python Interpreter (Python 3.7.1)\r\n").encode(encoding='UTF-8'))
				self.telnetConnection.send(("Brought to by LiveAPI.org\r\n").encode(encoding='UTF-8'))
				self.telnetConnection.send((">>> ").encode(encoding='UTF-8'))
		else:
			#Someone's connected, so lets interact with them.
			try:
				#If the client has typed anything, get it
				data = self.telnetConnection.recv(1)
				debug(data)
			except:
				#Nope they haven't typed anything yet
				data = "" #

			#If return is pressed, process the command (This if statement is so ugly because ableton python doesn't have universal newlines)
			if (data == "\n" or data == "\r") and (self.lastData != "\n" and self.lastData != "\r"):
				# continues = self.interpreter.push(self.telnetBuffer.rstrip()) #should be strip("/r/n") but ableton python throws an error
				continues = self.interpreter.push(self.telnetBuffer.strip("/r/n"))
				debug('sending commandBuffer:', self.telnetBuffer.rstrip())
				self.commandBuffer.append(self.telnetBuffer.rstrip())
				self.telnetBuffer = ""

				#if the user input is multi-line, continue, otherwise return the results

				if continues:
					self.telnetConnection.send(("... ").encode(encoding="UTF-8"))
				else:
					#return stdout to the client
					self.telnetConnection.send((self.stdout.getvalue().replace("\n","\r\n")).encode(encoding="UTF-8"))
					#return stderr to the client
					self.telnetConnection.send((self.stderr.getvalue().replace("\n","\r\n")).encode(encoding="UTF-8"))
					self.telnetConnection.send((">>> ").encode(encoding="UTF-8"))

				#Empty buffers by creating new stringIO objects
				#There's probably a better way to empty these
				self.stdin.close()
				self.stdout.close()
				self.stderr.close()
				self.stdin = io.StringIO()
				self.stdout = io.StringIO()
				self.stderr = io.StringIO()
				#re-redirect the stdio
				sys.stdin = self.stdin
				sys.stdout = self.stdout
				sys.stderr = self.stderr


			elif data == "\b": #deals with backspaces
				if len(self.telnetBuffer):
					self.telnetBuffer = self.telnetBuffer[:-1]
					self.telnetConnection.send((" \b").encode(encoding="UTF-8")) #deletes the character on the console
				else:
					self.telnetConnection.send((" ").encode(encoding="UTF-8"))
			elif data != "\n" and data != "\r":
				self.telnetBuffer = self.telnetBuffer + str(data)
			self.lastData = data

	def disconnect(self):
		#Be nice and return stdio to their original owners
		# sys.stdin = self.originalstdin
		# sys.stdout = self.originalstdout
		# sys.stderr = self.originalstderr
		self.telnetSocket.close()


#currently, live debug is balking at _posixsubprocess module load, as it's not available in the
#Live Python implementation.  We need to override the subprocess.py module in global namespace with the
#standard Python version?

class Debug(ControlSurface):


	def __init__(self, c_instance, *a, **k):
		super(Debug, self).__init__(c_instance, *a, **k)
		self._telnet_enabled = False
		# self.initialize_telnet_debug()
		# self.initialize_vscode_debug()
		# self.initialize_pycharm2016_debug()
		# self.initialize_pycharm2020_debug()
		self.log_message('_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_ DEBUG ON _^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_')
		self._scripts = []

		# self._scan()
		# self._log_version_data()
		# self._log_sys_modules()
		# self._log_dirs()
		# self._log_C_modules()
		# self.log_filenames()
		# self._log_functools()

	def connect_script_instances(self, instanciated_scripts):
		debug = no_debug
		for module in instanciated_scripts:
			if isinstance(module, Debug):
				debug = log_flattened_arguments
				break
		builtins.debug = debug

	def initialize_vscode_debug(self):
		# sys.modules['ctypes'] = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ctypes/'
		# sys.modules['ctypes'] = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/'
		# sys.modules['subprocess'] = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/'
		try:
			# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
			sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
		except:
			debug('couldnt append path')
		self._log_version_data()
		import debugpy
		debugpy.listen(5678)
		debugpy.wait_for_client()

	def initialize_pycharm2016_debug(self):
		# sys.modules['ctypes'] = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/'
		try:
			# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
			sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
		except:
			debug('couldnt append path')
		sys.stderr.flush = nop
		sys.stdout.flush = nop
		import pydevd
		pydevd.settrace('localhost', port=2334, stdoutToServer=True, stderrToServer=True)

	def initialize_pycharm2020_debug(self):
		# sys.modules['ctypes'] = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/'
		try:
			# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
			sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python')
		except:
			debug('couldnt append path')
		sys.stderr.flush = nop
		sys.stdout.flush = nop
		import pydevd_pycharm
		pydevd_pycharm.settrace('localhost', port=2334, stdoutToServer=True, stderrToServer=True)
		# pydevd_pycharm.settrace(<host name>, port=<port number>)

	def initialize_telnet_debug(self, port = 23):
		self._telnet = TelnetDebugger(self, self._c_instance, port)
		self._telnet_enabled = True


	def update_display(self):
		if self._telnet_enabled:
			self._telnet.update()

	def log_filenames(self):
		modules = [m.__file__ for m in list(sys.modules.values()) if m and getattr(m, '__file__', None)]
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

	def _log_functools(self):
		for item in dir(functools):
			self.log_message('functools item:   %s' %(item))

	def _log_sys_modules(self):
		pairs = ((v, k) for (v, k) in sys.modules.items())
		for module in sorted(pairs):
			self.log_message('---' + str(module))
		for mod in list(sys.modules.keys()):
			self.log_message('---------path' + str(sys.modules[mod]))
		#for item in dir(gc):
		#	self.log_message(str(item))
		#looks_at = gc.get_referrers(self)
		#for item in looks_at:
		#	self.log_message(str(item))


	def _clean_sys(self):
		for key, value in list(sys.modules.items()):
			if value == None:
				del sys.modules[key]
		for path in sys.path:
			if 'MIDI Remote Scripts' in path:
				name_list = os.listdir(path)
				for name in name_list:
					if name[0] != '_' or '_Mono_Framework' == name[:15]:
						for key in list(sys.modules.keys()):
							if name == key[:len(name)]:
								del sys.modules[key]
								#self.log_message('deleting key---' + str(key))
		#self._log_sys_modules()


	def log_message(self, *a):
		logger.info(a)


	def disconnect(self):
		if self._telnet_enabled:
			self._telnet.disconnect()
		builtins.debug = no_debug
		self.log_message('_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_ DEBUG OFF _v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_v_')
		super(Debug, self).disconnect()
