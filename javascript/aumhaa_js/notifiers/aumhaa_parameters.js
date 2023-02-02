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

function toControlArray(controls){
	return isClass(controls, 'GridClass') ? controls.controls() : controls instanceof Array ? controls : isClass(controls, 'NotifierClass') ? [controls] : [];
}

function buttonPressedInGroup(buttons_group){
	return buttons_group.reduce(function(found, button){
		return found ? true : button.pressed() ? true : false;
	}, false);
}

function buttonInGroup(button_groups, button){
	return button_groups.reduce(function(parent, group){
		return parent != undefined ? parent : group.indexOf(button)>-1 ? group : undefined;
	}, undefined);
}

/////////////////////////////////////////////////////////////////////////////
//Parameter is a notifier that automatically updates its listeners when its state changes
//It can either reflect an internal state or a JavaObject's value, and can be assigned a control


function ParameterClass(name, args){
	this.add_bound_properties(this, [
		'_onValue',
		'_offValue',
		'receive',
		'set_value',
		'update_single_control',
		'update_control',
		'_apiCallback',
		'_Callback',
		'set_control',
		'add_control',
		'remove_control',
		'clear_controls',
		'set_on_off_values',
		'_parent',
		'_control',
		'_controls'
	]);
	this._control = undefined;
	this._controls = [];
	this._parameter = undefined;
	this._num = 0;
	this._value = 0;
	this._onValue = 127;
	this._offValue = 0;
	this._text_length = 10;
	this._unassigned = 'None';
	this._apiProperty = 'value';
	//this._parent = {tasks:util.nop};
	ParameterClass.super_.call(this, name, args);
	this._Callback.owner = this;
}

util.inherits(ParameterClass, NotifierClass);

// ParameterClass.prototype.__defineGetter__('_control', function(){
// 	// lcl_debug('_control.getter:', this._name, JSON.stringify(this));
// 	return this._controls.length ? this._controls[0] : undefined;
// });

// ParameterClass.prototype.__defineSetter__('_control', function(control){
// 	lcl_debug('_control.setter:', control, this._name);
// 	var index = this._controls.indexOf(control);
// 	if(index>-1){
// 		this._controls.splice(index, 1);
// 	}
// 	this._controls.push(control);
// });

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

ParameterClass.prototype.update_single_control = function(control){if(control){control.send(Math.floor(this._value));}}

ParameterClass.prototype.update_control = function(){
	for(var i in this._controls){
		this.update_single_control(this._controls[i]);
	}
}

ParameterClass.prototype._Callback = function(obj){if(obj){this.receive(obj._value);}}

//ParameterClass.prototype._Callback.prototype.owner = function(){return this;}

ParameterClass.prototype.set_control = function(control){
	// if (control instanceof(NotifierClass) || !control){
	if (isClass(control, 'NotifierClass')|| !control){
		this.clear_controls();
		this.add_control(control);
	}
}

ParameterClass.prototype.add_control = function(control){
	if (isClass(control, 'NotifierClass')){
		var index = this._controls.indexOf(control);
		if(index==-1){
			this._controls.push(control);
			control.set_target(this._Callback);
		}
		if(this._control==undefined){
			this._control = control;
		}
		this.update_control();
	}
}

ParameterClass.prototype.remove_control = function(control){
	lcl_debug(this._name, 'remove_control', control._name);
	if (isClass(control, 'NotifierClass')){
		var index = this._controls.indexOf(control);
		if(index>-1){
			this._controls.splice(index, 1);
			control.remove_target(this._Callback);
		}
		control.reset();
		if(this._control == control){
			this._control = this._controls.length ? this._controls[0] : undefined;
		}
	}
}

