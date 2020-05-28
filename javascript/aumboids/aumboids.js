autowatch = 1;

outlets = 6;

var script = this;

aumhaa = require('_base');
var FORCELOAD = false;
var DEBUG = false;
aumhaa.init(this);


var timer = 0;
var modes = [];
for(var i=0;i<8;i++)
{
	modes[i] = [0, 0, 0, 0];
}

var leader;
var notes = [0, 5, 7, 10, 12, 17, 19, 24];
var durations = [8000, 4000, 2000, 1000];
var dist_array = [];
var boids = [];
var weights = [1., 1., 1., 1., 1., 1., 1., 1.];
var sixteenth = 1/16;
var centroid_x = 0.;
var centroid_y = 0.;
var avgvelocity_x = 0.;
var avgvelocity_y = 0.;
var myprime = 0;
var primes = [];
var mywind_x = 0.;
var mywind_y = 0.;
var myseparation = .1;
var myalignment = .07;
var mycoherence = .1;
var myobedience = .5;
var myinertia = .5;
var myfriction = .5;
var mysepthresh = .3;
var mymaxvel = .1;
var mygravity = .1;
var mygravpoint_x = .5;
var mygravpoint_y = 0.;
var myslip = 0.;
var mywind = 0.;
var myagentcount = 0;

function init()
{
	post('aumboids init post');
	debug('aumboids init');
	agentcount(8);
}

function Boid(num)
{
	var self = this;
	this.num = num;
	this.x = Math.random();
	this.y = Math.random();
	this.vx = (Math.random()-.5)*.1;
	this.vy = (Math.random()-.5)*.1;
	this.px = 0;
	this.py = 0;
	this.prime = num;
	this.order = num;
	this.speed = 1.;
	this.tonality = 1.;
	this.seperation = .5;
	this.alignment = .5;
	this.coherence = .5;
	this.inertia = .5;
	this.friction = .5;
	this.velocity = .5;
	this.size = 1.;
	this.attraction = 1.;
	this.gravity = 1.;
	this.weight = 1.;
	this.dist = 0;
	this._next_x = 0;
	this._next_y = 0;
}

function agentcount(v)
{
	//gb.myagentcount = clip(v,1,8);
	debug('agentcount', v);
	myagentcount = v;
	dist_array = [];
	boids = [];
	for(var i=0;i<v;i++)
	{
		dist_array.unshift(0);
		boids.unshift(new Boid(i));
	}
	leader = boids[0];
	debug('new count is:', v, 'leader is:', leader);
}

function tick(agent)
{
	var px = agent.px;
	var py = agent.py;

	separate(agent);
	align(agent);
	cohere(agent);
	gravitate(agent);
	follow(agent);

	//inertia
	agent.vx = px*myinertia + agent.vx*(1.-myinertia);
	agent.vy = py*myinertia + agent.vy*(1.-myinertia);

	//velocity limit
	agent.vx = clip(agent.vx, -mymaxvel, mymaxvel);
	agent.vy = clip(agent.vy, -mymaxvel, mymaxvel);

	//update position based on velocity and friction
	agent.x += agent.vx*(1.-myfriction);
	agent.y += agent.vy*(1.-myfriction);

	//slip(this);
	wrap(agent); //torus space
	//bounce(this);
}

function leader_in(v)
{
	debug('leader in', boids.length, v)
	bl = boids.length;
	if(bl&&(bl >= v))
	{
		leader = boids[v];
		debug('leader is:', leader);
	}
}

function prime(v)
{
	myprime = v;
}

function wind(v)
{
	mywind = v;
}

function separation(v)
{
	myseparation = clip(v, 0, 1)*.1;
}

function alignment(v)
{
	myalignment = clip(v, 0, 1)*.1;
}

function coherence(v)
{
	mycoherence = clip(v, 0, 1)*.1;
}

function friction(v)
{
	myfriction = clip(v, 0, 1)*.1;
}

function inertia(v)
{
	myinertia = clip(v, 0, 1)*.1;
}

function septhresh(v)
{
	mysepthresh = clip(v, 0, 1)*.1;
}

function maxvel(v)
{
	mymaxvel = clip(v, 0, 1)*.1;
}

function gravity(v)
{
	mygravity = clip(v, 0, 1)*.1;
}

function gravpoint(x, y)
{
	grav_x = mygravpoint_x*15;
	grav_y = mygravpoint_y*15;
	outlet(3,  grav_x, grav_y, 0);
	mygravpoint_x = clip(x, 0., 1.);
	mygravpoint_y = clip(y, 0., 1.);
	grav_x = mygravpoint_x*15;
	grav_y = mygravpoint_y*15;
	outlet(3,  grav_x, grav_y, 20);
}

function bang()
{
	debug('bang');
	//timer += 1
	//mywind_x = ((Math.random()-.5)*.05)*mywind_x
	//mywind_y = ((Math.random()-.5)*.05)*mywind_y
	//circle()
	//for agent in boids:
	//   maxObject.outlet(3, round(agent.x*15), round(agent.y*15), 0)
	outlet(3, 'clear');
	outlet(3, mygravpoint_x*15, mygravpoint_y*15, 20);
	//introspect(gb.leader)
	lead();

	var cx = 0;
	var cy = 0;
	var cvx = 0;
	var cvy = 0;

	for(var index in boids)
	{
		var agent = boids[index];
		tick(agent);
		//calculate current frames average position/velocity
		cx += agent.x;
		cy += agent.y;
		cvx += agent.vx;
		cvy += agent.vy;
	}
	centroid_x = cx/myagentcount;
	centroid_y = cy/myagentcount;
	avgvelocity_x = cvx/myagentcount;
	avgvelocity_y = cvy/myagentcount;
	//outlet(2, 'bang')
	//outlet(1, (centroid_x, centroid_y, avgvelocity_x, avgvelocity_y))

	for(var index in boids)
	{
		var agent = boids[index];
		var order = agent.order;
		var number = agent.num;
		outlet(3, Math.round(agent.x*15), Math.round(agent.y*15), (number==leader.num ? 1 : 0)+(order<4 ? 1 : 0)+1);
		if(order< 4)
		{
			outlet(4, number, notes[leader.num] + modes[number][order], 120 - (order*30), durations[order], agent.weight);
		}
		else
		{
			outlet(4, number, 'off');
		}
		outlet(5, number, agent.dist);
		//outlet(0, agent.x, agent.y, agent.vx, agent.vy);
	}
}

