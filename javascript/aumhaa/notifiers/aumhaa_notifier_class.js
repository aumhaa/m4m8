//aumhaa_notifier_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;

/////////////////////////////////////////////////////////////////////////
//This is the root object to be used for all controls, or objects that
//will serve as notifiers to other objects.  It maintains a list of listeners as well as a
//"target_stack" that can be used to push/pop targets to be notified when its value changes
//(only the first target in the stack is notified).  Notifier is "subclassed" by many other prototypes.

function NotifierClass(name, args){
	this.add_bound_properties(this, ['get_target_name', '_target_heap', '_listeners', '_enabled', 'add_listener', 'remove_listener', 'set_target', 'get_target', 'clear_targets', 'remove_target', 'notify', 'set_enabled']);
	//lcl_debug('making notifier:', name, this._bound_properties);
	this._value = -1;
	this._listeners = [];
	this._target_heap = [];
	this._enabled = true;
	this._display_value = false;
	this._is_setting = false;
	this._display_message = function(){};
	NotifierClass.super_.call(this, name, args);
	if(this._callback!=undefined){
		this.set_target(this._callback);
	}
}

util.inherits(NotifierClass, Bindable);

NotifierClass.prototype.get_target = function(){return this._target_heap[0];}

NotifierClass.prototype.get_target_name = function(){return this._target_heap[0]._name;}

NotifierClass.prototype.set_target = function(target){
	if (target){
		if (target in this._target_heap){
			//lcl_debug('target was present for' + this._name, 'placing at front');
			this._target_heap.unshift(this._target_heap.splice(this._target_heap.indexOf(target), 1));
		}
		else{
			this._target_heap.unshift(target);
			//lcl_debug('target added to heap for ' + this._name);
		}
	}
	else{
		this.remove_target();
	}
}

NotifierClass.prototype.remove_target = function(target){
	if (target){
		for(var item in this._target_heap){
			if(target === this._target_heap[item]){
				this._target_heap.splice(item, 1);
				break;
			}
		}
	}
	else{
		this._target_heap.shift();
	}
}

NotifierClass.prototype.clear_targets = function(){
	this._target_heap = [];
}

NotifierClass.prototype.add_listener = function(callback){
	//if(!(callback in this._listeners))
	//{
	//	this._listeners.unshift(callback);
	//}
	//lcl_debug('add listener:', this, this._name);
	var add = true;
	if (callback){
		for(var item in this._listeners){
			if(callback == this._listeners[item]){
				add = false;
				break;
			}
		}
	}
	if(add){
		this._listeners.unshift(callback);
	}
}

NotifierClass.prototype.remove_listener = function(callback){
	//if(callback in this._listeners){this._listeners.slice(this._listeners.indexOf(callback), 1);}
	if (callback){
		for(var item in this._listeners){
			if(callback === this._listeners[item]){
				this._listeners.splice(callback, 1);
			}
		}
	}
}

NotifierClass.prototype.notify = function(obj){
	if(!obj){
		obj = this;
	}
	//lcl_debug('notify', this._name, obj._name);
	if(this._target_heap[0]){
		var cb = this._target_heap[0];
		try{
			cb(obj);
		}
		catch(err){
			lcl_debug('target callback exception:', err.message, err.name);
			//for(var i in err)
			//{
			//	lcl_debug('err:', i);
			//}
			var error = new Error();
			var entire = cb.toString();
			var body = entire.slice(entire.indexOf('{') + 1, entire.lastIndexOf('}'));
			lcl_debug('-> for', this._name,' : error->', cb.toString(), ': error_stack->', error.stack);
			lcl_debug('-> for', this._name,' : callback->', cb.name, body);
		}
	}
	for (var i in this._listeners){
		var cb = this._listeners[i];
		try{
			cb(obj);
		}
		catch(err){
			lcl_debug('listener callback exception:', err);
			lcl_debug('-> for', this._name,' : callback ->', cb.toString());
		}
	}
	if(this._display_value>0){
		this._displayMessage(this._name + ' : ' + this._value);
	}
	// if(this._is_setting>0){
	// }
}

NotifierClass.prototype.set_enabled = function(val){
	this._enabled = (val>0);
}

exports.NotifierClass = NotifierClass;
