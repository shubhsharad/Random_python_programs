n = int(input("Enter Number: "))
for i in range(2,n):
    if n%i == 0:
        print("Number is not a prime no")
        break
else:
    print("Prime Number: ",n)