#5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# A-
# frsname=input("enter the first name ")
# lastname=input("enter the lastname")
# print(frsname[::-1]," ",lastname[::-1])


# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
#A-
# num=input("enter numbers").split(",")
# print(list(num))
# print(tuple(num))

# 7. Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
# Sample filename : abc.java
# Output : java
#A-
# filename=input("enter the filename").split(".")
# print(filename[-1])


#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615
#A-
# num=int(input("enter the number"))
# t=0
# sum=0
# for i in range(3):
#     n=num+t
#     print(n,end="",)
#     if i<2:
#         print("+",end="")
#     t=n*10
#     sum+=n
# print("\n",sum)