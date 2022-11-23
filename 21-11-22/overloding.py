class A:

    def __init__(self,x,y):

        self.x=x
        self.y=y
        print("init called")

    def __str__(self):
        print("str called")
        return "[({0},{1})]".format(self.x,self.y)

obj=A(10,20)
print(obj)
