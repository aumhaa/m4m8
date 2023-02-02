// aumhaa_midi_event_router.js
// transferred 070219
// updated 060520, working with Skin

LCL_DEBUG = true;

var util = require('aumhaa_util');
util.inject(this, util);

var DictModule = require('aumhaa_dict_module').DictModule;
var Bindable = require('aumhaa_bindable').Bindable;
var AumhaaGlobalProxy = require('aumhaa_global_proxy').AumhaaGlobalProxy;
var NodeScriptProxy = require('aumhaa_node_script_proxy').NodeScriptProxy;

var lcl_debug = LCL_DEBUG?new util.DebugNamespace('MidiEventRouterModule').debug:function(){};

function MidiEventRouterModule(name, args){
	var self = this;
	this._parent_script = undefined;
	this.Alive = false;
	this._uid;
	this.device_name = 'None';
	this.this_device_id = 0;
	this.target_menu = [{name:'Device', node:'Device', type:'Device'}];
	this.target_lookup_menu = {'Device':this.target_menu[0]};
	this.source_menu = [{name:'Device', node:'Device', type:'Device'}];
	this.source_lookup_menu = {'Device':this.target_menu[0]};
	this._input_ports = new ArrayParameter(this._name + '_inputPorts', {value:[]});
	this._output_ports = new ArrayParameter(this._name + '_outputPorts', {value:[]});
	this._inputPort = new ParameterClass(this._name + '_inputPort', {value:args.storedInputPort});
	this._outputPort = new ParameterClass(this._name + '_outputPort', {value:args.storedOutputPort});
	this.add_bound_properties(this, [
		'tasks',
		'routings',
		'update_menus',
		'schedule_local_update',
		'schedule_global_update',
		'global_update',
		'input',
		'_input_ports',
		'_output_ports',
		'_inputPort',
		'_outputPort',
		'available_outputs',
		'available_inputs',
		'target_menu',
		'target_lookup_menu',
		'source_menu',
		'source_lookup_menu',
		'_routing_translation'
	]);
	MidiEventRouterModule.super_.call(this, name, args);
	this.available_inputs = this._input_ports.receive;
	this.available_outputs = this._output_ports.receive;
	// this.call.init(this);
	this.setup_tasks();
	this.setup_dict();
	this.initGlobal();

}

util.inherits(MidiEventRouterModule, NodeScriptProxy);

MidiEventRouterModule.prototype.__defineGetter__('midi_output_ports', function(){
	return this._output_ports._value;
});

MidiEventRouterModule.prototype.__defineGetter__('midi_input_ports', function(){
	return this._input_ports._value;
});

MidiEventRouterModule.prototype.__defineGetter__('outputPort', function(){
	return this._outputPort._value;
});

MidiEventRouterModule.prototype.__defineGetter__('inputPort', function(){
	return this._inputPort._value;
});


// //this should be .receive, and it's handled by Super_().
MidiEventRouterModule.prototype.input = function(){
	var args = arrayfromargs(arguments);
	lcl_debug(this._name+'.input():', args);
	//lcl_debug('in?:', args[0], args[0] in this, this[args[0]]);
  //we need to send ArrayParameters [], so we use call here....probably a better way
	this[args[0]]&&this[args[0]].call(this, args.slice(1));
}

MidiEventRouterModule.prototype.init_routines = function(){
	this.Alive = true;
	//we're doing this to update all the available items in our global and voice menus when there's a port change
	this._output_ports.add_listener(this.update_menus);
	this._input_ports.add_listener(this.update_input_menu);
	//we're doing this to get the Global output value inside the translations_object
	// this._outputPort.add_listener(this.update_menus); //don't need to, we do it in the setter func below
	// this._input_ports.add_listener(this.update_menus);
}

MidiEventRouterModule.prototype.initGlobal = function(){
	//lcl_debug('setup_global()');
	this.aumhaaGlobal = new AumhaaGlobalProxy('AumhaaGlobal');
	this.aumhaaGlobal.set_scope('midiNodes', {});
	var tNodes = this.aumhaaGlobal.get_scope('midiNodes');
	tNodes[this._uid] = this;
	this.schedule_global_update();
}

