Q = []

def Qprint(Q):
    print("people in Queue are : ",Q)
def Qsize(Q):
     print("Queue size is : ",len(Q))

def add_patient(Q,i):
    Q.append(i)
    return Q

def del_patient(Q):
    Q.pop(0)
    return Q

w = int(input("enter current number of people in the queue for the doctor: "))
while w > 0:
    e = input("enter name of patient currently in Queue: ")
    Q.append(e)
    w = w-1
print("current Queue is : ",Q)

r = int(input("enter 1 if a patient has had their check up with the doctor or 2 to check size of Queue and 3 to add patient to the Queue : "))

if r == 1:
    del_patient(Q)
    print("patient has had succesful checkup")
    print("remaining Queue:  ",Q)

elif r == 2:
    Qprint(Q)
    Qsize(Q)

elif r == 3:
    i = input("enter name of patient: ")
    add_patient(Q,i)
    print(Q,"Patient has been added to Queue")
    
    
      
