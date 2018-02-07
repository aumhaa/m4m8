/*
operates in parent patch

takes in all the info needed to communicate to live.step via pattr
the list looks like this:
<nseq> <nstep> <unknown> <active> <unknown> <loop in> <loop out> <zoom lo> <zoom hi> <direction> <fold> 
<s1 note> <s1 vel> <s1 dur+> <s1 e1> and so on through all 16 steps.
                        +duration value is 0-7, representing 0, 128n, 64n,...,2n
<unknown>
I've seen one extra element at the end of the list, after all the step data, but I haven't reproduced. dunno what it is.

For the sake of possible future explorations, if there are 16 seqs of 16 steps in a live.step, there is:
header of 33 items (nseq, then 16 pairs of ? ?)
16 lists of 88 elements each for each seq, 
    first 8 elements are seq-specific header (active ? loopin loopout zoom lo zoomhi dir fold)
    the other 80 elements are 
        16 lists of 5 elements (note, vel, sur, ex1, ex2)
*/
autowatch = 1;
outlets=2;
setinletassist(0,"sequence data in");
setoutletassist(0,"to pattrstorage");
setoutletassist(1,"to coll for pitch data");


var DEBUG = 0;

var seq_id=0;
var pattrseq = new Array(); //array that is the same as the list that pattrstorage uses to describe all data in live.step
var seq = new Object;
seq.header = new Array();
seq.pitch = new Array();
seq.vel = new Array(); 
seq.dur = new Array();
seq.extra1 = new Array();
seq.extra2 = new Array();
seq.enable = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];//set up a default
seq.behav = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];//set up a default
seq.root = 60;

//datakeys object is used to make it easy to parse out what is important in the function anything():
var datakeys = {'pitch':'', 'vel':'','dur':'','extra1':'','extra2':'','enable':'','behav':''}
//durval is used to convert ticks to an index 0-7, which is what pattrstorage uses for live.step duration:
var durval = {7.5:0, 15:1, 30:2, 60:3, 120:4, 240:5, 480:6, 960:7}

var nstep = 16;
var loop = [0,16]; //loop in/out points
var zoom = [55,80]; //set bounds of live.step window
var direction = 0;
var fold = 0; //probably won't need this
var step_length = 5; //# of data elements in a step: note, vel, dur, extra1, extra2.

var scale_num = 0;
var modes = new Array();
modes[0] = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28]; 
modes[1] = [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24, 26, 27];
modes[2] = [0, 1, 3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27]; 
modes[3] = [0, 2, 4, 6, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28]; 
modes[4] = [0, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28]; 
modes[5] = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 28]; 
modes[6] = [0, 1, 3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 25, 27];


function sequpdate(){
    var a = arrayfromargs(arguments);     //the value or values. we're only concerned with the first element tho.
    var cut = a.slice(1);     //slice off heirarchy if it exists
    //call the sequence function with our data:
    sequence(cut.slice(0));
}

//update the behav-connected buttons by sending a message to pattrstorage:
function behaviors(){
    var a = arrayfromargs(arguments);
    var behavlist = a.slice(1); //get rid of the first element "sequence[<n>]::behaviors"
    for(var i=0;i<behavlist.length;i++){
        seq.behav[i]=behavlist[i];
        if(behavgate) outlet(0,"behav["+i+"]",behavlist[i]);
    }
}
//behaviors.immediate=0;

//with a [pattr sequence] bound to the live.step, we can get this info from pattrstorage, and process
//it from the list into the more manageable seq. object.
function sequence(){
    //the array we are interested in could be an array or it could all be crammed into the 1st element of an array, so we adjust:
    var a = arrayfromargs(arguments);
    if(a.length==1){
        pattrseq = a[0];
    }else{
        pattrseq = a.slice(0);
    }
    if(DEBUG) post("\nSEQIN---------------->");
    //post("\nasP: Seq Len",pattrseq.length);
    if(pattrseq.length == 91){
        //set up some variables from the first few elements in the array:
        //anygate = 0;
        nstep = pattrseq[1];
        loop=[pattrseq[5],pattrseq[6]];
        zoom=[pattrseq[7],pattrseq[8]];
        direction = pattrseq[9];
        fold = pattrseq[10];
        //headlength is always the same, it's the last 80 elements that describe each of the 16 steps (5 elements per step)
        var headlen = 11;
        var stepend = headlen+(nstep*step_length); //number of steps times number of elements in a step. for a 16 step seq, this is 80.
        seq.header=pattrseq.slice(0,headlen);
        var thesteps = pattrseq.slice(headlen,stepend); //from the 11th element to the end of the step data);
        seq.footer=pattrseq.slice(stepend,pattrseq.length); //everything else in the list. probably only 0-1 thing.
        //break up the list from pattrstorage into the various objects
        //step_length is the # of items in the list that make up the data in a step
        for(var i=0;i<nstep;i++){ //for a 16 step seq, this should be 80!
            var j=i*step_length;
            seq.pitch[i]=thesteps[j];
            seq.vel[i]=thesteps[j+1];
            seq.dur[i]=thesteps[j+2];
            seq.extra1[i]=thesteps[j+3];
            //post("\nasP: step",i,j,pitch[i],vel[i],dur[i]);
            seq.extra2[i]=thesteps[j+4];
        }
        seq.enable=seq.extra2.slice(0) //keep these in sync, since they are the same thing
        //modes[scale_num] is current scale
        scaleout();
        //don't let anything() get called for 20ms:
        //anylim.schedule(20);
    }
}

