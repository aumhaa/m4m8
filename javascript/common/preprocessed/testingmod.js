autowatch = 1;

var includes = new Global('includes');

function init()
{
	mod = new includes.mod('blah', 'notSoUnique', false);
	mod.init();
	post('mod id is:', mod.finder.id, '\n');
}


