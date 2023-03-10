#using function check the given number is prime or not
num=int(input("enter a number"))
def primeno(a):
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag=1
            break
    if flag==1:
        print(" not prime")
    else:
        print("prime")

primeno(num)
#find the sum of even numbers
numbrs=int(input("enter numbers"))
def sum(s):
    sum=0
    for i in range(s):
        if i%2==0:
            sum=sum+i
    print(sum)
sum(numbrs)