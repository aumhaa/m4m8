// aumhaa_floating_window.js

var util = require('aumhaa_util');
util.inject(this, util);

var LCL_DEBUG = false;
var lcl_debug = LCL_DEBUG?new util.DebugNamespace('floating_window').debug:function(){};

var Bindable = require('aumhaa_bindable').Bindable;
var ToggledParameter = require('aumhaa_parameters').ToggledParameter;
var colors = require('aumhaa_notifier_consts').consts.colors;

var OFFSET = 0;

function FloatingWindowModule(name, args){
	//debug('way in:', name, args);
	var self = this;
	this._origSizeX = 450;
	this._origSizeY = 700;
	this._sizeX = 450;
	this._sizeY = 700;
	this._nominimize = false;
	this._noclose = false;
	this._nozoom = false;
	this._nogrow = false;
	this._notitle = false;
	this._float = false;
	this._window_position = undefined;
	this.add_bound_properties(this, ['input_from_patcher', '_float_toggle', 'toggle_float', '_toggle', 'toggle_window', '_sizeX', '_sizeY', '_origSizeX', '_origSizeY', '_obj', '_window_position', '_pcontrol', '_thispatcher', 'lock', 'unlock', 'open', 'close', 'store_window_position']);
	FloatingWindowModule.super_.call(this, name, args);
	this._toggle = new ToggledParameter(this._name + '_Toggle', {'onValue':colors.RED, 'offValue':colors.CYAN, 'value':0});
	this._toggle.set_target(this.toggle_window);
	this._floatToggle = new ToggledParameter(this._name + '_FloatToggle', {'onValue':colors.BLUE, 'offValue':colors.CYAN, 'value':0});
	this._floatToggle.set_target(this.toggle_float);
}

util.inherits(FloatingWindowModule, Bindable);

FloatingWindowModule.prototype.input_from_patcher = function(){
  var args = arrayfromargs(arguments);
  try{
    this[args[0]].apply(this, args.slice(1));
  }
  catch(err){
		util.report_error(err);
  }
}

FloatingWindowModule.prototype.toggle_window = function(){
	// debug('toggle window');
	if(this._toggle._value){
		this.open();
	}
	else{
		this.close();
	}
}

FloatingWindowModule.prototype.toggle_float = function(){
	//debug('toggle window');
	if(this._floatToggle._value){
		this._float = true;
		this.lock();
	}
	else{
		this._float = false;
		this.lock();
	}
}

FloatingWindowModule.prototype.open = function(){
	//this._pcontrol.open();
	this._obj.front();
	this._toggle._value = 1;
	this._toggle.update_control();
}

FloatingWindowModule.prototype.floattoggle = function(){
	//this._pcontrol.close();
	this._float = !this._float;
	this.lock();
}

FloatingWindowModule.prototype.close = function(){
	//this._pcontrol.close();
	this._obj.wclose();
	this._toggle._value = 0;
	this._toggle.update_control();
}

FloatingWindowModule.prototype.lock = function(){
	//debug(this._name, 'lock');
	//var pos = settings_thispatcher.getsize();
	//var pos = this._window_position.getvalueof();
	var pos = this._obj.subpatcher().wind.location.map(function(v, i, a){return v+OFFSET;});
	pos[2] = pos[0] + this._sizeX;
	pos[3] = pos[1] + this._sizeY;
	this._obj.window('size', pos[0], pos[1], pos[2], pos[3]);
	this._obj.window('flags', this._nominimize ? 'nominimize' : 'minimize');
	this._obj.window('flags', this._nozoom ? 'nozoom' : 'zoom');
	this._obj.window('flags', this._noclose ? 'noclose' : 'close');
	this._obj.window('flags', this._nogrow ? 'nogrow' : 'grow');
	this._obj.window('flags', this._notitle ? 'notitle' : 'title');
	this._obj.window('flags', this._float ? 'float' : 'nofloat');
	this._obj.window('exec');
}

FloatingWindowModule.prototype.unlock = function(){
	var pos = [100, 100, 500, 500];
	// pos[2] = pos[0] + this._sizeX;
	// pos[3] = pos[1] + this._sizeY;
	this._obj.window('size', pos[0], pos[1], pos[2], pos[3]);
	this._obj.window('flags', 'minimize');
	this._obj.window('flags', 'zoom');
	this._obj.window('flags', 'close');
	this._obj.window('flags', 'grow');
	this._obj.window('flags', 'title');
	this._obj.window('flags', 'nofloat');
	this._obj.window('exec');
}

FloatingWindowModule.prototype.resize = function(sizeX, sizeY){
	//var pos = this._window_position.getvalueof();
	var pos = this._obj.subpatcher().wind.location.map(function(v, i, a){return v+OFFSET;});
	//lcl_debug('pos:', pos[0], pos[1], pos[2], pos[3]);
	this._sizeX = sizeX;
	this._sizeY = sizeY;
	pos[2] = pos[0] + this._sizeX;
	pos[3] = pos[1] + this._sizeY;
	//lcl_debug(pos[0], pos[1], pos[2], pos[3]);
	this._obj.window('size', pos[0], pos[1], pos[2], pos[3]);
	this._obj.window('exec');
}

FloatingWindowModule.prototype.set_to_original_size = function(){
	this.resize(this._origSizeX, this._origSizeY);
}

FloatingWindowModule.prototype.store_window_position = function(){
	//this._thispatcher.message('window', 'getsize');
	//debug('storing window position:', pos);
	if(this._window_position)
	{
		this._window_position.message(this._obj.subpatcher().wind.location.map(function(v, i, a){return v+OFFSET;}));
	}
}

exports.FloatingWindowModule = FloatingWindowModule;
