import re


OldString = "7760053653 # Kalyan's Phone Number"
words =re.split(' ',OldString)
chars =re.split('',OldString)
print(OldString)
print(type(words))
print(words)
print(chars)
