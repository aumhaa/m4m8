//aumhaa_scales.js

function Scales(parameters){
	var self = this;
	this.colors = {OFF : 0, WHITE : 1, CYAN : 5, MAGENTA : 9, RED : 17, BLUE : 33, YELLOW : 65, GREEN : 127};
	this._grid = undefined;
	this._grid_function = function(){}
	this.width = function(){return  !this._grid ? 0 : this._grid.width();}
	this.height = function(){return !this._grid ? 0 : this._grid.height();}
	this._NOTENAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];
	this.NOTENAMES = [];
	for(var i=0;i<128;i++){
		this.NOTENAMES[i]=(_NOTENAMES[i%12] + ' ' + (Math.floor(i/12)-2) );
	}
	this.WHITEKEYS = {0:0, 2:2, 4:4, 5:5, 7:7, 9:9, 11:11, 12:12};
	this.NOTES = [24, 25, 26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7];
	this.DRUMNOTES = [12, 13, 14, 15, 28, 29, 30, 31, 8, 9, 10, 11, 24, 25, 26, 27, 4, 5, 6, 7, 20, 21, 22, 23, 0, 1, 2, 3, 16, 17, 18, 19];
	this.SCALENOTES = [36, 38, 40, 41, 43, 45, 47, 48, 24, 26, 28, 29, 31, 33, 35, 36, 12, 14, 16, 17, 19, 21, 23, 24, 0, 2, 4, 5, 7, 9, 11, 12];
	this.KEYCOLORS = [this.colors.BLUE, this.colors.CYAN, this.colors.MAGENTA, this.colors.RED, this.colors.GREEN, this.colors.GREEN, this.colors.GREEN, this.colors.GREEN];
	this.SCALES = 	{'Chromatic':[0,1,2,3,4,5,6,7,8,9,10,11],
				'Major':[0,2,4,5,7,9,11],
				'Minor':[0,2,3,5,7,8,10],
				'Dorian':[0,2,3,5,7,9,10],
				'Mixolydian':[0,2,4,5,7,9,10],
				'Lydian':[0,2,4,6,7,9,11],
				'Phrygian':[0,1,3,5,7,8,10],
				'Locrian':[0,1,3,4,7,8,10],
				'Diminished':[0,1,3,4,6,7,9,10],
				'Whole-half':[0,2,3,5,6,8,9,11],
				'Whole Tone':[0,2,4,6,8,10],
				'Minor Blues':[0,3,5,6,7,10],
				'Minor Pentatonic':[0,3,5,7,10],
				'Major Pentatonic':[0,2,4,7,9],
				'Harmonic Minor':[0,2,3,5,7,8,11],
				'Melodic Minor':[0,2,3,5,7,9,11],
				'Dominant Sus':[0,2,5,7,9,10],
				'Super Locrian':[0,1,3,4,6,8,10],
				'Neopolitan Minor':[0,1,3,5,7,8,11],
				'Neopolitan Major':[0,1,3,5,7,9,11],
				'Enigmatic Minor':[0,1,3,6,7,10,11],
				'Enigmatic':[0,1,4,6,8,10,11],
				'Composite':[0,1,4,6,7,8,11],
				'Bebop Locrian':[0,2,3,5,6,8,10,11],
				'Bebop Dominant':[0,2,4,5,7,9,10,11],
				'Bebop Major':[0,2,4,5,7,8,9,11],
				'Bhairav':[0,1,4,5,7,8,11],
				'Hungarian Minor':[0,2,3,6,7,8,11],
				'Minor Gypsy':[0,1,4,5,7,8,10],
				'Persian':[0,1,4,5,6,8,11],
				'Hirojoshi':[0,2,3,7,8],
				'In-Sen':[0,1,5,7,10],
				'Iwato':[0,1,5,6,10],
				'Kumoi':[0,2,3,7,9],
				'Pelog':[0,1,3,4,7,8],
				'Spanish':[0,1,3,4,5,6,8,10]};
	this.SCALENAMES = [];
	var i = 0;
	for (var name in this.SCALES){this.SCALENAMES[i] = name;i++};
	this._noteMap = new Array(256);
	for(var i=0;i<256;i++){
		this._noteMap[i] = [];
	}
	this.DEFAULT_SCALE = 'Major';
	this.SPLIT_SCALES = {}; //{'DrumPad':1, 'Major':1};
	for(var param in parameters){
		self[param] = parameters[param];
	}
	this._update = function(){
		self._update_request = false;
		self._noteMap = [];
		for(var i=0;i<128;i++){
			self._noteMap[i] = [];
		}
		// if(self._grid instanceof Grid){
		if(isClass(self._grid, 'Grid')){
			var keyoffset = -1;
			var notes_in_step = self.notes_in_step();
			var selected = self._stepsequencer && self._select._value ? self._stepsequencer.key_offset._value : -1;
			var select_only = self._select_only._value;
			var width = self.width();
			var height = self.height();
			var offset = self._noteOffset._value;
			var vertoffset = self._vertOffset._value;
			var scale = SCALENAMES[self._scaleOffset._value];
			self._current_scale = scale;
			var scale_len = SCALES[scale].length;
			for(var column=0;column<width;column++){
				for(var row=0;row<height;row++){
					var note_pos = column + (Math.abs((height-1)-row))*parseInt(vertoffset);
					var note = offset + SCALES[scale][note_pos%scale_len] + (12*Math.floor(note_pos/scale_len));
					var button = self._grid.get_button(column, row);
					if(!select_only){button.set_translation(note%127);}
					else{button._translation = note%127}  //you slimy bastard....
					self._noteMap[note%127].push(button);
					//lcl_debug('note', note, 'keyoffset', keyoffset, note == keyoffset, note === keyoffset);
					button.scale_color = notes_in_step[note%127] ? this.colors.GREEN : note == selected ? this.colors.WHITE : KEYCOLORS[((note%12) in WHITEKEYS) + (((note_pos%scale_len)==0)*2)];// + ((notes_in_step[note%127])*4)];
					button.send(button.scale_color);
				}
			}
		}
	}
}

Scales.prototype.set_grid_function = function(func){
	self.grid_function = func;
}

exports.Scales = Scales;
