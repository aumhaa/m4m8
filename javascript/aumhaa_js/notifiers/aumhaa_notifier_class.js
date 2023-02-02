//aumhaa_notifier_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var EventEmitter = require('aumhaa_event_emitter').EventEmitter;

/////////////////////////////////////////////////////////////////////////
//This is the root object to be used for all controls, or objects that
//will serve as notifiers to other objects.  It maintains a list of listeners as well as a
//"target_stack" that can be used to push/pop targets to be notified when its value changes
//(only the first target in the stack is notified).  Notifier is "subclassed" by many other prototypes.

function NotifierClass(name, args){
	this.add_bound_properties(this, [
		'get_target_name',
		'_target_heap',
		'_listeners',
		'_enabled',
		'add_listener',
		'remove_listener',
		'set_target',
		'get_target',
		'clear_targets',
		'remove_target',
		'notify',
		'set_enabled',
		'_value'
	]);
	this._value = -1;
	this._target_heap = [];
	this._enabled = true;
	this._display_value = false;
	this._is_setting = false;
	this._display_message = function(){};
	NotifierClass.super_.call(this, name, args);
	this._events.Notify = [];
	this._events.NotifyTarget = [];
	this._events.NotifySend = [];
	if(this._callback!=undefined){
		this.set_target(this._callback);
	}
}

util.inherits(NotifierClass, EventEmitter);

NotifierClass.prototype.get_target = function(){return this._target_heap[0];}

NotifierClass.prototype.get_target_name = function(){return this._target_heap[0]._name;}

NotifierClass.prototype.set_target = function(target){
	this._target_heap = this._target_heap.filter(function(item){
		return item!=target
	});
	target&&this._target_heap.unshift(target);
	this._events.NotifyTarget = [];
	this.on('NotifyTarget', target);
}

NotifierClass.prototype.remove_target = function(target){
	if(target){
		this._target_heap = this._target_heap.filter(function(item){
			return item!=target
		});
	}
	else{
		this._target_heap.shift();
	}
	this._events.NotifyTarget = this._target_heap[0] ? [this._target_heap[0]] : [];
}

NotifierClass.prototype.clear_targets = function(){
	this._target_heap = [];
	this._events.NotifyTarget = [];
}

NotifierClass.prototype.add_listener = function(callback){
	this.on('Notify', callback);
}

NotifierClass.prototype.remove_listener = function(callback){
	this.off('Notify', callback);
}

NotifierClass.prototype.notify = function(obj){
	obj = obj!=undefined ? obj : this;
	this.emit('NotifyTarget', obj);
	this.emit('Notify', obj);
	if(this._display_value>0){
		this._displayMessage(this._name + ' : ' + this._value);
	}
}

NotifierClass.prototype.set_enabled = function(val){
	this._enabled = (val>0);
}

exports.NotifierClass = NotifierClass;
