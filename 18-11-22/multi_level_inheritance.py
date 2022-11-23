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

class C(B):


    def GetC(self,c):
        self.c=c

    def PutC(self):
        print("C:",self.c)


a=input("enter a:")
b=input("enter b:")
c=input("enter c:")

ob=C()
ob.GetA(a)
ob.PutA()
ob.GetB(b)
ob.PutB()
ob.GetC(c)
ob.PutC()







