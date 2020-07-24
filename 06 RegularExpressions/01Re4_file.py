import re

fileObj = open ("Book1.csv")
line = fileObj.readline()
while line:
    # print(line)
    matchObj = re.match(r'([0-9]{1,2}),([A-Za-z]{3}),(.*)', line,0)
    if matchObj:
        print(matchObj.group(3),matchObj.group(2),matchObj.group(1))
    line= fileObj.readline()

fileObj.close()
print('done file 1')

fileObj = open ("Book2.csv")
line = fileObj.readline()
while line:
    # print(line)
    matchObj = re.match(r'([0-9]{1,2})\t([A-Za-z]{3})\t(.*)', line,0)
    if matchObj:
        print(matchObj.group(3),matchObj.group(2),matchObj.group(1))
    line= fileObj.readline()

fileObj.close()
print('done file 2')

