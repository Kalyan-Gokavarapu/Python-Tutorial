class myException(Exception):
    pass

try:
    input("Enter a value :: ")
    raise myException
except Exception as e:
    print(str(type(e)))
    print(e)
