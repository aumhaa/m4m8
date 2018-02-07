autowatch = 1;

"include mod.js;"

var mod;

function init()
{
	mod = new ModComponent('blah', 'notSoUnique', false);
	mod.init();
	post('mod id is:', mod.finder.id, '\n');
}
