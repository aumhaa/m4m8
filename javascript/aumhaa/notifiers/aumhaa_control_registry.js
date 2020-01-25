// aumhaa_control_registry.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = true;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

function ControlRegistry(name){
	//lcl_debug('making ControlRegistry');
	var self = this;
	this._name = !name ? 'ControlRegistry' : name;
	this.registry = {};
	this.register_control = function(id, control){
		//lcl_debug('register_control:', id, control);
		self.registry[id] = control;
	}
	this.receive = function(id, value){
		// lcl_debug('ControlRegistry receive:', id, value);
		// lcl_debug('registry entry:', self.registry[id]);
		try{self.registry[id].receive(value);}
		catch(err){lcl_debug(err, 'id:', id, 'not registerd in registry:', self._name);}
	}
	return this;
}

exports.ControlRegistry = ControlRegistry;
