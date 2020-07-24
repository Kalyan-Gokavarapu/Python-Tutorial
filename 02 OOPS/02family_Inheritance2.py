class Mom:
    def __del__(self):
        print("Object Destroyed")
    def walk(self):
        # print("Walk Elegantly, address of self is", id(self))
        print("Walk - Mom")
    def __init__(self):
        print("Object Constructed successfully")

# Mother = Mom()
# Mother.walk()
# print ("The address of the Mother is",id(Mother))

class infant(Mom):
    def walk1(self):
        print("Walk - Infant")

baby = infant()
baby.walk()
# help(baby)