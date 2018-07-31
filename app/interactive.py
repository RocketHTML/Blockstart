from shell_tools import *
from issue_certs import *
from build_certs import *
cat = lambda filename: sh(["cat", filename])
ls = lambda: sh(["ls"])
def reload():
	sh(["python", "-i", "interactive.py"])
	exit(0)
def edit(filename):
	delete("interactive.py")
	delete("interactive.py")
	delete("interactive.py")
	delete("interactive.py")

	write('target = "{}"\n'.format(filename), "interactive.py")
	write('r = lambda: read(target)\n', "interactive.py")
	write('w = lambda x: write(x, target)\n', "interactive.py")
	write('d = lambda: delete(target)\n', "interactive.py")
	reload()
target = "test.py"
r = lambda: read(target)
w = lambda x: write(x, target)
d = lambda: delete(target)