ParameterClass.prototype.clear_controls = function(){
	lcl_debug(this._name, 'clear_controls:', this._controls.length);
	var controls = this._controls.slice();
	controls.forEach(function(control, i){
		lcl_debug(control._name, i);
	});
	controls.forEach(this.remove_control);
	lcl_debug('length is now:', this._controls.length);
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

MomentaryParameter.prototype.update_single_control = function(control){if(control){control.send(this._value ? this._onValue : this._offValue);}}

exports.MomentaryParameter = MomentaryParameter;



function ArrayParameter(name, args){
	ArrayParameter.super_.call(this, name, args);
}

util.inherits(ArrayParameter, ParameterClass);

ArrayParameter.prototype.receive = function(value){
	//lcl_debug('array change', arguments, arrayfromargs(arguments));
	// lcl_debug('receive:', value);
	// if(arguments.length>1){
	// 	this._value = arrayfromargs(arguments);
	// }
	// else{
	// 	this._value = value;
	// }
	if(util.isArray(value)){
		this._value = value;
	}
	else if(typeof value == 'string'){
		this._value = [value];
	}
	else{
		this._value = [];
	}

	this.update_control();
	this.notify();
}

exports.ArrayParameter = ArrayParameter;



function ToggledParameter(name, args){
	this.add_bound_properties(this, ['update_control', '_onValue', '_offValue']);
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

ToggledParameter.prototype.update_single_control = function(control){
	if(control){control.send(this._value > 0 ? this._onValue : this._offValue);}
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

RangedParameter.prototype.update_single_control = function(control){if(control){control.send(Math.floor((this._value/this._range)*127));}}

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
			// lcl_debug('Callback', this._name, obj._value, (this._value+1)%this._range);
			this.receive(this._value+1%this._range);
		}
	}
}

RangedButtonParameter.prototype.update_single_control = function(control){
	if(control){
		// for(var c in this.colors){
		// 	lcl_debug(c, 'color:', this.colors[c]);
		// }
		// lcl_debug('update_single_control:', this._name, this._value, this.colors.length, this.colors[this._value%(this.colors.length)]);
		control.send(this.colors[this._value%(this.colors.length)]);
	}
}

exports.RangedButtonParameter = RangedButtonParameter;


