# class Main:
#     def getdata(self):          #self is for the refference of the object
#         self.id=int(input("enter th ID:"))
#         self.name=input("enter the name")
#
#     def showdata(self):
#         print(f"ID:{self.id}\nNAME:{self.name}")
# obj1=Main()
# obj2=Main()
# obj1.getdata()
# obj2.getdata()
# obj1.showdata()
# obj2.showdata()

#
#
# class Rectangle:
#     def getdata(self):
#         self.leng=int(input("enter the length"))
#         self.brdth=int(input("enter the braedth"))
#     def display(self):
#         print("length is:",self.leng,"\nbreadth is :",self.brdth)
#
#     def area(self):
#         a=self.leng*self.brdth
#         return a
#
#
# r1=Rectangle()
# r2=Rectangle()
# r1.getdata()
# r1.display()
# r2.getdata()
# r2.display()
# f=r1.area()
# s=r2.area()
# print(f"area is:{f}\narea is{s}")
#



#accept values from user
# class Rectangle:
#     def getdata(self,a,b):
#         self.leng=a
#         self.brdth=b
#     def display(self):
#         print("length is:",self.leng,"\nbreadth is :",self.brdth)
#
#     def area(self):
#         a=self.leng*self.brdth
#         return a
#
# num1=int(input("enter the length"))
# num2=int(input("enter the braedth"))
# r1=Rectangle()
# r2=Rectangle()
# r1.getdata(num1,num2)
# r1.display()
# f=r1.area()
# print(f"area is:{f}")
# num3=int(input("enter the length"))
# num4=int(input("enter the length"))
# r2.getdata(num3,num4)
# r2.display()
# s=r2.area()
# print(f"area is:{s}")


#using constructor
class Rectangle:
    def __init__(self,a,b):
        self.leng=a
        self.brdth=b
        b=self.leng*self.brdth
        print(b)
    def display(self):
        print("length is:",self.leng,"\nbreadth is :",self.brdth)

    def area(self):
        a=self.leng*self.brdth

num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
obj=Rectangle(num1,num2)
obj2=Rectangle(num4,num3)