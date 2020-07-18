//aumhaa_notifier_consts.js


var NOTE_TYPE = 'NOTE_TYPE';
var CC_TYPE = 'CC_TYPE';
var NONE_TYPE = 'NONE_TYPE';
var MAXOBJ_TYPE = 'MAXOBJ_TYPE';
var CHANNEL = 0;
var NONE = 'NONE';
var colors = {OFF : 0, WHITE : 1, YELLOW : 2, CYAN : 3, MAGENTA : 4, RED : 5, GREEN : 6, BLUE : 7};
var LividColors = {OFF : 0, WHITE : 1, CYAN : 5, MAGENTA : 9, RED : 17, BLUE : 33, YELLOW : 65, GREEN : 127};
var PushColors = {OFF : 0, WHITE : 1, YELLOW : 2, CYAN : 3, MAGENTA : 4, RED : 5, GREEN : 6, BLUE : 7};
var MaxColors = {OFF : [0, 0, 0], WHITE : [1, 1, 1], YELLOW: [1, 1, 0], CYAN: [0, 1, 1], MAGENTA: [1, 0, 1], RED: [1, 0, 0], GREEN: [0, 1, 0], BLUE: [0, 0, 1]};
//PushColors = {OFF : 0, WHITE : 120, CYAN : 30, MAGENTA : 12, RED : 20, BLUE : 65, YELLOW : 11, GREEN : 125};

exports.consts = {
  NOTE_TYPE:NOTE_TYPE,
  CC_TYPE:CC_TYPE,
  NONE_TYPE:NONE_TYPE,
  MAXOBJ_TYPE:MAXOBJ_TYPE,
  CHANNEL:CHANNEL,
  NONE:NONE,
  colors:colors,
  PushColors:PushColors,
  LividColors:LividColors,
  MaxColors:MaxColors
};
