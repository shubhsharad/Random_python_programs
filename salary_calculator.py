import salary.salary_conversion

x = int(input("enter salary: "))

A = salary.salary_conversion.HRA(x)
B = salary.salary_conversion.DA(x)
print("basic salary : ",x)
print("HRA is: ",A)
print("DA is : ",B)

C = A+B+x
print("Total Salary is: ",C)