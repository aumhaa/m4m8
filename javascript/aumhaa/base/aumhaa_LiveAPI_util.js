// aumhaa_bindable.js
// transferred 070219
// completely untested

var util = require('aumhaa_util');
util.inject(this, util);


function APIUtility(){
	var self = this;
	this.finder = new LiveAPI(function(){}, 'this_device');
	this.device_id = parseInt(this.finder.id);
	this.container_id = parseInt(this.container_from_id(this.device_id));
}

APIUtility.prototype.track_from_id = function(id){
	this.finder.id = id;
	var recurse = function(id){
		if(id == 0){
			return 0;
		}
		this.finder.goto('canonical_parent');
		if(this.finder.type=='Track'){
			return parseInt(this.finder.id);
		}
		else{
			return recurse(id);
		}
	}
	return recurse(id);
}

APIUtility.prototype.container_from_id = function(id){
	this.finder.id = id;
	this.finder.goto('canonical_parent');
	return parseInt(this.finder.id);
}

APIUtility.prototype.previous_device = function(track, device){
	var device_id = device;
	this.finder.id = device;
	this.finder.goto('canonical_parent');
	if(!(this.finder.type=='Chain')){
		//debug('container is track')
		this.finder.id = track;
	}
	var devices = this.finder.get('devices').filter(function(element){return element !== 'id';});
	var index = devices.indexOf(device_id);
	if(index > 0){
		device_id = devices[index-1];
	}
	return device_id
}

APIUtility.prototype.next_device = function(track, device){
	var device_id = device;
	this.finder.id = device;
	this.finder.goto('canonical_parent');
	if(!(this.finder.type=='Chain')){
		//debug('container is track')
		this.finder.id = track;
	}
	var devices = this.finder.get('devices').filter(function(element){return element !== 'id';});
	var index = devices.indexOf(device_id);
	if(index < (devices.length-1)){
		device_id = devices[index+1];
	}
	return device_id
}

APIUtility.prototype.device_name_from_id = function(id){
	var new_name = 'None';
	this.finder.id = parseInt(id);
	if(id > 0){
		new_name = this.finder.get('name').slice(0,40);
		/*var new_name = [];
		new_name.unshift(this.finder.get('name'));
		this.finder.goto('canonical_parent');
		//this._this.finder.goto('canonical_parent');
		new_name.unshift(' || ');
		new_name.unshift(this.finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);*/
	}
	return new_name;
}

APIUtility.prototype.container_name_from_id = function(id){
	var new_name = 'None';
	this.finder.id = parseInt(id);
	if(id > 0){
		var new_name = this.finder.get('name').slice(0, 40);
	}
	return new_name;
}

APIUtility.prototype.name_from_id = function(id){
	var new_name = 'None';
	this.finder.id = parseInt(id);
	if(id > 0){
		var new_name = this.finder.get('name').slice(0, 40);
	}
	return new_name;
}

APIUtility.prototype.device_input_from_id = function(id){
	if(id==this_device_id){
		this.finder.id = parseInt(container_id);
		var new_name = [':Track Input'];
		new_name.unshift(this.finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);
		return new_name;
	}
	else{
		return device_name_from_id(id);
	}
}

APIUtility.prototype.device_output_from_id = function(id){
	if(id==this.device_id){
		this.finder.id = parseInt(this.container_id);
		var new_name = [':Track Output'];
		new_name.unshift(this.finder.get('name'));
		new_name = new_name.join('');
		new_name = new_name.slice(0, 40);
		return new_name;
	}
	else{
		return device_name_from_id(id);
	}
}

APIUtility.prototype.drum_output_note_from_drumchain = function(id){
	var note = undefined;
	this.finder.id = id;
	if(this.finder.type=='DrumChain'){
		note = this.finder.get('out_note')
	}
	debug('drum_note_from_chain', finder.path, note);
	return note;
}

APIUtility.prototype.drum_input_note_from_drumchain = function(id){
	var note = undefined;
	var drumchain_id = id;
	this.finder.id = drumchain_id;
	if(this.finder.type=='DrumChain'){
		this.finder.goto('canonical_parent');
		var drumrack_id = parseInt(this.finder.id);
		for(var i=0;i<127;i++){
			this.finder.id = drumrack_id;
			this.finder.goto('drum_pads', i);
			var count = this.finder.getcount('chains');
			//debug('count', count);
			if(count){
				var chains = this.finder.get('chains').filter(function(element){return element !== 'id';});
				//debug('chains', chains, drumrack_id);
				var index = chains.indexOf(drumchain_id);
				if((index >-1)||(chains==drumchain_id)){
					//debug('found chain!');
					note = this.finder.get('note');
					break;
				}
			}
		}
	}
	//debug('drum_note_from_chain', note);
	return note;
}

//draft
APIUtility.is_container = function(id){
	finder.id = id;
	var type = finder.type;
	return ['Track', 'Chain', 'DrumChain', 'RackDevice', 'DrumPad'].indexOf(type)>-1;
}

//draft
APIUtility.chain_ids_from_parent = function(id){
	var ids = [];
	finder.id = id;
	if(finder.get('can_have_chains')){
		ids = finder.get('chains').filter(function(element){return element !== 'id';});
	}
	return ids;
}

//draft
APIUtility.device_ids_from_parent = function(id){
	var ids = [];
	finder.id = id;
	ids = finder.get('devices').filter(function(element){return element !== 'id';});
	return ids;
}

exports.APIUtility = APIUtility;
