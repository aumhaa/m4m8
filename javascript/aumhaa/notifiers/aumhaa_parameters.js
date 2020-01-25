//aumhaa_parameters.js

//need to pass in tasks instance from main script

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;
var GridClass = require('aumhaa_grid_class').GridClass;
var Bindable = require('aumhaa_bindable').Bindable;
var colors = require('aumhaa_notifier_consts').consts.colors;


/////////////////////////////////////////////////////////////////////////////
//Parameter is a notifier that automatically updates its listeners when its state changes
//It can either reflect an internal state or a JavaObject's value, and can be assigned a control


function ParameterClass(name, args){
	this.add_bound_properties(this, ['_onValue', '_offValue', 'receive', 'set_value', 'update_control', '_apiCallback', '_Callback', 'set_control', 'set_on_off_values']);
	this._parameter = undefined;
	this._num = 0;
	this._value = 0;
	this._onValue = 127;
	this._offValue = 0;
	this._text_length = 10;
	this._unassigned = 'None';
	this._apiProperty = 'value';
	this._parent = {tasks:util.nop};
	ParameterClass.super_.call(this, name, args);
	this._Callback.owner = this;
}

util.inherits(ParameterClass, NotifierClass);

ParameterClass.prototype._apiCallback = function(args){
	if(args[0]==this._apiProperty){
		this.receive(args[1]);
	}
}

ParameterClass.prototype.receive = function(value){
	this._value = value;
	this.update_control();
	this.notify();
}

ParameterClass.prototype.set_value = function(value){
	this.receive(value);
}

ParameterClass.prototype.update_control = function(){if(this._control){this._control.send(Math.floor(this._value));}}

ParameterClass.prototype._Callback = function(obj){if(obj){this.receive(obj._value);}}

//ParameterClass.prototype._Callback.prototype.owner = function(){return this;}

ParameterClass.prototype.set_control = function(control){
	// if (control instanceof(NotifierClass) || !control){
	if (isClass(control, 'NotifierClass')|| !control){
		if(this._control){
			this._control.remove_target(this._Callback);
			this._control.reset();
		}
		this._control = control;
		if(this._control){
			this._control.set_target(this._Callback);
			//self.receive(self._value);
			this.update_control();
		}
	}
}

ParameterClass.prototype.set_on_off_values = function(onValue, offValue){
	this._onValue = onValue||127;
	this._offValue = offValue||0;
}

exports.ParameterClass = ParameterClass;



function MomentaryParameter(name, args){
	MomentaryParameter.super_.call(this, name, args);
}

util.inherits(MomentaryParameter, ParameterClass);

MomentaryParameter.prototype.update_control = function(){if(this._control){this._control.send(this._value ? this._onValue : this._offValue);}}

exports.MomentaryParameter = MomentaryParameter;



function ArrayParameter(name, args){
	ArrayParameter.super_.call(this, name, args);
}

util.inherits(ArrayParameter, ParameterClass);

ArrayParameter.prototype.receive = function(value){
	//lcl_debug('array change', arguments, arrayfromargs(arguments));
	if(arguments.length>1){
		this._value = arrayfromargs(arguments);
	}
	else{
		this._value = value;
	}
	this.update_control();
	this.notify();
}

exports.ArrayParameter = ArrayParameter;



function ToggledParameter(name, args){
	this.add_bound_properties(this, ['update_control']);
	ToggledParameter.super_.call(this, name, args);
	this._Callback.owner = this;
}

util.inherits(ToggledParameter, ParameterClass);

ToggledParameter.prototype._Callback = function(obj){
	if(obj._value){
		if(this._apiObj){
			this._apiObj.set(this._apiAction, Math.abs(this._value -1));
		}
		else{
			this.receive(Math.abs(this._value - 1));
		}
	}
}

ToggledParameter.prototype.update_control = function(value){
	if(this._control){this._control.send(this._value > 0 ? this._onValue : this._offValue);}
}

exports.ToggledParameter = ToggledParameter;



function LatchingToggledParameterBehaviour(parent_parameter_object){
	var self = this;
	var parent = parent_parameter_object;
	this.press_immediate = function(button){
		parent.receive(Math.abs(parent._value-1));
	}
	this.press_delayed = function(button){
	}
	this.release_immediate = function(button){
	}
	this.release_delayed = function(button){
		parent.receive(0);
	}
}

exports.LatchingToggledParameterBehaviour = LatchingToggledParameterBehaviour;



