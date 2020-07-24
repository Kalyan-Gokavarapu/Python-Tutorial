# Python uses Depth first search 
class MGF:
    def walk(self):
        print("Walk - MGF")
class MGM:
    def walk1(self):
        print("Walk - MGM")

class PGF:
    def walk(self):
        print("Walk - PGF")
class PGM:
    def walk(self):
        print("Walk - PGM")

class Dad(PGM,PGF):
    def walk(self):
        print("Walk - Dad")

class Mom(MGM,MGF):
    def walk1(self):
        print("Walk - Mom")

class infant(Mom,Dad):
    def walk1(self):
        print("Walk - Infant")

baby = infant()
baby.walk()
