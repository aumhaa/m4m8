var maxi = 16;
var theobj = "";
function anything(){
    theobj = messagename;
    for(var i=0;i<maxi;i++){
        var num=i;
        var inc=theobj+"["+num+"]";
        outlet(0,"script","delete", "pattr "+inc);
        outlet(0,"script","newobject", "newobj", "@text", "pattr "+inc, "@patching_position", 5+(i*20), 0);
       // outlet(0,"script","connect","unpack_"+theobj,i, inc,0);
    }
}

function tbut(){
    theobj = arguments[0];
    for(var i=0;i<maxi;i++){
        var num=i+1;
        var inc=theobj+"["+num+"]";
        outlet(0,"script","newobject", "textbutton", "@varname", inc, "@patching_rect", 5+(i*20), 5+(i*20),25,20,"@texton", num,"@text", num);
    }
}

//script sequences 4-16
function bpat(){
    theobj = arguments[0];
    for(var i=4;i<maxi;i++){
        var inc=theobj+"["+i+"]";
        outlet(0,"script","newobject", "bpatcher", "@varname", inc, "@patching_rect", (i*20), 600,535,175,"@args", arguments[1],arguments[2], "@name",theobj+".maxpat","@offset",0,0);
    }
}

function connect(v){
    if(v) theobj=v;
    for(var i=0;i<maxi;i++){
        var num=i+1;
       var inc=theobj+"["+num+"]";
       outlet(0,"script","connect","unpack_"+theobj,i, inc,0);
       outlet(0,"script","connect",inc,0,"pack_"+theobj,i );
    }
}

function cnc(v){
    tocon=v;
    for(var i=0;i<maxi;i++){
       var num=i;
       var inc=tocon+"["+num+"]";
       outlet(0,"script","connect",inc,0,"pack_"+tocon,i );
    }
}

function livebtn(v){
    theobj = arguments[0];
    for(var i=0;i<maxi;i++){
        var num=i+1;
        var inc=theobj+"["+num+"]";
        outlet(0,"script","delete", "pattr "+inc);
        outlet(0,"script","newobject", "newobj", "@text","live.text","@varname", inc, "@patching_position", 10+(i*30), 200,"@patching_size",30,15);
       outlet(0,"script","send",inc,"text",num);
       outlet(0,"script","send",inc,"texton",num);
    }
}

function con(a,b){
    for(var i=0;i<maxi;i++){
        var num=i+1;
        outlet(0,"script","connect",a+"["+num+"]",0,b+"["+num+"]",0);
        outlet(0,"script","connect",b+"["+num+"]",0,a+"["+num+"]",0);
    }
}