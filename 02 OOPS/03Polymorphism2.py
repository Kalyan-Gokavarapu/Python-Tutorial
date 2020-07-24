class date:
    def __init__(self):
        self.dd=21
        self.mm=7
        self.yy=2020
    def display(self):
        print(self.dd,self.mm,self.yy)

today = date()
today.display()