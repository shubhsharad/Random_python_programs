#Military time
t1 = input("enter time: ")
t2 = input("enter time: ")
print(int(t2[:2])-int(t1[:2]),"hours",int(t2[2:])-int(t1[2:]),"mins")