import library.libfunctions
l = []
q = int(input("enter no of elements in the list: "))
while q>0:
    w = input("enter element: ")
    l.append(w)
    q = q-1
print(l)
e = input("enter A to add ,D to delete and N to not change anything from the list:  ")
if e == "A":
    x = input("enter element: ")
    library.libfunctions.Ladd(l,x)
    print(l)
elif e == "D":
    x = input("enter element :")
    library.libfunctions.Ldel(l,x)
    print(l)
elif e =="N":
    print("nothing has been added or delelted ")
    
r = input("enter S to sort the list or N to skip this step : ")
if r == "S":
    library.libfunctions.Lsort(l)
    print(l)
elif r =="N":
    print("you have opted to do nothing. ")
    
t = input("enter U to update list or N to not change anything:  ")
if t =="U":
    y = int(input("enter no. of elements: "))
    l2 = []
    while y>0:
        p = input("enter element: ")
        l2.append(p)
        y = y-1
    #print(l2)
    library.libfunctions.Lupdate(l,l2)
    print(l)
elif t =="N":
    print("Opted to do nothing. ")
    
