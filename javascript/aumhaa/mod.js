autowatch = 1;

var util = require('util');

for(var i in util)
{
	this[i] = util[i];
}

var DEBUG_MOD = false;

ModComponent = function(parent, type, unique, legacy, attrs)
{
	var self = this;
	this.parent = parent;
	this.debug = DEBUG_MOD ? Debug : function(){};
	this.patch_type = type ? type : 'info';
	this.unique = unique ? unique : '---';
	this.legacy = legacy ? legacy : 0;
	this.attrs = attrs||[];
	this.MONOMODULAR=new RegExp(/(monomodular)/);
	this.FUNCTION = new RegExp(/(function)/);
	this.PROPERTY = new RegExp(/(property)/);
	this.WS = new RegExp('');
	this.modClientID = 0;
	this.modFunctions = [];
	this.modAddresses = [];
	this.this_device_id = 0;
	this.stored_messages = [];
	this.control_surface_ids = {0:true};
	this.restart = new Task(this.init, this);
	this.wiki_addy = 'http://www.aumhaa.com/wiki/index.php?title='+type;
	//this.debug('this.wiki_addy:', this.wiki_addy);
	this.finder = undefined;
	this.callback = function(args)
	{
		if((args[0]=='value')&&(args[1]!='bang'))
		{
			if(args[1] in parent)
			{
				parent[args[1]].apply(parent, args.slice(2));
			}
			else
			{
				parent.anything(args.slice(1));
			}
			if(args[1]=='disconnect')
			{
				
				self.disconnect();
			}
		}
	}	
}

ModComponent.prototype.disconnect = function()
{
	for(var address in this.modAddresses)
	{
		delete this[this.modAddresses[address]];
	}
	for(var func in this.modFunctions)
	{
		delete this[this.modFunctions[func]];
	}
	self.restart.schedule(3000);
}

ModComponent.prototype.assign_api = function(finder)
{
	this.finder = finder;
	this.init();
}

ModComponent.prototype.init = function()
{
	var found = false;
	this.debug('init_b996\n');
	this.assign_attributes(this.attrs);
	if((this.finder instanceof LiveAPI)&&(this.finder.id!=0))
	{
		this.finder.goto('this_device');
		this.this_device_id = parseInt(this.finder.id);
		this.debug('this device id:', this.this_device_id);
		this.finder.goto('control_surfaces');
		var number_children = parseInt(this.finder.children[0]);
		this.debug('control_surfaces length:', number_children );
		for(var i=0;i<number_children;i++)
		{
			this.debug('Checking control surface #:', i);
		   	this.finder.goto('control_surfaces', i);
			if(!this.control_surface_ids[parseInt(this.finder.id)])
			{
				this.debug('Control surface #:', i, 'was NOT in list of excluded surfaces.');
				var children = this.finder.info.toString().split(new RegExp("\n"));
				var functions = [];
				var properties = [];
				for(var item in children)
				{
					if(this.FUNCTION.test(children[item]))
					{
						//this.debug('adding function:', children[item].replace('function ', ''));
						functions.push(children[item].replace('function ', ''));
					}
					if(this.PROPERTY.test(children[item]))
					{
						//this.debug('adding property:', children[item].replace('property ', ''));
						properties.push(children[item].replace('property ', ''));
					}	
				}
				for(var item in properties)
				{
					//this.debug('Property #', item, ':', properties[item]);
					if(this.MONOMODULAR.test(properties[item])>0)
					{
						this.debug('in there\n');
						found = true;
						var new_id = this.finder.get('monomodular');
						this.debug('found, focusing on', new_id);
						this.finder.id = parseInt(new_id[1]);
						var modclient_id = this.finder.call('add_mod', 'id', this.this_device_id);
						this.debug('modclient id is:', modclient_id);
						this.finder.id = parseInt(modclient_id[1])
						this.debug('client id returned is: ', this.finder.id);
						this.modClientID = parseInt(modclient_id[1]);
						this.finder.property = 'value';
						var children = this.finder.info.toString().split(new RegExp("\n"));	
						for(var item in children)
						{
							if(this.FUNCTION.test(children[item]))
							{
								this.debug('adding function:', children[item].replace('function ', ''));
								this.modFunctions.push(children[item].replace('function ', ''));
							}	
						}
						this.modAddresses = this.finder.call('addresses');
						this.debug('addresses:', this.modAddresses);
						for(var address in this.modAddresses)
						{
							//this.debug('address length', this.modAddresses[address].length);
							this.debug('making receive func:', this.modAddresses[address]);
							this[this.modAddresses[address]] = this.make_receive_func(this.modAddresses[address]);
						}
						for(var func in this.modFunctions)
						{
							this.debug('making func:', this.modFunctions[func]);
							this[this.modFunctions[func]] = this.make_func(this.modFunctions[func]);
						}
						this.debug('setting legacy', this.legacy);
						this.finder.call('set_legacy', parseInt(this.legacy));
						if(this.parent.alive)
						{
							this.parent.alive(1);
							//if(!this.parent.wiki){this.parent.wiki = this.wiki;}
						}
						this.send_stored_messages();
					}
					else
					{
						//this.control_surface_ids[parseInt(this.finder.id)] = true;
					}
				}
			}
			else
			{
				this.debug('Control surface #:', i, 'WAS in list of excluded surfaces.');
			}
			if(found)
			{
				break;
			}
		}
		if(!found)
		{
			this.restart.schedule(10000);
		}
	}
}

