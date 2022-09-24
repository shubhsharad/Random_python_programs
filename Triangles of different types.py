#Matrix or Square
for r in range(1,4):
    for c in range(1,4):
        print("*",end = " ")
    print()
#Lower Left Triangle   
for r1 in range(1,5):
    for c1 in range(1,r1+1):
        print("*",end = " ")
    print()
#Upper Left Triangle    
for r2 in range(4,1,-1):
    for c2 in range(1,r2):
        print("*",end = " ")
    print()
#Upper Right Triangle    
for r3 in range(1,5):
    for s in range(1,5-r3):
        print(" ",end = " ")
    for c3 in range(1,r3+1):
        print("*",end = " ")
    print()
    
