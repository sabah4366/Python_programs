
#empty list creation
# ls=[]
# nw=list()
# print(nw)
# print(ls)

#1-Write a program to separate negative and positive numbers from a given list ?(accept input from the user.)
#A-
# nglst=[]
# pslst=[]
# lst=input("enter numbers in a list").split()
# print(lst)
# for i in lst:
#     if int(i)<0:
#         nglst.append(int(i))
#     else:
#         pslst.append(int(i))
# print(nglst)
# print(pslst)


#2 Write a python program to find the sum of all numbers in a list
# lst=input("enter numbers").split()
# sum=0
# for i in lst:
#     sum=sum+int(i)
# print(sum)
    

#3.	 Write a python program to find largest number in a given list with out using max()
#not accept from user
# nwlst=[1 ,2, 3, 240 ,5 ,6 ,7 ,8 ,10 ,101 ,210 ,230]
# nwlst.sort()
# print(nwlst)
# print(nwlst[-1])
#accept from user
# lst=input("enter numbers").split()
# max=0
# for i in lst:
#     if int(i)>max:
#         max=int(i)
# print(max)

#4.	 Write a python program to find the common numbers from two lists
# lst1=input("enter numbers to the first list").split()
# lst2=input("enter numbers to the second list").split()
# nwlst=[]
# for i in lst1:
#     if i in lst2:
#         nwlst.append(i)
# print(nwlst)


#5.	 Write a python program to print all even numbers from a given list
# lst=input("enter numbers to the list").split()
# for i in lst:
#     if int(i)%2==0:
#         print(i)


#6.	 Write a python program to create a list of even numbers and another list of odd numbers from a given list
# lst=input("enter numbers to the list").split()
# oddlst=[]
# evenlst=[]
# for i in lst:
#     if int(i)%2==0:
#         evenlst.append(i)
#     else:
#         oddlst.append(i)
# print("Even list:",evenlst)
# print("odd list:",oddlst)


#7.	 Write a python program to remove repeated elements from a given list without using built-in methods
# lst=input("enter elements to the list").split()
# nwlst=[]
# for i in lst:
#     if i not in nwlst:
#         nwlst.append(i)

# print(nwlst)


#8. lst=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#Write a python program to print website suffixes (com , org , net ,in) from this list.
# lst=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# for i in lst:
#     s=i.split('.')
#     print(s[-1])

#9.Reverse a given tuple .
# tpl=tuple(input("enter numbers to the tuple").split())
# print(tpl[::-1])

#10.Check if all items in the tuple are the same.
# tpl=tuple(input("enter numbers to the tuple").split())
# c=0
# for i in tpl:
#     for j in tpl:
#         if i!=j:
#             c=c+1

# if c==0:
#     print("All elements are in tuple are same")
# else:
#     print("All elements in tuple are not same")

#11.Write a Python program to find the third largest number from a given list of numbers Use the Python set data type.       
# stitm=set(input("enter numbers to the tuple").split())
# lst=list()
# for i in stitm:
#     lst.append(int(i))
# lst.sort()
# print(lst[-3])


#FILE I/O OPERATIONS
#1.	Write a Python program to read an entire text file.
# f=open("file_1.txt")
# print(f.read())
# f.close()


#2.	Write a Python program to read first n lines of a file.
# f=open("file_1.txt")
# print(f.readline())
# f.close()

#3.	Write a Python program to append text to a file and display the text.
# f=open("file_1.txt","a")
# f.write("\nhai hey")
# f.close()
# f1=open("file_1.txt")
# print(f1.read())
# f1.close()

#4.	Write a Python program to read last n lines of a file.
# f=open("file_1.txt")
# ln=f.readlines()
# for line in ln:
# 	pass
# last_line=line
# print(line)
# f.close()


#5.	Write a Python program to read a file line by line and store it into a list.
# f=open("file_1.txt")
# print(f.readlines().strip())
# f.close()


#6.	Write a Python program to copy the contents of a file to another file .
# f1=open("file_1.txt")
# f1r=f1.read()
# f2=open("file_2.txt","w")
# f2.writelines(f1r)
# f1.close()
# f2.close()

#3.	Write a Python program to convert more than one list to a nested dictionary.
# lst1=[1,2,3,4]
# lst2=['name','age','place','address']
# lst3=['sabah','22','kannur','noor mahal']
# lst=[]
# for (i,j,k) in zip(lst1,lst2,lst3):
# 	lst.append({i:{j,k}})
# print(lst)	


#4.	Write a Python program to filter the height and width of students, which are stored in a dictionary.


# students = {
#     "raina": {"height": 175, "width": 60,"age":26,"place":"kannur"},
#     "ram": {"height": 180, "width": 70,"age":22,"place":"thalassery"},
#     "sam": {"height": 165, "width": 55,"age":24,"place":"kambil"},
#     "tom": {"height": 190, "width": 80,"age":25,"place":"calicut"},
#     "neha": {"height": 170, "width": 65,"age":27,"place":"cochin"}
# }

# height_students = {name: data['height'] for name, data in students.items() if data["height"]}

# width_students = {name: data['width'] for name, data in students.items() if data["width"]}

# print("Height of students:", height_students)
# print("Width of  students:", width_students)


# 2.	Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list4
#  from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.



# 7.	From the given json file write a program 
# •	To print all the data of a particular day is the date is given.
# •	Print the day of  highest temperature. 
# •	Print the day of snow rate is high.



import json
# •	To print all the data of a particular day is the date is given.
f=open("/home/sabah/PycharmProjects/luminar1/Lumnr_workshop/rdu-weather-history.json")
data=json.load(f)
print(data)
for d in data:
    if d['date']=="2018-12-29":
        print(d)


#	Print the day of  highest temperature.    
hg_temp=max(data,key=lambda item:item['tmax'])
print(hg_temp)


# •	Print the day of snow rate is high.
snw=max(data,key= lambda itm:itm['snow'])
print(snw)

f.close()