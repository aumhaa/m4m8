// aumhaa_modes.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = true;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;
var Bindable = require('aumhaa_bindable').Bindable;
var GridClass = require('aumhaa_grid_class').GridClass;
var ControlClass = require('aumhaa_control_class').ControlClass;
var ToggledParameter = require('aumhaa_parameters').ToggledParameter;
var colors = require('aumhaa_notifier_consts').consts.colors;

////////////////////////////////////////////////////////////////////////////
//Mode is a notifier that automatically updates buttons when its state changes

var PRS_DLY = 750;


function DefaultPageStackBehaviour(parent_mode_object){
	var self = this;
	var parent = parent_mode_object;
	this.press_immediate = function(button){
		//debug('press_immediate', parent, parent.mode_buttons);
		var mode = parent.mode_buttons.indexOf(button);
		parent.splice_mode(mode);
		parent.push_mode(mode);
		parent.recalculate_mode();
	}
	this.press_delayed = function(button){
		//debug('press_delayed');
	}
	this.release_immediate = function(button){
		//debug('release_immediate');
		parent.clean_mode_stack();
	}
	this.release_delayed = function(button){
		//debug('release_delayed');
		var mode = parent.mode_buttons.indexOf(button);
		parent.pop_mode(mode);
		parent.recalculate_mode();
	}
}

exports.DefaultPageStackBehaviour = DefaultPageStackBehaviour;


function DefaultPageStackBehaviourWithModeShift(parent_mode_object){
	//debug('initializing DefaultPageStackBehaviourWithModeShift');
	var self = this;
	var parent = parent_mode_object;
	this.press_immediate = function(button){
		//debug('press_immediate', parent, parent.mode_buttons);
		var mode = parent.mode_buttons.indexOf(button);
		if(mode!=parent.current_mode()){
			parent.splice_mode(mode);
			parent.push_mode(mode);
			parent.recalculate_mode();
		}
		else{
			var page = parent.current_page();
			parent.current_page()._mode_button_value(button);
		}
	}
	this.press_delayed = function(button){
		//debug('press_delayed');

	}
	this.release_immediate = function(button){
		//debug('release_immediate');
		parent.clean_mode_stack();
		var mode = parent.mode_buttons.indexOf(button);
		if(mode==parent.current_mode()){
			parent.current_page()._mode_button_value(button);
		}
	}
	this.release_delayed = function(button){
		//debug('release_delayed');
		var mode = parent.mode_buttons.indexOf(button);
		//if(mode!=parent.current_mode())
		//{
			parent.pop_mode(mode);
			parent.recalculate_mode();
		//}
		//else
		//{
			parent.current_page()._mode_button_value(button);
		//}
	}
}

exports.DefaultPageStackBehaviourWithModeShift = DefaultPageStackBehaviourWithModeShift;


function CyclePageStackBehaviour(parent_mode_object){
	var self = this;
	this.__lineage__ = 'CyclePageStackBehaviour';
	var parent = parent_mode_object;
	this.press_immediate = function(button){
		//debug('press_immediate', parent, parent.mode_buttons);
		//debug(parent._value, parent._mode_callbacks);
		var mode = (parent._value + 1) % parent._mode_callbacks.length;
		//debug('new_mode:', mode);
		parent.splice_mode(mode);
		parent.push_mode(mode);
		parent.recalculate_mode();
	}
	this.press_delayed = function(button){
		//debug('press_delayed');
	}
	this.release_immediate = function(button){
		//debug('release_immediate');
		parent.clean_mode_stack();
	}
	this.release_delayed = function(button){
		//debug('release_delayed');
		//var mode = parent.mode_buttons.indexOf(button);
		parent.pop_mode();
		parent.recalculate_mode();
	}
}

exports.CyclePageStackBehaviour = CyclePageStackBehaviour;



