#1)sigle level inheritance:-

class A():

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)


class B(A):


    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)


a=input("enter a:")
b=input("enter b:")

ob=B()
ob.GetA(a)
ob.PutA()
ob.GetB(b)
ob.PutB()
