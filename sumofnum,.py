num=int(input("enter the number:"))

i=0
while num>0:
    # this gives the last digit  10/45 it gives 5 which is last number
    i=num%10 
    sum=i+num
    # this remove the last digit 45//10 so the answer is 4 its remove 5 from the num 
    i=num//10

print(sum)