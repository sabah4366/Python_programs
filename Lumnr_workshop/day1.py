# # 5
# num=123476
# print(len(str(num)))

# # 6
# num=5
# for i in range(num,0-1,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
    

# #7
# num=int(input("enter a number"))
# t=num
# sum=0
# for i in range(1,num+1):
#     print(t,end="")
#     if i<num:
#         print("+",end="")
#     sum=sum+t
#     t=(t*10)+num
# print(sum)

# num=int(input("enter the number"))
# i=1
# while num>0:
#     sum=sum+i



# #8
# lmt=5
# star=1
# for i in range(1,2*lmt+1):
#     for j in range(star):
#         print("*",end=" ")
#     if i<lmt:
#             star+=1
#     else:
#             star-=1
            
#     print()
    
# 9
# for i in range(1500,2700+1):
#  	if i%7==0 and i%5==0:
#  	    print(i)

    

#10
# word=input("enter a word")
# print(word[::-1])



#11

# def factfun(num):
#     if num<=1:
#         return num
#     return num*factfun(num-1)
# res=factfun(5)
# print(res)


#12


#13
# def sumfun(num):
#     if num<=1:
#         return num
#     return num+sumfun(num-1)
    	
# res=sumfun(5)
# print(res)



#1 if question
# num=int(input("enter a number"))
# def fun(num):
#     if num>=18:
#         print("you are eligible")
#     else:
#         print("not eligible")



# fun(num)

#2-
# n=int(input("enter a number"))
# def mul(n):
#     if n%7==0:
#         return (n,'is divisible 7')
#     else:
#         return ("not divisible by  7")

# res=mul(n)
# print(res)
#upper code into lambda function
# n=int(input("enter a number"))
# mul=lambda x: " is divisible by 7" if x%7==0 else "{x} not divisible by 7"
# print(mul(n))





#3

# n=int(input("enter a number"))
# def even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(n)
#upper code into lambda function
# even_odd=lambda num:"even " if num%2==0 else "odd"
# n=int(input("enter a number"))
# print(even_odd(n))



#4
# n=int(input("enter a number"))
# def strng(val):
#     if val%5==0:
#         return "Hello"
#     else:
#         return "Bye"

# res=strng(n)
# print(res)
#upper code into lambda function
# string=lambda x:"Hello" if x%5==0 else "bye"
# print(string(6)) 



#5
# n=int(input("enter a number"))
# def unitprgrm(unit):
#     if unit<100:
#         return "no cost"
#     elif unit>=100 and unit<=200:
#         return unit*5
#     else:
#         return unit*10
# res=unitprgrm(n)
# print(res)
#upper code into lambda function
# unit=lambda x:"no cost" if x<100 else x*5 if x>=100 and x<=200 else x*10
# n=int(input("enter a number"))
# print(unit(n))

#6

# def lastNum():
#     num=int(input("enter a number"))
#     num1=num%10
#     if num1%4==0:
#         print("Yes")
#     else:
#         print("Not")
# lastNum()





#7
# num=int(input("enter a number"))
# def program(n):
#     if n>90:
#         print("Grade A")
#     elif n>80 and n<=90:
#         print("Grade B")
#     elif n>60 and n<=80:
#         print("Grade C")
#     elif n<=60:
#         print("Grade D")

# program(num)

#8

# rate=int(input("enter the rate"))
# def bikecost(cost):
#     if cost>100000:
#         res=(cost*15)/100
#         return res
#     elif cost>50000 and cost<=100000:
#         res=(cost*10)/100
#         return res
#     elif cost<=50000:
#         res=(cost*5)/100
#         return res
# val=bikecost(rate)
# print(val)

#9

# yr=int(input("enter the year"))
# def leap(year):
#     if year%400==0 and year%100==0:
#         print("it is leap year")
#     elif year%4==0 and year%100!=0:
#         print("it is leap year")
#     else:
#         print("not leap year")

# leap(yr)

#10

# def days():
#     print("1:Sunday 2:Monday 3:Tuesday 4:Wednesday 5:Thursday 6:Friday 7:Saturday ")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         print("Sunday")
#     elif choice==2:
#         print("Monday")
#     elif choice==3:
#         print("Tuesday")
#     elif choice==4:
#         print("wednesday")
#     elif choice==5:
#         print("Thursday")
#     elif choice==6:
#         print("Friday")
#     elif choice==7:
#         print("Saturday")
#     else:
#         print("Wrong Choice")
# days()



#12
def fibonaccisers(n):
    if(n <= 1):
        return n
    else:
        return(fibonaccisers(n-1) + fibonaccisers(n-2))
n = int(input("Enter number:"))
print("Fibonacci series:")
for i in range(n):
    print(fibonaccisers(i),end=" ")

	
	
#14
# def powerfun(a, b):
#     if b != 0:
#         return a * powerfun(a, b - 1)
#     else:
#         return 1


# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter  a number:"))
# res=powerfun(n1,n2)
# print(res)