//the id or index of the currently selected drumpad:
function seqid(v){
    seq_id=v;
    get();
    seqout();
}

//some synonmyms which get the sequence info from pattrstorage, to be processed by this script's function sequence():
function bang(){
    get();
}
function recall(){
    get();
    seqout();
}
function read(){
    get();
}
function get(){    
    if(DEBUG) post("\nGET",seq_id);
    outlet(0,"getsequence["+seq_id+"]::sequence");
    outlet(0,"getsequence["+seq_id+"]::behaviors");
}

//anything limiter: if data is coming into sequence, we'll get a bunch of stuff into anything that we don't really need
//so I setup a speed limiter to gate that
var anygate=1;
var anylim = new Task(anygater);
function anygater(){
    anygate = 1;
}

var enablegate = 1; //supress enable message out when the anything coming in is an enable message
var behavgate = 1; //supress enable message out when the anything coming in is an enable message
//anything() takes a key/value pair and puts it in seq Object. For example "enable[1] 1" would become seq.enable[1]=1
function anything(){
    //post("\npregate.....");
    if(anygate){
        var a = arrayfromargs(arguments);     //the value or values. we're only concerned with the first element tho.
        //post("ANY",messagename,a);
        var cut = messagename.split("::");     //slice off heirarchy if it exists
        var key = cut[cut.length-1].split("["); //the object name we care about, like "pitch" or "dur" is at the end of heirarchy (the 'cut' Array)
        //use the datakeys object so we only do something if it is a key that we care about (i.e., in 'datakeys' - pitch,vel,dur,extra1,extra2,enable):
        if(key[0] in datakeys){
            enablegate = 1;
            behavgate = 1;
            var index = parseInt(key[1].split("]")); //ditch the brackets and get the index
            if(DEBUG) post("\nasP: any",key[0],"i",index,"v",a); //here's what we got
            if(!seq[key[0]]) {
                seq[key[0]]=new Array(); //initialize the object if it doesn't exist
            }
            if(key[0]=="dur"){
                seq[key[0]][index]=durval[a[0]]; //convert the ticks value into the 0-7 value that pattr wants
            }else{
                seq[key[0]][index]=a[0];
                if(key[0]=="enable"){
                    seq.extra2=seq.enable.slice(0); //seq.extra2 and seq.enable are synonymous, so keep them synced
                    enablegate = 0;
                }
                if(key[0]=="behav"){
                    behavgate = 0;
                }
            }
            seqout();
            enablegate = 1;
            behavgate = 1;
        }
    }
}

//manipulate the seq object to assemble the live.step list for pattr 
function seqout(){
    if(seq.pitch.length){
        var undef=0;
        if(DEBUG) post("\n---->seqout");
        var thesteps=new Array();
        for(var i=0;i<nstep;i++){ 
            var j=i*step_length;
            thesteps[j]=seq.pitch[i];
            thesteps[j+1]=seq.vel[i];
            thesteps[j+2]=seq.dur[i];//need to use a lookup table 'durval' to convert the duration into ticks
            //for reasons unknown, was getting durations as undefined at init. This supresses that problem, tho makes no attempt to understand!
            if(thesteps[j+2]==undefined){
                undef=1
                //post("UNDEF");
            }
            thesteps[j+3]=seq.extra1[i];
            thesteps[j+4]=seq.extra2[i];
        }
        if(!undef){
            //prepend the header data and append the footer data:
            var joined = seq.header.concat(thesteps,seq.footer);
            //prepend with sequence[<seq_id>]:: so we address a heirarchy of sequence bpatchers
            outlet(0,"sequence["+seq_id+"]::"+"sequence",joined);
            outlet(0,"sequence["+seq_id+"]::"+"behaviors",seq.behav);
            //update the enable toggles in the UI:
            if(enablegate){
                for(i in seq.enable){
                    var inti=parseInt(i);
                    var enable_msg = "enable["+inti+"]";
                    outlet(0,enable_msg,seq.enable[i]);
                }
            }
            //send current scale out outlet 1:
            scaleout();
        }
    }
}

