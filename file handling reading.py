m = open("C:\\Users\\user\\Desktop\\practice.txt","r")
s = m.read()
print(s)

x = m.readline()
print(x)

y = m.readlines()
print(y)

m.close()