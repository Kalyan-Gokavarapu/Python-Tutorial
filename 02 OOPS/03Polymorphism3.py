class date:
    def __init__(self):
        self.dd=21
        self.mm=7
        self.yy=2020
    def display(self):
        print(self.dd,self.mm,self.yy)
    def __add__(self,value):
        return self


today = date()
today.display()
tomorrow = today+1
tomorrow.display()