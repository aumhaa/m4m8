/*
used to gather all named objects and collect their rectangles. Makes it easy to restore an arrangement of objects.
the onlyselected variant will only gather the coordinates of selected objects. very useful for patches that have multiple possible interfaces.
*/

autowatch = 1;
var count = 0;
function anything(){
    var a = arrayfromargs(messagename,arguments);
    var v = a[0];
    var ob = this.patcher.getnamed(v);
    outlet(0,count,v,ob.rect[0],ob.rect[1],ob.rect[2]-ob.rect[0],ob.rect[3]-ob.rect[1]);
    count++;
}

function clear(){
    count = 0;
}
function bang(){
    counter = 0;
    this.patcher.apply(iterfun);
}
function onlyselected(){
    post("\nonlyselected");
    counter = 0;
    this.patcher.apply(itersel);
}

function iterfun(b)
{
    if(b.varname){
    post("\nname",b.varname);
    outlet(0,b.varname,b.rect[0],b.rect[1],b.rect[2]-b.rect[0],b.rect[3]-b.rect[1]);
    }
    return true;    
}
iterfun.local=1; // keep private

function itersel(b)
{
    post("\nsel",b.varname,b.selected);
    if(b.varname && b.selected){
        outlet(0,counter,'script','send',b.varname,'presentation_rect',b.rect[0],b.rect[1],b.rect[2]-b.rect[0],b.rect[3]-b.rect[1]);
        counter++;
    }
    return true;    
}
