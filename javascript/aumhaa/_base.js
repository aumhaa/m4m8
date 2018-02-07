autowatch = 1;

exports.mod = require('mod');
exports.notifiers = require('notifiers');
exports.util = require('util');
//exports.scales = require('scales');

DEBUG = false;
debug = DEBUG&&exports.util.Debug?exports.util.Debug:function(){};

exports.init = function(script)
{
	script['autowatch'] = 1;
	var util = require('util');
	var mod = require('mod');
	var notifiers = require('notifiers');
	//var scales = require('scales');

	Function.prototype.clone = function()
	{
		var that = this;
		var temp = function temporary() { return that.apply(this, arguments); };
		for(var key in this) {
			if (this.hasOwnProperty(key)) {
				temp[key] = this[key];
			}
		}
		return temp;
	};

	Function.prototype.getName = function()
	{
		return /function ([^(]*)/.exec( this+"" )[1];
	}

	var loadProtos = function(dict)
	{
		for(var i in dict)
		{
			//debug('adding:', i);
			script[i] = dict[i];
		}
	}

	loadProtos(util);
	loadProtos(mod);
	loadProtos(notifiers);
	//loadProtos(scales);

	script['debug'] = script['DEBUG'] ? util.Debug : function(){};
	script['forceload'] = script['FORCELOAD'] ? util.Forceload : function(){};

}


exports.init_deprecated_prototypes = function(script)
{
	script['autowatch'] = 1;
	var _deprecated = require('_deprecated');

	var loadProtos = function(dict)
	{
		for(var i in dict)
		{
			debug('adding:', i);
			script[i] = dict[i];
		}
	}
	
	loadProtos(_deprecated);
}
