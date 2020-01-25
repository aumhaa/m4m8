autowatch = 1;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);
var script = this;


var _name = 'api_parser.js';
var finder;
var pointer;
var root_paths = ['this_device', 'control_surfaces', 'live_app', 'live_set'];
var menu_contents = [];
var second_menu_contents = [];
var current_subject = -1;
var main_readout_contents = [];

function init(){
	debug('init', this._name);
	find_patcher_objects(script, patcher, get_patcher_script_names(patcher));
	main_menu.message('clear');
	second_menu.message('clear');
	finder = new LiveAPI();
	pointer = new LiveAPI(pointer_callback);
	populate_main_menu();
	print_main_readout([]);
}

function pointer_callback(args){
	debug('pointer_callback', args);
	if(args[0]=='id'){
		print_main_readout(pointer.info.split('\n').slice(0,-1));
		populate_second_menu();
	}
}

function populate_main_menu(){
	menu_contents = pointer.children;
	if(pointer.id!=0){
		menu_contents.push('top');
	}
	var type = pointer.type;
	debug('menu_contents:', menu_contents);
	main_menu.message('clear');
	for(var i in menu_contents){
		main_menu.message('append', menu_contents[i]);
	}
}

function populate_second_menu(){
	second_menu.message('clear');
	finder.id = Math.floor(pointer.id);
	var path = finder.path;
	var entry = menu_contents[current_subject];
	var count = pointer.getcount(entry);
	if(count){
		second_menu_contents = [];
		for(var i=0;i<count;i++){
			finder.path = path;
			finder.goto(entry, i);
			var info = finder.info.split('\n');
			debug('info:', info.length, info);
			var name = '';
			var type = 'no type';
			if(info.indexOf('property name str')>-1){
				var name = finder.get('name');
			}
			var type = finder.type;
			second_menu_contents.push(i + ' : ' + type + ' - ' + name);
		}
		for(var i in second_menu_contents){
			second_menu.message('append', second_menu_contents[i]);
		}
	}
}

function print_main_readout(data){
	main_readout_contents = data;
	main_readout.message('clear');
	for(var i=0;i<data.length;i++){
		main_readout.message('append', main_readout_contents[i]);
	}
}

function print_second_readout(data)
{
	second_readout.message('clear');
	for(var i=0;i<data.length;i++){
		second_readout.message('append', data[i]);
	}
}

function mainmenu_in(val)
{
	current_subject = val;
	var entry = menu_contents[current_subject];
	if(entry == 'top'){
		pointer.id = 0;
	}
	else{
		finder.id = Math.floor(pointer.id);
		var count = finder.getcount(entry);
		debug('count:', count);
		if(count==-1){
			pointer.goto(entry);
		}
		else{
			finder.goto(entry);
			print_main_readout(finder.info.split('\n').slice(0,-1));
			populate_second_menu();
		}
	}
	populate_main_menu();

}

function secondmenu_in(val)
{
	var entry = menu_contents[current_subject];
	finder.id = Math.floor(pointer.id);
	var count = finder.getcount(entry);
	if((count>0)&&(val<count)){
		pointer.goto(entry+' '+val);
		populate_main_menu();
	}
}

function thirdmenu_in(val)
{
	var entry = main_readout_contents[val].split(' ');
	if(entry[0]=='property')
	{
		print_second_readout(['property:', entry[1], pointer.get(entry[1])]);
	}
	if(entry[0]=='function')
	{
		print_second_readout(['function:', entry[1], pointer.call(entry[1])]);
	}
}


forceload(this);
