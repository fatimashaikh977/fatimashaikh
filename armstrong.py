num=int(input("enter the number:"))
original=num

power=len(str(num))

sum=0
while num!=0:
    digit=num%10
    sum=sum+digit**power
    num=num//10
if original==sum:
    print("the number is armstrong!")
else:
    print("the number is not armstrong!")


