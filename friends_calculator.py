rant=int(input("enter the rent you'are paying:"))
food=int(input("enter the amount of food ordered :"))
electricity=int(input("enter the electricity unit:"))
charge=int(input("enter the chargeper unit :"))
person=int(input("enter the no of person living :"))

electricity_charged=electricity * charge
total=rant+ food + electricity_charged 
pay=total//person
print("per person you have to pay=",pay)