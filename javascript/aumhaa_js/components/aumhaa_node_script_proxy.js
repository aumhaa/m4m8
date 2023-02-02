// aumhaa_node_script_proxy.js
// 050920

/**This object wraps the nodescript object with some async process handling
*  methods.  It requires a corresponding asyncJS method to be added to its subject.
*  There are two types of methods that handle async call/returns.
*  -  asyncScriptCall  communicates with the maxObj [nodescript] instance and
*  deals with the state of the script (running, install, etc).
*  -  asyncCall communicates with the running script via maxApi.handler asyncJS.
*  The jsobject instance does not need to be cabled to the nodescript object,
*  but the nodescript object needs both its outlets cabled to the jsobject's input.
*  Inputs from nodescript must be manually configured in the script containing this
*  object, there are not yet automatic methods to deal with that.
/**
*  TODO:
*	 -handling for NSProxy.message rejections (async)
*  -collect list of available asyncCall _targets
*  -handling for non-compliant node.script modules (asyncJS not available in script)
*
*  -auto-route the parent-scripts inputs so they reach this object (nodeDump, js, etc)
*  -asyncResolve needs a way to forward calls from nodescript instance.
*/

var LCL_DEBUG = false;
//if you want to see detailed debug from nodescript obj, be sure to set this._debug to true also
var util = require('aumhaa_util');
util.inject(this, util);

var Bindable = require('aumhaa_bindable').Bindable;
var EventEmitter = require('aumhaa_event_emitter').EventEmitter;
var ArrayParameter = require('aumhaa_parameters').ArrayParameter;
var Promise = require('aumhaa_promise').Promise;
var AumhaaGlobalProxy = require('aumhaa_global_proxy').AumhaaGlobalProxy;
var DictModule = require('aumhaa_dict_module').DictModule;

var lcl_debug = LCL_DEBUG ? new util.DebugNamespace('nodeproxy->').debug : function(){};
var dump_log = new util.DebugNamespace('NS.dump===>').debug;

/**Used to parse dump dict responses*/
if (!Object.entries) {
  Object.entries = function( obj ){
    var ownProps = Object.keys( obj ),
        i = ownProps.length,
        resArray = new Array(i); // preallocate the Array
    while (i--)
      resArray[i] = [ownProps[i], obj[ownProps[i]]];

    return resArray;
  };
}


function psuedouuid(){
	return Math.random().toString(15).substring(2, 6) + Math.random().toString(15).substring(2, 6)
}


function Callback(proxy, resolve, reject, oargs){
	var self = this;
	this._proxy = proxy;
	this._name = proxy._name + oargs[0] + psuedouuid();
	this._resolve = resolve;
	this._reject = reject;
	this._proxy._callbacks[this._name] = this;
	this.callback = function(){
		var func_args = [].concat(arrayfromargs(arguments));
		// lcl_debug('Callback...', func_args);
		if(self._name in self._proxy._callbacks){
			delete self._proxy._callbacks[self._name];
		}
		if(func_args[0]=='ERROR'){
			self._reject(new Error(func_args[1]));
		}
		else{
			self._resolve.apply(self, func_args);
		}
	}
}


function ScriptCallback(proxy, resolve, reject, oargs){
	var self = this;
	// lcl_debug('ScriptCallback', proxy, func, oargs);
	this._proxy = proxy;
	this._name = oargs[0];
	this._resolve = resolve;
	this._reject = reject;
	this._proxy._scriptCallbacks[this._name] = this;
	this.callback = function(){
		var func_args = [].concat(arrayfromargs(arguments));
		if(self._name in self._proxy._scriptCallbacks){
			delete self._proxy._scriptCallbacks[self._name];
		}
		// lcl_debug('func_args:', func_args, JSON.stringify(func_args));
		if((func_args[0].state)&&(func_args[0].state == 'error')){
			// lcl_debug('ScriptCallback throw:', func_args[0].data.message);
			self._reject(new Error(func_args[0].data.message));
		}
		else{
			self._resolve.apply(self, func_args);
		}
	}
}


function NodeScriptProxy(name, args){
	var self = this;
	//this._running = false;
	this._callbacks = {};
	this._scriptCallbacks = {};
	this._messagePort = 0;
	this._cabled = false;
	this._debug = false;
	this._debugTypes = ['error'];
	this._terminationCallbacks = [];
	this.add_bound_properties(this, [
    '_debug',
		'_callbacks',
		'_obj',
		'_cabled',
		'asyncScriptResolve',
		'asyncResolve',
		'asyncScriptCall',
		'asyncCall',
		'receive',
		'_messagePort',
		'_cabled',
		'message',
		'nodeDump',
		'initialize'
  ]);
	NodeScriptProxy.super_.call(this, name, args);
	if((this._receive_name)&&(this._script)){
		this._script[this._receive_name] = this.receive;
	}
}

util.inherits(NodeScriptProxy, EventEmitter);

NodeScriptProxy.prototype.__defineGetter__('is_running', function(){
	return this._obj.getattr('running');
});

//NODE.SCRIPT COMMUNICATION//

