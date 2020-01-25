var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;

function AumhaaGlobalProxy(name, args){
	var self = this;
	this.add_bound_properties(this, []);
	this.__dependencies = {};
	for(var i in this.__dependencies)
	if(this.__dependencies[i] == undefined){
		lcl_debug(i + ' must be provided to ControlSurfaceClass.');
	}
	AumhaaGlobalProxy.super_.call(this, name, args);
	this.init();
}

util.inherits(AumhaaGlobalProxy, Bindable);

AumhaaGlobalProxy.prototype.init = function(){
	//debug('setup_global()');
	this._global = new Global('aumhaaGlobal');
}

AumhaaGlobalProxy.prototype.has_scope = function(name){
	return this._global.hasOwnProperty(name);
}

AumhaaGlobalProxy.prototype.set_scope = function(name, value){
	if(!this.has_scope(name)){
		this[name] = value;
	}
}

AumhaaGlobalProxy.prototype.get_scope = function(name){
	if(!this.has_scope(name)){
		return this[name];
	}
	else{
		return false;
	}
}

AumhaaGlobalProxy.prototype.global = function(){
	return this._global;
}

exports.AumhaaGlobalProxy = AumhaaGlobalProxy;
