
# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:

# ['My', 'name', 'is', 'Kelly']
#answer
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# lst3=[ i + j for i, j in zip(list1,list2)]
# print(lst3)


#Exercise 3: Turn every item of a list into its square
#answer
# lst=[1,2,3,4,5,6]
# lst2=[i*i for i in lst]
# print(lst2)


# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#answer
#using list comprehension
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# lst3=[i+j for i in list1 for j in list2]
# print(lst3)
#using normal for loop
# lst3=[]
# for i in list1:
#     for j in list2:
#         lst3.append(i+j)
# print(lst3)

# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# Given

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:

# 10 400
# 20 300
# 30 200
# 40 100
#Answer
#using normal forloop
# list1 = [10, 20, 30, 40]
#list2 = [100, 200, 300, 400]
# for i in range(len(list1)):
#     for j in range(len(list2),len(list2)+1):
#         print(list1[i]," ",list2[-i-1])

#using zip,tiple

# for x,y in zip(list1,list2[::-1]):
#     print(x,y)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]

#Answer
#one method
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# lst=[i for i in list1 if i!=""]
# print(lst)

#anothet method

# remove None from list1 and convert result into list
# lst= list(filter(None, list1))
# print(lst)


# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

#answer
# val=int(input("enter the value"))
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# (list1[2][2]).append(val)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:

# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:

# [5, 10, 15, 200, 25, 50, 20]
#answer
#one method
# list1 = [5, 10, 15, 20, 25, 50, 20]
# for i in range(len(list1)):
#     if 20==list1[i]:
#         list1[i]=200
#         break
# print(list1)
#second method
# index=list1.index(20)
# list1[index]=200
# print(list1)



# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]
#answer
#using list comprehention
# list1 = [5, 20, 15, 20, 25, 50, 20]
# lst2=[i for i in list1 if i!=20]
# print(lst2)


#using while loop
# list1 = [5, 20, 15, 20, 25, 50, 20]
# i=0
# lst3=[]
# while i<len(list1):
#     if list1[i]!=20:
#         lst3.append(list1[i])
#     i+=1
# print(lst3)

#using while easy method
# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)

