// aumhaa_grid_class.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;


/////////////////////////////////////////////////////////////////////////////
//A notifier that collects a grid of buttons

function GridClass(width, height, name, args){
	var self = this;
	this.add_bound_properties(this, ['get_target', 'mask', 'add_control', 'controls', 'receive', 'get_button', 'reset', 'clear_buttons', 'sub_grid', 'clear_translations', 'button_coords']);
	//lcl_debug('making GridClass:', width, height, name, args, this._bound_properties);
	//this._bound_properties = ['receive'];
	var contents = [];
	for(var i = 0; i < width; i++){
		contents[i] = [];
		for(var j = 0; j < height; j++){
			contents[i][j] = undefined;
		}
	}
	this._grid = contents;
	this.width = function(){return width;}
	this.height = function(){return height;}
	this.size = function(){return width * height;}
	GridClass.super_.call(this, name, args);
}

util.inherits(GridClass, NotifierClass);

GridClass.prototype.receive = function(button){this.notify(button);}

GridClass.prototype.controls = function(){
	var buttons = [];
	for(var y=0;y<this.height();y++){
		for(var x=0;x<this.width();x++){
			// if(this._grid[x][y] instanceof NotifierClass){
			if(isClass(this._grid[x][y], 'NotifierClass')){
				buttons.push(this._grid[x][y]);
			}
		}
	}
	return buttons;
}

GridClass.prototype.add_control = function(x, y, button){
	if(x < this.width()){
		if(y < this.height()){
			// if(button instanceof NotifierClass){
			if(isClass(button, 'ControlClass')){
				this._grid[x][y] = button;
				//button._grid[this._name] = {x:x, y:y, obj:this};
				button.register_grid(this._name, {x:x, y:y, obj:this});
				button.add_listener(this.receive);
			}
		}
	}
}

GridClass.prototype.send = function(x, y, value){
	this._grid[x][y].send(value);
}

GridClass.prototype.mask = function(x, y, value){
	this._grid[x][y].mask(value);
}

GridClass.prototype.get_button = function(x, y){
	var button = undefined;
	if(this._grid[x]){
		if(this._grid[x][y]){
			button = this._grid[x][y];
		}
	}
	return button;
}

GridClass.prototype.reset = function(){
	var buttons = this.controls();
	for (var index in buttons){
		// if(buttons[index] instanceof NotifierClass){
		if(isClass(buttons[index], 'NotifierClass')){
			buttons[index].reset();
		}
	}
}

GridClass.prototype.clear_buttons = function(){
	var buttons = this.controls();
	for (var i in buttons){
		// if(buttons[i] instanceof NotifierClass){
		if(isClass(buttons[i], 'NotifierClass')){
			buttons[i].remove_listener(this.receive);
			delete buttons[i]._grid[this._name];
		}
	}
	var contents = [];
	for(var i = 0; i < this.width(); i++){
		contents[i] = [];
		for(var j = 0; j < this.height(); j++){
			contents[i][j] = undefined;
		}
	}
	this._grid = contents;
}

GridClass.prototype.sub_grid = function(subject, x_start, x_end, y_start, y_end){
	for(var x=0;x<(x_end-x_start);x++){
		for(var y=0;y<(y_end-y_start);y++){
			var button = subject.get_button(x+x_start, y+y_start);
			//lcl_debug('adding button', button._name);
			this.add_control(x, y, button);
		}
	}
	return this;
}

GridClass.prototype.clear_translations = function(){
	var buttons = this.controls();
	for(var index in buttons){
		if(buttons[index]){
			buttons[index].set_translation(-1);
		}
	}
}

GridClass.prototype.button_coords = function(button){
	for(var y=0;y<this.height();y++){
		for(var x=0;x<this.width();x++){
			if(this._grid[x][y] == button){
				return [x, y];
			}
		}
	}
	return false;
}

exports.GridClass = GridClass;
