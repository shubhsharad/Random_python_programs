import lengthconversion

x = int(input("enter in miles: "))
A = lengthconversion.miletokm(x)
print(A)

y = int(input("enter in km: "))
B = lengthconversion.kmtomile(y)
print(B)

w = int(input("enter in feet: "))
C = lengthconversion.feettoinches(w)
print(C)

z = int(input("enter in inches: "))
D = lengthconversion.inchestofeet(z)
print(D)