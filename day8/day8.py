# #factorial*

# num=int(input("enter a number"))
# fact=1
# for i in range(1,num+1,1):
#     fact=i*fact
#     print(fact)


# #sum of odd and and even numbers upto limit
# n=int(input("enter a limit"))
# sum1=0
# sum2=0
# for i in range(1,n,1):
#     if i%2==0:
#         sum1 = sum1 + i
#     else:
#         sum2=sum2+i
# print("sum od even numbers is=",sum1)
# print("sum od odd numbers is=",sum2)


# #1,2,3-this is multiple of 3,4,5,6-this is multiple of 3,....

# num=int(input("enter a limit"))
# for i in range(1,num,1):
#     if i%3==0:
#         print(i," it is a multiple of 3")
#     else:
#         print(i)


# find all factors of a given number,sum of all factors,count the numbers of factors
num = int(input("enter a number"))
print("these are the factors of a ",num)
sum=0
count=0
for i in range(1, num + 1, 1):
    if num % i == 0:
        print(i)
        sum=sum+i
        count=count+1
print("sum of all factors are:",sum)
print("count of factors are:",count)

