s = input("enter string: ")
l = s.split()
d = {}
print(l)
for a  in l:
    if a not in d:
        d[a] = l.count(a)
print(d)

