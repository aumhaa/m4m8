//aumhaa_chooser

var util = require('aumhaa_util');
util.inject(this, util);

var NotifierClass = require('aumhaa_notifier_class').NotifierClass;

var LOCAL_DEBUG = false;
var lcl_debug = LOCAL_DEBUG && util.Debug ? util.Debug : function(){}


function CellBlockChooserComponent(name, args){
  var self = this;
  if(!args.obj){
    throw new Error('CellBlockChooserComponent requires [cellblock] as its second argument');
  }
  this.add_bound_properties(this, [
    'input',
    'clear',
    'set',
    'set_height',
    'append',
    'multiselect',
    'doublepress_timer',
    '_last_pressed',
    '_bgcolor',
    'back',
    '_max_size',
    '_single_active',
    '_last_single_active'
  ]);
  this._max_size = 100000;
  this._row_height = 12;
  this._contents = [];
  this._single_active = undefined;
  this._last_single_active = undefined;
  this._active = [];
  this._active_items = [];
  this._active_indexes = [];
  this._multiSelect = false;
  this._reselect = false;
  this._doublepress_delay = 250;
  this._last_pressed = undefined;
  this._last_selected = undefined;
  this._doublepressed = false;
  this.COLORS = {
    transparent:[255, 255, 255, 0],
    white:[200, 200, 200, 255],
    off:[100, 100, 100, 255],
		red:[180, 0, 0, 255],
		green:[0, 180, 0, 255],
		blue:[0, 0, 180, 255],
		cyan:[0, 180, 180, 255],
		yellow:[180, 180, 0, 255],
		magenta:[180, 0, 180, 255],
    selected:[220, 150, 0, 130]
  };
  this._bgcolor = [.8, .8, .8, 1.];
  this._selected_color = 'selected';

  CellBlockChooserComponent.super_.call(this, name, args);
  this.doublepress_timer = new Task(function(){
    // lcl_debug('doublepress_timer');
    self._last_pressed = undefined;
    self._doublepressed = false;
  }, self);
  this._init.apply(this);
}

util.inherits(CellBlockChooserComponent, NotifierClass);

CellBlockChooserComponent.prototype._init = function(){
  lcl_debug('setting bgcolor:', this._bgcolor);
  this._obj.message('bgcolor', this._bgcolor);
  this.clear();
}

CellBlockChooserComponent.prototype.multiselect = function(val){
  if(val != this._multiSelect){
    this._multiSelect = val;
    if(!val){
      this._single_active = this._active_indexes[0];
      for(var i in this._contents){
        this._contents[i].active = false;
      }
    }
    if(this._single_active!=undefined){
      this._contents[this._single_active].active = true;
    }
    this._refresh();
    this._report_selected();
  }
}

CellBlockChooserComponent.prototype.append = function(){
  var args = arrayfromargs(arguments);
  this._contents.push({value:args.join(' '), _active:false});
  this._obj.message('rows', this._contents.length);
  this._obj.message('set', 0, this._contents.length-1, args);
  this._obj.message('vscroll', this._contents.length>this._row_height);
  //_refresh();
}

CellBlockChooserComponent.prototype.set_contents_from_obj = function(obj){
  // lcl_debug('cellblock_chooser.set_contents_from_obj', obj.length);
  this._contents = obj;
  this._contents.length = this._contents.length < this._max_size ? this._contents.length : this._max_size;
  // lcl_debug('cellblock_chooser.set_contents_from_obj new length:', obj.length);
  this._obj.message('rows', parseInt(this._contents.length));
  var len = this._contents.length;
  for(var i=0;i<len;i++){
    this._obj.message('set', 0, i, this._contents[i].value);
  }
  this._obj.message('vscroll', this._contents.length>this._row_height);
  this._refresh();
}

CellBlockChooserComponent.prototype.clear = function(){
  this._obj.message('rows', 0);
  this._obj.message('set', 0, 0, '');
  this._obj.message('vscroll', 0);
  this._contents = [];
  this._single_active = undefined;
  this._active = [];
  this._active_items = [];
  this._active_indexes = [];
  this._refresh();
}

