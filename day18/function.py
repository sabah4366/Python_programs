
#function withou return and argument
def msg():
    print("hello world")
msg()

#function with arg and without return
def argtype(name):
    print("hai:",name)
argtype("sabah")

#eg of function with arg and without return
#sum of 2 numbers
def sum(num1,num2): #this num1 and num2 is formal argument/paramaters
    s=num1+num2
    print(f"sum of {num1} + {num2} ={s}")
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
sum(num1,num2)      #this num1 and num2 are actual parametrs/arguments


#sum and sub and mult and div and mod
def add(a,b):
    sum=a+b
    print(sum)
def mul(a,b):
    mul=a*b
    print(mul)
def div(a,b):
    div=a/b
    print(div)
def sub(a,b):
    sub=a-b
    print(sub)


print("1:addition\n2:multiplication\n3:division\n4:subtraction")
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
choice=int(input("enter your choice"))
if choice==1:
    add(num1,num2)
elif choice==2:
    mul(num1,num2)
elif choice==3:
    div(num1,num2)
elif choice==4:
    sub(num1,num2)
else:
    print("invalid number")


#factorial of a number using function
def fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    print(f"factorial of {n} is={fa}")
num=int(input("enter a number"))
fact(num)



#print only even numbers in a list using function
list1=[1,2,3,4,5,6]
def listt(list):
    for i in list:
        if i%2==0:
            print(i)

listt(list1)
