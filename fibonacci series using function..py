x = int(input("enter number:"))
def fibonacci(x):
    a = 0
    b = 1
    print(a,b,end = " ")
    while x>=3:
        c = b+a
        a = b
        b = c
        x = x-1
        print(c,end = " ")
fibonacci(x)
    