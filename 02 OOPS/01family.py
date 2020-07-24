class Mom:
    def walk(self):
        print("Walk Elegantly, address of self is", id(self))

Mother = Mom()
Mother.walk()
print ("The address of the Mother is",id(Mother))
class infant:
    pass

baby = infant()
help(baby)