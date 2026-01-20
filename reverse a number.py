num=int(input("enter the number:"))

reve=0

while num!=0:
    digit=num%10
    reve=reve*10+digit
    num=num//10

print("the reversed is:",reve)