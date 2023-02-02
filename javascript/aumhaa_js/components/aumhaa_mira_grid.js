// aumhaa_mira_grid.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;
var GridClass = require('aumhaa_grid_class').GridClass;


function MiraGridComponent(name, args){
	var self = this;
	this._input_gate = true;
	this.add_bound_properties(this, ['_input_gate', '_grid', 'set_grid', 'update', '_button_press']);
	this._pallette = [];
	this._grid = undefined;
	this._cells = undefined;
	this._keys = undefined;
	this._parent = {grid:util.nop, key:util.nop, shift:util.nop, alt:util.nop, main_note_output:util.nop};
	MiraGridComponent.super_.call(this, name, args);
	this._button_press.owner = this;
}

util.inherits(MiraGridComponent, Bindable);

MiraGridComponent.prototype.set_grid = function(grid){
	lcl_debug('MiraGridComponent set_grid', grid);
	// if(this._grid instanceof GridClass){
	if(isClass(this._grid, 'GridClass')){
		this._grid.remove_listener(this._button_press);
	}
	this._grid = grid;
	// if(this._grid instanceof GridClass){
	if(isClass(this._grid, 'GridClass')){
		this._grid.add_listener(this._button_press);
	}
	this._update();
}

MiraGridComponent.prototype.update = function(){}

MiraGridComponent.prototype._button_press = function(){
	var args = arrayfromargs(arguments)
	//debug('MiraGrid._button_press:', args);
	if(args[0] == 'region'){
		var x = args[1]%8;
		var y = Math.floor(args[1]/8);
		var z = args[3] ? 127 : 0;
		if(this._input_gate){
			this._parent.main_note_input.message('list', (x + (Math.abs(y-7)*8) + 36), z);
		}
		this._parent.grid(x, y, z);
	}
}

MiraGridComponent.prototype._key_press = function(){
	var args = arrayfromargs(arguments)
	//debug('MiraGrid._button_press:', args);
	if(args[0] == 'region'){
		this._parent.key(args[1], args[3] ? 127 : 0);
	}
}

MiraGridComponent.prototype._shift_press = function(){
	var args = arrayfromargs(arguments)
	//debug('MiraGrid._button_press:', args);
	if(args[0] == 'region'){
		this._parent.shift(args[3] ? 127 : 0);
	}
}

MiraGridComponent.prototype._alt_press = function(){
	var args = arrayfromargs(arguments)
	//debug('MiraGrid._button_press:', args);
	if(args[0] == 'region'){
		this._parent.alt(args[3] ? 127 : 0);
	}
}

MiraGridComponent.prototype.send = function(x, y, val){
	// this._cells[x + (y*8)].message('bgcolor', ROLI.PALLETTE[val]);
	this._cells[x + (y*8)].message('bgcolor', this.pallette[val]);
}

exports.MiraGridComponent = MiraGridComponent;
