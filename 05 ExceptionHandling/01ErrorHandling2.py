ctrl =1
while ctrl != -1:
    try:
        ctrl = int(input("Enter a number (-1 to exit) :"))  
        ctrl1      
    except ValueError:
        print("That was not a number. Enter 0 to 9")
    except NameError:
        print("Guess you made a spelling mistake in the name",ctrl1)