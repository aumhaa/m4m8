//aumhaa_event_emitter.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;

var indexOf;
if(typeof Array.prototype.indexOf === 'function'){
  indexOf = function (haystack, needle) {
    return haystack.indexOf(needle);
	};
}
else{
  indexOf = function (haystack, needle) {
    var i = 0, length = haystack.length, idx = -1, found = false;
    while (i < length && !found) {
      if (haystack[i] === needle) {
        idx = i;
        found = true;
      }
    	i++;
    }
    return idx;
	};
};


function EventEmitter(name, args){
	this._events = {};
	this.add_bound_properties(this, [
		 '_events',
		 'on',
		 'off',
		 'emit',
		 'once'
	]);
	EventEmitter.super_.call(this, name, args);
};

util.inherits(EventEmitter, Bindable);

EventEmitter.prototype.on = function(event, listener){
		this.off(event, listener);
    if (typeof this._events[event] !== 'object') {
        this._events[event] = [];
    }
    this._events[event].push(listener);
};

EventEmitter.prototype.off = function(event, listener){
    var idx;
    if (typeof this._events[event] === 'object') {
        idx = indexOf(this._events[event], listener);
        if (idx > -1) {
            this._events[event].splice(idx, 1);
        }
    }
};

EventEmitter.prototype.emit = function(event){
    var i, listeners, length, args = [].slice.call(arguments, 1);
		try{
        listeners = this._events[event].slice();
        length = listeners.length;
        for (i = 0; i < length; i++) {
            listeners[i].apply(this, args);
        }
    }
		catch(e){
			e.message = 'emit error' + e.message;
			LOCAL_DEBUG && util.report_error(e);
		}
};

EventEmitter.prototype.once = function(event, listener){
    this.on(event, function g () {
        this.off(event, g);
        listener.apply(this, arguments);
    });
};

exports.EventEmitter = EventEmitter;
