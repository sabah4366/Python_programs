#countfactors
num=int(input("enter the number"))
count=0
for i in range(1,num+1,1):
    if num % i == 0:
        print(i)
        count=count+1
print("total count",count)

#check the given number is prime or not
num=int(input("enter a number"))
c=0
for i in range(1,num+1,1):
    if num%i==0:
        c=c+1
if c==2:
    print("it is a prime number")
else:
    print("its not   a prime  number")

#fibanocci series
num=int(input("enter a number"))
s=1
f=0
for i in range(1,num):
    print(f)
    t=f+s
    f=s
    s=t

#forloop
#for ietr_var in loop
#body of the loop
a=input("enter a string")
for i in a:
    print(i)


# count the characters
st = input("enter a string")
c=0
for i in st:
    c = c + 1
print("number of charaters", c)

#count of the vowels given string
s=input("enter a string")
c=0
for i in s:
    if i in 'aeiouAEIOU':
        c=c+1
print("count of vowels are:",c)