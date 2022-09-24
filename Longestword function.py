def Longestword(string):
    
    l = s.split()
    print(l)
    n = len(l)
    m  = 0
    x = None
    for i in range (0,n):
        if len(l[i])>m:
            x = l[i]
            m = len(l[i])
    print("longest word is: ",x)
s = input("enter string: ")
Longestword(s)