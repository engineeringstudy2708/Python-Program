a=input("Enter value of a")
b=input("Enter value of b")
c=input("Enter value pf c")

if(a>b):
    if(a>c):
        print("A is greater =",a)
    else:
        print("C is greater =",c)
elif(b>c):
    if(b>a):
        print("B is greater =",b)
    else:
        print("A is greater =",a)
elif(c>a):
    if(c>b):
        print("C is greater =",c)
    else:
        print("B is greater =",b)
        
    