function LatchingToggledParameter(name, args){
	var self = this;
	this._timered = function(){
		//debug('timered...', arguments[0]._name);
		button = arguments[0];
		if(button&&button.pressed()){
			this._behaviour.press_delayed(button);
		}
	}
	this._behaviour_timer = new Task(this._timered, this);
	this.add_bound_properties(this, ['_behaviour_timer', '_timered', ]);
	this._behaviour = this._behaviour!= undefined ? new this._behaviour(this) : new LatchingToggledParameterBehaviour(this);
	this._press_delay = this._press_delay ? this._press_delay : PRS_DLY;
	LatchingToggledParameter.super_.call(this, name, args);
	this._Callback.owner = self;
}

util.inherits(LatchingToggledParameter, ToggledParameter);

LatchingToggledParameter.prototype._Callback = function(button){
	if(button.pressed()){
		if(this._behaviour_timer.running){
			this._behaviour_timer.cancel();
		}
		this._behaviour.press_immediate(button);
		this._behaviour_timer.arguments = button;
		this._behaviour_timer.schedule(this._press_delay);
	}
	else{
		if(this._behaviour_timer.running){
			this._behaviour_timer.cancel();
			this._behaviour.release_immediate(button);
		}
		else{
			this._behaviour.release_delayed(button);
		}
	}
	this.notify();
}

exports.LatchingToggledParameter = LatchingToggledParameter;



function RangedParameter(name, args){
	this._range = this._range||128;
	RangedParameter.super_.call(this, name, args);
	this._Callback.owner = this;
}

util.inherits(RangedParameter, ParameterClass);

RangedParameter.prototype._Callback = function(obj){
	if(obj._value!=undefined){
		if(this._javaObj){
			//lcl_debug('Callback', self._name, obj._value);
			this._javaObj.set(obj._value, this._range);
		}
		else{
			this.receive(Math.floor((obj._value/127)*this._range));
		}
	}
}

RangedParameter.prototype.update_control = function(){if(this._control){this._control.send(Math.floor((this._value/this._range)*127));}}

exports.RangedParameter = RangedParameter;



function RangedButtonParameter(name, args){
	this.colors = args['colors'] || [colors.OFF, colors.WHITE, colors.YELLOW, colors.CYAN, colors.MAGENTA, colors.RED, colors.GREEN, colors.BLUE];
	this._range = this._range||8;
	RangedButtonParameter.super_.call(this, name, args);
	this._Callback.owner = this;
}

util.inherits(RangedButtonParameter, ParameterClass)

RangedButtonParameter.prototype._Callback = function(obj){
	if(obj._value){
		if(this._javaObj){
			//lcl_debug('Callback', this._name, obj._value);
			this._javaObj.set(obj._value, this._range);
		}
		else{
			lcl_debug('Callback', this._name, obj._value, (this._value+1)%this._range);
			this.receive(this._value+1%this._range);
		}
	}
}

RangedButtonParameter.prototype.update_control = function(){
	if(this._control){
		for(var c in this.colors){
			lcl_debug(c, 'color:', this.colors[c]);
		}
		lcl_debug('update_control:', this._name, this._value, this.colors.length, this.colors[this._value%(this.colors.length)]);
		this._control.send(this.colors[this._value%(this.colors.length)]);
	}
}

exports.RangedButtonParameter = RangedButtonParameter;



function DelayedRangedParameter(name, args){
	this._delay = 1;
	DelayedRangedParameter.super_.call(this, name, args);
}

util.inherits(DelayedRangedParameter, RangedParameter);

DelayedRangedParameter.prototype.receive = function(value){
	this._value = value;
	this.update_control();
	this._parent.tasks.addTask(this.delayed_receive, [value], this._delay);
}

DelayedRangedParameter.prototype.delayed_receive = function(value){
	if(value == this._value){
		this.notify();
	}
}

exports.DelayedRangedParameter = DelayedRangedParameter;



function ParameterGroup(name, notifiers, args){
	var self = this;
	this.add_bound_properties(this, ['set_controls', 'set_gui_controls']);
	this._notifiers = notifiers;
	ParameterGroup.super_.call(this, name, args);
}

util.inherits(ParameterGroup, Bindable);

ParameterGroup.prototype.set_controls = function(controls){
	// controls = controls instanceof GridClass ? controls.controls() : control instanceof Array ? controls : controls instanceof NotifierClass ? [controls] : [];
	controls = isClass(controls, 'GridClass') ? controls.controls() : control instanceof Array ? controls : isClass(controls, 'NotifierClass') ? [controls] : [];
	for(var i=0;i<this._notifiers.length;i++){
		var control = controls[i]?controls[i]:undefined;
		this._notifiers[i].set_control(control);
	}
}

exports.ParameterGroup = ParameterGroup;



/////////////////////////////////////////////////////////////////////////////
//Notifier that uses two buttons to change an offset value

