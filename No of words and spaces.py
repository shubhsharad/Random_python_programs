f = open("C:/Users/user/Desktop/cons.txt","r")
a = f.read()
num_words = 0
b = a.count(" ")
print("blank spaces",b)
f.close()
f = open("C:/Users/user/Desktop/cons.txt","r")
for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
f.close()
f = open("C:/Users/user/Desktop/cons.txt","r")
z = f.readlines()
print(z)
nl = len(z)
print("number of lines = ", nl)
f.close()
#program work kar raha tha pehle
#no of lines 11 aa rahe hain?