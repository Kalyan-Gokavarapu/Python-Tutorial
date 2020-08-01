import sys

fileName= sys.argv[1]
fileObj = open(fileName)
fileContent = fileObj.read()
print(fileContent)
fileObj.close()