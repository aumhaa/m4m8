// aumhaa_midi_io_modulejs
// transferred 060420
// working with destination.js

var INIT_GLOBAL = false;
var VIEW_DEVICEDICT = true;
var CLEAR_DICT = false;

var LCL_DEBUG = true;

var util = require('aumhaa_util');
util.inject(this, util);
var lcl_debug = LCL_DEBUG?new util.DebugNamespace('midi_io_node').debug:function(){};

var Bindable = require('aumhaa_bindable').Bindable;
var AumhaaGlobalProxy = require('aumhaa_global_proxy').AumhaaGlobalProxy;
var NodeScriptProxy = require('aumhaa_node_script_proxy').NodeScriptProxy;
var DictModule = require('aumhaa_dict_module').DictModule;
DictModule.prototype._initialize = function()  {
	CLEAR_DICT&&this._dict.clear();
	if(!this._dict.contains('Nodes')){
		this._dict.set('Nodes', new Dict('Nodes'));
		this._dict.setparse("Nodes", '{}');
	}
	this._keys = this._dict.getkeys();
	this.refresh_window();
}

function is_name(args){
	return args ? args[0]=='name' : false;
}

function ensure_array(obj){
	if(typeof(obj)=='string'){
		return [obj];
	}
	return obj;
	//probably easier to do:
	//return [].concat(obj)
}

/** Sample dict entry:
{
	"Nodes" : 	{
		"uid_8" : 		{
			"name" : "destination",
			"container" : "1-MIDI",
			"input_device" : "1-MIDI:Track Input",
			"output_device" : "1-MIDI:Track Output",
			"id" : 8,
			"source_name" : "disabled",
			"source_node" : 0,
			"target_name" : "disabled",
			"target_node" : 0
		}
	}
}
**/

/** We have a Global() that holds references to all the available instances
  of this class.  We also maintain a dictionary of the same information.
  The class is a subclass of the nodeProxy class, and maintains the connection and
  settings of the nodescript object (but it receives and sends midi on it's own).
  When the position or metadata of the m4l object changes, listeners should
  catch it, and send an update request to all members of the Global.
  We also have to maintain an accurate list of all the Global's members, as some
  could disconnect or new one's join.
**/


function MidiIoNodeModule(name, args){
	var self = this;
	this._parent_script = undefined;
	this.Alive = false;
	this._uid;  //= 'uid_'+unique;
 	this._global; //= new Global('aumhaaGlobal');
	this.device_name = 'None';
	this.device_id = 0;
	this.target_menu = [{name:'disabled', node:0}];
	this.source_menu = [{name:'disabled', node:0}];
	this.target_name = '';
	this.source_name = '';
	this.device_output_id = 0;
	this.device_input_id = 0;
	this.device_output = '';
	this.device_input = '';
	this.track_id = 0;
	this.container_id = 0;
	this.settings_dict = new Dict();
	this._midiInputPort = 'disabled';
	this._midiOutputPort = 'disabled';
	this._midi_input_ports = new ArrayParameter(this._name + '_midiInputPorts', {value:[]});
	this._midi_output_ports = new ArrayParameter(this._name + '_midiOutputPorts', {value:[]});
	this._inputPort = new ParameterClass(this._name + '_inputPort', {value:args.storedInputPort?args.storedInputPort:'disabled'});
	this._outputPort = new ParameterClass(this._name + '_outputPort', {value:args.storedOutputPort?args.storedOutputPort:'disabled'});
	this.require_dependencies(this, [
		'_parent_script',
		'_unique',
		'_max_receive_dynamicObj',
		'_max_receive_staticObj',
		'_max_forward_dynamicObj',
		'_max_forward_staticObj'
	]);
	this.add_bound_properties(this, [
		'_parent_script',
		'_uid',
		'_global',
		'_unique',
		'_max_receive_dynamicObj',
		'_max_receive_staticObj',
		'_max_forward_dynamicObj',
		'_max_forward_staticObj',
		'_midi_input_ports',
		'_midi_output_ports',
		'_midiInputPort',
		'_midiOutputPort',
		'_inputPort',
		'_outputPort',
		'routings',
		'settings_dict',
		'update_device_id',
		'update_container_name',
		'update_name',
		'update_menus',
		'update_device_input',
		'update_device_output',
		'schedule_menu_update',
		'local_update',
		'global_update',
		'on_source_chosen',
		'on_target_chosen',
		'dissolve',
		'Alive',
		'check_ports'
	]);
	MidiIoNodeModule.super_.call(this, name, args);
}

