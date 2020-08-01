import sys
import re

fileName =""

# Todo Validation
if len(sys.argv) > 1:
    fileName =sys.argv[1]
else:    
    fileName = input("Enter a file name: ")

with open(fileName,'r') as fileObj:
    line = fileObj.readline()
    while line:
        # print(line)
        matchObj = re.match(r'#.*', line,0)
        if not matchObj:
            print(line) 
        line = fileObj.readline()   
    
