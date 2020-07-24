import re

sentence  = "she sells sea shells on the sea shore"
matchObj = re.match(r'.*shells.*',sentence,0)
print(type(matchObj))
print(matchObj.string)