//no idea what this is used by, but some of it's dependencies were altered without testing 071720
function DelayedRangedParameter(name, args){
	this._delay = 1;
	this.require_dependencies(this, ['_parent']);
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



function ParameterGroup(name, parameters, args){
	var self = this;
	this.add_bound_properties(this, [
		'_parameters',
		'set_controls',
		'add_controls',
		'remove_controls',
		'clear_controls',
		'_controls',
		'_controls_groups'
	]);
	this._parameters = parameters;
	this._controls = [];
	this._controls_groups = [];
	ParameterGroup.super_.call(this, name, args);
}

util.inherits(ParameterGroup, ParameterClass);

ParameterGroup.prototype.set_controls = function(controls){
	// controls = isClass(controls, 'GridClass') ? controls.controls() : controls instanceof Array ? controls : isClass(controls, 'NotifierClass') ? [controls] : [];
	controls = toControlArray(controls);
	for(var i=0;i<this._parameters.length;i++){
		var control = controls[i]?controls[i]:undefined;
		this._parameters[i].set_control(control);
	}
}

ParameterGroup.prototype.add_controls = function(controls){
	// controls = isClass(controls, 'GridClass') ? controls.controls() : controls instanceof Array ? controls : isClass(controls, 'NotifierClass') ? [controls] : [];
	controls = toControlArray(controls);
	for(var i=0;i<this._parameters.length;i++){
		var control = controls[i]?controls[i]:undefined;
		this._parameters[i].add_control(control);
	}
}

ParameterGroup.prototype.remove_controls = function(controls){
	// controls = isClass(controls, 'GridClass') ? controls.controls() : controls instanceof Array ? controls : isClass(controls, 'NotifierClass') ? [controls] : [];
	lcl_debug(this._name, 'remove_controls');
	controls = toControlArray(controls);
	for(var i=0;i<this._parameters.length;i++){
		var control = controls[i]?controls[i]:undefined;
		this._parameters[i].remove_control(control);
	}
}

ParameterGroup.prototype.clear_controls = function(controls){
	for(var i=0;i<this._parameters.length;i++){
		this._parameters[i].clear_controls();
	}
}

exports.ParameterGroup = ParameterGroup;



/////////////////////////////////////////////////////////////////////////////
//Notifier that uses two buttons to change an offset value

//inc/dec functions need to be separated for more convenient internal calls can be made.

function OffsetComponent(name, minimum, maximum, initial, callback, onValue, offValue, increment, args){
	this.add_bound_properties(this, [
		'receive',
		'set_value',
		'update_control',
		'_apiCallback',
		'_Callback',
		'set_control',
		'incCallback',
		'decCallback',
		'_incButton',
		'_decButton',
		'_incButtons',
		'_decButtons',
		'set_inc_dec_buttons',
		'add_inc_dec_buttons',
		'remove_inc_dec_buttons',
		'clear_inc_dec_buttons',
		'set_inc_button',
		'set_dec_button',
		'add_inc_button',
		'add_dec_button',
		'remove_inc_button',
		'remove_dec_button',
		'clear_inc_button',
		'clear_dec_button',
		'_update_buttons',
		'_update_single_inc_button',
		'_update_single_dec_button'
	]);
	this._min = minimum!=undefined?minimum:0;
	this._max = maximum!=undefined?maximum:127;
	this._increment = increment!=undefined?increment:1;
	this._incButton;
	this._decButton;
	this._incButtons = [];
	this._decButtons = [];
	this._onValue = onValue!=undefined?onValue:127;
	this._offValue = offValue!=undefined?offValue:0;
	this._displayValues = [this._onValue, this._offValue];
	this._scroll_hold = false;
	this._scroll_delay = 1;
	this._callback = callback;
	OffsetComponent.super_.call(this, name, args);
	//something, somewhere uses this bc it sends its parent's task group to constructor
	//...find it and kill it.  In the meantime....
	if(this._parent&&this._parent.tasks){
		this._scroll_hold = true;
		this._tasks = this._parent.tasks;
	}
	this._scroll_hold&&this.require_dependencies(this, ['_tasks']);
	this.check_dependencies();
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
			this._tasks.addTask(this.incCallback, [obj], this._scroll_delay, false, this._name+'_UpHoldKey');
		}
	}
}

OffsetComponent.prototype.decCallback = function(obj){
	if((this._enabled)&&(obj._value>0)){
		this._value = Math.max(this._value - this._increment, this._min);
		this._update_buttons();
		this.notify();
		if(this._scroll_hold){
			this._tasks.addTask(this.decCallback, [obj], this._scroll_delay, false, this._name+'_DnHoldKey');
		}
	}
}

OffsetComponent.prototype.set_value = function(value){
	this._value = Math.max(Math.min(value, this._max), this._min);
	this._update_buttons();
	this.notify();
}

OffsetComponent.prototype._update_buttons = function(){
	// var _update_single_inc_button = function(incButton){
	// 	if(incButton){
	// 		if((this._value<this._max)&&(this._enabled)){
	// 			incButton.send(this._onValue);
	// 		}
	// 		else{
	// 			incButton.send(this._offValue);
	// 		}
	// 	}
	// }
	// var _update_single_dec_button = function(decButton){
	// 	if(decButton){
	// 		if((this._value>this._min)&&(this._enabled)){
	// 			decButton.send(this._onValue);
	// 		}
	// 		else{
	// 			decButton.send(this._offValue);
	// 		}
	// 	}
	// }

	for(var i in this._incButtons){
		this._update_single_inc_button(this._incButtons[i]);
	}
	for(var i in this._decButtons){
		this._update_single_dec_button(this._decButtons[i]);
	}
}

OffsetComponent.prototype._update_single_inc_button = function(incButton){
	if(incButton){
		if((this._value<this._max)&&(this._enabled)){
			incButton.send(this._onValue);
		}
		else{
			incButton.send(this._offValue);
		}
	}
}

