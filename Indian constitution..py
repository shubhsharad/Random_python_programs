f = open("C:/Users/user/Desktop/cons.txt","r")
a = f.readlines()
x = len(a)
print(f.read())
for i in range(x-4,x) :
    print(a[i])
f.close()
#last three lines
