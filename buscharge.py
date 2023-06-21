#ACB, the Omni Bus Company, has decided to give a 20% traveling fare concession for senior citizens; the actual fare will be Rs 1020.
#The upper age limit for senior citizens is above 60. 
#For verification, they will ask for the date of birth (take the year alone), and if satisfied, they will be given a concession and will be displayed the final traveling charge; if not, the original fare will be displayed. 
print("welcome to ABC omini bus company")
year=int(input("enter your birth year: "))
age=2023-year
print(age)
if age>=60:
    fare=1020-(4/2)*102
    print("the traveling charge is: ",fare)
else:
    print("the traveling charge is: 1020")
