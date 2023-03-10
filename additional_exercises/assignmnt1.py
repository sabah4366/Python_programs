
#NEW QUESTIONS
#1. Check a given no. is a perfect no. or not
# n=int(input("enter a number"))
# sum=0
# for i in range(1,n):
# 	if n%i==0:
# 		sum=sum+i
# if sum==n:
# 	print("Perfect number")
# else:
# 	print("Not perfect number")

# 2. print the pattern
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

# lmt=int(input("enter the limit"))
# star=1
# for i in range(lmt,0,-1):
#     for j in range(1,star):
#         print("",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     star+=1
#     print()


# 3. Print the pattern
#   A
#   B B
#   C C C
#   D D D D
#   E E E E E

# lmt=int(input("enter the limit"))
# for i in range(1,lmt+1):
#     for j in range(1,i+1):
#         print(chr(i+64),end=" ")
#     print()

#4. Print only even length words in a given string
# string=input("enter string").split()
# print(string)
# print(len(string))
# for i in range(0,len(string)):
#     if i%2==0 and i!=0:
#         print(string[i],i)
    


#5.Find words which are greater than given length
# string=input("enter string").split()
# lngth=int(input("enter the length "))
# for i in range(len(string)):
#     if i>lngth:
#         print(string[i])


    
#6-Check a string is symmetrical
# string=input("enter the string")
# mid=int(len(string)/2)
# if len(string)%2!=0:
#     ss=string[mid+1:]
# else:
#     ss=string[mid:]
# fs=string[:mid]
# if ss==fs:
#     print("string is symmetrical")
# else:
#     print("not symmetrical")


#7.Remove character at even indices of a string
# string=input("enter a string")
# for i in range(0,len(string)):
#     if i%2!=0:
#         print(string[i])


        
        

    


#8.Count the number of words in a string
# string=input("enter a string").split()
# c=0
# for i in string:
#     c=c+1
# print("count of words :",c)


#9.check a given year is leap year or not
# year=int(input("enter the year"))
# if year%400==0 and year%100==0:
#     print("its is a leap year")
# elif year%4==0 and year%100!=0:
#     print("leap year")
# else:
#     print("it is not leap year")



#10. Multiply all the numbers in a list
# lst=input("enter the list").split()
# mul=1
# for i in lst:
#     mul=mul*int(i)
# print(mul)

#11. Sort elements in a llist without using bult in function sort()

# lst=input("enter the lis").split()
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[int(i)]>lst[int(j)]:
#             temp=lst[int(i)]
#             lst[int(i)]=lst[int(j)]
#             lst[int(j)]=temp
# print(lst)


            


#12. Count the no. in a list which is greater than a given no.
# lst=input("enter the number of list").split()
# num=int(input("enter the number"))
# c=0
# for i in lst:
#     if int(i)>num:
#         c+=1
# print(c)


#13. Count the no. of uppercase and lowercase characters in a string
# string=input("enter the string")
# c1=0
# c2=0
# for i in string:
#     if i.isupper():
#         c1+=1
#     elif i.islower():
#         c2+=1
# print("count of uppercase letters:",c1,"\ncount of lower case letters:",c2)



#14.let farm={'1:Eeman',2:'Catrine',3:'David'} be a dictionary.
#  To dd the key value pair(8:'Jack').
#  To display the number of items in the dicionary.
#  To remove the key value pair(2:'Catrine').
# farm={1:"Eeman",2:"Catrine",3:"David"}
# farm[8]="jack"
# print(farm)
# print(len(farm))
# del farm[2]
# print(farm)



#15.Create a tuple from an existing tuple. New tuple contains only the elements divisible by 3
# tup=tuple(input("enter numbers to the tuple").split())
# print("old tuple",tup)
# newtup=[]
# for i in tup:
#     if int(i)%3==0:
#         newtup.append(int(i))
# print("new tuple",tuple(newtup))




