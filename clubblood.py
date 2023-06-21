#A Rotary Club has decided to conduct a blood donation camp.
#The eligibility criteria for the blood donation camp will be that the person should be above 18 and his or her weight should be above 40. 
#The volunteers will enter the name, age, and weight of the person, and then it will display whether they are eligible or not.
print("welcome to blood donation camp")
name=str(input("enter your name: "))
age=int(input("enter your age: "))
weight=int(input("enter your weight: "))
if age>18 and weight>40:
    print("eligibility for blood donation")
else:
    print("not eligibility for blood donate")
