import json
import re

scores ={"Sachin":100,"Sehwag":82}

fileObj=open("scores.txt",'w')
fileObj.write(str(scores))
fileObj.close()

fileObj1=open("scores.txt",'r')
line =fileObj1.readline()
fileObj1.close()

print(line)
line =re.sub(r"\'","\"",line)
print(line)
scoreJson = json.loads(line)
print(type(scoreJson))
print(scoreJson)
print (scoreJson['Sachin'])
print (scoreJson['Sehwag'])