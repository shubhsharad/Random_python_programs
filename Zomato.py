import mysql.connector
import random
mycon=mysql.connector.connect(host="localhost",user='root',passwd="shubh",database="zomato")
if mycon.is_connected():
    print('SUCCESS')
cursor = mycon.cursor()

j=1
n=input("Kindly enter your name: ")
#HERE WE ASK USER HIS/HER NAME
pn=int(input("Kindly enter your Phone no: "))
#USER_PHONE_NUMBER
c=input('KINDLY CHOOSE CUSINE FROM INDIAN/ITALIAN/CONTINENTAL: ')
#Preffered cuisine out of three options
x = int(input("enter 0 for booking and 1 for delivery :"))
#choice of delivery or booking
if x ==0:
    i=1
    #IF BOOKING IS CHOSEN
    print("you have opted for booking","the",c,"restaurants are: ")
    k= "select RID,RNAME,RRATING from restaurants where RCUISINE=%s"
    g=(c,)
    cursor.execute(k,g)
    data=cursor.fetchall()
    for row in data:
        print(row)
    r = input("enter Restaurant's unique ID: ")
    t = int(input("enter time of booking: "))
    s = int(input("enter No of seats required: "))
    b= "B"+str(random.randint(100,999))
    st = "INSERT INTO booking(BID,RID,SEATS_REQD,NAME,PH_NO,TIME) VALUES ('{}','{}',{},'{}',{},{})".format(b,r,s,n,pn,t)
    cursor.execute(st)
    # invoice(n,pn,b,r,s,t)
    mycon.commit()
    

   

if x==1:
    ar=input("Kindly enter the name of your area: ")
    g=(ar,c)
    print('YOU HAVE OPTED FOR DELIVERY',"THE",c,"RESTAURANTS IN",ar, "ARE: ")
    s="select RID,RNAME,RRATING from restaurants where RAREA=%s and RCUISINE=%s "
    cursor.execute(s,g)
    data1=cursor.fetchall()
    for row in data1:
        print(row)
    r1=input("select RID for reqd area: ")
    h=(r1,)
    y="select RDELIVERY from restaurants where RID=%s"
    cursor.execute(y,h)
    d=cursor.fetchall()
    if d[0]==('NO',):
        print("THIS RESTAURANT DOESN'T DELIVER FOOD PLS SELECT ANOTHER RESTAURANT")
        r1=input("select RID from the above list: ")
        h=(r1,)
        y="select RDELIVERY from restaurants where RID=%s"
        cursor.execute(y,h)
        d=cursor.fetchall()