ModComponent.prototype.assign_attributes = function(attrs)
{
	for(var i=0;i<attrs.length;i++)
	{
		var new_att = attrs.slice(1).toString();
		this[new_att] = attrs[i];
	}
}

ModComponent.prototype.make_receive_func = function(address)
{
	this.debug('make receive func', address);
	var func = function()
	{
		var args = protoarrayfromargs(arguments);
		this.debug('accessing receive func', address);
		this.finder.call('receive', address, args[0], args.slice(1).join('^').replace(',','^'));
	}
	return func;
}

ModComponent.prototype.make_receive_func = function(address)
{
	this.debug('make receive func', address);
	var func = function()
	{
		var args = protoarrayfromargs(arguments);
		this.debug('accessing Receive func', address);
		this.finder.call.apply(this.finder, ['Receive', address].concat(args));
	}
	return func;
}

ModComponent.prototype.make_func = function(address)
{
	this.debug('make func', address);
	var func = function()
	{
		var args = protoarrayfromargs(arguments);
		this.debug('accessing func', address, args.join('^').replace(',','^'));
		this.finder.call('distribute', address, args.join('^').replace(',','^'))
	}
	return func;
}

ModComponent.prototype.make_func = function(address)
{
	this.debug('make func', address);
	var func = function()
	{
		var args = protoarrayfromargs(arguments);
		this.debug('accessing Distribute func', address, args);
		this.finder.call.apply(this.finder, ['Distribute', address].concat(args));
	}
	return func;
}

ModComponent.prototype.anything = function()
{
	var args = flatten1(arguments);
	this.debug('anything', args[0], args.slice(1));
	if(this.finder == undefined)
	{
		this.debug('adding to stack:', args[0], args.slice(1));
		if(this.stored_messages.length>500)
		{
			this.stored_messages.shift();
		}
		this.stored_messages.push([args[0], args.slice(1)]);
		this.debug('added:', stored_messages[0]);
	}
}

ModComponent.prototype.list_functions = function()
{
	return modFunctions;
}

ModComponent.prototype.list_addresses = function()
{
	return modAddresses;
}

ModComponent.prototype.send_stored_messages = function()
{
	this.debug('send_stored_messages()');
	for(var index in this.stored_messages)
	{
		this.debug('sending stored message:', stored_messages[index]);
		if(this.stored_messages[index][0] in this)
		{
			this.debug('found function in script.');
			this[stored_messages[index][0]].apply(this, (this.stored_messages[index][1]));
		}
	}
}

ModComponent.prototype.send_explicit = function()
{
	var args = protoarrayfromargs(arguments);
	//debug('finder.call('+args[0], args[1], args[2], args[3], args[4], args[5]+');');
	this.finder.call(args[0], args[1], args[2], args[3], args[4], args[5]);
}

ModComponent.prototype.SendDirect = function()
{
	var args = flatten1(arguments);
	try
	{
		this.finder.call.apply(this.finder, args);
	}
	catch(err)
	{
		this.debug('SendDirect error:', err, args);
	}
}

ModComponent.prototype.Send = function()
{
	var args = flatten1(arguments);
	try
	{
		this[args[0]].apply(this, args.slice(1));
	}
	catch(err)
	{
		this.debug('Send error:', err, args);
		this.anything(arguments);
	}
}

ModComponent.prototype.wiki = function()
{
	max.launchbrowser(this.wiki_addy);
}

exports.ModComponent = ModComponent;



ModProxyComponent = function(parent, props)
{
	var self = this;
	this.debug = DEBUG_MOD ? Debug : function(){};
	this.patch_type = 'mod_proxy';
	this.unique = '---';
	this.legacy = 0;
	this.attrs = [];
	this.modFunctions = [];
	this.modAddresses = [];
	this.this_device_id = 0;
	this.stored_messages = [];
	this.control_surface_ids = {0:true};
	this.wiki_addy = undefined;
	this.finder = undefined;
	if(props!=undefined)
	{
		for(var i in props)
		{
			this[props[i]] = function(){}.bind(this);
		}
	}
}

exports.ModProxyComponent = ModProxyComponent;
