autoselect = 1;

inlets =2;
outlets =2;

var hold = 0;
var row = [];

for(var i=0;i<16;i++)
{
    row[i] = -1;
}

function list(x, y, z)
{
    if(z>0)
    {
        row[y] = x;
        outlet(1, y, 1);
        outlet(0, y, x);
    }
    else
    {
        if((x == row[y])&&(hold==0))
        {
            outlet(1, y, 0);
            outlet(0, y, x);
        }
    }
}

function msg_int(val)
{
    //post('hold', val, '\n');
    if(inlet == 1)
    {
        hold = val;
    }
}

function anything()
{
    return;
}