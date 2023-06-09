def equation(x,y):
    z=abs(x-y)*(x+y)
    return z
x=float(input("enter a number: "))
y=float(input("enter a nuumber: "))
z=equation(x,y)
print("the value of z is: ",z)