NodeScriptProxy.prototype.receive = function(){
	/**Recieve internal functions and distribute to class methods.*/
	var args = arrayfromargs(arguments);
	// lcl_debug('NSProxy.receive:', args[0]);
	if(args[0] in this){
		this[args[0]].apply(this, args.slice(1));
	}
	else{
		this.message.apply(this, args);
	}
}

NodeScriptProxy.prototype.message = function(){
	/**Forward a direct, synchronous message to the proxy's target object.*/
	var args = [].concat(arrayfromargs(arguments));
	// lcl_debug('NSProxy.message:', args);
	var self = this;
	if(this._cabled){
		var args = [this._messagePort].concat(args);
		outlet.apply(self, args);
	}
	else{
		self._obj.message(args);
	}
}

NodeScriptProxy.prototype.asyncCall = function(){
	/**
	*  Forward an async call to running nodescript instance.  On response, callback
	*  is used to resolve promisory return, but no mechanism to deal within
	*  errors on the wrapped NS instance side.
	*/
	var args = [].concat(arrayfromargs(arguments));
	var argsClone = util.flatten1(args.slice());
	// lcl_debug('asyncCall', args);
	var self = this;
	var ret = new Promise(function(resolve, reject) {
		var callback = new Callback(self, resolve, reject, argsClone);
		self.is_running||reject(self._name + ' instance not currently running');
		try {
			if(self._cabled){
				var new_args = [self._messagePort, 'asyncJS', callback._name].concat(argsClone);
				outlet.apply(self, new_args);
			}
			else{
				var new_args = ['asyncJS', callback._name].concat(argsClone);
				self._obj.message(new_args);
			}
		}
		catch(error) {
			reject(error);
		}
	});
	return ret
}

NodeScriptProxy.prototype.asyncResolve = function(){
	/**Counterpart to asyncCall method, used to resolve promise and make callbacks*/
	var args = arrayfromargs(arguments);
	lcl_debug('asyncResolve:', args);
	if(args[0] in this._callbacks){
		/**following is for handling non-complinat NS modules*/
		// lcl_debug(args[0] in this._callbacks);
		// if((args[1])=='dictionary'){
		// 	var dict = new Dict(args[2]);
		// 	var data = util.dict_to_jsobj(dict);
		// 	lcl_debug('dict:', dict);
		// 	lcl_debug('stringify:', JSON.stringify(dict));
		// if(this._debug){
		// 	var log = Object.entries(data).map(function(i) {
		// 		return i.join(':')+'\n';
		// 	});
		// 	lcl_debug(log);
		// }
		// }
    // debug('callback:', this._callbacks[args[0]].callback);
		this._callbacks[args[0]].callback.apply(this, args.slice(1));
	}
}

NodeScriptProxy.prototype.script_message = function(){
	/**Transport mechanism for sending messages targetting node-script maxObj functions*/
	//async
	var args = [].concat(arrayfromargs(arguments));
	// lcl_debug('NSProxy.script_message:', args);
	var ret = '';
	this.asyncScriptCall(args).then(function(res){
		// lcl_debug('success script_message', res);
		ret = res;
	},
	function(err){
		// lcl_debug('error script_message', err.message);
		ret = err;
	});
	return ret;
}

NodeScriptProxy.prototype.asyncScriptCall = function(){
	/**
	*  Forward an async call to the maxObj node.script instance.  Uses different
	*  callback buffer, only used to communicate with non-running module non-specific
	*  functions of the encompassing max object, via the script_message method
	*/
	var args = [].concat(arrayfromargs(arguments));
	//this is getting zero'd somehow, presumably in ScriptCallback, so we clone...
	var argsClone = args.slice();
	// lcl_debug('asyncScriptCall', args);
	var self = this;
	var ret = new Promise(function(resolve, reject){
		var callback = new ScriptCallback(self, resolve, reject, argsClone);
		try {
			if(self._cabled){
				var new_args = [self._messagePort, 'script'].concat(argsClone);
				// lcl_debug('sending:', new_args);
				outlet.apply(self, new_args);
			}
			else{
        // lcl_debug('asyncScriptCall', argsClone);
				self._obj.message(['script'].concat(argsClone));
			}
		} catch(error) {
			reject(error);
		}
	});
	return ret
}

NodeScriptProxy.prototype.asyncScriptResolve = function(){
	/**Counterpart to asyncScriptCall method, used to resolve promise and make callbacks*/
	var args = arrayfromargs(arguments);
	var action = args[0];
	var state = args[1];
	var data = args[2];
	var dataSpace = args[3];
	if(data=='dictionary'){
		var dict = new Dict(dataSpace);
		data = util.dict_to_jsobj(dict);
	}
	response = {action:action, state:state, data:data};
	if(action in this._scriptCallbacks){
		this._scriptCallbacks[action].callback.apply(this, [response]);
	}
	// if(response.data.code){
	// 	lcl_debug('code is:', response.data.code);
	// }
	if((this._debug)&&(this._debugTypes.indexOf(state)>-1)||(this._debugTypes.indexOf('all')>-1)){
		var log = ('action: '+action+'\nstate: '+state+'\n') + Object.entries(data).map(function(i) {
			return i.join(':')+'\n';
		});
		dump_log(log);
	}
	if(action=='terminated'){
		this.notifyTermination();
	}
}

