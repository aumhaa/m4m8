autowatch = 1;

var GLOBAL_DEBUG = false;
var module_file_list;
var global_exports;

function parse_modules(){
	module_file_list = [];
	var f = new Folder('base');
	while (!f.end) {
		module_file_list.push(f.filename.split('.')[0]);
		f.next();
	}
	f = new Folder('notifiers');
	while (!f.end) {
		module_file_list.push(f.filename.split('.')[0]);
		f.next();
	}
	f = new Folder('components');
	while (!f.end) {
		module_file_list.push(f.filename.split('.')[0]);
		f.next();
	}
	// for(var i in module_file_list){
	// 	post(module_file_list[i]);
	// }
}

function build_exports(){
	global_exports = {};
	for(var i in module_file_list){
		var module = require(module_file_list[i]);
		for(var j in module){
			global_exports[j] = module[j];
			exports[j] = module[j];
		}
	}
}

parse_modules();

build_exports();

exports.init = function(script){

	Function.prototype.clone = function(){
		var that = this;
		var temp = function temporary() { return that.apply(this, arguments); };
		for(var key in this) {
			if (this.hasOwnProperty(key)) {
				temp[key] = this[key];
			}
		}
		return temp;
	}

	Function.prototype.getName = function(){
		return /function ([^(]*)/.exec( this+"" )[1];
	}

	for(var i in global_exports){
		script[i]=global_exports[i];
	}
	script['debug'] = (script['DEBUG']||GLOBAL_DEBUG) ? script.Debug : function(){};
	script['forceload'] = script['FORCELOAD'] ? script.Forceload : function(){};
}
