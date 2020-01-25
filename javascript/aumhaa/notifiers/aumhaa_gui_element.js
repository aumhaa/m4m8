// aumhaa_gui_element.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;
var ControlClass = require('aumhaa_control_class').ControlClass;

function GUI_Element(name, args){
	var self = this;
	this._grid = {};
	this.add_bound_properties(this, ['receive', 'receive_notifier', '_x', '_y']);
	ControlClass.super_.call(this, name, args);
}

util.inherits(GUI_Element, NotifierClass);

GUI_Element.prototype.receive = function(value){
	//lcl_debug('receive:', self._name, value);
	if(this._enabled){
		this._value = value;
		this.notify();
	}
}

GUI_Element.prototype.receive_notifier = function(notification){
	if(this._enabled){this.send(notification._value);}
}

GUI_Element.prototype._x = function(grid){if(this._grid[grid._name]!=undefined){return(this._grid[grid._name].x)}}

GUI_Element.prototype._y = function(grid){if(this._grid[grid._name]!=undefined){return(this._grid[grid._name].y)}}

GUI_Element.prototype._send = function(value){}//this should be overridden by subclass

GUI_Element.prototype.send = function(value){
	//midiBuffer[this._type][this._id] = [this, value];
	this._last_sent_value = value;
	this._send(value);
}

GUI_Element.prototype.reset = function(){
	this.send(0);
}

exports.GUI_Element = GUI_Element;
