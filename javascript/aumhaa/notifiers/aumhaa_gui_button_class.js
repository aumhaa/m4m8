// aumhaa_gui_button_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var ControlClass = require('aumhaa_control_class').ControlClass;
var GridClass = require('aumhaa_grid_class').GridClass;
var consts = require('aumhaa_notifier_consts').consts;

function GUIButton(name, args){
	var self = this;
	this._type = consts.NOTE_TYPE;
	this._onValue = 1;
	this._offValue = 0;
	this._flash = false;
	this._grid = {};
	GUIButton.super_.call(this, 0, name, args);
	//var self = this;
}

util.inherits(GUIButton, ControlClass);

GUIButton.prototype.set_send_function = function(func){
	this._send = func;
}

GUIButton.prototype.pressed = function(){
	return this._value > 0;
}

GUIButton.prototype.send = function(value, flash){
	this._last_sent_value = value;
	this._send(value);
}

GUIButton.prototype._send = function(value){lcl_debug('Haven\'t defined _send for GUIButton:', this._name)}

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

GUIButton.prototype.get_coords= function(grid){
	// if(grid instanceof GridClass && this._grid[grid._name]){
	if(isClass(grid, 'GridClass') && this._grid[grid._name]){
		return([this._grid[grid._name].x, this._grid[grid._name].y]);
	}
}

exports.GUIButton = GUIButton;