OffsetComponent.prototype._update_single_dec_button = function(decButton){
	if(decButton){
		if((this._value>this._min)&&(this._enabled)){
			decButton.send(this._onValue);
		}
		else{
			decButton.send(this._offValue);
		}
	}
}

OffsetComponent.prototype.set_inc_button = function(incButton){
	if (isClass(incButton, 'NotifierClass') || !incButton){
		this.clear_inc_buttons();
		this._incButton = incButton;
		this.add_inc_button(this._incButton);
	}
}

OffsetComponent.prototype.set_dec_button = function(decButton){
	if (isClass(decButton, 'NotifierClass') || !decButton){
		this.clear_dec_buttons();
		this._decButton = decButton;
		this.add_dec_button(this._decButton);
	}
}

OffsetComponent.prototype.add_inc_button = function(incButton){
	if (isClass(incButton, 'NotifierClass')){
		var index = this._incButtons.indexOf(incButton);
		if(index==-1){
			this._incButtons.push(incButton);
			incButton.set_target(this.incCallback);
		}
		if(this._incButton == undefined){
			this._incButton = incButton;
		}
	}
}

OffsetComponent.prototype.add_dec_button = function(decButton){
	if (isClass(decButton, 'NotifierClass')){
		var index = this._decButtons.indexOf(decButton);
		if(index==-1){
			this._decButtons.push(decButton);
			decButton.set_target(this.decCallback);
		}
		if(this._decButton == undefined){
			this._decButton = decButton;
		}
	}
}

OffsetComponent.prototype.remove_inc_button = function(incButton){
	if (isClass(incButton, 'NotifierClass')){
		var index = this._incButtons.indexOf(incButton);
		if(index>-1){
			this._incButtons.splice(index, 1);
			incButton.remove_target(this.incCallback);
			incButton.reset();
		}
	}
	if(this._incButton = incButton){
		this._incButton = this._incButtons.length ? this._incButtons[0] : undefined;
	}
}

OffsetComponent.prototype.remove_dec_button = function(decButton){
	if (isClass(decButton, 'NotifierClass')){
		var index = this._decButtons.indexOf(decButton);
		if(index>-1){
			this._decButtons.splice(index, 1);
			decButton.remove_target(this.decCallback);
			decButton.reset();
		}
	}
	if(this._decButton = decButton){
		this._decButton = this._decButtons.length ? this._decButtons[0] : undefined;
	}
}

OffsetComponent.prototype.clear_inc_buttons = function(){
	// for(var i in this._incButtons){
	// 	this._remove_inc_button(this._incButtons[i]);
	// }
	var incButtons = this._incButtons.slice();
	incButtons.forEach(this.remove_inc_button);
}

OffsetComponent.prototype.clear_dec_buttons = function(){
	// for(var i in this._decButtons){
	// 	this._remove_dec_button(this._decButtons[i]);
	// }
	var decButtons = this._decButtons.slice();
	decButtons.forEach(this.remove_dec_button);
}

OffsetComponent.prototype.set_inc_dec_buttons = function(incButton, decButton){
	// lcl_debug('set_inc_dec_buttons:', incButton, decButton);
	this.set_inc_button(incButton);
	this.set_dec_button(decButton);
	this._update_buttons();
}

OffsetComponent.prototype.add_inc_dec_buttons = function(incButton, decButton){
	this.add_inc_button(incButton);
	this.add_dec_button(decButton);
	this._update_buttons();
}

OffsetComponent.prototype.remove_inc_dec_buttons = function(incButton, decButton){
	this.remove_inc_button(incButton);
	this.remove_dec_button(decButton);
}

OffsetComponent.prototype.clear_inc_dec_buttons = function(){
	this.clear_inc_buttons();
	this.clear_dec_buttons();
}

OffsetComponent.prototype.set_enabled = function(val){
	this._enabled = (val>0);
	this._update_buttons();
}

