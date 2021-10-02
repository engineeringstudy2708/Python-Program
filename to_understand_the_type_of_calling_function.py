def comp(a,b,c=0): # Here if i write c=0 so it is default argument
    print(a)       # Here a,b,c require three argument ,that is called Required argument
    print(b)
    print(c)

    return (a,b,c)

inc=lambda x:x+1

a=print("The value of inc",inc(6))

p=comp(10,20,30)  

q=comp(a=10,b=20,c=9) #Keyword argument

r=comp(10,20) # It take Default argument (c=0), if we can't give third argument

abc=inc

print("abc value :",abc(7))

inc=comp # Here we are swapping a function directly
comp=abc  # This is a magic of python language

s=comp(1) #Note:  now comp become inc and inc become comp
print(s)  #So, inc take three argument instead of one argument and same comp will take only one argument now.

t=inc(10,20,30)
