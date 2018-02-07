autowatch = 1;

inlets = 0;
outlets = 0;

var DEBUG = true;
var DEBUG_CB = false;

var thisMod = undefined;

global ModPrototype = Mod;

function Mod(type, unique, arguments)
{
	var self = this;
	this._type = type;
	this._unique = unique;
	this.assign_attributes(arguments);

	this.finder = undefined;

	this.modFunctions = [];
	this.modAddresses = [];
	this.this_device_id = 0;
	this.stored_messages = [];
	this.legacy = false;
}

Mod.prototype.init = function()
{
	var MONOMODULAR=new RegExp(/(monomodular)/);
	var FUNCTION = new RegExp(/(function)/);
	var PROPERTY = new RegExp(/(property)/);
	var WS = new RegExp('');
	var found = false;

	if(DEBUG){post('init_b996\n');}
	//this.assign_attributes();
	if(!this.finder)
	{
		this.finder = new LiveAPI(callback, 'this_device');
	}
	this.finder.goto('this_device');
	this.this_device_id = parseInt(finder.id);
	if(DEBUG){post('this device id:', this.this_device_id);}
	this.finder.goto('control_surfaces');
	var number_children = parseInt(this.finder.children[0]);
	if(DEBUG){post('control_surfaces length:', number_children , '\n');}
	for(var i=0;i<number_children;i++)
	{
		if(DEBUG){post('Checking control surface #:', i, '\n');}
	   	this.finder.goto('control_surfaces', i);
		var children = this.finder.info.toString().split(new RegExp("\n"));
		var functions = [];
		var properties = [];
		for(var item in children)
		{
			if(FUNCTION.test(children[item]))
			{
				//if(DEBUG){post('adding function:', children[item].replace('function ', ''), '\n');}
				functions.push(children[item].replace('function ', ''));
			}
			if(PROPERTY.test(children[item]))
			{
				//if(DEBUG){post('adding property:', children[item].replace('property ', ''), '\n');}
				properties.push(children[item].replace('property ', ''));
			}	
		}
		for(var item in properties)
		{
			//if(DEBUG){post('\nProperty #', item, ':', properties[item]);}
			if(MONOMODULAR.test(properties[item])>0)
			{
				if(DEBUG){post('in there\n');}
				found = true;
				var new_id = this.finder.get('monomodular');
				if(DEBUG){post('found, focusing on', new_id, '\n');}
				this.finder.id = parseInt(new_id[1]);
				this.finder.id = parseInt(finder.call('add_mod', 'id', this.this_device_id)[1]);
				if(DEBUG){post('client id returned is: ', this.finder.id, '\n');}
				this.finder.property = 'value';
				var children = this.finder.info.toString().split(new RegExp("\n"));	
				for(var item in children)
				{
					if(FUNCTION.test(children[item]))
					{
						//if(DEBUG){post('adding function:', children[item].replace('function ', ''), '\n');}
						this.modFunctions.push(children[item].replace('function ', ''));
					}	
				}
				this.modAddresses = this.finder.call('addresses');
				//if(DEBUG){post('addresses:', modAddresses, '\n');}
				for(var address in this.modAddresses)
				{
					//if(DEBUG){post('address length', modAddresses[address].length);}
					//if(DEBUG){post('making func:', modAddresses[address], '\n');}
					this[modAddresses[address]] = this.make_receive_func(this.modAddresses[address]);
				}
				for(var func in this.modFunctions)
				{
					this[modFunctions[func]] = make_func(this.modFunctions[func]);
				}
				if(this.legacy)
				{
					this.finder.call('set_legacy', 1);
				}
				this.output(1, 'init');
				this.send_stored_messages();
				return;
			}
		}
	}
}

Mod.prototype.assign_attributes = function(arguments)
{
	for(var i=0;i<arguments.length;i++)
	{
		if(arguments[i].toString().charAt(0) == '@')
		{
			var new_att = arguments[i].slice(1).toString();
			this[new_att] = arguments[i+1];
		}
	}
}

Mod.prototype.make_receive_func = function(address)
{
	var func = function()
	{
		//if(DEBUG){post('accessing func', address, '\n');}
		var args = arrayfromargs(arguments);
		this.finder.call('receive', address, args[0], args.slice(1).join('^'));
	}
	return func;
}

Mod.prototype.make_func = function(address)
{
	var func = function()
	{
		var args = arrayfromargs(arguments);
		//if(DEBUG){post('accessing func', address, args.join('^'), '\n');}
		//finder.apply(address, args);
		finder.call('distribute', address, args.join('^'))
	}
	return func;
}

Mod.prototype.callback = function(args)
{
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		if(DEBUG_CB){post('from client:', args, '\n');}
		this.output(0, args.slice(1));
	}
}

Mod.prototype.send_stored_messages = function()
{
	if(DEBUG){post('send_stored_messages()');}
	for(index in this.stored_messages)
	{
		if(DEBUG){post('sending stored message:', this.stored_messages[index], '\n');}
		if(stored_messages[index][0] in script)
		{
			if(DEBUG){post('found function in script.\n');}
			this[stored_messages[index][0]].apply(this, (this.stored_messages[index][1]));
		}
	}
}

Mod.prototype.send_explicit = function()
{
	var args = arrayfromargs(arguments);
	if(DEBUG){post('finder.call('+args[0], args[1], args[2], args[3], args[4], args[5]+');');}
	this.finder.call(args[0], args[1], args[2], args[3], args[4], args[5]);
}

Mod.prototype.output = function()
{
	script.apply('outlet', arguments);
}

Mod.prototype.wiki = function()
{
	this.max.launchbrowser('http://www.aumhaa.com/wiki/index.php?title='+this._type);
}


Mod.prototype.anything = function()
{
	var args = arrayfromargs(arguments);
	if(DEBUG){post('anything', messagename, args, '\n');}
	if(finder == null)
	{
		//if(DEBUG){post('adding to stack:', messagename, args, '\n');}
		if(stored_messages.length>500)
		{
			stored_messages.shift();
		}
		stored_messages.push([messagename, args]);
		//if(DEBUG){post('added:', stored_messages[0], '\n');}
	}
}

function list_functions()
{
	outlet(0, 'available_functions', thisMod.modFunctions);
}

function list_addresses()
{
	outlet(0, 'available_addresses', thisMod.modAddresses);
}

function init()
{
	post('init!\n');
	thisMod = new Mod(jsarguments[1], jsarguments[2], jsarguments.slice(3));
}