OffsetComponent.prototype.set_range = function(min, max){
	this._min = min;
	this._max = max;
	this.set_value(Math.max(this._min, Math.min(this._max, this._value)));
}

exports.OffsetComponent = OffsetComponent;



/////////////////////////////////////////////////////////////////////////////
//Notifier that uses multiple buttons to change an offset value, displaying the current value

function RadioComponent(name, minimum, maximum, initial, callback, onValue, offValue, args){
	this.add_bound_properties(this, [
		'_callback',
		'_min',
		'_max',
		'set_value',
		'_buttons',
		'_buttons_groups',
		'update_controls',
		'update_controls_group',
		'_apiCallback',
		'_Callback',
		'set_controls',
		'add_controls',
		'remove_controls',
		'clear_controls',
		'set_enabled'
	]);
	this._min = minimum!=undefined?minimum:0;
	this._max = maximum!=undefined?maximum:1;
	this._buttons = [];
	this._buttons_groups = [];
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
	lcl_debug('RadioComponent._Callback():', obj._name, obj._value);
	if(obj._value){
		var val = this._buttons.indexOf(obj) + this._min;
		lcl_debug('val is:', val);
		this.set_value(val);
	}
}

RadioComponent.prototype.receive = function(value){
	this._value = Math.max(Math.min(value, this._max), this._min);
	this.update_controls();
	this.notify();
}

RadioComponent.prototype.set_controls = function(controls){
	// controls = (controls instanceof Array) ? controls : isClass(controls, 'GridClass') ? controls.controls() : [];
	// controls = toControlArray(controls);
	this.clear_controls();
	this.add_controls(controls);
}

RadioComponent.prototype.add_controls = function(controls){
	// controls = (controls instanceof Array) ? controls : isClass(controls, 'GridClass') ? controls.controls() : undefined;
	controls = toControlArray(controls);
	if(controls.length){
		var index = this._buttons_groups.indexOf(controls);
		if(index==-1){
			// lcl_debug(this._name, 'add_controls', controls);
			this._buttons_groups.push(controls);
			for(var i in controls){
				if(controls[i]&&isClass(controls[i], 'NotifierClass')){
					controls[i].set_target(this._Callback);
				}
			}
		}
		//what IS THIS SHIT???
		// if(this._buttons==[]){
		// 	lcl_debug('this._buttons==[]');
		// 	this._buttons = controls;
		// 	lcl_debug('and now is our controls', controls);
		// }
		this._buttons = controls;
		this.update_controls();
	}
}

RadioComponent.prototype.remove_controls = function(controls){
	// controls = (controls instanceof Array) ? controls : isClass(controls, 'GridClass') ? controls.controls() : [];
	controls = toControlArray(controls);
	// lcl_debug(this._name, 'remove_controls');
	if(controls.length){
		// var index = this._buttons_groups.indexOf(controls);
		var index = arrayIndexOf(this._buttons_groups, controls);
		// lcl_debug(this._name, 'remove_controls index:', index);
		if(index>-1){
			this._buttons_groups.splice(index, 1);
			for(var i in controls){
				if(controls[i]){
					controls[i].remove_target(this._Callback);
					controls[i].reset();
				}
			}
		}
	}
	if(controls == this._buttons){
		this._buttons = this._buttons_groups.length ? this._buttons_groups[0] : [];
	}
}

RadioComponent.prototype.clear_controls = function(controls){
	// for(var group in this._buttons_groups){
	// 	this.remove_controls(this._buttons_groups[group]);
	// }
	var groups = this._buttons_groups.slice();
	groups.forEach(this.remove_controls);
	// lcl_debug(this._name, 'cleared controls', this._buttons_groups);
}

RadioComponent.prototype.set_value = function(value){
	this.receive(value);
}

RadioComponent.prototype.update_controls = function(){
	for(var i in this._buttons_groups){
		this.update_controls_group(this._buttons_groups[i]);
	}
}

