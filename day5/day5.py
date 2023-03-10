#check given number is odd or even
num1=int(input("enter a number"))
if num1 % 2 == 0:
    print("it is an even number")
else:
    print("it is an odd number")



#one greater than other
num1=int(input("enter first number"))
num2=int(input("enter second number"))

if num1 > num2 :
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than ",num1)


#check given numbers is multiple of 5 and 7
n=int(input("enter a number"))
if n%5==0 and n%7==0:
    print(n,"is a multiple of 5 and 10")
else:
    print(n,"is not a multiple of 5 and 7")



#temperature conversion using if and elif
num1=int(input("enter the 1st mark"))
num2=int(input("enter the 2nd mark"))
num3=int(input("enter the 3rd mark"))
totalmar=num1+num2+num3
per=(totalmar/300)*100
print("perscentage is:",per)
if per>=80:
    print("A GRADE")
elif per>=60:
    print("B GRADE")
elif per>=40:
    print("C GRADE")
else:
    print("YOU ARE FAILED")



#largest among three numbers
num1=int(input("enter three numbers"))
num2=int(input())
num3=int(input())

if num1>=num2 and num1>=num3:
    print("ths is num1",num1,"is greater than",num2,"and",num3)
elif num2>=num1 and num2>=num3:
    print("ths is num2",num2, "is greater than", num1, "and", num3)
else:
    print("ths is num3",num3, "is greater than", num2, "and", num1)