function OffsetComponent(name, minimum, maximum, initial, callback, onValue, offValue, increment, args){
	this.add_bound_properties(this, ['receive', 'set_value', 'update_control', '_apiCallback', '_Callback', 'set_control', 'incCallback', 'decCallback']);
	this._min = minimum!=undefined?minimum:0;
	this._max = maximum!=undefined?maximum:127;
	this._increment = increment!=undefined?increment:1;
	this._incButton;
	this._decButton;
	this._onValue = onValue!=undefined?onValue:127;
	this._offValue = offValue!=undefined?offValue:0;
	this._displayValues = [this._onValue, this._offValue];
	this._scroll_hold = true;
	this._callback = callback;
	OffsetComponent.super_.call(this, name);
	this._value = initial!=undefined?initial:0;
	this.incCallback.owner = this;
	this.decCallback.owner = this;
	//if(callback!=undefined)
	//{
	//	this._callback = callback;
	//	this.set_target(callback);
	//}
}

util.inherits(OffsetComponent, NotifierClass);

OffsetComponent.prototype._apiCallback = function(args){
	if(args[0]=='value'){
		self.receive(args[1]);
	}
}

OffsetComponent.prototype.incCallback = function(obj){
	if((this._enabled)&&(obj._value>0)){
		this._value = Math.min(this._value + this._increment, this._max);
		this._update_buttons();
		this.notify();
		if(this._scroll_hold){
			this._parent.tasks.addTask(this.incCallback, [obj], 1, false, this._name+'_UpHoldKey');
		}
	}
}

OffsetComponent.prototype.decCallback = function(obj){
	if((this._enabled)&&(obj._value>0)){
		this._value = Math.max(this._value - this._increment, this._min);
		this._update_buttons();
		this.notify();
		if(this._scroll_hold){
			this._parent.tasks.addTask(this.decCallback, [obj], 1, false, this._name+'_DnHoldKey');
		}
	}
}

OffsetComponent.prototype.set_value = function(value){
	this._value = Math.max(Math.min(value, this._max), this._min);
	this._update_buttons();
	this.notify();
}

OffsetComponent.prototype._update_buttons = function(){
	if(this._incButton){
		if((this._value<this._max)&&(this._enabled)){
			this._incButton.send(this._onValue);
		}
		else{
			this._incButton.send(this._offValue);
		}
	}
	if(this._decButton){
		if((this._value>this._min)&&(this._enabled)){
			this._decButton.send(this._onValue);
		}
		else{
			this._decButton.send(this._offValue);
		}
	}
}

OffsetComponent.prototype.set_inc_dec_buttons = function(incButton, decButton){
	// if (incButton instanceof(NotifierClass) || !incButton){
	if (isClass(incButton, 'NotifierClass') || !incButton){
		if(this._incButton){
			this._incButton.remove_target(this.incCallback);
			this._incButton.reset();
		}
		this._incButton = incButton;
		if(this._incButton){
			this._incButton.set_target(this.incCallback);
		}
	}
	// if (decButton instanceof(NotifierClass) || !decButton){
	if (isClass(decButton, 'NotifierClass') || !decButton){
		if(this._decButton){
			this._decButton.remove_target(this.decCallback);
			this._decButton.reset();
		}
		this._decButton = decButton;
		if(this._decButton){
			this._decButton.set_target(this.decCallback);
		}
	}
	this._update_buttons();
}

OffsetComponent.prototype.set_enabled = function(val){
	this._enabled = (val>0);
	this._update_buttons();
}

exports.OffsetComponent = OffsetComponent;



/////////////////////////////////////////////////////////////////////////////
//Notifier that uses multiple buttons to change an offset value, displaying the current value

function RadioComponent(name, minimum, maximum, initial, callback, onValue, offValue, args){
	this.add_bound_properties(this, ['_callback', '_min', '_max', 'set_value', 'update_controls', '_apiCallback', '_Callback', 'set_controls', 'set_enabled']);
	this._min = minimum!=undefined?minimum:0;
	this._max = maximum!=undefined?maximum:1;
	this._buttons = [];
	this._onValue = onValue!=undefined?onValue:127;
	this._offValue = offValue!=undefined?offValue:0;
	this._displayValues = [this._onValue, this._offValue];
	this._callback = callback;
	RadioComponent.super_.call(this, name, args);
	this._value = initial!=undefined?initial:this._min;
	this._Callback.owner = this;
	//debug(this._name, 'initial is:', initial, this._value);
	//if(callback!=undefined)
	//{
	//	this.set_target(callback);
	//}
}

util.inherits(RadioComponent, NotifierClass);

RadioComponent.prototype._apiCallback = function(args){
	if(args[0]=='value'){
		self.receive(args[1]);
	}
}

RadioComponent.prototype._Callback = function(obj){
	lcl_debug('RadioComponent._Callback():', obj);
	if(obj._value){
		var val = this._buttons.indexOf(obj) + this._min;
		this.set_value(val);
	}
}

