print("WELCOME TO A TO Z RESTAURANT")
print("enter your feedback")
print("Ratings will be: \n1.bad \n2. not bad \n3.average \n4.good \n5.excellent")
food=int(input("enter your ratings for food: "))
service=int(input("enter your ratings for service: "))
ambience=int(input("enter your ratings for ambience: "))
bill_amount=int(input("enter your bill amount: "))
if food==4 or food==5:
                if service==5 or service==4 and ambience==5 or ambience==4:
                    total_amount=bill_amount/10
                    orginal_amount=bill_amount-total_amount
                    print("10% discount remaining you wants to pay: ",orginal_amount)
                else:
                    total_amount=bill_amount/20
                    orginal_amount=bill_amount-total_amount
                    print("5% discount remaining you wants to pay: ",orginal_amount)
elif food==3 or food==2 or food==1:
                if service==5 or service==4 and ambience==5 or ambience==4:
                    total_amount=bill_amount/20
                    orginal_amount=bill_amount-total_amount
                    print("5% discount remaining you wants to pay: ",orginal_amount)
                else:
                    total_amount=bill_amount/bill_amount
                    orginal_amount=bill_amount-total_amount
                    print("1% discount remaining you wants to pay: ",orginal_amount)
else:
    print("enter valid ratings ")
                    
                    
                    
                    
