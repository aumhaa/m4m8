// aumhaa_control_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;
var consts = require('aumhaa_notifier_consts').consts;
//////////////////////////////////////////////////////////////////////////
//A Notifier representing a physical control that can send and receive MIDI

function ControlClass(identifier, name, args){
	this.add_bound_properties(this, ['receive', 'receive_notifier', '_x', '_y', '_send', 'send']);
	//lcl_debug('making control:', name, this._bound_properties);
	this._type = consts.NONE_TYPE;
	this._id = identifier;
	this._channel = consts.CHANNEL;
	this._grid = {};
	this._last_sent_value = 0;
	ControlClass.super_.call(this, name, args);
}

util.inherits(ControlClass, NotifierClass);

ControlClass.prototype.receive = function(value){
	//lcl_debug('receive:', self._name, value);
	if(this._enabled){
		this._value = value;
		this.notify();
	}
}

ControlClass.prototype.receive_notifier = function(notification){
	if(this._enabled){
		this.send(notification._value);
	}
}

ControlClass.prototype.register_grid = function(name, args){
	this._grid[name] = args;
}

ControlClass.prototype._x = function(grid){
	if(this._grid[grid._name]!=undefined){
		return(this._grid[grid._name].x);
	}
	else{
		return false;
	}
}

ControlClass.prototype._y = function(grid){
	if(this._grid[grid._name]!=undefined){
		return(this._grid[grid._name].y)
	}
	else{
		return false;
	}
}

ControlClass.prototype.identifier = function(){
	return this._id;
}

ControlClass.prototype._send = function(value){
	lcl_debug('ControlClass.send()');
}//this should be overridden by subclass

ControlClass.prototype._mask = function(value){}//this should be overridden by subclass

ControlClass.prototype.send = function(value){
	//debug('ControlClass.send():', value);
	this._last_sent_value = value;
	this._send(value);
}

ControlClass.prototype.reset = function(){
	this.send(0);
}

exports.ControlClass = ControlClass;
