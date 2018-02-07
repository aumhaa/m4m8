autowatch = 1;
outlets = 2;
var nstep = 16;
var width = 354;
var height = 20;
var unit = width/height;
var spacing = 0.135;
var fontsize = 9;
var font = "Arial Bold";
var fonty = 12;
var fontcolor = [0,0,0,255];
var oncolor = [173, 198, 163, 255];
var offcolor = [173, 188, 209, 255];
var modes = ['----','only 2','only 4','only 8','skip 2','skip 4','skip 8','only 16'];
var tog = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];
var item = 0;
var black = [0,0,0,255];
var white = [255,255,255,255];
var blue = [80,80,120,255];
var red = [180,60,60,255];
var colors = new Array();
/*
colors[0]=[140,145,153,255];
colors[1]=[230,228,245,255];
colors[2]=[192,232,241,255];
colors[3]=[217,193,246,255];
colors[4]=[217,163,171,255];
colors[5]=[189,201,240,255];
colors[6]=[233,229,201,255];
colors[7]=[185,231,191,255];
*/
colors[0]=[140,145,153,255];
colors[1]=[255,255,255,255];
colors[2]=[167,232,246,255];
colors[3]=[234,182,228,255];
colors[4]=[255,144,144,255];
colors[5]=[166,170,251,255];
colors[6]=[246,251,164,255];
colors[7]=[170,255,174,255];
function colortest(v){
	outlet(0,'brgb',colors[v]);
}

function loadbang(){
    draw();
}

function dims(w,h,nstep){
    width = w;
    height = h;
    unit = width/nstep;
    draw();
}

var b_pvs = -1;
function mouse(x,y,b){
    if(b!=b_pvs && x<width){
        item=Math.floor(x/unit);
        b_pvs=b;
        if(b){
            //post("\nitem",item);
            ruling(item);
        }
    }
}

function list(){
    var a = arrayfromargs(arguments);
    //post("\nlist in",a);
    nstep = a.length;
    tog = a.slice(0);
    draw();
}

function ruling(v){
    tog[v] = (tog[v]+1) % modes.length;
    outlet(1,tog);
    draw();
}

function draw(){
    unit=width/tog.length; //same as nstep/width;
    outlet(0,'clear');
    for(var i=0;i<tog.length;i++){
        var tval = tog[i]; //toggle value
        var xo = i*unit; //x origin
        var xe = xo+unit; //x end
        var tspace = Math.floor(unit*spacing);
        var to = xo+tspace; //text origin
        //post("\n---------",i,width,unit,tval,xo,xe,to);
        
        //paint the rects for each button
        outlet(0,'paintrect',xo,0,xe,height,colors[tval]);
        outlet(0,'linesegment',xo,0,xo,height,black);
        
        //change properties for text
        if(tval>3){
            fontcolor=blue
        }else{
            fontcolor=red
        }
        outlet(0,'frgb',fontcolor);
        if(tval==0){
        	outlet(0,'frgb',black);
        }
        outlet(0,'font',font,fontsize);
        
        //make the message
        var msg=modes[tval].split(" ");
        var noshift = -3*( (parseInt(msg[1]))>9 )
        
        //draw the MODE (only or skip) portion
        //move the cursor
        outlet(0,'moveto',to,height-3);
        //write the text
        outlet(0,'write',msg[0]);
        
        //draw the NUMBER portion
        outlet(0,'frgb',fontcolor);
        outlet(0,'font',font,fontsize+4);
        outlet(0,'moveto',noshift+to+4,height-8);
        //write the text
        outlet(0,'write',msg[1]);

    }        
	//a black border
	outlet(0,'framerect',0,0,width,height,black);
}