//sub is the sub-list that is rotated:
var sub = new Object;
sub.pitch = new Array();
sub.velocity = new Array();
sub.duration = new Array();
sub.extra1 = new Array();
sub.extra2 = new Array();
//rotation limiter: for whatever reason, I'm getting 2x messages from pattrstorage when I send a message to the parent
//so I setup a speed limiter to get rid of unintended repeats: 
var rotgate=1;
var rotlim = new Task(rotgater);
function rotgater(){
    rotgate = 1;
}
function rot(dir,sub_size){
    if(rotgate && dir>=0){ //only allow 1 message every 10ms with rotgate, and ignore negative number direction
        rotgate = 0;
        //clear buffer and initialize components as new array:
        var buf = new Object;
        for(p in datakeys){
            buf[p]=new Array();
        }
    
        var chunk = sub_size; //length of sub
        var toend = 0;
        var groups = Math.ceil(seq.pitch.length/chunk); //number of subs
        //post("\nasP: ROT test",sub_size,seq.pitch.length,chunk,groups)
        for(var i=0;i<groups;i++){
            var mins= i*chunk;
            var maxs = mins+(chunk);
            //post("\nasP: mm",mins,maxs,chunk,groups);
            for(p in datakeys){
                sub[p] = seq[p].slice(mins,maxs);
            }
            //The shift() method removes the first element of an array, and returns that element.
            switch(dir){
                case 0: //left shift
                    for(p in datakeys){
                        //post("\nasP: L",p,sub[p],"....");
                        toend=sub[p].shift();//remove the first element and store it
                        sub[p].push(toend); //then add it to the end
                        //post("postrot:",sub[p]);
                    }
                break;
                case 1: //right shift
                    for(p in datakeys){
                        toend=sub[p].pop();//remove the first element and store it
                        sub[p].unshift(toend); //then add it to the end
                    }
                break;
            }
            //need to work in the subchunks to the mains...
            for(p in datakeys){
                buf[p] = buf[p].concat(sub[p]);
            }
        }
        for(p in datakeys){
            seq[p]=buf[p].slice(0);
            if(DEBUG) post("\nasP: rot_",p,seq[p]);    
        }
        seqout();
    }
    rotlim.schedule(10); //open up the gate in 10 ms
}

//transpose limiter: for whatever reason, I'm getting 2x messages from pattrstorage when I send a message to the parent
//so I setup a speed limiter to get rid of unintended repeats. 
var transgate=1;
var translim = new Task(transgater);
function transgater(){
    transgate = 1;
}
function transpose(v){
    if(transgate && v!=0){ //only allow transpose messages every 10ms, and only if the v is not 0
        transgate=0;
        var a = new Array();
        for(var i=0;i<nstep;i++){
            a[i]=v
        }
        if(DEBUG) post("\nasP: trans",a);
        shift_pitch(a);
        translim.schedule(10); //open up the gate in 10 ms
    }
}

function shift_pitch()
{
    var args = arrayfromargs(arguments);
    //when we call this from transpose, the array is crammed into the first element. let's release it:
    if (args.length==1){
        args=args[0];
    }
    //post('\nas: shift', args,args.length);
    
    //add the shift to the current values:
    for(var i=0;i<seq.pitch.length;i++)
    {
        seq.pitch[i] = seq.pitch[i]+args[i];
        if(DEBUG) post("\nasP: pitch",seq.pitch[i]);
    }
    //change the zoom:
    var bottom=Math.min.apply( Math, seq.pitch ); //find the lowest pitch in the seq.pitch array
    var top=Math.max.apply( Math, seq.pitch ); //find the highest pitch in the seq.pitch array
    var zoompad = 5;
    seq.header[7]=bottom-zoompad;
    seq.header[8]=top+zoompad;
    var chainorigin = 36;
    //update the root
    rootupdate();
    outlet(0,"lowpitch",seq_id,(bottom-chainorigin)); //used for drumrack to map the encoders to the notes chain. e.g., note 36 maps to chain 0, 37 to chain 1, and so on.
    //send the sequence data out:
    seqout();
}
function scaleout(){
    if(seq.pitch.length){
        if(DEBUG) post('\nas: root',seq.root,"pitch",seq.pitch,"scale",modes[scale_num]);
        for (p in modes[scale_num]){
            var offset = parseInt(p);
            //post("\nasP: as: scaleout",p,modes[scale_num][p],seq.root,seq.root+modes[scale_num][p]);
            outlet(1,parseInt(p),seq.root+modes[scale_num][p]); //output the pitches in the current scale to coll
        }
    }
}
function rootupdate(){
    seq.root=Math.min.apply( Math, seq.pitch );
}
function scale(v){
    //get the lowest value in the seq and call that root
    rootupdate();
    //post("\nasP: root",seq.root);
    shift_scale(seq.root,v);
}

function shift_scale(root, num)
{
    if((root!=undefined)&&(num!=undefined)){
        //post('shift_scale', root, num, '\nas: ');
        var changes = [];
        for(var i=0;i<modes[num].length;i++)
        {
            changes[i] = (modes[num][i]) - (modes[scale_num][i]);
        }
        for(var i=0;i<seq.pitch.length;i++)
        {
            var bitie = modes[scale_num].indexOf(seq.pitch[i]-root);
            if(bitie > -1)
            {
                seq.pitch[i] += changes[bitie];
            }
        }
        scale_num = num;
        seqout();
    }
}

function dbug(v){
    DEBUG = v;
}

function poster(){
/*
    for(i in seq){
        post("\nas POSTER: ",i,seq[i]);
    }
*/
}