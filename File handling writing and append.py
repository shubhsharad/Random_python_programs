s = open("C:\\Users\\user\\Desktop\\writing.txt","w")
for i in range(0,5):
    x= input("enter name: ")
    s.write(x)
    s.write("\n")
s.close()

a = open("C:\\Users\\user\\Desktop\\writing.txt","a")
b = a.write("this is an appended line")
a.close()


# USING WRITELINES

s = open("C:\\Users\\user\\Desktop\\writing.txt","w")
l = []
for i in range(5):
    x =input("enter name: ")
    l.append(x + "\n")
s.writelines(l)
s.close()