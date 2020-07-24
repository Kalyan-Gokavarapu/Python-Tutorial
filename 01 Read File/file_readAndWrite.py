import sys

fileName1= sys.argv[1]
fileName2= sys.argv[2]
fileObj = open(fileName1)
fileObj2 = open(fileName2,"w")
#fileContent = fileObj.read()
#fileObj2.write(fileContent)
fileObj2.writelines(fileObj.readlines())
fileObj.close()
fileObj2.close()



