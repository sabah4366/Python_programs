#whileloop
#odd numbers
limit=int(input("enter a limit"))
i=1
while i<=limit:
    print(i)
    i = i + 2

#even numbers
limit1=int(input("enter a limit"))
i=2
while i<=limit1:
    print(i)
    i=i+2


#sum of even numbers
limit=int(input("enter a limit"))
i=2
sum=0
while i<=limit:
    sum=sum+i
    i=i+2
print("sum is:",sum)



#print digits of a number

num=int(input("enter a number"))
while num>0:
    a=num%10
    print(a)
    num=num//10



#sum of digits of a number
num=int(input("enter a number"))
sum=0
while num>0:
    a=num%10
    num//=10
    sum=sum+a**2
print('sum=',sum)



#amstrong number -153->   1cube3+2cube3+3cube3=153 aayirikkanam
num=int(input("enter a number"))
num1=num
sum=0
while num>0:
    a=num%10
    num=num//10
    sum=sum+a**3
if num1==sum:
    print("it is a amstrong number")
else:
    print("it is not a amstrong number")


#amstrong,digits of given number,sum of digits
num=int(input("enter a  number"))
n=num
sum=0
ams=0
while num>0:
    v=num%10
    print(v)
    num=num//10
    sum=sum+v**3
print(sum)
if n==sum:
    print("amstrong")
else:
    print("not amstrong")






