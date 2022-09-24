def Bsearch(AR,ITEM):
    beg = 0
    last = len(AR) - 1
    while beg<= last:
        mid = (beg+last)//2
        if ITEM == AR[mid]:
            return mid
        elif ITEM > AR[mid]:
            beg = mid+1
        else:
            last = mid-1
    else:
        return False
    
N = int(input("Enter desired linear list size : "))
print("\n Enter elements for Linear list \n")
AR = [0]*N
for i in range(N):
    AR[i] = int(input("Element"+str(i)+":"))
ITEM = int(input("\n Enter element to be searched for : "))
index  = Bsearch(AR,ITEM)

if index:
    print("element found at index:",index,",Position:",(index+1))
else:
    print("Sorry!! Given element could not be found.")