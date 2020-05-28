autowatch=1;

outlets=2;

var prefix="256";
var slash=new RegExp(/^\//);
var space=new RegExp(/^\S/);

function set(str)
{
	prefix=str.replace(slash, "");
	post("prefix:", prefix, "\n");
}


function anything()
{
	var args=arrayfromargs(arguments);
	var str=messagename.split("/");
	for (i in str)
	{
		str[i].replace(space, "");
	}
	//for(i in str)
	//{
	//	post(str[i]);
	//}
	//post("\n");
	switch (str[2])
	{
		case "led":	
			outlet(0, args[0], args[1], args[2]);
			break;
		case "clear":
			for(var x=0;x<15;x++)
			{
				for(var y=0;y<15;y++)
				{
					outlet(0, x, y, 0);
				}
			}
		case "led_col":
			var dec1=deciToBin(args[1]);
			for(var i=0;i<dec1.length;i++)
			{
				outlet(0, parseInt(args[0]), i, parseInt(dec1.charAt(dec1.length-i-1)));
			}
			break;
		case "led_row":
			var dec1=deciToBin(args[1]);
			for(var i=0;i<dec1.length;i++)
			{
				outlet(0,  i, parseInt(args[0]), parseInt(dec1.charAt(dec1.length-i-1)));
			}
			break;
		case "prefix":
			outlet(1, "set", args);
			outlet(1, "bang");
			//outlet(0, "/sys/"+prefix);  //causes feedback loop
			break;
		case "cable":
			post(args, "\n");
			break;
	}
}

function deciToBin(arg)
{
	res1 = 999;
	args = arg;
	while(args>1)
	{
		arg1 = parseInt(args/2);
		arg2 = args%2;
		args = arg1;
		if(res1 == 999)
		{
			res1 = arg2.toString();
		}
		else
		{
			res1 = arg2.toString()+res1.toString();
		}
	}
	if(args == 1 && res1 != 999)
	{
		res1 = args.toString()+res1.toString();
	}
	else if(args == 0 && res1 == 999)
	{
		res1 = 0;
	}
	else if(res1 == 999)
	{
		res1 = 1;
	}
	var ll = res1.length;
	while(ll%16 != 0)
	{
		res1 = "0"+res1;
		ll = res1.length;
	}	
	return res1;
}



