import sys

fileObj = open(sys.argv[1])
currLocation = 0   

while fileObj.readline():
    
    fileObj.seek(currLocation)
    print(fileObj.readline())
    fileObj.seek(currLocation)
    print(fileObj.readline())
    currLocation = fileObj.tell()  



