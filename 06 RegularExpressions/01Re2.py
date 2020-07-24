import re

sentence  = "she sells sea shells on the sea shore"
matchObj = re.match(r'(.*)shells(.*)',sentence,0)
print(type(matchObj))
print(matchObj.string)
print(matchObj.group())
print("[",matchObj.group(1),"]")
print("[",matchObj.group(2),"]")
