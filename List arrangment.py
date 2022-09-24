l = []
y = int(input("enter no of elements:"))
while y > 0:    
    y = y-1
    x = int(input("enter list element: "))
    l.append(x)
print(l)
c = len(l) -1
b = l.pop(c)
l.insert(0,b)
print(l)