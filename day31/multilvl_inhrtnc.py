#thes are single,multilevel and multiple innheritance
#so these combination of inheritance are callled hybrid inheritance

class MainClass:
    def details(self):
        self.name = input("enter your name")
        self.rollno = int(input("enter rollno"))
        self.place = input("enter the place")



class SecondClass(MainClass):
    def accept(self):
        self.num1 = int(input("enter your totalmark"))


class ThirdClass(SecondClass):
    def sum(self):
        total=(self.num1/500)*100
        if total>=90:
            print("A")
        elif total<90 and total>=80:
            print("B")
        elif total<80 and total>=70:
            print("C")
        elif total<70 and total>=60:
            print("D")
        elif total<=60 and total>=50:
            print("E")
        else:
            print("FAILED")


obj=ThirdClass()
obj.details()
obj.accept()
obj.sum()