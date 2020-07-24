class Dad:
    def walk(self):
        print("Walk - Dad")

class Mom:
    def walk(self):
        print("Walk - Mom")

class infant(Mom,Dad):
    def walk_nothin(self):
        print("Walk - Infant")

baby = infant()
baby.walk()
