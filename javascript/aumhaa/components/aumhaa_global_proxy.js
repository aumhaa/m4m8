var util = require('aumhaa_util');
util.inject(this, util);


var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.DebugNamespace ? new util.DebugNamespace('GlobalProxy').debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;

function AumhaaGlobalProxy(name, args){
	var self = this;
	this.add_bound_properties(this, [
		'_global',
		'has_scope',
		'set_scope',
		'get_scope'
	]);
	AumhaaGlobalProxy.super_.call(this, name, args);
	this.init.call(this);
}

util.inherits(AumhaaGlobalProxy, Bindable);

AumhaaGlobalProxy.prototype.__defineGetter__('global', function(){
	return this._global;
})

AumhaaGlobalProxy.prototype.init = function(){
	this._global = new Global('aumhaaGlobal');
}

AumhaaGlobalProxy.prototype.has_scope = function(name){
	return this.global.hasOwnProperty(name);
}

AumhaaGlobalProxy.prototype.set_scope = function(name, value){
	if(!this.has_scope(name)){
		this.global[name] = value;
	}
}

AumhaaGlobalProxy.prototype.get_scope = function(name){
	if(!this.has_scope(name)){
		post('WARNING! '+this._name+' missing scope: '+name+'\n');
		this.global[name]={};
	}
	return this.global[name];
}

AumhaaGlobalProxy.prototype.clear_scope = function(name){
	if(!this.has_scope(name)){
		post('WARNING! '+this._name+' missing scope: '+name+'\n');
		this.global[name]=null;
		delete this.global[name];
	}
}


exports.AumhaaGlobalProxy = AumhaaGlobalProxy;
