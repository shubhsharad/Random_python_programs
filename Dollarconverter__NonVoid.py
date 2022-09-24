def DollarConv(x):
    return x*75

x = int(input("enter amount in dollars: "))

RS = DollarConv(x)

print("Amount in Rupees: ", RS)