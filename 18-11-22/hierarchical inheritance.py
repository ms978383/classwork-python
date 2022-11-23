# 3) hierarchical Inheritance:-

class A:

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)


class B(A):

    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)
class C(A):

    def GetC(self,c):
        self.c=c

    def PutC(self):
        print("C:",self.c)
class D(A):

    def GetD(self,d):
        self.d=d

    def PutD(self):
        print("D:",self.d)

a=input("enter A:")
b=input("enter B:")
c=input("enter C:")
d=input("enter D:")


ob=B()
ob.GetA(a)
ob.GetB(b)

obc=C()
ob.GetC(c)

obd=D()
ob.GetD(d)

ob.putA()
ob.putB()
obc.putC()
obd.putD()



















        
        

        