MidiEventRouterModule.prototype.setup_dict = function(){
	this.routings = new DictModule('routing', {dict_name:'midinode_routing'});  // obj:patcher.getnamed('midinode_routing')
	//var dict_name = patcher.getnamed('settings').getattr('name');
	//this.settings_dict.name = dict_name;
	//this.routings.set('Nodes::'+uid, settings_dict);
}

MidiEventRouterModule.prototype.schedule_global_update = function(){
	// lcl_debug('schedule_global_update()');
	// var tNodes = this.aumhaaGlobal.midiNodes;
	var nodes = this.aumhaaGlobal.get_scope('midiNodes');
	var local_update = true;
	for(var i in nodes){
		if((nodes[i]!=this)&&(nodes[i].hasOwnProperty('global_update'))){
			local_update = false;
			nodes[i].schedule_global_update();
			break;
		}
	}
	local_update&&this.schedule_local_update();
}

MidiEventRouterModule.prototype.schedule_global_update = function(){
	if(this.Alive){
		this.tasks.addTask(this.global_update, {}, 1, false, 'menu_update');
	}
}

MidiEventRouterModule.prototype.global_update = function(){
	//function validate_all_nodes(){
	// lcl_debug('global_update()', this._name);
	// var nodes = this.aumhaaGlobal.midiNodes;
	var nodes = this.aumhaaGlobal.get_scope('midiNodes');
	var remove_node = function(uid){
		//lcl_debug('remove_node:', uid);
		delete nodes[uid];
	}

	for(var uid in nodes){
		// lcl_debug('nodes[uid]', nodes[uid].uid);
		try{
			if((!nodes[uid].hasOwnProperty('Alive'))||(!nodes[uid].Alive)){
				//lcl_debug('not Alive:', uid);
				remove_node(uid);
			}
		}
		catch(err){
			//lcl_debug('error:', err);
			remove_node(uid);
		}
	}

	var registered_nodes = [];
	for(var n in nodes){
		// lcl_debug('adding to registered nodes:', nodes[n].uid);
		registered_nodes.push(nodes[n].uid);
	}
	//lcl_debug('registered nodes:', registered_nodes);
	//lcl_debug(nodes.forEach(function(node){if(node.hasOwnProperty('uid')){lcl_debug('registered node:', node.uid)};}))


	var Nodes = this.routings.get('Nodes');
	var Routings = this.routings;

	var remove_routing = function(uid){
		// lcl_debug('remove_routing:', uid);
		Routings.remove('Nodes::'+uid);
	}

	var keys = [];
	if(Routings._dict.contains('Nodes')){
		keys = ensure_array(Nodes.getkeys());
	}
	for(var i in keys){
		//lcl_debug(keys[i], 'indexOf:', registered_nodes.indexOf(keys[i]));
		if(registered_nodes.indexOf(keys[i])==-1){
			remove_routing(keys[i]);
		}
	}
	//lcl_debug('keys are:', keys);

	this.update_nodes();
}

MidiEventRouterModule.prototype.update_nodes = function(exclude_local){
	// var nodes = this.aumhaaGlobal.midiNodes;
	var nodes = this.aumhaaGlobal.get_scope('midiNodes');
	for(var i in nodes){
		if(nodes[i]==this){
			exclude_local || nodes[i].schedule_local_update();
		}
		else{
			nodes[i].schedule_local_update();
		}
	}
}

MidiEventRouterModule.prototype.schedule_local_update = function(){
	if(this.Alive){
		this.tasks.addTask(this.update_menus, {}, 1, false, 'menu_update');
	}
}




