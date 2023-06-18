#Check if the nth power of a number is even or not (get the number and the power as an input)
num=int(input("enter a number: "))
power=int(input("enter a number: "))
res=num**power
print("result for given number is: ",res)
if res%2==0:
    print("is even")
else:
    print("is not even")
