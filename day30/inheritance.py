class ParentClass:
    def getname(self):
        self.name=input("enter the name")
        self.rollno=int(input("enter he roll number"))
    def readname(self):
        print(f"{self.name}\n{self.rollno}")
class ChildClass(ParentClass):
    def totalmark(self):
         self.tmark=int(input("enter the totall mark"))
         print(self.tmark)

    def grade(self):
        grade=self.tmark/500*100
        print(grade)
obj1=ChildClass()
obj1.getname()
obj1.readname()
obj1.totalmark()
obj1.grade()
