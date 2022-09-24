s = input("Enter String: ")
x = " "
count1 = 0
count2 = 0
count3 = 0
n = len(s)
for a in s:
    if a.islower() == True:
        count1 = count1+1
        x = a.upper()+x
    elif a.isupper()== True:
        count2 = count2+1
        x = a.lower()+x
    elif a.isspace()==True:
        count3 = count3+1
        x = a+x
print("Uppercase",count1)
print("Lowercase",count2)
print("Whitespaces",count3)
print(x[::-1])

