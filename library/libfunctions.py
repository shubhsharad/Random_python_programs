def Ladd(lst,x):
    lst.append(x)
    return lst

def Ldel (lst,x):
    lst.remove(x)
    return lst

def Lsort(lst):
     y = int(input("enter 0 if list should be in ascending order and 1 if in descending order :"))
     if  y == 0:
         return lst.sort()
     else:
         return lst.sort(reverse = True)
     
def Lupdate(lst,i):
    lst.extend(i)
    return lst

 
    
    

    