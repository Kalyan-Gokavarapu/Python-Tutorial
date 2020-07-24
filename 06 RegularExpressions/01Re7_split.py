import re


OldString = "This is    a:sample;string"
words =re.split('[ :;\t]',OldString)

print(OldString)
print(words)

