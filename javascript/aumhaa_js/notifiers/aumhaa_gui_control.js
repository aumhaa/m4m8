// aumhaa_gui_control_class.js
// written 3/29/20 to make use of new jsMaxObjListner object introduced in Max 8.14 beta
// this class can deal with input from mod (using a control_registry to divy calls to its recieve func) or can be used standalone as a maxobject proxy.

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var ControlClass = require('aumhaa_control_class').ControlClass;
var GridClass = require('aumhaa_grid_class').GridClass;
var consts = require('aumhaa_notifier_consts').consts;



function GUIControl(name, args){
	var self = this;
	this.add_bound_properties(this, [
		'set_send_function',
		'get_coords',
		'receive',
		'receive_notifier',
		'_x',
		'_y',
		'_send',
		'send',
		'_momentary'
	]);
	this._valueListener = undefined;
	this._momentary = false;
	GUIControl.super_.call(this, 0, name, args);
	if(this._jsObj){
		this._valueListener = new MaxobjListener(this._jsObj, this.receive);
	}
	// lcl_debug('GUIControl created:', this._name);
}

util.inherits(GUIControl, ControlClass);

GUIControl.prototype.receive = function(maxJsObjListenerData){
	// debug('receive:', this._name, value);
	if(this._enabled){
		var value = maxJsObjListenerData.value;
		this._value = value != undefined ? value : this._momentary ? 1 : 0;
		//lcl_debug('receive:', this._name, this._value);
		this.notify();
		if(this._momentary){
			this._value = 0;
			this.notify();
		}
	}
}

GUIControl.prototype.set_send_function = function(func){
	this._send = func;
}

GUIControl.prototype.send = function(value, flash){
	this._last_sent_value = value;
	this._send(value);
}

GUIControl.prototype._send = function(value){
	//lcl_debug('Haven\'t defined _send for GUIButton:', this._name)
	if(this._valueListener){
		this._valueListener.setvalue(value);
	}
}

GUIControl.prototype.set = function(value){
	this._last_sent_value = value;
	this._set(value);
}

GUIControl.prototype._set = function(value){
	//lcl_debug('Haven\'t defined _send for GUIButton:', this._name)
	// lcl_debug('_set', value);
	if(this._valueListener){
		this._valueListener.setvalue_silent(value);
	}
}

GUIControl.prototype.get_coords= function(grid){
	// if(grid instanceof GridClass && this._grid[grid._name]){
	if(isClass(grid, 'GridClass') && this._grid[grid._name]){
		return([this._grid[grid._name].x, this._grid[grid._name].y]);
	}
}

exports.GUIControl = GUIControl;



function GUIButton(name, args){
	var self = this;
	this.add_bound_properties(this, ['pressed', 'turn_on', 'turn_off', 'set_on_off_values', 'set_translation', 'flash']);
	this._type = consts.MAXOBJ_TYPE;
	this._onValue = 1;
	this._offValue = 0;
	this._flash = false;
	this._skin = consts.MaxColors;
	GUIButton.super_.call(this, name, args);
	this._skin_array = [];
	for(var i in this._skin){
		this._skin_array.push(this._skin[i]);
	}
	this._skin_size = this._skin.length;
}

util.inherits(GUIButton, GUIControl);

GUIButton.prototype.set_skin = function(skin){
	this._skin = skin;
	for(var i in this._skin){
		this._skin_array.push(this._skin[i]);
	}
	this._skin_size = this._skin.length;
}

GUIButton.prototype.pressed = function(){
	return this._value > 0;
}

GUIButton.prototype.turn_on = function(){
	this.send(this._onValue);
}

GUIButton.prototype.turn_off = function(){
	this.send(this._offValue);
}

GUIButton.prototype.set_on_off_values = function(onValue, offValue){
	this._onValue = onValue||127;
	this._offValue = offValue||0;
}

GUIButton.prototype.set_translation = function(newID){
	//lcl_debug(this._name, 'set translation', this._id, newID);
	this._translation = newID;
	//Note_Translation_Table[this._id] = this._translation;
	//recalculate_translation_map = true;
}

GUIButton.prototype.flash = function(val){
	if(val!=this._flash){
		this._flash = val;
		//if(!val)
		//{
		//	flash.remove(this);
		//}
		//else
		//{
		//	flash.add(this);
		//}
	}
}

exports.GUIButton = GUIButton;



function GUIDial(name, args){
	var self = this;
	// this.add_bound_properties(this]);
	this._type = consts.MAXOBJ_TYPE;
	GUIDial.super_.call(this, name, args);
}

util.inherits(GUIDial, GUIControl);

exports.GUIDial = GUIDial;



function GUITextButton(name, args){
	var self = this;
	this.add_bound_properties(this, ['_color_attribute']);
	this._color_attribute = 'bgcolor';
	GUITextButton.super_.call(this, name, args);
}

util.inherits(GUITextButton, GUIButton);

GUITextButton.prototype.pressed = function(){
	return this._value > 0;
}

GUITextButton.prototype.turn_on = function(){
	//this.send(this._onValue);
	if(this._jsObj){
		this._jsObj.setattr(this._color_attribute, this._onValue);
	}
}

GUITextButton.prototype.turn_off = function(){
	if(this._jsObj){
		this._jsObj.setattr(this._color_attribute, this._offValue);
	}
}

GUITextButton.prototype._send = function(value){
	if(this._jsObj){
		// lcl_debug(this._name + '._send:', value);
		var val = value in this._skin ? this._skin[value] : this._skin_array.length > value ? this._skin_array[value] : value;
		this._jsObj.setattr(this._color_attribute, val);
	}
}

// GUIControl.prototype._set = function(value){
// 	this._send(value);
// }

exports.GUITextButton = GUITextButton;



function GUILiveText(name, args){
	var self = this;
	this.add_bound_properties(this, []);
	GUILiveText.super_.call(this, name, args);
	this._color_attribute = 'activebgcolor';
}

util.inherits(GUILiveText, GUITextButton);

exports.GUILiveText = GUILiveText;
