# import sys
class date:
    def __init__(self):
        self.dd=21
        self.mm=7
        self.yy=2020
        # self.dd=30
        # self.mm=12
        # self.yy=2020
    def display(self):
        print(self.dd,self.mm,self.yy)
        
    def __add__(self,days):
        while days > 0:
                if (self.dd + 1 <= self.daysPerMonth(self.mm,self.yy)):                    
                    self.addDay()                   
                else:
                    if(self.mm == 12):
                        self.addYear()             
                    else:
                        self.addMonth()                
                days-=1                
        return self
    
    def addMonth(self):
        self.mm+=1
        self.dd=1
    
    def addYear(self):
        self.yy+=1
        self.mm=1
        self.dd=1 
    
    def addDay(self):
        self.dd+=1
                    

    def daysPerMonth(self, month, year):
        if(month == 2):            
            if (self.isLeapYear(year)):                
                return 29
            else:                
                return 28            
        if (month in (4,6,9,11)):
            return 30
        else:
            return 31

    def isLeapYear(self,year):
        # if (year%4 ==0):
        if ((year % 4 ==0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)):
            return True
        else:
            return False 
    

  


today = date()
today.display()
# tomorrow = today+22
# tomorrow = today+int(sys.argv[1])

print("Enter days to add :")
days = input()
# print ("Start Time:" + )
tomorrow = today + int(days)
tomorrow.display()
input()


# mydate =date()
# year = sys.argv[1]
# if year:    
#     i=1
#     while i<=12:
#         print(mydate.daysPerMonth(i,int(year)))
#         i+=1

