// aumhaa_notification_display.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;
var NotifierClass = require('aumhaa_notifier_class').NotifierClass;

function NotificationDisplayComponent(name, args){
	this.add_bound_properties(this, ['_show_message', '_clear_messages_queued', '_display_messages', 'show_message', 'add_subject', 'remove_subject', 'clear_subjects', 'make_parameter_function', 'set_priority']);
	var self = this;
	this._subjects = {};
	this._groups = [];
	this._scheduled_messages = [];
	this._last_priority = 0;
	this._parent = {tasks:util.nop};
	NotificationDisplayComponent.super_.call(this, name, args);
}

util.inherits(NotificationDisplayComponent, Bindable);

NotificationDisplayComponent.prototype._show_message = function(obj){
	if(obj._name in this._subjects){
		var entry = this._subjects[obj._name];
		if(entry.priority>=this._last_priority){
			this._scheduled_messages.unshift(obj._name);
			this._last_priority = entry.priority;
			this._display_messages();
			this._parent.tasks.addTask(self._clear_messages_queued, undefined, 5, false, 'display_messages');
		}
	}
}

NotificationDisplayComponent.prototype._clear_messages_queued = function(){
	//self._display_messages();
	self._last_priority = 0;
}

NotificationDisplayComponent.prototype._display_messages = function(){
	var entry_name = undefined;
	var priority = this._last_priority;
	for(var item in this._scheduled_messages){
		var entry = this._subjects[this._scheduled_messages[item]];
		//lcl_debug('entry is', self._scheduled_messages[item], entry.display_name, entry.priority);
		if(entry.priority>=priority){
			entry_name = this._scheduled_messages[item];
			priority = entry.priority;
		}
	}
	//lcl_debug('display_message', entry_name);
	var message = [];
	if(entry_name in this._subjects){
		var entry = this._subjects[entry_name];
		if(entry.group != undefined){
			for(var i in this._groups[entry.group]){
				var member = this._subjects[this._groups[entry.group][i]];
				message.push(member.display_name + ' : ' + member.parameter());
			}
		}
		else{
			message.push(entry.display_name + ' : ' + entry.parameter());
		}
	}
	//host.showPopupNotification(message.join('   '));
	this.Send_Message(message.join('   '));
	this._scheduled_messages = [];
}

NotificationDisplayComponent.prototype.show_message = function(message){
	//host.showPopupNotification(message);
	this.Send_Message(message);
}

NotificationDisplayComponent.prototype.add_subject = function(obj, display_name, parameters, priority, group){
	// if(obj instanceof NotifierClass){
	if(isClass(obj, 'NotifierClass')){
		if(!(obj._name in this._subjects)){
			priority = priority||0;
			display_name = display_name||obj._name;
			var parameter_function = this.make_parameter_function(obj, parameters);
			this._subjects[obj._name] = {'obj': obj, 'display_name':display_name, 'parameter':parameter_function, 'priority':priority, 'group':group};
			if(group != undefined){
				if(!(group in self._groups)){
					self._groups[group] = [];
				}
				self._groups[group].push(obj._name);
			}
			obj.add_listener(this._show_message);
		}
	}
}

NotificationDisplayComponent.prototype.remove_subject = function(obj){
	// if(obj instanceof NotifierClass){
	if(isClass(obj, 'NotifierClass')){
		for(var subject in this._subjects){
			if(subject === obj._name){
				subject.remove_listener(this._show_message);
				delete this._subjects[subject];
			}
		}
	}
}

NotificationDisplayComponent.prototype.clear_subjects = function(){
	for(var item in this._subjects){
		var obj = this._subjects[item].obj;
		// if(obj instanceof NotifierClass){
		if(isClass(obj, 'NotifierClass')){
			obj.remove_listener(this._show_message);
		}
	}
	this._subjects = {};
}

NotificationDisplayComponent.prototype.make_parameter_function = function(obj, parameter_values){
	if((parameter_values)&&(parameter_values instanceof Array)){
		var parameter_function = function(){
			return parameter_values[obj._value%(parameter_values.length)];
		}
		return parameter_function;
	}
	else{
		var parameter_function = function(){
			return obj._value;
		}
		return parameter_function;
	}
}

NotificationDisplayComponent.prototype.set_priority = function(priority){
	this._last_priority = priority;
}

NotificationDisplayComponent.prototype.Send_Message = function(message){
	lcl_debug('NotificationDisplayComponent.prototype.Send_Message is abstract, no override provided.\nMessage to be displayed:', message);
}

exports.NotificationDisplayComponent = NotificationDisplayComponent;