function ModeClass(number_of_modes, name, args){
	var self = this;
	this.add_bound_properties(this, ['mode_cycle_value', 'mode_value', 'toggle_value', 'change_mode', 'update', 'add_mode', 'set_mode_buttons', 'set_mode_cycle_button', 'current_mode', 'recalculate_mode', 'push_mode', 'splice_mode']);
	this._value = 0;
	this._mode_callbacks = new Array(number_of_modes);
	this._mode_stack = [];
	this.mode_buttons = [];
	this.mode_cycle_button = undefined;
	this._mode_colors = [0, 1];
	this._timered = function(){
		//debug('timered...', arguments[0]._name, self._name);
		var button = arguments[0];
		if(button&&button.pressed()){
			self._behaviour.press_delayed(button);
		}
	}
	this.add_bound_properties(this, ['_task_server', '_behaviour', '_behaviour_timer', '_timered', '_mode_stack', 'mode_value', 'mode_toggle']);
	ModeClass.super_.call(this, name, args);
	//lcl_debug('making timer for:', this._name, this._main_script);
	//this._behaviour_timer = new Task(this._timered, this._main_script ? this._main_script : this, undefined); //, self);
	this._behaviour = this._behaviour!= undefined ? new this._behaviour(this) : new DefaultPageStackBehaviour(this);
	this._press_delay = this._press_delay ? this._press_delay : PRS_DLY;
	this.mode_toggle = new ToggledParameter(this._name + '_Mode_Toggle', {'onValue':colors.BLUE, 'offValue':colors.CYAN, 'value':0});
	this.mode_toggle.add_listener(this.toggle_value);
	this.mode_value.owner = this;
}

util.inherits(ModeClass, NotifierClass);

ModeClass.prototype.mode_cycle_value = function(button){
	if(button.pressed()){
		this.change_mode((this._value + 1) % this._mode_callbacks.length)
		//this.notify();
	}
}

