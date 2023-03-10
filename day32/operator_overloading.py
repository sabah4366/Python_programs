class OperatorOverloading:
    def __init__(self,a,b,c,d):
        self.x=a
        self.y=b
        self.v=c
        self.z=d
    def __add__(self, other):
        num1=self.x+other.x
        num2=self.y+other.y
        num3=self.v+other.v
        num4=self.z+other.z
        num=num1+num2+num3+num4
        return OperatorOverloading(num1,num2,num3,num4)
    def __str__(self):
        return '({},{},{},{})'.format(self.x,self.y,self.v,self.z)

p1=OperatorOverloading(3,5,4,5)
p2=OperatorOverloading(4,6,7,10)
print(p1+p2)