MidiEventRouterModule.prototype.update_menus = function(obj){
	lcl_debug('update_menus()', obj._value);
	this.target_menu = [{name:'Device', node:'Device', type:'Device'}];
	this.target_lookup_menu = {'Device':this.target_menu[0]};
	this._routing_translation.message('clear');
	this._routing_translation.message('store', 'Device', ['Device', 'Device']);
	var keys = [];
	if(this.routings._dict.contains('Nodes')){
		keys = ensure_array(this.routings._dict.get('Nodes').getkeys());
	}
	for(var i in keys){
		if(keys[i]!=this._uid){
			var entry = {name:this.routings.get('Nodes::'+keys[i]+'::output_device')+' ('+this.routings.get('Nodes::'+keys[i]+'::name')+':'+keys[i]+')', node:keys[i], type:'IONode'};
			this.target_menu.push(entry);
			this.target_lookup_menu[entry.name] = entry;
			this._routing_translation.message('store', entry.name, [entry.type, entry.node+'_in']);
		}
	}
	for(var i in this.midi_output_ports){
		var entry = {name:this.midi_output_ports[i], node:0, type:'MIDI'};
		this.target_menu.push(entry);
		this.target_lookup_menu[entry.name] = entry;
		this._routing_translation.message('store', entry.name, [entry.type, entry.name]);
	}

	var entry = this.target_lookup_menu[this.outputPort];
	entry&&this._routing_translation.message('store', 'Global', [entry.type, entry.type == 'IONode' ? entry.node+'_in' : this.outputPort+'']);

	for(var i in this.midi_input_ports){
		var entry = {name:this.midi_input_ports[i], node:0, type:'MIDI'};
		this.source_menu.push(entry);
		this.source_lookup_menu[entry.name] = entry;
	}

	this.update_output_menu();
	// this.update_input_menu();
	// this._target_options_obj.message('clear');
	// for(var i in this.target_menu){
	// 	this._target_options_obj.message('append', this.target_menu[i].name);
	// 	lcl_debug('target_options:', this.target_menu[i].name);
	// }
	// this._target_options_obj.message('setsymbol', this._output_port);


	// this._script.update_global_output_menu()
	//var target = this.routings.get('Nodes::'+this._uid+'::target_node');
	/*for(var i in this.target_menu){
		if(target==(this.target_menu[i].type == 'MIDI' ? this.target_menu[i].name : this.target_menu[i].node)){
			this._target_options_obj.message('symbol', this.target_menu[i].name);
			break;
		}
	}*/
}

MidiEventRouterModule.prototype.update_output_menu = function(){
	lcl_debug(this._name+'.update_output_menu()');
	// lcl_debug('target_menu:', JSON.stringify(this.target_menu));
	// var ports = obj._value;
	//lcl_debug('update_input_menu', ports);
	this._target_options_obj.message('clear');
	this._voice_target_options_obj.message('clear');
	for(var i in this.target_menu){
		this._target_options_obj.message('append', this.target_menu[i].name);
		this._voice_target_options_obj.message('append', this.target_menu[i].name);
		// lcl_debug('target_options:', this.target_menu[i].name);
	}
	// this._voice_target_options_obj.message('append', 'Global');  //we need to add this to only the single voice options
	this._target_options_obj.message('setsymbol', this.outputPort);
}

MidiEventRouterModule.prototype.update_input_menu = function(){
	lcl_debug(this._name + '.update_input_menu()');
	var ports = this.midi_input_ports;
	this._source_options_obj.message('clear');
	for(var i in ports){
			this._source_options_obj.message('append', ports[i]);
	}
	this._source_options_obj.message('setsymbol', this.inputPort);
}

MidiEventRouterModule.prototype.setup_tasks = function(){
	this.tasks = new TaskServer(script, 100);
}

MidiEventRouterModule.prototype.dissolve = function(){
	delete nodes.uid;
	for(var i in nodes){
		if(nodes[i]!=script){
			nodes[i].schedule_global_update();
			break;
		}
	}
}

// MidiEventRouterModule.prototype._update_midi_port_list = function(obj){
// 	// post('----------------------------port list updated:', obj._value);
// 	// lcl_debug('length of outputs:', obj._value.length);
// 	this.midi_output_ports = obj._value;
// 	this.update_menus();
// }

MidiEventRouterModule.prototype.set_input_port = function(port){
	var self = this;
	NSProxy.asyncCall('set_input_port', port).then(function(returned_port){
		// lcl_debug('new input is:', returned_port);
		self._inputPort.set_value(returned_port);
	}).catch(function(e){
		util.report_error(e);
	})
}

MidiEventRouterModule.prototype.set_output_port = function(port){
	var entry = this.target_lookup_menu[this.outputPort];
	if(entry){
		this._routing_translation.message('store', 'Global', [entry.type, entry.type == 'IONode' ? entry.node+'_in' : this.outputPort]);
		this._outputPort.set_value(port);
	}
}

MidiEventRouterModule.prototype.dissolve = function(){
	this.aumhaaGlobal._global[this._uid] = null;
	delete this.aumhaaGlobal._global[this._uid];
}

exports.MidiEventRouterModule = MidiEventRouterModule;
