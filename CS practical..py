import mysql.connector
mycon=mysql.connector.connect(host="localhost",user='root',passwd="shubh",database="zomato")
if mycon.is_connected():
    print("Done")
cursor = mycon.cursor()
i = 1
j = 1
n=input("Kindly enter your name: ")
pn=int(input("Kindly enter your Phone no: "))
#ar=input("Kindly enter the name of your area: ")
#st = "insert into booking(NAME,PH_NO) values ("{}",{})".format(n,pn)
x = int(input("enter 0 for booking and 1 for delivery :"))
if x ==0:
    print("you have opted for booking:")
    cursor.execute("select RID,RNAME from restaurants")
    data = cursor.fetchall()
    for row in data:
        print(row)
    r = input("enter Restaurant's unique ID: ")
    t = int(input("enter time of booking: "))
    s = int(input("enter No of seats required: "))
    b = "BID"+str(i)
    print(b)
    st = "INSERT INTO booking(BID,RID,SEATS_REQD,NAME,PH_NO,TIME) VALUES ('{}',{},'{}',{},{})".format(b,r,s,n,pn,t)
    cursor.execute(st)
    mycon.commit()
    i = i+1
    
elif x==1:
    ar=input("Kindly enter the name of your area: ")
    g=(ar,)
    print('YOU HAVE OPTED FOR DELIVERY')
    s="select RID,RNAME from restaurants where RAREA=%s"
    cursor.execute(s,g)
    data=cursor.fetchall()
    print(data)
    r1=input("select RID for reqd area")
    y="select RDELIVERY from restaurants where RID=%s"
    cursor.execute(y,r1)
    d=cursor.fetchall()
    if d=="NO":
        print("THIS RESTAURANT DOESN'T DELIVER FOOD PLS SELECT ANOTHER")
    else: 
        r1=input("select RID for reqd area")
    y="select RDELIVERY from restaurants where RID=%s"
    cursor.execute(y,r1)
    d=cursor.fetchall()