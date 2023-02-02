// aumhaa_APIUtility.js
// transferred 070219

var util = require('aumhaa_util');
util.inject(this, util);

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}

function APIUtility(){
	var self = this;
	this.finder = new LiveAPI(function(){}, 'this_device');
	this.device_id = parseInt(this.finder.id);
	this.container_id = parseInt(this.container_from_id(this.device_id));
	this.id_list = [];
}

APIUtility.prototype.dissolve = function(){
	this.finder.id = 0;
}

APIUtility.prototype.is_valid = function(id){
	//catch doesn't work when liveAPI throws for some reason, but finally does.
	//we're posting to suppress the red jsliveapi warning in the max log....because its irritating.
	//do yourself a favor and don't adjust this, it seems to be working.
	var finder = this.finder;
	id = parseInt(id);
	if(id!=0){
		try{
			post('is_valid: '+id);
			finder.id = id;
			post(finder.id == id ? 'true' : 'false');
		}catch(e){}finally{
			post('\n');
			return (finder.id == id)
		}
	}
	return false
}

APIUtility.prototype.track_from_id = function(id){
	var finder = this.finder;
	// lcl_debug('finder:', finder.type);
	finder.id = id;
	// lcl_debug('finder.id:', id);
	// lcl_debug('finder:', finder.type);
	var recurse = function(id){
		if(id == 0){
			return 0;
		}
		finder.goto('canonical_parent');
		if(finder.type=='Track'){
			return parseInt(finder.id);
		}
		else{
			return recurse(id);
		}
	}
	return recurse(id);
}

APIUtility.prototype.container_from_id = function(id){
	var finder = this.finder;
	finder.id = id;
	finder.goto('canonical_parent');
	return parseInt(finder.id);
}

APIUtility.prototype.previous_device = function(track, device){
	var finder = this.finder;
	var device_id = device;
	finder.id = device;
	finder.goto('canonical_parent');
	if(!(finder.type=='Chain')){
		//debug('container is track')
		finder.id = track;
	}
	var devices = finder.get('devices').filter(function(element){return element !== 'id';});
	var index = devices.indexOf(device_id);
	if(index > 0){
		device_id = devices[index-1];
	}
	return device_id
}

APIUtility.prototype.next_device = function(track, device){
	var finder = this.finder;
	var device_id = device;
	finder.id = device;
	finder.goto('canonical_parent');
	if(!(finder.type=='Chain')){
		//debug('container is track')
		finder.id = track;
	}
	var devices = finder.get('devices').filter(function(element){return element !== 'id';});
	var index = devices.indexOf(device_id);
	if(index < (devices.length-1)){
		device_id = devices[index+1];
	}
	return device_id
}

APIUtility.prototype.device_name_from_id = function(id){
	var finder = this.finder;
	var new_name = 'None';
	finder.id = parseInt(id);
	if(id > 0){
		new_name = finder.get('name').slice(0,40);
		/*var new_name = [];
		new_name.unshift(finder.get('name'));
		finder.goto('canonical_parent');
		//finder.goto('canonical_parent');
		new_name.unshift(' || ');
		new_name.unshift(finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);*/
	}
	return new_name;
}

APIUtility.prototype.container_name_from_id = function(id){
	var finder = this.finder;
	var new_name = 'None';
	finder.id = parseInt(id);
	if(id > 0){
		var new_name = finder.get('name').slice(0, 40);
	}
	return new_name;
}

APIUtility.prototype.name_from_id = function(id){
	var finder = this.finder;
	var new_name = 'None';
	finder.id = parseInt(id);
	if(id > 0){
		var new_name = finder.get('name').slice(0, 40);
	}
	return new_name;
}

APIUtility.prototype.device_input_from_id = function(id){
	var finder = this.finder;
	if(id==this.device_id){
		finder.id = parseInt(this.container_from_id(id));
		var new_name = [':Track Input'];
		new_name.unshift(finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);
		return new_name;
	}
	else{
		return this.device_name_from_id(id);
	}
}