RadioComponent.prototype.update_controls_group = function(button_group){
	// debug('update_controls_group', button_group, JSON.stringify(button_group));
	for(var i in button_group){
		var button = button_group[i];
		if(button){
			button.send(button_group.indexOf(button) + this._min ==this._value ? this._onValue : this._offValue);
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
	this.add_bound_properties(this, [
		'receive',
		'set_value',
		'update_controls',
		'update_controls_groups',
		'_Callback',
		'set_controls',
		'add_controls',
		'remove_controls',
		'clear_controls',
		'set_value',
		'set_start_value',
		'set_end_value'
	]);
	this._min = minimum||0;
	this._max = maximum||16;
	this._start_value = initial_start||0;
	this._end_value = initial_end||16;
	this._buttons = [];
	this._buttons_groups = [];
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
		var buttons_group = buttonInGroup(this._buttons_groups, obj);
		for(var i in buttons_group){
			if(buttons_group[i].pressed()&&(!(buttons_group[i]==obj))){
				button_pressed = buttons_group[i];
				break;
			}
		}
		var val = buttons_group.indexOf(obj) + this._min;
		var ref_index = button_pressed ? buttons_group.indexOf(button_pressed) : val>this._start_value ? this._start_value : this._end_value;
		var set_func = val > ref_index ? this.set_end_value : this.set_start_value;
		set_func(val);
	}
}

DoubleSliderComponent.prototype.receive = function(value){
	this.set_value(value);
}

DoubleSliderComponent.prototype.set_controls = function(controls){
	this.clear_controls();
	this.add_controls(controls);
}

DoubleSliderComponent.prototype.add_controls = function(controls){
	controls = toControlArray(controls);
	if(controls.length){
		var index = this._buttons_groups.indexOf(controls);
		if(index==-1){
			this._buttons_groups.push(controls);
			for(var i in controls){
				if(controls[i]){
					controls[i].set_target(this._Callback);
				}
			}
		}
		if(this._buttons==[]){
			this._buttons = controls;
		}
		this.update_controls();
	}
}

DoubleSliderComponent.prototype.remove_controls = function(controls){
	// lcl_debug(this._name, 'remove_controls');
	controls = toControlArray(controls);
	if(controls.length){
		// var index = this._buttons_groups.indexOf(controls);
		var index = arrayIndexOf(this._buttons_groups, controls);
		// var newIndex = arrIndexOf(this._buttons_groups, controls);
		lcl_debug(this._name, 'remove_controls index:', index);
		if(index>-1){
			this._buttons_groups.splice(index, 1);
			for(var i in controls){
				if(controls[i]){
					lcl_debug('removing target from:', controls[i]._name);
					controls[i].remove_target(this._Callback);
					controls[i].reset();
				}
			}
		}
	}
	if(controls = this._buttons){
		this._buttons = this._buttons_groups.length ? this._buttons_groups[0] : [];
	}
}

DoubleSliderComponent.prototype.clear_controls = function(controls){
	// lcl_debug(this._name, 'clear_controls');
	// for(var group in this._buttons_groups){
	// 	this.remove_controls(this._buttons_groups[group]);
	// }
	var groups = this._buttons_groups.slice();
	groups.forEach(this.remove_controls);
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
	for(var i in this._buttons_groups){
		this.update_controls_group(this._buttons_groups[i]);
	}
}

DoubleSliderComponent.prototype.update_controls_group = function(controls_group){
	for(var i in controls_group){
		if(controls_group[i]){
			var index = controls_group.indexOf(controls_group[i]) + this._min;
			controls_group[i].send(index<this._start_value ? this._offValue : index>this._end_value ? this._offValue : this._onValue);
		}
	}
}

DoubleSliderComponent.prototype.set_enabled = function(val){
	this._enabled = (val>0);
	this._update_controls();
}

exports.DoubleSliderComponent = DoubleSliderComponent;
