import re


OldString = "7760053653 # Kalyan's Phone Number"
newstring =re.sub(r' #.*$',"",OldString)
print(OldString)
print(newstring)
