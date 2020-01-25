// aumhaa_node_script_proxy.js
// transferred 070219
// untested

var util = require('aumhaa_util');
util.inject(this, util);

var Bindable = require('aumhaa_bindable').Bindable;
var ArrayParameter = require('aumhaa_parameters').ArrayParameter;



function NodeScriptProxy(name, args){
	var self = this;
	//this._running = false;
	this.add_bound_properties(this, []);
	NodeScriptProxy.super_.call(this, name, args);
	if((this._receive_name)&&(this._script)){
		this._script[this._receive_name] = this.receive;
	}
}

util.inherits(NodeScriptProxy, Bindable);

NodeScriptProxy.prototype.check_dependencies = function(){
	//this._obj.message('script', 'start');
}

NodeScriptProxy.prototype.install = function(){
	//this._obj.message('script', 'npm', 'install');
}

NodeScriptProxy.prototype.start = function(){
	this._obj.message('script', 'start');
}

NodeScriptProxy.prototype.stop = function(){
	this._obj.message('script', 'stop');
}

NodeScriptProxy.prototype.running = function(){
	return this._obj.getattr('running');
}

NodeScriptProxy.prototype.send = function(){
	this._obj.message.apply(this, arguments);
}

exports.NodeScriptProxy = NodeScriptProxy;


function MIDIRouterNodeScriptProxy(name, args){
	var self = this;
	this.add_bound_properties(this, ['receive', '_inputs', '_outputs', 'available_outputs', 'available_inputs']);
	this._input_ports = new ArrayParameter(this._name + '_inputPorts', {'value':[]});
	this._output_ports = new ArrayParameter(this._name + '_outputPorts', {'value':[]});
	MIDIRouterNodeScriptProxy.super_.call(this, name, args);
	this.available_inputs = this._input_ports.receive;
	this.available_outputs = this._output_ports.receive;
}

util.inherits(MIDIRouterNodeScriptProxy, NodeScriptProxy);

MIDIRouterNodeScriptProxy.prototype.receive = function(){
	var args = arrayfromargs(arguments);
	//debug(this._name+'.receive():', args);
	//debug('in?:', args[0], args[0] in this, this[args[0]]);
	this[args[0]]&&this[args[0]].apply(this, args.slice(1));
}

MIDIRouterNodeScriptProxy.prototype.node_script_init = function(){
	this._obj.message('set_input_port', inputPort);
}

exports.MIDIRouterNodeScriptProxy = MIDIRouterNodeScriptProxy;
