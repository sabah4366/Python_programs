#return function
def values(a,b):
    sum=a+b
    return sum

num1=int(input("enter two numbers"))
num2=int(input())
res=values(num1,num2)
print(res)
avg=res/2
print(avg)

#in python we can return multiple values
#this is function is only in python compared to other languages
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    di=a/b
    return sum,sub,mul,di
num1=int(input("enter two numbers"))
num2=int(input())
a,b,c,d=calc(num1,num2)
print(f"sum is{a}\nsub is{b}\nmul is{c}\ndiv is{d}")


#default argument
#if you put a default argument then put at the last otherwise it will get an error
def arg(rl,nm,crs='BCA'):
    print(f"name   :{nm}\nrollno :{rl}\ncourse :{crs}")

arg(23,'sabah')
arg(24,'asif')
arg(25,'safwan')
arg(26,'sahal','BBA')


#keyword argument
def keyarg(name,place):
    return name,place
a,b=keyarg(place='kannur',name='sabah')
print(a,":",b)