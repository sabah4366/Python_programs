#lambda function or anonymous function
#we cannot write lambda function in some large statement
mul=lambda a,b:a*b      #mul - is variable,lambda-keyword,a and b-arguments,a+b-expression
print(mul(3,4))

#user input square of a number
sqr=lambda s:s*s
num1=int(input("enter a number"))
print(sqr(num1))

#find the largest among two numbers
#syntax-variablename=lambda arguments:true_statement if condition  else false_statement
largstnumber=lambda a,b:a if a>b else b
num1=int(input("enter two numbers"))
num2=int(input())
print(largstnumber(num1,num2))



#if we compare three numbers we cant use elif in lambda function
#we can use only if else statement
large=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
num1=int(input("enter thre numbers"))
num2=int(input())
num3=int(input())
print(large(num1,num2,num3))
