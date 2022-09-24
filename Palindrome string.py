print(ord("Z"))
print(chr(98))
s1 = input("Enter the string: ")
s2 = s1[::-1]
if s1 == s2:
    print("Given string is palindrome")
else:
    print("Not a palindrome")