function circle()
{
	phase = int(floor((timer%64.)/16.))
	switch(phase)
	{
		case 0:
			mygravpoint_x += sixteenth;
			break;
		case 1:
			mygravpoint_y += sixteenth;
			break;
	 	case 2:
			mygravpoint_x -= sixteenth;
			break;
		case 3:
			mygravpoint_y -= sixteenth;
			break;
	}
}

function separate(agent)
{
	for(var index in boids)
	{
		var boid = boids[index];
		if(boid!=agent)
		{
			var boid = boids[index]
			var dx = boid.x - agent.x
			var dy = boid.y - agent.y

			//torus space
			dx>.5 ? dx -= 1 : dx += 1;

			//torus space
			dy>.5 ? dy -= 1 : dy += 1;

			if(Math.abs(dx)>.0001 && Math.abs(dy)>.0001)
			{
				mag = (dx*dx+dy*dy); //cheap mag, no sqrt
			}
			else
			{
				mag = .01;
			}

			if(mag<mysepthresh)
			{
				mag<.0001 ? proxscale = 8 :proxscale = clip(mysepthresh/(mysepthresh-(mysepthresh-mag)), 0, 8);
				agent.vx -= dx*myseparation*proxscale;
				agent.vy -= dy*myseparation*proxscale;
			}
		}
	}
}

function align(agent)
{
	var dvx = avgvelocity_x - agent.vx;
	var dvy = avgvelocity_y - agent.vy;
	agent.vx += dvx*myalignment;
	agent.vy += dvy*myalignment;
}

function cohere(agent)
{
	var dx = centroid_x - agent.x;
	var dy = centroid_y - agent.y;
	agent.vx +=dx*mycoherence;
	agent.vy +=dy*mycoherence;
}

function gravitate(agent)
{
	if(agent == leader)
	{
		var dx = mygravpoint_x - agent.x;
		var dy = mygravpoint_y - agent.y;
		agent.vx += dx*mygravity;  // + mywind_x
		agent.vy += dy*mygravity; // + mywind_y
	}
	/*else:
		a.vx += dx*mygravity
		a.vy += dy*mygravity*/
}

function slip(agent)
{
	agent.y += myslip;
}

function lead()
{
	if(leader)
	{
		//introspect(gb.leader)
		dist_array = [];
		dist_sort = [];
		lead_x_off = leader.x;
		lead_y_off = leader.y;
		for(var index in boids)
		{
			agent = boids[index];
			agent.dist = Math.sqrt(Math.pow(Math.abs(lead_x_off - agent.x), 2) + Math.pow(Math.abs(lead_y_off - agent.y), 2));
			dist_array.push(agent.dist)
		}

		dist_sort = dist_array.slice(0);
		//debug('dist_sort', dist_sort);
		dist_sort.sort(function(a, b){return a-b});
		//debug('---sorted:', dist_sort);
		for(var index in boids)
		{
			agent = boids[index];
			agent.order = dist_sort.indexOf(agent.dist);
			//debug('order:', index, agent.order);
		}
	}
}

function calculate_leader()
{
	var min = 100;
	var lead = 0;
	for(var index in boids)
	{
		var agent = boids[index];
		if(agent.dist < min)
		{
			min = agent.dist;
			lead = agent.num;
		}
	}
	return lead;
}

function follow(agent)
{
	//move towards center
	var dx = mygravpoint_x - leader.x;
	var dy = mygravpoint_y - leader.y;
	if(agent.num != leader.num)
	{
		agent.vx += dx*myobedience;
		agent.vy += dy*myobedience;
	}
}

function wrap(agent)
{
	agent.x<0 ? agent.x = agent.x + 1 : agent.x > 1 ? agent.x = agent.x -1. : {};
	agent.y<0 ? agent.y = agent.y + 1 : agent.y > 1 ? agent.y = agent.y -1. : {};
}

function bounce(agent)
{
	if(agent.x>0||agent.x>1)
	{
		agent.vx = -agent.vx;
		agent.x = clip(agent.x, 0., 1.);
	}
	if(agent.y>0||agent.y>1)
	{
		agent.vy = -agent.vy;
		agent.y = clip(agent.y, 0., 1.);
	}
}

function clip(x, low, hi)
{
	return Math.min(Math.max(x, low), hi);
}

function assign_mode(x, y, val)
{
	modes[x][y]=val;
}

function assign_note(num, val)
{
	notes[num]=val;
}

function assign_duration(num, val)
{
	durations[num] = val;
}

function assign_weight(num, val)
{
	bl = boids.length;
	if(bl&&(bl >= num))
	{
		boids[num].weight = val;
	}
}

function anything()
{
	debug(arrayfromargs(messagename, arguments));
}

forceload(this);
