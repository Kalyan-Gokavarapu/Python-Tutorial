import sys

fileName =""

# Todo Validation
if len(sys.argv) > 1:
    fileName =sys.argv[1]
else:    
    fileName = input("Enter a file name: ")

lineno = 0
with open(fileName,'r') as fileObj:
    line = fileObj.readline()
    while line:
        lineno+= 1
        print(str(lineno) + ":" + line)    
        line = fileObj.readline()   