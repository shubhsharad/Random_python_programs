def createQ():
    Q=[]
    return Q

def size(Q):
    return len(Q)

def Enqueue(Q,item):
    Q.append(item)
    
    
def Dequeue(Q):
    Q.pop(0)
    
x = createQ()
    
for i in range(0,3):
    a = input("enter name: ")
    Enqueue(x,a)
    
print(x)

print("One customer was served")

Dequeue(x)
print(x)
print("Size of Queue is: ",size(x))