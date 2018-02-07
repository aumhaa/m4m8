autowatch = 1;

//var wiki_addy = 'http://www.aumhaa.com/wiki/index.php?title='+patch_type;
var DEBUG = false;
var DEBUG_CB = false;

function ModComponent(patch_type, unique, legacy)
{
	var self = this;
	this.patch_type = patch_type;
	this.unique = unique||'---';
	this.legacy = legacy||false;
	this.MONOMODULAR=new RegExp(/(monomodular)/);
	this.FUNCTION = new RegExp(/(function)/);
	this.PROPERTY = new RegExp(/(property)/);
	this.WS = new RegExp('');
	this.modFunctions = [];
	this.modAddresses = [];
	this.this_device_id = 0;
	this.stored_messages = [];
	this.finder = new LiveAPI(this.callback, 'this_device');
}

ModComponent.prototype.init = function()
{
	var found = false;
	if(DEBUG){post('init_b996\n');}
	this.assign_attributes();
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
			if(this.FUNCTION.test(children[item]))
			{
				//if(DEBUG){post('adding function:', children[item].replace('function ', ''), '\n');}
				functions.push(children[item].replace('function ', ''));
			}
			if(this.PROPERTY.test(children[item]))
			{
				//if(DEBUG){post('adding property:', children[item].replace('property ', ''), '\n');}
				properties.push(children[item].replace('property ', ''));
			}	
		}
		for(var item in properties)
		{
			//if(DEBUG){post('\nProperty #', item, ':', properties[item]);}
			if(this.MONOMODULAR.test(properties[item])>0)
			{
				if(DEBUG){post('in there\n');}
				found = true;
				var new_id = finder.get('monomodular');
				if(DEBUG){post('found, focusing on', new_id, '\n');}
				this.finder.id = parseInt(new_id[1]);
				this.finder.id = parseInt(finder.call('add_mod', 'id', this_device_id)[1]);
				if(DEBUG){post('client id returned is: ', this.finder.id, '\n');}
				this.finder.property = 'value';
				var children = this.finder.info.toString().split(new RegExp("\n"));	
				for(var item in children)
				{
					if(this.FUNCTION.test(children[item]))
					{
						if(DEBUG){post('adding function:', children[item].replace('function ', ''), '\n');}
						this.modFunctions.push(children[item].replace('function ', ''));
					}	
				}
				this.modAddresses = finder.call('addresses');
				if(DEBUG){post('addresses:', this.modAddresses, '\n');}
				for(var address in this.modAddresses)
				{
					if(DEBUG){post('address length', this.modAddresses[address].length);}
					if(DEBUG){post('making func:', this.modAddresses[address], '\n');}
					this.modAddresses[address] = this.make_receive_func(this.modAddresses[address]);
				}
				for(var func in this.modFunctions)
				{
					this.modFunctions[func] = make_func(this.modFunctions[func]);
				}
				if(legacy)
				{
					this.finder.call('set_legacy', 1);
				}
				//outlet(1, 'init');
				alive(1);
				this.send_stored_messages();
			}
		}
	}
}

ModComponent.prototype.assign_attributes = function()
{
	for(var i=0;i<jsarguments.length;i++)
	{
		if(jsarguments[i].toString().charAt(0) == '@')
		{
			var new_att = jsarguments[i].slice(1).toString();
			this[new_att] = jsarguments[i+1];
		}
	}
}

ModComponent.prototype.make_receive_func = function(address)
{
	var func = function()
	{
		if(DEBUG){post('accessing func', address, '\n');}
		var args = arrayfromargs(arguments);
		finder.call('receive', address, args[0], args.slice(1).join('^'));
	}
	return func;
}

ModComponent.prototype.make_func = function(address)
{
	var func = function()
	{
		var args = arrayfromargs(arguments);
		if(DEBUG){post('accessing func', address, args.join('^'), '\n');}
		//finder.apply(address, args);
		finder.call('distribute', address, args.join('^'))
	}
	return func;
}

ModComponent.prototype.anything = function()
{
	var args = arrayfromargs(arguments);
	if(DEBUG){post('anything', messagename, args, '\n');}
	if(finder == null)
	{
		if(DEBUG){post('adding to stack:', messagename, args, '\n');}
		if(stored_messages.length>500)
		{
			stored_messages.shift();
		}
		stored_messages.push([messagename, args]);
		if(DEBUG){post('added:', stored_messages[0], '\n');}
	}
}

ModComponent.prototype.list_functions = function()
{
	outlet(1, 'available_functions', modFunctions);
}

ModComponent.prototype.list_addresses = function()
{
	outlet(1, 'available_addresses', modAddresses);
}

ModComponent.prototype.callback = function(args)
{
	if((args[0]=='value')&&(args[1]!='bang'))
	{
		if(DEBUG_CB){post('from client:', args, '\n');}
		outlet(0, args.slice(1));
	}
}

ModComponent.prototype.send_stored_messages = function()
{
	if(DEBUG){post('send_stored_messages()');}
	for(index in stored_messages)
	{
		if(DEBUG){post('sending stored message:', stored_messages[index], '\n');}
		if(stored_messages[index][0] in script)
		{
			if(DEBUG){post('found function in script.\n');}
			script[stored_messages[index][0]].apply(this, (stored_messages[index][1]));
		}
	}
}

ModComponent.prototype.send_explicit = function()
{
	var args = arrayfromargs(arguments);
	//post('finder.call('+args[0], args[1], args[2], args[3], args[4], args[5]+');');
	finder.call(args[0], args[1], args[2], args[3], args[4], args[5]);
}
	