l = []
x = int(input("enter how many numbers u have"))
while x >0:
    s = int(input("enter numbers:"))
    l.append(s)
    x = x-1
print(l)
t = tuple(l)
print(t)
for a in t:
    print(a)