import re

sentence  = "she sells sea shells on the sea shore"
matchObj = re.match(r'(.*) (.*)shells(.*) (.*)',sentence,0)
# It returns None if there is no match and none.group(1) would raise an exception
print(matchObj.group())
print("[",matchObj.group(1),"]")
print("[",matchObj.group(2),"]")
print("[",matchObj.group(3),"]")
print("[",matchObj.group(4),"]")
