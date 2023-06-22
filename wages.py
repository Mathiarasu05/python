name=str(input("enter your name: "))
age=int(input("enter your age: "))
gender=int(input("enter your gender is male enter 1 or female enter 2: "))
if age<18:
    print("enter age above 18")
elif age>=18 and age<30:
    if gender==1:
        wages=700
        days=int(input("enter number of days worked: "))
        total_amount=wages*days
        print("the total amount paid : ",total_amount)
    if gender==2:
        wages=750
        days=int(input("enter number of days worked: "))
        total_amount=wages*days
        print("the total amount paid : ",total_amount)
elif age>=30 and age<40:
    if gender==1:
        wages=800
        days=int(input("enter number of days worked: "))
        total_amount=wages*days
        print("the total amount paid : ",total_amount)
    if gender==2:
        wages=800
        days=int(input("enter number of days worked: "))
        total_amount=wages*days
        print("the total amount paid : ",total_amount)        
else:
    print("enter age below 40")

        
        
