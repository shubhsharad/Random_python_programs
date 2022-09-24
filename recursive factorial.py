def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 7
print("The factorial of", num, "is", recur_factorial(num))