util.inherits(MidiIoNodeModule, NodeScriptProxy);

MidiIoNodeModule.prototype.__defineGetter__('midi_output_ports', function(){
	return this._midi_output_ports._value;
});

MidiIoNodeModule.prototype.__defineGetter__('midi_input_ports', function(){
	return this._midi_input_ports._value;
});

MidiIoNodeModule.prototype.__defineGetter__('outputPort', function(){
	return this._outputPort._value;
});

MidiIoNodeModule.prototype.__defineGetter__('inputPort', function(){
	return this._inputPort._value;
});


MidiIoNodeModule.prototype.init_routines = function(){
	debug(this._name, this._uid, 'init');
	this.setup_dict.call(this);
	this.setup_tasks.call(this);
	this.setup_api.call(this);
	this.setup_global.call(this);  //after setup_api so that we have a valid _uid
	this.setup_patcher.call(this);
	this.Alive = true;

	//we need to be Alive before we call listeners
	this.setup_liveapi_listeners.call(this);
	this.setup_aumhaa_listeners.call(this);
	this.update_device_id.call(this);

	//these 3 update this.routings dict values
	//we really need to init all the potential dict values in a sane way
	this.detect_container();
	this.detect_input_device();
	this.detect_output_device();
}

MidiIoNodeModule.prototype.setup_tasks = function(){
	if(!this.tasks){
		this.tasks = new TaskServer(this._parent_script, 100);
	}
}

MidiIoNodeModule.prototype.setup_api = function(){
	this.apiUtility = new APIUtility(this._name + 'apiUtility');
	// this.finder = new LiveAPI(function(){}, 'this_device');
	this.device_id = parseInt(this.apiUtility.device_id);
	this._uid = 'uid_'+this.device_id;
	// lcl_debug = LCL_DEBUG?util.DebugNamespace(this._name+'::'+this._uid+'->'):function(){};
}

// MidiIoNodeModule.prototype.setup_global = function(){
// 	this._global = new AumhaaGlobalProxy('aumhaaGlobal');
// 	this._global.set_scope('midiNodes', {});
// 	// this._global.get_scope('midiNodes')[this._uid] = this;
// 	this._global.global[this._uid] = this;
// 	debug('GLOBAL space:', this._global.global.midiNodes[this._uid]._uid);
// }

MidiIoNodeModule.prototype.setup_global = function(){
	this._global = new Global('aumhaaGlobal');
	if(!this._global.midiNodes){
		this._global.midiNodes = {};
	}
	this._global.midiNodes[this._uid]=this;
}

