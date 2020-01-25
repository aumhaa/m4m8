// aumhaa_dict_module.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;


function DictModule(name, args){
	var self = this;
	this.add_bound_properties(this, ['_dict_name', 'get', 'set', 'getNumberSafely', 'keys', '_dict', '_initialize']);
	this._VIEW_DEVICEDICT = false;
	DictModule.super_.call(this, name, args);
	this._dict = new Dict(this._dict_name);
	this._dict.quiet = this._quiet ? this._quiet : false;
	this._initialize && this._initialize();
}

util.inherits(DictModule, Bindable);

DictModule.prototype.initialize = function(){
	lcl_debug('DictModule._initialize() is abstract, needs override');
}

DictModule.prototype.set = function(address, value){
	try{
		this._dict.replace(address, value);
		this.refresh_window();
		return true;
	}
	catch(err){
		return false;
	}
}

DictModule.prototype.setMember = function(address, member, value){
	lcl_debug('address:', address, 'member:', member, 'value:', value);
	try{
		var strng_val = JSON.stringify(value);
		lcl_debug('strng_val:', strng_val);
		this._dict.setparse(member, strng_val);
		//var sub = this._dict.get(address);
		//lcl_debug('sub is:', sub, typeof(sub));
		//for(var i in sub)
		//{
		//	lcl_debug(i, sub[i]);
		//}
		//sub.setparse(member, value);
		//sub.replace(member, value);
		//this._dict.replace(
		return true;
	}
	catch(err){
		return false;
	}
}

DictModule.prototype.get = function(address, type, def){
	var value = this._dict.contains(address) ? this._dict.get(address) : def != undefined ? def : type == 'Array' ? [] : false;
	switch(type){
		case 'Array':
			value = typeof value == 'object' ? value : [];
			break;
		case 'Number':
			value = typeof value == 'number' ? isNaN(parseInt(value)) ? 0 : value : 0;
			break;
		case 'String':
			value = typeof value == 'string' ? value : value + '';
			break;
		default:
			break;
	}
	return value;
}

DictModule.prototype.getNumberSafely = function(address){
	return this.get(address, 'number');
}

DictModule.prototype.hasKey = function(address){
	return this._dict.contains(address);
}

DictModule.prototype.refresh_window = function(){
	this._VIEW_DEVICEDICT&&this._obj.message('wclose');
	this._VIEW_DEVICEDICT&&this._obj.message('edit');
}

DictModule.prototype.remove = function(address){
	if(this.hasKey(address)){
		this._dict.remove(address);
	}
}

DictModule.prototype.getKeys = function(){
	return this._dict.getkeys();
}

exports.DictModule = DictModule;
