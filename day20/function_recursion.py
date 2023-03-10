#funtion recursion is a function calling iteself
#find the factorial of a number using recursion
num=int(input("enter a number"))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
fa=fact(num)
print(f"factorial of {num} is {fa}")



#find the  sum  of n natural numbers
num=int(input("enter a number"))
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
fa=sum(num)
print(f"sum of n natural no:{num} is {fa}")
