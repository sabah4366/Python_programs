num=int(input("enter a number"))
num2=num1=num
c=0
sum=0
while num>0:
    num=num//10
    c=c+1
while num1>0:
    ab=num1%10
    num1=num1//10
    sum=sum+ab**c
if sum==num2:
    print("amstrong")
else:
    print("not amstrong")

