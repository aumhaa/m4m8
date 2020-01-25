// aumhaa_button_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var ControlClass = require('aumhaa_control_class').ControlClass;
var GridClass = require('aumhaa_grid_class').GridClass;
var consts = require('aumhaa_notifier_consts').consts;


function ButtonClass(identifier, name, _send, args){
	var self = this;
	//lcl_debug('making button:', name, this._bound_properties);
	this.add_bound_properties(this, ['get_target', 'set_send_function', 'pressed', 'turn_on', 'turn_off', 'set_on_off_values', 'set_translation', 'flash', 'get_coords', '_grid']);
	this._type = consts.NOTE_TYPE;
	this._onValue = 127;
	this._offValue = 0;
	this._translation = -1;
	this._flash = false;
	this._grid = [];
	ButtonClass.super_.call(this, identifier, name, args);
	this._send = !_send ? function(){lcl_debug('No _send function assigned for:', self._name);} : _send;
	this._mask = this._mask ? this._mask : function(){lcl_debug('No _mask function assigned for:', self._name);};
	//register_control(this);
}

util.inherits(ButtonClass, ControlClass);

ButtonClass.prototype.set_send_function = function(func){
	this._send = func;
}

ButtonClass.prototype.pressed = function(){
	return this._value > 0;
}

ButtonClass.prototype.send = function(value, flash){
	//midiBuffer[this._type][this._id] = [this, value];
	//debug('ButtonClass.send():', value);
	this.flash(flash);
	ControlClass.prototype.send.call(this, value);
	//this.Super_().prototype.send.call(this, value);
}

ButtonClass.prototype.mask = function(value, flash){
	//midiBuffer[this._type][this._id] = [this, value];
	//this.flash(flash);
	//this._last_sent_value = value;
	this._mask(value);
}

ButtonClass.prototype.turn_on = function(){
	this.send(this._onValue);
}

ButtonClass.prototype.turn_off = function(){
	this.send(this._offValue);
}

ButtonClass.prototype.set_on_off_values = function(onValue, offValue){
	this._onValue = onValue||127;
	this._offValue = offValue||0;
}

ButtonClass.prototype.set_translation = function(newID){
	//lcl_debug(this._name, 'set translation', this._id, newID);
	this._translation = newID;
	//Note_Translation_Table[this._id] = this._translation;
	//recalculate_translation_map = true;
}

ButtonClass.prototype.flash = function(val){
	if(val!=this._flash)
	{
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

ButtonClass.prototype.get_coords= function(grid){
	// if(grid instanceof GridClass && this._grid[grid._name])
	if(isClass(grid, 'GridClass') && this._grid[grid._name]){
		return([this._grid[grid._name].x, this._grid[grid._name].y]);
	}
	else{
		return([-1, -1]);
	}
}

exports.ButtonClass = ButtonClass;



function TextButtonClass(identifier, name, _send, args){
	var self = this;
	this.add_bound_properties(this, ['_text_button', 'set_target', 'remove_target', 'clear_targets']);
	TextButtonClass.super_.call(this, identifier, name, _send, args);
}

util.inherits(TextButtonClass, ButtonClass);

TextButtonClass.prototype.update_textbutton = function(){
	//debug('update_textbutton', this._name, this._text_button);
	var target = this.get_target();
	this._text_button && this._text_button.message('text', target ? target.owner._name : '');
}

TextButtonClass.prototype.set_target = function(target){
	if (target){
		if (target in this._target_heap){
			this._target_heap.unshift(this._target_heap.splice(this._target_heap.indexOf(target), 1));
			//this._text_button && this._text_button.message('text', '');
		}
		else{
			this._target_heap.unshift(target);
			//this._text_button && this._text_button.message('text', target.owner ? target.owner._name : 'No Name');
		}
	}
	else{
		this.remove_target();
		//this._text_button && this._text_button.message('text', '');
	}
	this.update_textbutton();
}

TextButtonClass.prototype.remove_target = function(target){
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
	this.update_textbutton();
}

TextButtonClass.prototype.clear_targets = function(){
	this._target_heap = [];
	this.update_textbutton();
}

exports.TextButtonClass = TextButtonClass;
