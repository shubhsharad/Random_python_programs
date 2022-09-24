#Program to convert infix to postfix

#Basic things written in the program
x=list(input('kindly enter the expression with no spaces:  '))
y=[]
stack=[]

#Utilizing the dictionary for the priority order
operators={"+":1,"-":1,"*":2,"/":2,"^":3,"(":4,")":4}

#Putting the brackets
stack.append("(")
x.append(")")

#Traversing through each of the element of x
for i in x:
   
    #When we encounter a left parenthesis,we push it into the stack
    if i=="(":
        stack.append(i)
     
    #when we encounter variables or numbers
    if i not in ["+","-","/","*",'^',")","("]:
        y.append(i)
       
    #When we encounter an operator    
    elif i in ["+","-","/","*",'^']:
        t=len(stack)-1
        p=stack[t]
        while operators[p]>=operators[i] and operators[p]!=4:
            a=stack.pop()
            y.append(a)
            t=t-1
            p=stack[t]
        stack.append(i)
   
    #When we encounter a right parenthesis
    elif i==")":
        r=len(stack)-1
        q=stack[r]    
        while q!="(":
             k=stack.pop()
             y.append(k)
             r=r-1
             q=stack[r]
        m=stack.pop()

#to get it back into string
w=""
for i in y:
    w=w+i
print(w) 
