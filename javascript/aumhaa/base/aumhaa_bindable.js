// aumhaa_bindable.js

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}


/////////////////////////////////////////////////////////////////////////
//Base Class that allows automatic binding of prototypal properties based on
//the _bound_properties array.  Also provides very basic dependency checking

function Bindable(name, args){
	var self = this;
	this._name = name;
	this.instance = function(){return self;}
	for(var i in args){
		this['_'+i] = args[i];
	}
	this.add_bound_properties(this, this._mixin_bound_properties);
	this.add_bound_properties(this, [
		'super_',
		'_name',
		'Super_',
		'__dependencies',
		'require_dependencies',
		'check_dependencies'
	]);
	//lcl_debug('making bindable:', name, 'args:', args, 'bound_props:', this._bound_properties);
	this.bind_properties(this);
	// util.autobind(this);
	// this.require_dependencies(this, ['_name']);
	this.check_dependencies();

}

Bindable.prototype._mixin_bound_properties = [];

Bindable.prototype.check_dependencies = function(){
	lcl_debug(this._name + 'check_dependencies, deps are:', this.__dependencies);
	this.__dependencies = this.__dependencies ? this.__dependencies : [];
	var self = this;
	var missing = this.__dependencies.filter(function(dep){
		// debug('dependency:', dep, self[dep]);
		return self[dep]==undefined
	});
	if(missing.length){
		throw new Error('Missing constructor dependency: '+this._name+' :: '+missing);
	};
}

Bindable.prototype.require_dependencies = function(instance, dependencies){
	lcl_debug('adding dependency requirement to:', instance._name, '\n original deps:', instance.__dependencies, '\nnew deps:', dependencies);
	var old_deps = instance.__dependencies ? instance.__dependencies : [];
	instance.__dependencies = old_deps.concat(dependencies);
}

Bindable.prototype.add_bound_properties = function(instance, properties){
	// lcl_debug('adding bound properties to:', instance._name, '\n original props:', instance._bound_properties, '\nnew props:', properties);
	var old_props = instance._bound_properties ? instance._bound_properties : [];
	instance._bound_properties = old_props.concat(properties);
}

Bindable.prototype.bind_properties = function(instance){
	// lcl_debug('binding properties for:', instance._name, '\nprops are:', instance._bound_properties)
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
