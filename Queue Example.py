def createQ():
    Q=[]
    return Q

def size(Q):
    return len(Q)


def isEmpty(Q):
    if len(Q) == 0:
        print(" empty Queue")
    else:
        print(" Queue is not empty ")
        
def Enqueue(Q,item):
    Q.append(item)
    
def Dequeue(Q):
    return Q.pop(0)


createQ()
Q = createQ()
print(Q)

for i in range(0,5):
    Enqueue(Q, i)
    
print(Q)

Dequeue()
print()