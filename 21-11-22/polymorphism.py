class A:

    def Show(self):
        print("Show From Class A")

class B(A):

    def Show(self):
        super().Show()
        print("Show From Class B")

class C(B):

    def Show(self):
        super().Show()
        print("Show From Class C")
        
obj=C()
obj.Show()
