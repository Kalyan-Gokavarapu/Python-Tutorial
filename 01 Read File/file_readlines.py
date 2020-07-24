import sys

filename = sys.argv[1]
fileObj = open(filename)
lines = fileObj.readlines()
fileObj.close()
ctr =0
for line in lines:
    print(ctr+1, line) 
    
