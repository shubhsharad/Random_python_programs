def student(x):
    s= open("C:\\Users\\user\\Desktop\\students.txt","w")
    x = int(input("enter number of students : "))
    for i in range(0,x):
        name = input("enter name :")
        rno = int(input("enter roll no: "))
        marks = int(input("enter marks: "))
        final = name +" roll no is: "+str(rno) +"  marks are : "+str(marks)
        s.write(final)
        s.write("\n")
    s.close()
        
def read():
    s = open("C:\\Users\\user\\Desktop\\students.txt","r")
    a = s.read()
    print(a)
    s.close()
    
student(2)
read()