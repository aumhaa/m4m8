// aumhaa_multi_notifier.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;
var ControlClass = require('aumhaa_control_class').ControlClass;


function MultiControlClass(identifier, name, args){
	var self = this;
	this._controls = [];
	this._type = consts.NOTE_TYPE;
	this._onValue = 127;
	this._offValue = 0;
	this._translation = -1;
	this._flash = false;
	this.add_bound_properties(this, ['_name', '_controls']);
	MultiControlClass.super_.call(this, identifier, name, args);
}

util.inherits(MultiControlClass, ControlClass);

MultiControlClass.prototype.add_control = function(control){
	//lcl_debug('MultiControlClass.add_control()', this._name);
	if((this._controls.indexOf(control)==-1)&&(util.isClass(control, 'ControlClass'))){
		this._controls.push(control);
		control.add_listener(this.receive)
		lcl_debug('adding_control:', control._name);
		for(var i in this._grid){
			control.register_grid(i, this._grid[i]);
		}
	}
}

MultiControlClass.prototype.remove_control = function(control){
	var index = this._controls.indexOf(control);
	if(index >-1){
		for(var i in this._grid){
			control.register_grid(i, undefined);
		}
		this._controls.slice(index, 1);
	}
	debug('MultiControlClass.remove_control()', 'controls length are now:', this._controls.length);
}

MultiControlClass.prototype.clear_controls = function(){
	for(var i in this._controls){
		this.remove_control(this._controls[i]);
	}
}

MultiControlClass.prototype.add_controls = function(controls){
	if(controls instanceof Array){
		for(var i in controls){
			this.add_control(controls[i])
		}
	}
	else{
		this.add_control(controls);
	}
}

MultiControlClass.prototype.send = function(value){
	for(var i in this._controls){
		this._controls[i].send(value);
	}
}

MultiControlClass.prototype.receive = function(control){
	lcl_debug('MultiControlClass.receive()', this._name, control._name, control._value);
	this._value = control._value;
	this.notify();
}

MultiControlClass.prototype.receive_notifier = function(notification){
	if(this._enabled){this.send(notification._value);}
}

MultiControlClass.prototype._mask = function(value){
	for(var i in this._controls){
		this._controls[i]._mask(value);
	}
}

MultiControlClass.prototype.reset = function(){
	this.send(0);
}

MultiControlClass.prototype.register_grid = function(name, args){
	this.Super_().prototype.register_grid.call(this, name, args);
	for(var i in this._controls){
		this._controls[i].register_grid(name, args);
	}
}

MultiControlClass.prototype.pressed = function(){
	for(var i in this._controls){
		if(this._controls[i].pressed()){
			return true;
		}
	}
	return false
}

MultiControlClass.prototype.turn_on = function(){
	this.send(this._onValue);
}

MultiControlClass.prototype.turn_off = function(){
	this.send(this._offValue);
}

MultiControlClass.prototype.set_on_off_values = function(onValue, offValue){
	this._onValue = onValue||127;
	this._offValue = offValue||0;
}

MultiControlClass.prototype.set_translation = function(newID){
	this._translation = newID;
}

MultiControlClass.prototype.flash = function(val){
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

MultiControlClass.prototype.get_coords= function(grid){
	// if(grid instanceof GridClass && this._grid[grid._name])
	if(isClass(grid, 'GridClass') && this._grid[grid._name]){
		return([this._grid[grid._name].x, this._grid[grid._name].y]);
	}
	else{
		return([-1, -1]);
	}
}

exports.MultiControlClass = MultiControlClass;



// function MultiButtonClass(id, name, args){
// 	var self = this;
// 	MultiButtonClass.super_.call(this, id, name, args);
// }
//
// util.inherits(MultiButtonClass, ButtonClass);
