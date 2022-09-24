def MinOne(x,y):
    if x%10 == y%10:
        print("both One's digit are equal")
    elif x%10 > y%10:
        print("One's digit of the first number is greater")
    elif x%10 < y%10:
        print("Ones digit of second number is greater:")
        
x = int(input("enter number: "))
y = int(input("enter number: "))
MinOne(x,y)