MidiIoNodeModule.prototype.setup_dict = function(){
	this.routings = new DictModule('routing', {dict_name:'midinode_routing', 'VIEW_DEVICEDICT':VIEW_DEVICEDICT});
	var dict_name = this._parent_script.patcher.getnamed('settings').getattr('name');
	this.settings_dict.name = dict_name;
	// this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

//double check that this is unnecesarry, but it really should be part of init_routines.
MidiIoNodeModule.prototype.setup_patcher = function(){
	lcl_debug(this._name+'.setup_patcher() has not been overridden.');
}

//these get initialized with api routes when detect_container/input/output fire
MidiIoNodeModule.prototype.setup_liveapi_listeners = function(){

	this.devices_listener = new LiveAPI(this.on_devices_changed);

	this.device_input_listener = new LiveAPI(this.on_device_input_changed);

	this.device_output_listener = new LiveAPI(this.on_device_output_changed);

	this.container_name_listener = new LiveAPI(this.on_container_name_changed);

	this.devices_listener = new LiveAPI(this.on_devices_changed);
	this.devices_listener.mode = 1;

	this.name_listener = new LiveAPI(this.on_name_changed, 'this_device');
	this.name_listener.property = 'name';

	//track_name_listener.id = track_id;
	//track_name_listener.property = 'name';
}

MidiIoNodeModule.prototype.setup_aumhaa_listeners = function(){
	//shouldn't these be midi_input_ports and midi_output_ports?
	//or contain a listing for all the internally available ports for the instance?
	//maybe it does....that's probably the best pattern for now.
	this._midi_output_ports.add_listener(this.schedule_menu_update);
	this._midi_input_ports.add_listener(this.schedule_menu_update);

	//ArrayParameterClass wants a single array as a value.  It sucks, right?
	this.available_inputs = function(){
		var args = arrayfromargs(arguments);
		debug('inputs are:', args);
		this._midi_input_ports.set_value(args);
	}.bind(this);

	this.available_outputs = function(){
		var args = arrayfromargs(arguments);
		debug('outputs are:', args);
		this._midi_output_ports.set_value(args);
	}.bind(this);
}

//this also probably needs to be done in init_routines, and overridden in sub
MidiIoNodeModule.prototype.gather_patcher_settings = function(){
	debug('gather_patcher_settings()');
	this.on_name_changed('name');
}


MidiIoNodeModule.prototype.detect_container = function(){
	debug('detect_container()');
	var old_id = this.container_id;
	this.container_id = this.apiUtility.container_from_id(this.device_id);
	if(old_id != this.container_id){
		this.container_name_listener.id = this.container_id;
		this.container_name_listener.property = 'name';
		//outlet(1, 'path', container_name_listener.unquotedpath + ' devices');
		this.devices_listener.path = this.container_name_listener.unquotedpath + ' devices'
	}
	return old_id != this.container_id;
}

MidiIoNodeModule.prototype.detect_input_device = function(){
	//detects the device/container that is feeding this device
	debug('detect_input_device()');
	var old_id = this.device_input_id;
	this.device_input_id = this.apiUtility.previous_device(this.container_id, this.device_id);
	if(old_id != this.device_input_id){
		this.device_input_listener.id = this.device_input_id;
		this.device_input_listener.property = 'name';
	}
	return old_id != this.device_input_id;
}

MidiIoNodeModule.prototype.detect_output_device = function(){
	//detects the device/container that this device is feeding
	debug('detect_output_device()');
	var old_id = this.device_output_id;
	this.device_output_id = this.apiUtility.next_device(this.container_id, this.device_id);
	if(old_id != this.device_output_id){
		this.device_output_listener.id = this.device_output_id;
		this.device_output_listener.property = 'name';
	}
	return old_id != this.device_output_id;
}

MidiIoNodeModule.prototype.dissolve = function(){
	// debug('dissolve', this._uid);
	this.Alive = false;
	// outlet(1, 'path', 0);
	this.devices_listener.property = '';
	this.device_input_listener.property = '';
	this.device_output_listener.property = '';
	this.container_name_listener.property = '';
	this.name_listener.property = ''
	var nodes = this._global.midiNodes;
	delete nodes[this._uid];
	//debug('typeof nodes:', typeof(nodes));
	//this needs to be a method of AumhaaGlobalProxy, e.g. this._global.delete_item
	// delete this._global.get_scope('midiNodes')[this._uid];
	for(var i in nodes){
		if(nodes[i]!=this){
			nodes[i].schedule_global_update();
			break;
		}
	}
	// debug('nodes:', nodes);
}


//callback for name_listener liveAPI object
MidiIoNodeModule.prototype.on_name_changed = function(args){
	if((this.Alive)&&(is_name(args))){
		debug('on_name_changed()', args);
		this.update_name();
		var update = this.detect_container() + this.detect_input_device() + this.detect_output_device();
		update&&this.update_nodes();
		//update_nodes(true);
	}
}

MidiIoNodeModule.prototype.on_container_name_changed = function(args){
	if((this.Alive)&&(is_name(args))){
		debug('on_container_name_changed()', args);
		this.update_container_name();
		this.detect_input_device();
		this.detect_output_device();
		this.update_nodes();
	}
}

MidiIoNodeModule.prototype.on_device_input_changed = function(args){
	if((this.Alive)&&(is_name(args))){
		debug('on_device_input_changed()', args);
		this.update_device_input();
		this.update_nodes(true);
	}
}

MidiIoNodeModule.prototype.on_device_output_changed = function(args){
	if((this.Alive)&&(is_name(args))){
		debug('on_device_output_changed()', args);
		this.update_device_output();
		this.update_nodes(true);
	}
}

MidiIoNodeModule.prototype.on_devices_changed = function(args){
	if(this.Alive){
		debug('on_devices_changed()', args);
		var update = this.detect_container() + this.detect_input_device() + this.detect_output_device();
		update&&this.update_nodes();
	}
}


//this is called when an instance is freed
MidiIoNodeModule.prototype.schedule_global_update = function(){
	if(this.Alive){
		this.tasks.addTask(this.global_update, {}, 1, false, 'menu_update');
	}
}

MidiIoNodeModule.prototype.global_update = function(){
	//function validate_all_nodes(){
	debug('global_update()');

	var nodes = this._global.midiNodes;
	// var nodes = this._global.get_scope('midiNodes');

	// var node_ids = Object.entries(nodes).map(function(node){
	// 	return node._name;
	// });
	// debug('nodes:', node_ids);

	var remove_node = function(uid){
		//debug('remove_node:', uid);
		delete nodes[uid];
	}

	for(var uid in nodes){
		debug('nodes[uid]', uid, nodes[uid]._uid);
		try{
			if((!nodes[uid].hasOwnProperty('Alive'))||(!nodes[uid].Alive)){
				// debug('not Alive:', uid);
				remove_node(uid);
			}
		}
		catch(err){
			util.report_error(err);
			remove_node(uid);
		}
	}

	var registered_nodes = [];
	for(var n in nodes){
		// debug('adding to registered nodes:', nodes[n]._uid);
		registered_nodes.push(nodes[n]._uid);
	}
	debug('registered nodes:', registered_nodes);
	// debug(nodes.forEach(function(node){if(node.hasOwnProperty('_uid')){debug('registered node:', node._uid)};}))

	var self = this;
	var Nodes = this.routings.get('Nodes');
	var remove_routing = function(uid){
		debug('remove_routing:', uid);
		self.routings.remove('Nodes::'+uid);
	}

	var keys = ensure_array(Nodes.getkeys());
	for(var i in keys){
		debug(keys[i], 'indexOf:', registered_nodes.indexOf(keys[i]));
		if(registered_nodes.indexOf(keys[i])==-1){
			remove_routing(keys[i]);
		}
	}
	debug('keys are:', keys);

	this.update_nodes();
}

MidiIoNodeModule.prototype.update_nodes = function(exclude_local){
	// var nodes = this._global.get_scope('midiNodes');
	var nodes = this._global.midiNodes;
	for(var i in nodes){
		if(nodes[i]==this){
			exclude_local || nodes[i].schedule_local_update();
		}
		else{
			nodes[i].schedule_local_update();
		}
	}
}


//this is called within each instance when global_update fires
MidiIoNodeModule.prototype.schedule_local_update = function(){
	//debug('schedule_local_update()')
	if(this.Alive){
		this.tasks.addTask(this.local_update, {}, 1, false, 'local_update');
	}
}

MidiIoNodeModule.prototype.local_update = function(){
	// lcl_debug('local_update()');
	this.update_device_id();
	this.update_container_name();
	this.update_name();
	this.update_device_input();
	this.update_device_output();
	this.schedule_menu_update();
}

MidiIoNodeModule.prototype.update_device_id = function(){
	this.routings.set('Nodes::'+this._uid+'::id',  this.device_id);
	this.settings_dict.set('id',  this.device_id);
	// debug('update_device_id()');
}

MidiIoNodeModule.prototype.update_track_id = function(){
	this.track_id = this.apiUtility.track_from_id(this.device_id);
}

MidiIoNodeModule.prototype.update_container_id = function(){
	// debug('update_container_id()');
	this.container_id = this.apiUtility.container_from_id(this.device_id);
	// debug('container_id:', this.container_id);
}

MidiIoNodeModule.prototype.update_name = function(){
	// debug('update_name()');
	this.device_name = this.apiUtility.device_name_from_id(this.device_id);
	// this.routings.set('Nodes::'+this._uid+'::name',  this.device_name);
	this.settings_dict.set('name',  this.device_name);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

MidiIoNodeModule.prototype.update_container_name = function(){
	// debug('update_container_name()');
	this.container_name = this.apiUtility.container_name_from_id(this.container_id);
	// debug('container_name is:', this.container_name);
	// this.routings.set('Nodes::'+this._uid+'::container', this.container_name);
	this.settings_dict.set('container', this.container_name);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

MidiIoNodeModule.prototype.update_device_output = function(){
	// debug('update_device_output()');
	this.device_output = this.apiUtility.device_output_from_id(this.device_output_id);
	// this.routings.set('Nodes::'+this._uid+'::output_device',  this.device_output);
	this.settings_dict.set('output_device',  this.device_output);
	//device_output_obj.message('set', device_output);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

MidiIoNodeModule.prototype.update_device_input = function(){
	// debug('update_device_input()');
	this.device_input = this.apiUtility.device_input_from_id(this.device_input_id);
	// this.routings.set('Nodes::'+this._uid+'::input_device',  this.device_input);
	this.settings_dict.set('input_device',  this.device_input);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
	//device_input_obj.message('set', device_input);
}


MidiIoNodeModule.prototype.check_ports = function(){
	lcl_debug('check_ports...');
	this.asyncCall('check_ports').then(function(){
		return true
	}).catch(function(e){
		util.report_error(e);
		return false
	});
}

//this is called when a local update fires
MidiIoNodeModule.prototype.schedule_menu_update = function(){
	//debug('schedule_menu_update()');
	if(this.Alive){
		this.tasks.addTask(this.update_menus, {}, 1, false, 'menu_update');
	}
}

MidiIoNodeModule.prototype.update_menus = function(){
	lcl_debug('update_menus()');
	this.target_menu = [{name:'disabled', node:0}];
	this.source_menu = [{name:'disabled', node:0}];
	var keys = ensure_array(this.routings._dict.get('Nodes').getkeys());
	for(var i in keys){
		if(keys[i]!=this._uid){
			this.target_menu.push({name:this.routings.get('Nodes::'+keys[i]+'::output_device')+' ('+this.routings.get('Nodes::'+keys[i]+'::name')+')', node:keys[i], type:'IONode'});
			this.source_menu.push({name:this.routings.get('Nodes::'+keys[i]+'::input_device')+' ('+this.routings.get('Nodes::'+keys[i]+'::name')+')', node:keys[i], type:'IONode'});
		}
	}
	for(var i in this.midi_input_ports){
		this.source_menu.push({name:this.midi_input_ports[i], node:0, type:'MIDI'});
	}
	for(var i in this.midi_output_ports){
		this.target_menu.push({name:this.midi_output_ports[i], node:0, type:'MIDI'});
	}
}

//these two methods accept input from patcher objects and
MidiIoNodeModule.prototype.on_source_chosen = function(val){
	lcl_debug('_on_source_chosen()', val);
	var entry = this.source_menu[val];
	this.source_name = entry ? entry.name : 'disabled';
	this.source_node = entry ? entry.node : 0;
	this.source_type = entry ? entry.type : 'disabled';
	this.write_input_settings_entry();
	// this.set_midi_input_port(entry.type == 'MIDI' ? this.source_name : 'disabled');
	this.set_dynamic_recieve(entry.type == 'IONode' ? entry.node+'_out' : undefined);
	var self = this;
	this.set_midi_input_port(entry.type == 'MIDI' ? this.source_name : 'disabled').then(function(){
		self._inputPort.set_value(self.source_type == 'MIDI' ? self._midiInputPort : self.source_name);
	}).catch(function(e){
		util.report_error(e);
		self._inputPort.set_value(self.source_type == 'MIDI' ? self._midiInputPort : self.source_name);
	});
}

MidiIoNodeModule.prototype.on_target_chosen = function(val){
	lcl_debug('_on_target_chosen()', val);
	var entry = this.target_menu[val];
	// lcl_debug('entry is:', JSON.stringify(entry));
	this.target_name = entry ? entry.name : 'disabled';
	this.target_node = entry ? entry.node : 0;
	this.target_type = entry ? entry.type : 'disabled';
	this.write_output_settings_entry();
	this.set_dynamic_forward(entry.type == 'IONode' ? entry.node+'_out' : undefined);
	var self = this;
	this.set_midi_output_port(entry.type == 'MIDI' ? self.target_name : 'disabled').then(function(){
		self._outputPort.set_value(self.target_type == 'MIDI' ? self._midiOutputPort : self.target_name);
	}).catch(function(e){
		self._outputPort.set_value(self.target_type == 'MIDI' ? self._midiOutputPort : self.target_name);
	});
	// self._outputPort.set_value(this.target_type == 'MIDI' ? returned_port : port_name);
}

MidiIoNodeModule.prototype.set_dynamic_recieve = function(source){
	this._max_receive_dynamicObj.message('set', source);
}

MidiIoNodeModule.prototype.set_dynamic_forward = function(source){
	this._max_forward_dynamicObj.message('set', source);
}

MidiIoNodeModule.prototype.set_midi_input_port = function(port_name){
	var self = this;
	var result = new Promise(function(resolve, reject){
		self.asyncCall('set_input_port', port_name).then(function(returned_port){
			// self._inputPort.set_value(this.source_type == 'MIDI' ? returned_port : port_name);
			self._midiInputPort = port_name;
			// lcl_debug('resolving...');
			resolve(true);
		}).catch(function(e){
			util.report_error(e);
			// lcl_debug('rejecting');
			self._midiInputPort = 'disabled';
			reject(false);
		});
	});
	return result
}

MidiIoNodeModule.prototype.set_midi_output_port = function(port_name){
	var self = this;
	var result = new Promise(function(resolve, reject){
		// lcl_debug('setting to:', port_name);
		self.asyncCall('set_output_port', port_name).then(function(returned_port){
			// debug('new midi output is:', returned_port);
			// self._outputPort.set_value(this.target_type == 'MIDI' ? returned_port : port_name);
			self._midiOutputPort = port_name;
			resolve(true);
		}).catch(function(e){
			util.report_error(e);
			self._midiOutputPort = 'disabled';
			reject(false);
		});
	});
	return result
}

MidiIoNodeModule.prototype.write_input_settings_entry = function(){
	this.settings_dict.set('source_name',  this.source_name);
	this.settings_dict.set('source_node',  this.source_node);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

MidiIoNodeModule.prototype.write_output_settings_entry = function(){
	this.settings_dict.set('target_name',  this.target_name);
	this.settings_dict.set('target_node',  this.target_node);
	this.routings.set('Nodes::'+this._uid, this.settings_dict);
}

MidiIoNodeModule.prototype._on_enable_input = function(val){
	debug('_on_enable_input()', val);
	this.input_enable = val>0;
}

MidiIoNodeModule.prototype._on_enable_output = function(val){
	debug('_on_enable_output()', val);
	this.output_enable = val>0;
}

MidiIoNodeModule.prototype.dissolve = function(){
	this._global.midiNodes[this._uid]=null;
	delete this._global[this._uid];
}

exports.MidiIoNodeModule = MidiIoNodeModule;
