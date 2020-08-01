import sys

filename = sys.argv[1]
fileObj = open(filename)
line = fileObj.readline()
ctr = 1
while line:
    print (ctr,line)
    ctr+= 1
    line= fileObj.readline()

fileObj.close()