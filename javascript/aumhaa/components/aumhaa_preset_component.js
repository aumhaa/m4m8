// aumhaa_preset_component
// transferred 071519
// untested

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = true;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;


function PresetComponent(name, storage, storage_menu, args){
	var self = this;
	this.add_bound_properties(this, ['_presets', '_storage', '_storage_menu', '_current_pset']);
	this._storage = storage;
	this._storage_menu = storage_menu;
	this._current_pset = 0;
	PresetComponent.super_.call(this, name, args);
}

util.inherits(PresetComponent, Bindable);

PresetComponent.prototype.read = function(){
	this._storage.message('read');
}

PresetComponent.prototype.write = function(){
	this._storage.message('write');
}

PresetComponent.prototype.del = function(){
	if(this._current_pset){
		this._storage.message('remove', current_pset);
		this._storage.message('getslotnamelist');
	}
}

PresetComponent.prototype.clear = function(){

}

PresetComponent.prototype.recall = function(){
	var args = arrayfromargs(arguments);
	lcl_debug('PresetComponent.recall():', args[1]);
	if(!args[1]){
		this._storage.message('recall', 1);
	}
	else{
		//Device._dict._initialize();
		args[1] = args[1] ? args[1] : 1;
		this._current_pset = args[1];
		storage_menu.message('set', this._current_pset-1);
	}
}

PresetComponent.prototype.text = function(){
	var args = arrayfromargs(arguments);
	lcl_debug('PresetComponent.text:', args);
	args.shift();
	var name = args.join(' ');
	lcl_debug('create_preset:', name);
	this._storage.message('insert', 1);
	this._storage.message('slotname', 1, name);
	this._storage_text.message('clear');
	this._storage.message('getslotnamelist');
}

PresetComponent.prototype.menu = function(){
	var args = arrayfromargs(arguments);
	lcl_debug('storage menu:', args);
	this._storage.message(args[1]+1);
}

PresetComponent.prototype.slotname = function(){
	var args = arrayfromargs(arguments);
	lcl_debug('PresetComponent.slotname:', args);
	if(args[1]==0){
		this._storage_menu.message('clear');
	}
	else if(args[1]=='done'){
	}
	else{
		args.splice(0,2);
		args.unshift('append');
		this._storage_menu.message(args);
	}
}

exports.PresetComponent = PresetComponent;



function PresetSelector(name, parent, args){
	var self = this;
	this._parent = parent;
	this.add_bound_properties(this, ['_parent']);
	PresetSelector.super_.call(this, args);
}

util.inherits(PresetSelector, Bindable);

PresetSelector.prototype.__init = function(){

}

PresetSelector.prototype.recall = function(num){}


exports.PresetSelector = PresetSelector;
