//aumhaa_task_server.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

var Bindable = require('aumhaa_bindable').Bindable;


/////////////////////////////////////////////////////////////////////////////
//Overlay interface to host.scheduleTask that allows singlerun tasks and removable repeated tasks

function TaskServer(script, interval){
	var self = this;
	this.add_bound_properties(this, ['_script', '_queue', '_interval', '_run', '_tsk']);
	this._queue = {};
	this._interval = interval || 100;
	this._run = function(){
		for(var index in self._queue){
			var task = self._queue[index];
			//lcl_debug('run...', index, task);
			if(task.ticks == task.interval){
				if(!task.repeat){
					delete self._queue[index];
				}
				task.callback.apply(script, task.arguments);
				task.ticks = 0;
			}
			else{
				task.ticks += 1;
			}
		}
		//host.scheduleTask(self._run, null, self._interval);
	};
	this._tsk = new Task(this._run, this, undefined);
	this._tsk.interval = interval;
	this._tsk.initialdelay = 10000;
	this._tsk.repeat();
	TaskServer.super_.call(this, 'TaskSever', {'_script':script});
}

util.inherits(TaskServer, Bindable);

TaskServer.prototype.addTask = function(callback, arguments, interval, repeat, name){
	//lcl_debug('addTask', arguments, interval, repeat, name);
	if(typeof(callback)==='function'){
		interval = interval||1;
		repeat = repeat||false;
		if(!name){name = 'task_'+this._queue.length;}
		this._queue[name] = {'callback':callback, 'arguments':arguments, 'interval':interval, 'repeat':repeat, 'ticks':0};
	}
}

TaskServer.prototype.schedule = function(callback, name){
	this.addTask(callback, {}, 1, false, name)
}

TaskServer.prototype.resetTask = function(name){
	if((name)&&(this._queue[name])){
		this._queue[name].ticks = 0;
	}
}

TaskServer.prototype.taskIsRunning = function(callback, name){
	if(name){
		if(this._queue[name]){
			return true;
		}
	}
	else if(callback){
		for(var i in this._queue){
			if(this._queue[i].callback == callback){
				return true;
			}
		}
	}
	else{
		return false;
	}
}

TaskServer.prototype.removeTask = function(callback, arguments, name){
	lcl_debug('removing task:', name);
	if(name){
		if(this._queue[name]){
			delete this._queue[name];
		}
	}
	else{
		for(var i in this._queue){
			if((this._queue[i].callback == callback)&&(this._queue[i].arguments = arguments)){
				delete this._queue[i];
			}
		}
	}
}

exports.TaskServer = TaskServer;