NodeScriptProxy.prototype.notifyTermination = function(){
	for(var i in this._terminationCallbacks){
		this._terminationCallbacks[i]();
	}
}

NodeScriptProxy.prototype.addTerminationCallback = function(callback){
	this._terminationCallbacks.push(callback);
}

NodeScriptProxy.prototype.removeTerminationCallback = function(callback){
	var index = this._terminationCallbacks.indexOf(callback);
	if(index>-1){
		this._terminationCallbacks.splice(index);
	}
}

//PROXIED NODE.SCRIPT METHODS//

NodeScriptProxy.prototype.initialize = function(){
	/**Check dependencies and start script*/
	//async
	var self = this;
	var ret = new Promise(function(respond, reject){
		if(this.is_running){
			respond(self._name + ' node_script instance is already running.');
		}
		else{
			self.verify_module_dependencies().then( function(){
				return self.start();
			}).then(function(){
				return self.init_routines();
			}).then(function(){
				if(self.is_running){
					respond(self._name + ' has successfully started and is running');
				}
				else {
					reject(new Error('NSProxy.start error: the start command returned \
						successful but the instance is still not running'));
				}
			}).catch(function(){
				reject('start error', err.message);
			});
		}
	});
	return ret
}

NodeScriptProxy.prototype.init_routines = function(){
	/**Placeholder for user specific code, called at end of initialize
  These methods are called directly by proxy whenever this.start() is but
  before any further constructor functions from overlaid classes have fired.
  **/
	lcl_debug('NSProxy.init_routines has not been overridden');
	return Promise.resolve(true)
}

NodeScriptProxy.prototype.verify_module_dependencies = function(){
	lcl_debug('NSProxy.verify_module_dependencies');
	/**Currently not implemented, perhaps use "npm ls"?*/
	return Promise.resolve(true)
}

NodeScriptProxy.prototype.install = function(){
	/**Async method that calls "npm install"*/
	var success = false;
	var self = this;
	var ret = new Promise(function(respond, reject){
		self.asyncScriptCall('npm', 'install').then(
			function(res){
				success = true;
				if(success){
					respond(res);
					lcl_debug('npm install success');
				}
			},
			function(err){
				reject(err);
				lcl_debug('npm install error', err.message);
			}
		);
	});
	return ret;
}

NodeScriptProxy.prototype.start = function(){
	/**Async method that calls "script start"*/
	//async
	lcl_debug('NSProxy.start');
	var self = this;
	var ret = new Promise(function(respond, reject){
		self.asyncScriptCall('start').then(
			function(res){
				respond(res);
			},
			function(err){
				reject(err);
			}
		);
	});
	return ret;
}

NodeScriptProxy.prototype.stop = function(){
	/**Async method that calls "script stop"*/
	// async
	var self = this;
	var ret = new Promise(function(respond, reject){
		self.asyncScriptCall('stop').then(
			function(res){
				// lcl_debug('Nodescript stopped.');
				respond(res);
			},
			function(err){
				// lcl_debug('Nodescript not stopped,', err);
				reject(err);
			}
		);
	});
	return ret;
}

exports.NodeScriptProxy = NodeScriptProxy;

//DEPRECATED//

NodeScriptProxy.prototype.nodeDump = function(){
	var args = arrayfromargs(arguments);
	// lcl_debug(this._name, 'nodeDump:', args);
	this.asyncScriptResolve.apply(this, args);

}

NodeScriptProxy.prototype.send = function(){
	this.message.apply(this, arguments);
}

NodeScriptProxy.prototype.running = function(){
	return this.is_running
}


/*
// function MIDIRouterNodeScriptProxy(name, args){
// 	var self = this;
// 	this.add_bound_properties(this, [
//     'input',
//     '_inputs',
//     '_outputs',
//     '_input_ports',
//     '_output_ports',
//     'available_outputs',
//     'available_inputs'
//   ]);
// 	this._input_ports = new ArrayParameter(this._name + '_inputPorts', {'value':[]});
// 	this._output_ports = new ArrayParameter(this._name + '_outputPorts', {'value':[]});
// 	MIDIRouterNodeScriptProxy.super_.call(this, name, args);
// 	this.available_inputs = this._input_ports.set_value;
// 	this.available_outputs = this._output_ports.set_value;
// }
//
// util.inherits(MIDIRouterNodeScriptProxy, NodeScriptProxy);
//
// MIDIRouterNodeScriptProxy.prototype.input = function(){
// 	var args = arrayfromargs(arguments);
// 	lcl_debug(this._name+'.input():', args);
// 	//debug('in?:', args[0], args[0] in this, this[args[0]]);
//   //we need to send ArrayParameters [], so we use call here....probably a better way
// 	this[args[0]]&&this[args[0]].call(this, args.slice(1));
// }
//
// MIDIRouterNodeScriptProxy.prototype.init_routines = function(){
// 	// this._obj.message('set_input_port', inputPort);
// }
//
// exports.MIDIRouterNodeScriptProxy = MIDIRouterNodeScriptProxy;
*/
