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

ret = subprocess.run("dir", shell=True, capture_output=True)
print(ret.stdout)
print(ret.stdout.decode()) # To handle carriage return and newline

# we can also use Text =True, no need to use decode
ret = subprocess.run("dir", shell=True, capture_output=True, text=True)
print(ret.stdout)



#send the output to a pipe
#add symbolic constant PIPE
ret = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
print(ret.stdout)



#Send the output as input to the next command
#How to pass a command and its param
# Use a utility called more

ps1 =subprocess.run(["type","subps.py"], shell=True,capture_output=True, text=True)
# print(ps1.stdout)
ps2 = subprocess.run(["more"], shell=True,capture_output=True, text=True, input=ps1.stdout)
print(ps2.stdout)