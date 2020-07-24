
range1 =[x for x in range (1,51)]

def even(x):
    if x%2==0:
        return 1
    else:
        return 0

List1= list(range1)
print (List1)

mapObj = map(even,List1)
print(mapObj)
print(list(mapObj))



