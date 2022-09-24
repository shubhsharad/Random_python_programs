s = input("Enter String:  ")
countv = 0
countc = 0
n = ["A","E","I","O","U","a","e","i","o","u"]
for a in s:
    if a  in n:
        countv = countv+1
    else: 
        countc = countc+1
print("No of vowels:",countv)
print("No of consonants:",countc)