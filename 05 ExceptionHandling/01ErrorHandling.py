ctrl =1
while ctrl != -1:
    try:
        ctrl = int(input("Enter a number (-1 to exit) :"))
    except ValueError:
        print("That was not a number. Enter 0 to 9")