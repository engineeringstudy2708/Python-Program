
def fact(x):
    "This function is used to find the factorial" # docstring of a funciton
    if(x==0):
        return 1
    else:
        return (x*fact(x-1))


x=int(input("Enter the number to find factorial :"))

fac=fact(x)

print("The factorial of %d is %d"%(x,fac))

print(fact.__doc__)      #to find the docstring of a fact function 
