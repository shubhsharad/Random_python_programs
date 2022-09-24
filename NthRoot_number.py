def NthRoot(x, n = 2):
    return x**(1/n)
x = int(input("enter number: "))
n = int(input("enter Number: "))
A = NthRoot(x,n = 2)
print("answer is: ", A)