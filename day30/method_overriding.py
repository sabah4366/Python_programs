class Main:
    def details(self):
        self.name = input("enter your name")
        self.rollno = int(input("enter rollno"))
        self.place = input("enter the place")


    def sum(self):
        total=self.num1+self.num2
        print("total",total)
class SecondMain(Main):
    def details(self):
        super().details()
        self.num1 = int(input("enter two numbers"))
        self.num2 = int(input())

ob=SecondMain()
ob.details()
ob.sum()