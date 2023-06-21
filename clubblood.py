print("welcome to blood donation camp")
name=str(input("enter your name: "))
age=int(input("enter your age: "))
weight=int(input("enter your weight: "))
if age>18 and weight>40:
    print("eligibility for blood donation")
else:
    print("not eligibility for blood donate")
