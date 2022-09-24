def sequence(x,y):
    a = (y-x)/3
    l = [x,x+a,x+2*a,y]
    print(l)
x = int(input("enter 1st number: "))
y = int(input("enter 2nd number: "))
sequence(x,y)
