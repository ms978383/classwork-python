class A:

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)
class B:

    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)

class C(A,B):

    def GetC(self,c):
        self.c=c

    def PutC(self):
        print("C:",self.c)

ob=C()
ob.GetA(10)
ob.GetB(30)
ob.GetC(30)


ob.PutA()
ob.PutB()
ob.PutC()







        
        
