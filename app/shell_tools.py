from subprocess import call
def sh(arguments):
        return call(arguments)

def delete(filename):
	call(["bash", "del", filename])

def write(string, filename):
	call(["bash", "write", string, filename])

def read(filename):
	call(["cat", filename])

def recompile():
	print("recompiling...")

def delete_line(filename):
	delete(filename)
