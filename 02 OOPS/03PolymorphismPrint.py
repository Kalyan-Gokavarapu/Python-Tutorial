import sys
class date:
    def __init__(self):
        self.dd=21
        self.mm=7
        self.yy=2020
    def display(self):
        print(self.dd,self.mm,self.yy)
    def __str__(self):
        return(str(self.dd)+ "/" + str(self.mm) +"/" + str(self.yy))
today= date()
print(today)

