import subprocess

# subprocess.run("dir")
# The above will give an error

subprocess.run("attrib")
# The above will work

subprocess.run("dir",shell=True)
ret= subprocess.run("dir",shell=True)
print(ret)
print(ret.args)
print(ret.returncode)
subprocess.run("dir", shell=True)