RadioComponent.prototype.receive = function(value){
	this._value = Math.max(Math.min(value, this._max), this._min);
	this.update_controls();
	this.notify();
}

RadioComponent.prototype.set_controls = function(control){
	// control = (control instanceof Array)||(control instanceof GridClass) ? control : [];
	control = (control instanceof Array)|| isClass(control, 'GridClass') ? control : [];
	for(var i in this._buttons){
		this._buttons[i].remove_target(this._Callback);
		this._buttons[i].reset();
	}
	// this._buttons = control instanceof GridClass ? control.controls() : control;
	this._buttons = isClass(control, 'GridClass') ? control.controls() : control;
	if(this._buttons){
		for(var i in this._buttons){
			if(this._buttons[i]){
				//lcl_debug('assigning radio:', this._buttons[i]._name);
				this._buttons[i].set_target(this._Callback);
			}
		}
	}
	this.update_controls();
}

RadioComponent.prototype.set_value = function(value){
	this.receive(value);
}

RadioComponent.prototype.update_controls = function(){
	for(var i in this._buttons){
		if(this._buttons[i]){
			this._buttons[i].send(this._buttons.indexOf(this._buttons[i]) + this._min ==this._value ? this._onValue : this._offValue);
		}
	}
}

RadioComponent.prototype.set_enabled = function(val){
	this._enabled = (val>0);
	this._update_controls();
}

exports.RadioComponent = RadioComponent;



/////////////////////////////////////////////////////////////////////////////
//Notifier that uses two buttons to change an offset value

function DoubleSliderComponent(name, minimum, maximum, initial_start, initial_end, callback, onValue, offValue, args){
	this.add_bound_properties(this, ['receive', 'set_value', 'update_controls', '_Callback', 'set_controls', 'set_value', 'set_start_value', 'set_end_value']);
	this._min = minimum||0;
	this._max = maximum||16;
	this._start_value = initial_start||0;
	this._end_value = initial_end||16;
	this._buttons = [];
	this._onValue = onValue||127;
	this._offValue = offValue||0;
	this._displayValues = [this._onValue, this._offValue];
	this._callback = callback;
	DoubleSliderComponent.super_.call(this, name, args);
	this._Callback.owner = this;
	//if(callback!=undefined)
	//{
	//	this.set_target(callback);
	//}
}

util.inherits(DoubleSliderComponent, NotifierClass);

DoubleSliderComponent.prototype._Callback = function(obj){
	if(obj._value){
		var button_pressed = false;
		for(var i in this._buttons){
			if(this._buttons[i].pressed()&&(!(this._buttons[i]==obj))){
				button_pressed = this._buttons[i];
				break;
			}
		}
		var val = this._buttons.indexOf(obj) + this._min;
		var ref_index = button_pressed ? this._buttons.indexOf(button_pressed) : val>this._start_value ? this._start_value : this._end_value;
		var set_func = val > ref_index ? this.set_end_value : this.set_start_value;
		set_func(val);
	}
}

DoubleSliderComponent.prototype.receive = function(value){
	this.set_value(value);
}

DoubleSliderComponent.prototype.set_controls = function(control){
	// control = (control instanceof Array)||(control instanceof GridClass) ? control : [];
	control = (isClass(control, 'Array'))||(isClass(control, 'GridClass')) ? control : [];
	for(var i in this._buttons){
		this._buttons[i].remove_target(this._Callback);
	}
	// this._buttons = control instanceof GridClass ? control.controls() : control;
	this._buttons = isClass(control, 'GridClass') ? control.controls() : control;
	if(this._buttons){
		for(var i in this._buttons){
			if(this._buttons[i]){
				this._buttons[i].set_target(this._Callback);
			}
		}
	}
	this.update_controls();
}

DoubleSliderComponent.prototype.set_value = function(value){
	this._value = Math.max(Math.min(value, this._max), this._min);
	this.update_controls();
	this.notify();
}

DoubleSliderComponent.prototype.set_start_value = function(value){
	this._start_value = Math.max(Math.min(value, this._max), this._min);
	this.update_controls();
	this.notify();
}

DoubleSliderComponent.prototype.set_end_value = function(value){
	this._end_value = Math.max(Math.min(value, this._max), this._min);
	this.update_controls();
	this.notify();
}

DoubleSliderComponent.prototype.update_controls = function(){
	for(var i in this._buttons){
		if(this._buttons[i]){
			var index = this._buttons.indexOf(this._buttons[i]) + this._min;
			this._buttons[i].send(index<this._start_value ? this._offValue : index>this._end_value ? this._offValue : this._onValue);
		}
	}
}

DoubleSliderComponent.prototype.set_enabled = function(val){
	this._enabled = (val>0);
	this._update_controls();
}

exports.DoubleSliderComponent = DoubleSliderComponent;
