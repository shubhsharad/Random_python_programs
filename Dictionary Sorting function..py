price = {"Apple":1.5,"Grapes":4.5,
         "Banana":6}
print(sorted(price))
#print(sorted(price.itervalues()))
#print(sorted(price.iterkeys()))
print(sorted(price.items(),key = lambda x: x[1]))
print(sorted(price.keys()))