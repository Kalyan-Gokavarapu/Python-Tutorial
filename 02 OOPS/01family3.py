class Mom:
    def __del__(self):
        print("Object Destroyed")
    def walk(self):
        print("Walk Elegantly, address of self is", id(self))
    def __init__(self):
        print("Object Constructed successfully")

Mother = Mom()
Mother.walk()
print ("The address of the Mother is",id(Mother))
class infant:
    pass

baby = infant()
help(baby)