ModeClass.prototype.mode_cycle_value = function(button){
	lcl_debug('mode_cycle_value:', button);
	if(button.pressed()){
		if(this._behaviour_timer.running){
			this._behaviour_timer.cancel();
		}
		this._behaviour.press_immediate(button);
		//this._behaviour_timer = new Task(this._timered, this);
		this._behaviour_timer.arguments = [button];
		//this._behaviour_timer.object = this;
		//this._behaviour_timer = new Task(this._timered, this);
		this._behaviour_timer.schedule(this._press_delay);
	}
	else
	{
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

ModeClass.prototype.mode_cycle_value = function(button){
	lcl_debug('mode_cycle_value:', button);
	if(this._task_server){
		if(button.pressed()){
			this._task_server.removeTask(this._timered)
			this._behaviour.press_immediate(button);
			this._task_server.addTask(this._timered, [button], 1, false);
		}
		else{
			if(this._task_server.taskIsRunning(this._timered)){
				this._task_server.removeTask(this._timered);
				this._behaviour.release_immediate(button);
			}
			else{
				this._behaviour.release_delayed(button);
			}
		}
	}
	else{
		if(button.pressed()){
			this.change_mode((this._value + 1) % this._mode_callbacks.length)
		}
	}
	this.notify();
}

ModeClass.prototype.mode_value = function(button){
	//lcl_debug('mode value', this._name, ':', button, button.pressed());
	if(button.pressed()){
		this.change_mode(this.mode_buttons.indexOf(button));
		this.notify();
	}
}

ModeClass.prototype.mode_value = function(button){
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

ModeClass.prototype.mode_value = function(button){
	if(this._task_server){
		if(button.pressed()){
			if(this._task_server.taskIsRunning(this._timered)){
				this._task_server.removeTask(this._timered);
			}
			this._behaviour.press_immediate(button);
			this._task_server.addTask(this._timered, [button], 1, false);
		}
		else{
			if(this._task_server.taskIsRunning(this._timered)){
				this._task_server.removeTask(this._timered);
				this._behaviour.release_immediate(button);
			}
			else{
				this._behaviour.release_delayed(button);
			}
		}
	}
	else{
		if(button.pressed()){
			this.change_mode(this.mode_buttons.indexOf(button));
		}
	}
	this.notify();
}

ModeClass.prototype.toggle_value = function(button){
	this.change_mode(button._value);
	//this.notify();
}

ModeClass.prototype.change_mode = function(value, force){
	if (value < (this._mode_callbacks.length)){
		if((this._value != value)||(force)){
			this._value = value;
			this.update();
			//this.notify();
		}
	}
}

ModeClass.prototype.update = function(){
	var callback = this._mode_callbacks[this._value];
	if(callback){
		try{
			callback();
		}
		catch(err){
			lcl_debug('callback error:', err, 'for mode index', this._value,'for', this._name, 'mode component');
		}
	}
	for(var i in this.mode_buttons){
		if (i == this._value){

			this.mode_buttons[i].turn_on();
		}
		else{
			this.mode_buttons[i].turn_off();
		}
	}
	if(this.mode_cycle_button){
		this.mode_cycle_button.send(this._mode_colors[this._value%this._mode_colors.length]);
	}
}

ModeClass.prototype.add_mode = function(mode, callback){
	if (mode < this._mode_callbacks.length){
		this._mode_callbacks[mode] = callback;
	}
}

ModeClass.prototype.set_mode_buttons = function(buttons){
	//lcl_debug('set_mode_buttons:', buttons ? 'buttons length:' + buttons.length : 'incoming buttons undefined', this._mode_callbacks.length);
	if (((buttons == undefined)||(buttons.length == this._mode_callbacks.length))&&(buttons != this.mode_buttons)){
		for (var i in this.mode_buttons){
			this.mode_buttons[i].remove_target(this.mode_value);
			this.mode_buttons[i].reset()
		}
		if(!buttons){
			buttons = [];
		}
		this.mode_buttons = [];
		for (var i in buttons){
			this.mode_buttons.push(buttons[i]);
			buttons[i].set_target(this.mode_value);
			i == this._value ? buttons[i].turn_on() : buttons[i].turn_off();
		}
		//lcl_debug('mode buttons length: ' + this._name + ' ' + this.mode_buttons.length)
	}
}

ModeClass.prototype.set_mode_cycle_button = function(button){
	if(this.mode_cycle_button){
		this.mode_cycle_button.remove_target(this.mode_cycle_value);
	}
	this.mode_cycle_button = button;
	if(button){
		button.set_target(this.mode_cycle_value);
	}
}

ModeClass.prototype.current_mode = function(){
	return(this._value)
}

ModeClass.prototype.push_mode = function(mode){
	if(mode>-1){this._mode_stack.unshift(mode);}
}

ModeClass.prototype.splice_mode = function(mode){
	var index = this._mode_stack.indexOf(mode);
	if(index>-1){this._mode_stack.splice(index, 1);}
}

ModeClass.prototype.clean_mode_stack = function(){
	if(this._mode_stack.length > 1){
		this._mode_stack.splice(1, this._mode_stack.length-1);
	}
}

ModeClass.prototype.pop_mode = function(){
	if(this._mode_stack.length > 1){this._mode_stack.shift();}
}

ModeClass.prototype.pop_all_modes = function(){
	this._mode_stack = [];
}

ModeClass.prototype.recalculate_mode = function(){
	//debug('recalculate_mode');
	var mode = this._mode_stack.length ? this._mode_stack[0] : 0;
	this.change_mode(mode);
}

exports.ModeClass = ModeClass;



/////////////////////////////////////////////////////////////////////////////
//PageStack is a Mode subclass that handles entering/leaving pages automatically

function PageStack(number_of_modes, name, args){
	this.add_bound_properties(this, ['current_page', 'restore_mode']);

	//lcl_debug('making pagestack', number_of_modes, name, args);
	this._pages = new Array(number_of_modes);
	PageStack.super_.call(this, number_of_modes, name, args);
	this._value = -1;
}

util.inherits(PageStack, ModeClass);

PageStack.prototype.add_mode = function(mode, page){
	// if ((page instanceof Page) && (mode < this._mode_callbacks.length)){
	if ((isClass(page, 'Page')) && (mode < this._mode_callbacks.length)){
		this._pages[mode] = page;
		//lcl_debug('adding page:', page, this._pages);
	}
	else{
		lcl_debug('Invalid add_mode assignment for', this._name, mode, ':', page);
	}
}

PageStack.prototype.change_mode = function(value, force){
	//lcl_debug('change_mode:', value, '#callbacks:', this._mode_callbacks.length);
	if((-1 < value)&&(value < this._mode_callbacks.length)){
		if((this._value != value)||(force)){
			//lcl_debug('changing mode, old mode:', this._value, 'new mode:', value);
			this._pages[this._value]&&this._pages[this._value].exit_mode();
			this._value = value;
			this._pages[this._value]&&this._pages[this._value].enter_mode();
			this.update();
		}
	}
}

PageStack.prototype.current_page = function(){
	return this._pages[this.current_mode()];
}

PageStack.prototype.restore_mode = function(){
	this.change_mode(this._value, true);
}

exports.PageStack = PageStack;



////////////////////////////////////////////////////////////////////////////
//Page holds a controls dict that can hash a control to an internal function

function Page(name, args){
	this.add_bound_properties(this, ['controlInput', '_shiftValue', '_altValue',
		'_shift_button', '_shifted', '_alt_button', '_alted', 'set_shift_button',
		'set_alt_button']);
	this._controls = {};
	this.active = false;
	this._shifted = false;
	this._shift_button = undefined;
	this._alted = false;
	this._alt_button = undefined;
	Page.super_.call(this, name, args);
}

util.inherits(Page, Bindable);

Page.prototype.controlInput = function(control){this.control_input(control);}

Page.prototype._shiftValue = function(obj){
	lcl_debug('shiftValue', obj._value);
	var new_shift = false;
	if(obj){
		new_shift = obj._value > 0;
	}
	if(new_shift != this._shifted){
		this._shifted = new_shift;
		this.update_mode();
	}
}

Page.prototype._altValue = function(obj){
	lcl_debug('altValue', obj._value);
	var new_alt = false;
	if(obj){
		new_alt = obj._value > 0;
	}
	if(new_alt != this._alted){
		this._alted = new_alt;
		this.update_mode();
	}
}

Page.prototype.enter_mode = function(){
	lcl_debug(this._name, ' entered!');
}

Page.prototype.exit_mode = function(){
	lcl_debug(this._name, ' exited!');
}

Page.prototype.update_mode = function(){
	lcl_debug(this._name, ' updated!');
}

Page.prototype.refresh_mode = function(){
	this.exit_mode();
	this.enter_mode();
}

Page.prototype.set_shift_button = function(button){
	// debug('shift_button:', button._name, button != this._shift_button, button instanceof ControlClass);
	// if (((button != this._shift_button)&&(button instanceof ControlClass)) || (!button)){
	if (((button != this._shift_button)&&(isClass(button, 'ControlClass'))) || (!button)){
		if(this._shift_button){
			this._shift_button.remove_target(this._shiftValue);
			this._shift_button.reset();
			this._shifted = false;
		}
		this._shift_button = button;
		if(this._shift_button){
			this._shift_button.set_target(this._shiftValue);
		}
	}
}

Page.prototype.set_alt_button = function(button){
	// if (((button != this._alt_button)&&(button instanceof NotifierClass)) || (!button)){
	if (((button != this._alt_button)&&(isClass(button, 'ControlClass'))) || (!button)){
		if(this._alt_button){
			this._alt_button.remove_target(this._altValue);
			this._alt_button.reset();
			this._alted = false;
		}
		this._alt_button = button;
		if(this._alt_button){
			this._alt_button.set_target(this._altValue);
		}
	}
}

Page.prototype.control_input = function(control){
	lcl_debug('Page: ', this._name, 'recieved control input ', control._name);
	if(control in this._controls){
		this._controls[control](control);
	}
}

Page.prototype.register_control = function(control, target){
	// if (control instanceof GridClass){
	if (isClass(control, 'GridClass')){
		var grid_controls = control.controls();
		for(var index in grid_controls){
			this._controls[grid_controls[index]] = target;
		}
		lcl_debug('grid added to ', this._name, 's control dict');
	}
	// else if(control instanceof FaderBank)
	// {
	// 	lcl_debug('faderbank found......');
	// 	var faderbank_controls = control.controls();
	// 	for(index in faderbank_controls)
	// 	{
	// 		this._controls[faderbank_controls[index]] = target;
	// 	}
	// 	lcl_debug('faderbank added to ', this._name, 's control dict');
	// }
	// else if(control instanceof ControlClass){
	else if(isClass(control, 'ControlClass')){
		this._controls[control] = target;
		lcl_debug('control: ', control._name, ' added to ', this._name, 's control dict');
	}
}

exports.Page = Page;



function ModeSwitchablePage(name, args){
	var self = this;
	this._moded = false;
	this.add_bound_properties(this, ['_moded', '_mode_button_value']);
	ModeSwitchablePage.super_.call(this, name, args);
}

util.inherits(ModeSwitchablePage, Page);

ModeSwitchablePage.prototype._mode_button_value = function(obj){
	//lcl_debug('old altValue');
	//debug('_mode_button_value', obj, obj._value);
	var new_mode = false;
	if(obj){
		new_mode= obj._value > 0;
	}
	if(new_mode != this._moded){
		this._moded = new_mode;
		this.update_mode();
	}
}

exports.ModeSwitchablePage = ModeSwitchablePage;
