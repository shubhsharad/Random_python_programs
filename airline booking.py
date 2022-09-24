"Flight booking"
def booking(x):
    
    #x = int(input("enter no of tickets:"))
    global t 
    t = t-x
    b = int(input("enter 1 for business class and 2 for economy class"))
    if b == 1:
        print("Business class booked")
    elif b == 2:
        print("Economy class booked")
    print("remaining tickets:",t)
    print("tickets booked:",x)
    
def cancel(c):
    #c = int(input("enter no of tickets to be cancelled:"))
    global t 
    t = t+c
    print("tickets remaining:",t)
    print("no of cancelled tickets:",c)
    
t = 50

"""a = int(input("Enter 1 for booking and 2 for cancellation:"))
          
if a ==1:
    while t > 0:
        booking()
    else:
        print("All tickets are booked.")
        
if a == 2:
    while t < 50:
        cancel()
    else:
        print("None of the tickets are booked")"""
        
f = open('C:/Users/user/Desktop/demofile.txt','r', encoding = "utf-8")
l = f.readlines()
for i in l:
    w1 = i.split()
    print(w1)
    if w1[0] == "booking":
        booking(int(w1[1]))
    else:


    
    
    
    
    
    
    