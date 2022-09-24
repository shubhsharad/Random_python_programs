import Conversion.Length.lengthconversion
import Conversion.Mass.massconversion

x = int(input("enter miles: "))
A = Conversion.Length.lengthconversion.miletokm(x)
print(A)

y = int(input("enter in kgs: "))
B = Conversion.Mass.massconversion.kgtopound(y)
C = Conversion.Mass.massconversion.kgtotonne(y)
print(B)
print(C)

z = int(input("enter in pounds: "))
D = Conversion.Mass.massconversion.poundtokg(z)
print(D)