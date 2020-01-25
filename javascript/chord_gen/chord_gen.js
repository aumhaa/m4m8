editfontsize = 12;
autowatch = 1;
outlets = 1;
inlets = 1;
setinletassist(0,"note value");
setoutletassist(0,"chord as list");

var root = 36;
var athird = 4; //semitones
var afifth = 7; //semitones
var aoctave = 12;
var pitches = [0,4,7,0,0];
var chord = [36,40,43,0,0];
var chordout = [];
var dominor = [0,-1];
var treatfifth = [0,-1,1];
var treatseventh = [0,9,10,11,14];
var treatninth = [0,1,3,5,9];
var invs = [0,0,0,0,0];
var ova = [0,0,0,0,0];
var vdev = 0;
var DBUG = 1;
 
function notevel(nn,vel){
  var velout = 100;
  note(nn);
  for (i in chordout){
    if(i!=0){ //keep root orignal velocity
      if(vel>0){
        var random_variation = Math.random() * vdev * vel;
        velout = Math.round(vel - ( random_variation ));
      } else {
        velout = vel;
      }
    }else{
      velout = vel
    }
    outlet(0,chordout[i],velout);
  }
  
}

function note(v){
  var v = limiter(v,0,127);
	root = v;
	chord = [];
	for (var i=0;i<pitches.length;i++){
	  if(pitches[i]>0 || i==0){
	    //post("\nmake",root,pitches[i],invs[i],ova[i]);
      chord[i]=root+pitches[i]+invs[i]+ova[i];
      chord[i]=limiter(chord[i],0,127);
    } else {
      
    }
	}
	chordout = [];
	var count = 0;
	//drop any zero pitches and compact the list
	for (var i=0;i<chord.length;i++){
	  if(chord[i]>0){
      chordout[count]=chord[i];
	  }
	  count++;
	}
	//if root is 0, this falls apart. band-aid:
	chordout[0] = chord[0];
	//filter repetitions
	chordout = uniq(chordout);
	//output
	//outlet(0,chordout);
	if(DBUG) post("\nchordlist",chordout);
}

//flat the third
function minor(v){
  var v = limiter(v,0,1);
  pitches[1] = athird+dominor[v];
  if(DBUG) note(root);
}

//flat or sharp the fifth
function fifth(v){
  var v = limiter(v,0,4);
  pitches[2] = afifth+treatfifth[v];
  if(DBUG) note(root);
}

//add a 4th note to the chord
function seventh(v){
  var v = limiter(v,0,4);
  pitches[3] = treatseventh[v];
  if(DBUG) note(root);
} 

//add a 5th note to the chord
function ninth(v){
  var v = limiter(v,0,4);
  pitches[4] = treatninth[v];
  if(DBUG) note(root);
}

//inversion transposes the parts of the triad up an octave. 1st inversion treats root, 2nd treats the third, 3rd treats the fifth.
function inversion(v){
  var v = limiter(v,0,3);
  for (var i=0;i<invs.length;i++){
    if(i<v){
      invs[i] = aoctave;
    }else{
      invs[i] = 0;
    }
  }
  if(DBUG) note(root);
}

//drop the root <v> octaves and raise the fifth <v> octaves
function disposition(v){
  var v = limiter(v,0,3);
  ova[0] = (-1) * v * aoctave;
  ova[2] = v * aoctave;
  if(DBUG) note(root);
}

function spread(v){
  var v = limiter(v,0,3);
  if(v%2){
  ova[1] = v * aoctave;
  } else {
  ova[3] = v * aoctave;
  }
  if(DBUG) note(root);
}

//utility to limit an input to a range
function limiter(v,min,max){
  var v = Math.min(Math.max(v, min), max);
  return v;
}

//0.0-1.0 deviation probability in velocities of notes when chord is played
function velocity_var(v){
  vdev = v;
}

function uniq(arr) {
    var dups = {};
    return arr.filter(function(el) {
        var hash = el.valueOf();
        var isDup = dups[hash];
        dups[hash] = true;
        return !isDup;
    });
}