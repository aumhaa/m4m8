// aumhaa_midi_event_router.js
// transferred 070219
// untested

var util = require('aumhaa_util');
util.inject(this, util);

var DictModule = require('aumhaa_dict_module').DictModule;
var Bindable = require('aumhaa_bindable').Bindable;
var AumhaaGlobalProxy = require('aumhaa_global_proxy').AumhaaGlobalProxy;

function MidiEventRouterModule(name, args){
	var self = this;
	this.Alive = false;
	this.target_menu = [{name:'Device Output', node:0}];
	this.midi_output_ports = [];
	this.lookup_menu = {'Device Output':this.target_menu[0]};
	//this.target_menu_lookup = {'Device Output':0};
	//this.target_menu = {'Device Output':0};
	this.add_bound_properties(this, ['_update_midi_port_list', 'tasks', 'routings',
							'update_menus', 'schedule_local_update', 'schedule_global_update',
							'global_update']);
	MidiEventRouterModule.super_.call(this, name, args);
	this.init();
	this.setup_tasks();
	this.setup_dict();
	this.initGlobal();

}

util.inherits(MidiEventRouterModule, Bindable);

MidiEventRouterModule.prototype.init = function(){
	this.Alive = true;
}

MidiEventRouterModule.prototype.initGlobal = function(){
	//debug('setup_global()');
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
	// debug('schedule_global_update()');
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
	// debug('global_update()', this._name);
	// var nodes = this.aumhaaGlobal.midiNodes;
	var nodes = this.aumhaaGlobal.get_scope('midiNodes');
	var remove_node = function(uid){
		//debug('remove_node:', uid);
		delete nodes[uid];
	}

	for(var uid in nodes){
		// debug('nodes[uid]', nodes[uid].uid);
		try{
			if((!nodes[uid].hasOwnProperty('Alive'))||(!nodes[uid].Alive)){
				//debug('not Alive:', uid);
				remove_node(uid);
			}
		}
		catch(err){
			//debug('error:', err);
			remove_node(uid);
		}
	}

	var registered_nodes = [];
	for(var n in nodes){
		// debug('adding to registered nodes:', nodes[n].uid);
		registered_nodes.push(nodes[n].uid);
	}
	//debug('registered nodes:', registered_nodes);
	//debug(nodes.forEach(function(node){if(node.hasOwnProperty('uid')){debug('registered node:', node.uid)};}))


	var Nodes = this.routings.get('Nodes');
	var Routings = this.routings;

	var remove_routing = function(uid){
		// debug('remove_routing:', uid);
		Routings.remove('Nodes::'+uid);
	}

	var keys = [];
	if(Routings._dict.contains('Nodes')){
		keys = ensure_array(Nodes.getkeys());
	}
	for(var i in keys){
		//debug(keys[i], 'indexOf:', registered_nodes.indexOf(keys[i]));
		if(registered_nodes.indexOf(keys[i])==-1){
			remove_routing(keys[i]);
		}
	}
	//debug('keys are:', keys);

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

MidiEventRouterModule.prototype.update_menus = function(){
	// debug('update_menus()');
	this.target_menu = [{name:'Device', node:'Device', type:'Device'}];
	this.lookup_menu = {'Device':this.target_menu[0]};
	routing_translation.message('clear');
	routing_translation.message('store', 'Device', ['Device', 'Device']);
	var keys = [];
	if(this.routings._dict.contains('Nodes')){
		keys = ensure_array(this.routings._dict.get('Nodes').getkeys());
	}
	for(var i in keys){
		if(keys[i]!=this._uid){
			var entry = {name:this.routings.get('Nodes::'+keys[i]+'::output_device')+' ('+this.routings.get('Nodes::'+keys[i]+'::name')+':'+keys[i]+')', node:keys[i], type:'IONode'};
			this.target_menu.push(entry);
			this.lookup_menu[entry.name] = entry;
			routing_translation.message('store', entry.name, [entry.type, entry.node+'_in']);
		}
	}

	for(var i in this.midi_output_ports){
		var entry = {name:this.midi_output_ports[i], node:0, type:'MIDI'};
		this.target_menu.push(entry);
		this.lookup_menu[entry.name] = entry;
		routing_translation.message('store', entry.name, [entry.type, entry.name]);
	}

	var entry = this.lookup_menu[outputPort];
	entry&&routing_translation.message('store', 'Global', [entry.type, entry.type == 'IONode' ? entry.node+'_in' : outputPort+'']);

	this._target_options_obj.message('clear');
	for(var i in this.target_menu){
		this._target_options_obj.message('append', this.target_menu[i].name);
		//debug('target_options:', this.target_menu[i].name);
	}

	update_global_output_menu()
	//var target = this.routings.get('Nodes::'+this._uid+'::target_node');
	/*for(var i in this.target_menu){
		if(target==(this.target_menu[i].type == 'MIDI' ? this.target_menu[i].name : this.target_menu[i].node)){
			this._target_options_obj.message('symbol', this.target_menu[i].name);
			break;
		}
	}*/
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

MidiEventRouterModule.prototype._update_midi_port_list = function(obj){
	//debug('port list updated:', obj._value);
	// debug('length of outputs:', obj._value.length);
	this.midi_output_ports = obj._value;
	this.update_menus();
}

exports.MidiEventRouterModule = MidiEventRouterModule;
