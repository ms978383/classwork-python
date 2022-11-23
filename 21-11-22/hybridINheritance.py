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

class D(B,C):

    def GetD(self,d):
        self.d=d

    def PutD(self):
        print("D:",self.d)

obj=D()
obj.GetA(10)
obj.GetB(20)
obj.GetC(30)
obj.GetD(40)

obj.PutA()
obj.PutB()
obj.PutC()
obj.PutD()
        
















    
