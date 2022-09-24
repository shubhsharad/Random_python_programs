d = {}
i =1
n = int(input("enter number of employees:"))
while n>0:
    n = n-1
    x = input("enter Name:")
    y = int(input("enter age:"))
    z = int(input("enter salary:"))
    d[i] = {"Name":x,"Age":y,"Salary":z}
    i = i+1
print(d)
s = int(input("enter EMP ID:"))
print(d[s]["Name"])