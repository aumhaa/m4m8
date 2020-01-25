// aumhaa_control_surface.js
// transferred 070519

var util = require('aumhaa_util');
util.inject(this, util);

LOCAL_DEBUG = false;
lcl_debug = LOCAL_DEBUG ? util.Debug : function(){};

var Bindable = require('aumhaa_bindable').Bindable;

var M4LCOMPONENT=new RegExp(/(M4LInterface)/);

function ControlSurfaceClass(name, parent, control_surface_type, init_callback, args){
	var self = this;
	this.add_bound_properties(this, []);
	this.__dependencies = {parent:parent, control_surface_type:control_surface_type, init_callback:init_callback};
	for(var i in this.__dependencies)
	if(this.__dependencies[i] == undefined){
		lcl_debug(i + ' must be provided to ControlSurfaceClass.');
	}
	this._parent = parent;
	this._init_callback = init_callback
	this._control_surface_type = control_surface_type||'None';
	ControlSurfaceClass.super_.call(this, name, args);
	this._finder = this._finder ? this._finder : new LiveAPI(this._callback, 'control_surfaces');
	this._control_surface_id = undefined;
	this.init();
}

util.inherits(ControlSurfaceClass, Bindable);

ControlSurfaceClass.prototype.init = function(){
	lcl_debug('ControlSurfaceClas.init()');
	var number_children = parseInt(this._finder.children[0]);
	lcl_debug('control_surfaces length:', number_children);
	for(var i=0;i<number_children;i++){
		lcl_debug('Checking control surface #:', i);
		this._finder.goto('control_surfaces', i);
		lcl_debug('type is:', this._finder.type);
		if(this._finder.type == this._control_surface_type){
			this._control_surface_id = this._finder.id;
			var components = this._finder.get('components');
			for (var i in components){
				lcl_debug('component is:', this._finder.type);
				this._finder.id = components[i];
			}
		}
	}
	if(this._control_surface_id!=undefined){
		lcl_debug('enabled...');
		this._init_callback(true);
		this._finder.id = parseInt(this._control_surface_id);
	}
}

ControlSurfaceClass.prototype._call_function = function(){
	var args = arrayfromargs(arguments);
	func = args[0] ? args[0] : undefined;
	lcl_debug('call_function:', func, 'args:', args);
	try{
		this.finder.call.apply(this.finder, args);
	}
	catch(err){
		this.lcl_debug('_call_function error:', err, args);
	}
}

ControlSurfaceClass.prototype._callback = function(args){}

exports.ControlSurfaceClass = ControlSurfaceClass;
