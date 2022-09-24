import pickle
s = open("C:\\Users\\user\\Desktop\\binary","wb+")
stu = {}
x = int(input("enter no of students: "))
for i in range(0,x):
    rno = int(input("enter roll  no of student: "))
    name = input("enter name :")
    marks = int(input("enter marks: "))
    stu["Rno."] = rno
    stu["Name"] = name
    stu["Marks"] = marks
    pickle.dump(stu,s)
s.close()
    
a = {}
s= open("C:\\Users\\user\\Desktop\\binary","rb")
try:
    while True:
        a = pickle.load(s)
        print(a)
except EOFError:
    s.close()