APIUtility.prototype.device_output_from_id = function(id){
	var finder = this.finder;
	if(id==this.device_id){
		finder.id = parseInt(this.container_id);
		var new_name = [':Track Output'];
		new_name.unshift(finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);
		return new_name;
	}
	else{
		return this.device_name_from_id(id);
	}
}

APIUtility.prototype.drum_output_note_from_drumchain = function(id){
	var finder = this.finder;
	var note = undefined;
	finder.id = id;
	if(finder.type=='DrumChain'){
		note = finder.get('out_note')
	}
	debug('drum_note_from_chain', finder.path, note);
	return note;
}

APIUtility.prototype.drum_input_note_from_drumchain = function(id){
	var finder = this.finder;
	var note = undefined;
	var drumchain_id = id;
	finder.id = drumchain_id;
	if(finder.type=='DrumChain'){
		finder.goto('canonical_parent');
		var drumrack_id = parseInt(finder.id);
		for(var i=0;i<127;i++){
			finder.id = drumrack_id;
			finder.goto('drum_pads', i);
			var count = finder.getcount('chains');
			//debug('count', count);
			if(count){
				var chains = finder.get('chains').filter(function(element){return element !== 'id';});
				//debug('chains', chains, drumrack_id);
				var index = chains.indexOf(drumchain_id);
				if((index >-1)||(chains==drumchain_id)){
					//debug('found chain!');
					note = finder.get('note');
					break;
				}
			}
		}
	}
	//debug('drum_note_from_chain', note);
	return note;
}

APIUtility.prototype.set_component_by_type = function (api_inst, comp_type){
	var path = api_inst.path;
	var comps = api_inst.get('components').filter(function(element){return element !== 'id';});
	for(var i in comps){
		// debug('testing:', comps[i]);
		api_inst.id = comps[i];
		// debug('name:', api_inst.get('name'));
		var type = api_inst.type;
		// debug(type, '==', comp_type, type == comp_type);
		if(type == comp_type){
			// debug('found component', comp_type);
			return
		}
	}
	api_inst.id = 0;
}

APIUtility.prototype.set_component_by_name = function (api_inst, comp_name){
	var path = api_inst.path;
	var comps = api_inst.get('components').filter(function(element){return element !== 'id';});
	for(var i in comps){
		api_inst.id = comps[i];
		var name = api_inst.get('name');
		// debug(name, '==', comp_name, name == comp_name);
		if(name == comp_name){
			// debug('found component', comp_type);
			return
		}
	}
	api_inst.id = 0;
}

APIUtility.prototype.set_control_by_name = function (api_inst, control_name){
	var path = api_inst.path;
	var controls = api_inst.get('controls').filter(function(element){return element !== 'id';});
	for(var i in controls){
		api_inst.id = controls[i];
		var name = api_inst.get('name');
		// debug(name, '==', comp_name, name == comp_name);
		if(name == control_name){
			// debug('found component', comp_type);
			return
		}
	}
	api_inst.id = 0;
}

//draft
APIUtility.prototype.is_container = function(id){
	finder.id = id;
	var type = finder.type;
	return ['Track', 'Chain', 'DrumChain', 'RackDevice', 'DrumPad'].indexOf(type)>-1;
}

//draft
APIUtility.prototype.chain_ids_from_parent = function(id){
	var ids = [];
	finder.id = id;
	if(finder.get('can_have_chains')){
		ids = finder.get('chains').filter(function(element){return element !== 'id';});
	}
	return ids;
}

//draft
APIUtility.prototype.device_ids_from_parent = function(id){
	var ids = [];
	finder.id = id;
	ids = finder.get('devices').filter(function(element){return element !== 'id';});
	return ids;
}

APIUtility.prototype.find_control_surface = function(control_surface_type){
	var finder = this.finder;
	finder.goto('control_surfaces');
	var number_children = parseInt(finder.children[0]);
	lcl_debug('control_surfaces length:', number_children);
	for(var i=0;i<number_children;i++)
	{
		lcl_debug('Checking control surface #:', i);
		finder.goto('control_surfaces', i);
		if(finder.type == control_surface_type)
		{
			return parseInt(finder.id);
		}
	}
	return 0
}

exports.APIUtility = APIUtility;
