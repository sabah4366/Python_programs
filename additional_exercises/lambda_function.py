# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#  also create a lambda function that multiplies argument x with argument y and prints the result.
#Answer
# n=int(input("enter a number"))
# num=lambda x:x+15
# print(num(n))

# n1=int(input("enter first number"))
# n2=int(input("enter the second number"))
# num=lambda x,y:x*y
# print(num(n1,n2))

# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. Go to the editor
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
#Answer
# n1=int(input("enter the multiplication  number"))
# n2=int(input("enter the value"))
# def compute(n):
#     return lambda x:x*n
# result=compute(n1)
# print(result(n2))

# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
#Answer
# def even(n):
#     if n%2==0:
#         return n
# def odd(n):
#     if n%2!=0:
#         return n
# lst=[1,2,3,4,5,6,7,8,9]
# lst2=filter(odd,lst)
# lst1=filter(even,lst)
# print("even list:",list(lst1))
# print("odd list:",list(lst2))

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#Answer
# lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst1=map(lambda x:x**2,lst)
# lst2=map(lambda x:x**3,lst)
# print(list(lst1))
# print(list(lst2))


# 7. Write a Python program to find if a given string starts with a given character using Lambda. Go to the editor
# Sample Output:
# True
# False
#Answer
# str1=input("enter a string")
# chrctr=input("enter only one character")
# lst=lambda x,y:True if x[0]==y else False
# print(lst(str1,chrctr))


# 8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
#Answer
# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))



# . Write a Python program to check whether a given string is a number or not using Lambda. Go to the editor
# Sample Output:
# True
# True
# False
# True
# False
# True
# Print checking numbers:
# True
# True

# 11. Write a Python program to find the intersection of two given arrays using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]
#Answer
# lst1=[1, 2, 3, 5, 7, 8, 9, 10]
# lst2=[1, 2, 4, 8, 9]
# lst3=list(filter(lambda x: x in lst1,lst2))
# print(lst3)

# 13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5
# lst=[1, 2, 3, 5, 7, 8, 9, 10]
# lst2=filter(lambda x:x%2==0,lst)
# print("count oof even numbers:",len(list(lst2)))
# lst3=filter(lambda x:x%2!=0,lst)
# print("count of oddlist numbers are",len(list(lst3)))



# 14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda. Go to the editor
# Sample Output:
# Monday
# Friday
# Sunday
#Answer
# lst=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# lst1=filter(lambda x: len(x)==6,lst)
# print(list(lst1))


# 15. Write a Python program to add two given lists using map and lambda. Go to the editor
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]
#Answer
# lst1=[1, 2, 3]
# lst2=[4, 5, 6]
# lst3=map(lambda x,y:x+y,lst1,lst2)
# print(list(lst3))



# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. Go to the editor
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]
#Answer
# lst=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# lst1=filter(lambda x:x%19==0 or x%13==0,lst)
# print(list(lst1))

# 18. Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']
#Answer
# lst=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# lst2=filter(lambda x:x==x[::-1],lst)
# print(list(lst2))


# 19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda. 
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']
# from collections import Counter
# str="abcd"  
# lst=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# lst2=filter(lambda x:(Counter(str)==Counter(x)),lst)
# print(list(lst2))


# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22
# lst= [2, 4, 6, 9, 11]
# n=2
# lst2=map(lambda x:x*2,lst)
# print(list(lst2))

# 23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function. Go to the editor
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48
#Answer
# lis=[2, 4, -6, -9, 11, -12, 14, -5, 17]
# lst=filter(lambda x: x>0 ,lis )
# lst1=filter(lambda x:x<0 ,lis )
# print(sum(lst))
# print(sum(lst1))