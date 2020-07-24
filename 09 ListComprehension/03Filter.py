calender=['Jan','Feb','Mar','Apr','May', 'Jun']

def Month31Days(cal):
    Month31List= ['Jan','Mar','May','Jul','Aug','Oct','Dec']
    if cal in Month31List:
        return True
    return False

Mon30Days = filter(Month31Days, calender)
print(list(Mon30Days))