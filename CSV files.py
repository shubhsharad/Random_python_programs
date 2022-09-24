import csv
c = open("C:\\Users\\user\\Desktop\\trial.csv","w")
writer = csv.writer(c)
x = int(input("enter No of students : "))
for i in range(0,x):
    name = input("enter name :")
    sname = input("enter sname : ")
    marks = int(input("enter marks: "))
    l  = [name,sname,marks]
    writer.writerow(l)

c.close()


c = open("C:\\Users\\user\\Desktop\\trial.csv","r",newline = "\r\n")
reader = csv.reader(c)
for i in reader:
    print(i)
    
c.close()