CellBlockChooserComponent.prototype._refresh = function(){
  this._active = [];
  this._active_items = [];
  this._active_indexes = [];
  if(this._multiSelect){
    for(var i in this._contents){
      if(this._contents[i].active){
        this._active.push(this._contents[i]);
        this._active_items.push(this._contents[i].value);
        this._active_indexes.push(parseInt(i));
      }
      this._obj.message('cell', 0, parseInt(i), 'brgb', this._contents[i].active ? this.COLORS.selected : this.COLORS.transparent);
    }
  }
  else{
    this._active = this._single_active ? [this._contents[this._single_active]] : [];
    this._active_items = this._single_active ? [this._contents[this._single_active].value] : [];
    this._active_indexes = this._single_active ? [this._single_active] : [];
    for(var i in this._contents){
      this._contents[i].active = i == this._single_active;
      // this._obj.message('cell', 0, parseInt(i), 'brgb', parseInt(i) == this._single_active ? this.COLORS[this._selected_color]: this.COLORS.transparent);
    }
    this._obj.message('cell', 0, parseInt(this._last_single), 'brgb');
    this._last_single = this._single_active;
    this._obj.message('cell', 0, parseInt(this._single_active), 'brgb', this.COLORS.selected);
  }
  this._obj.message('vscroll', this._contents.length>this._row_height);
}

CellBlockChooserComponent.prototype.input = function(col, row, item){
  lcl_debug('cellblock_input', col, row, item);
  if(col == '<==back'){
    this.back();
  }
  else{
    if(row == this._last_pressed){
      this._doublepressed = true;
    }
    else{
      this._last_pressed = row;
      this.doublepress_timer.cancel();
      this.doublepress_timer.schedule(this._doublepress_delay);
    }
    if(this._contents[row]){
      if(this._multiSelect){
        this._contents[row].active = !this._contents[row].active;
      }
      if(this._reselect){
        this._single_active = row != undefined ? row : undefined;
      }
      else{
        this._single_active = row == this._single_active ? undefined : row;
      }
      this._refresh();
      this._report_selected();
    }
  }
}

CellBlockChooserComponent.prototype._report_selected = function(){
  if(this._multiSelect){
    this._value = this._active_items;
  }
  else {
    this._value = this._single_active!=undefined ?
      [this._single_active, this._contents[this._single_active].value, this._doublepressed] :
      [undefined, ''];
  }
  this.notify();
}

CellBlockChooserComponent.prototype.set = function(num){
  // lcl_debug('set', num);
  if(this._contents[num]){
    this._contents[num].active = true;
    this._single_active = num;
  }
  else{
    this._contents.forEach(function(obj){
      obj.active = false;
    });
    this._single_active = undefined;
  }
  this._refresh();
}

CellBlockChooserComponent.prototype.set_multi = function(){
  if(this.multiSelect){
    var items = arrayfromargs(argumnents);
    lcl_debug('set_multi', items, items.length);
    this._active = [];
    this._active_items = [];
    this._active_indexes = [];
    for(var i in this._contents){
      this._contents[i].active = items.indexOf(i) > -1;
      this._active.push(this._contents[i]);
      this._active_items.push(this._contents[i]._value);
      this._active_indexes.push(i);
    }
    this._refresh();
  }
}

CellBlockChooserComponent.prototype.set_height = function(val){
  this._row_height = val;
  this._refresh();
}

CellBlockChooserComponent.prototype.back = function(){
  lcl_debug('back', this._contents[this._contents.length-1].value);
  if(this._contents[this._contents.length-1].value == '<==back'){
    // this._active = [this._contents[this._contents.length-1]];
    // this._active_items = ['<==back'];
    // this._active_indexes = [this._contents.length-1]
    this._single_active = this._contents.length-1;
    this._refresh()
    this._report_selected();
  }
}

exports.CellBlockChooserComponent = CellBlockChooserComponent;
