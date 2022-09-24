def Encrypt(string,key):
    return key.join(string)
def Decrypt(string,key):
    return string.split(key)

x = input("Enter string :")
y = input("enter encryption key: ")
A = Encrypt(x,y)
print(A)
w = input("enter encrypted string: ")
z = input("enter decryption key: ")
B = Decrypt(w,z)
C = "".join(B)
print(C)