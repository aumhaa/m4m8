// aumhaa_bindable.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

/////////////////////////////////////////////////////////////////////////
//Base Class that allows automatic binding of prototypal properties based on
//the _bound_properties array.

function Bindable(name, args){
	var self = this;
	this._name = name;
	this.instance = function(){return self;}
	for(var i in args){
		this['_'+i] = args[i];
	}
	this.add_bound_properties(this, this._mixin_bound_properties);
	this.add_bound_properties(this, ['super_', '_name', 'Super_']);
	//lcl_debug('making bindable:', name, 'args:', args, 'bound_props:', this._bound_properties);
	this.bind_properties(this);

}

Bindable.prototype._mixin_bound_properties = [];

Bindable.prototype.add_bound_properties = function(instance, properties){
	lcl_debug('adding bound properties to:', instance._name, '\n original props:', instance._bound_properties, '\nnew props:', properties);
	var old_props = instance._bound_properties ? instance._bound_properties : [];
	instance._bound_properties = old_props.concat(properties);
}

Bindable.prototype.bind_properties = function(instance){
	lcl_debug('binding properties for:', instance._name, '\nprops are:', instance._bound_properties)
	//bind_properties(instance, instance._bound_properties);
	if(instance._bound_properties){
		var prop_list = instance._bound_properties;
		for(var index in prop_list){
			var prop = prop_list[index];
			if(instance.constructor.prototype[prop]){
				//lcl_debug('has prop:', prop);
				instance[prop] = instance.constructor.prototype[prop].bind(instance);
			}
		}
	}
}

exports.Bindable = Bindable;
