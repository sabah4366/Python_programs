class Main:
    def __init__(self,l,b):
        self.len=l
        self.bre=b

    def sum(self):
        s=self.len*self.bre
        print(s)

o1=Main(2,6)
o2=Main(3,5)
o1.sum()
o2.sum()