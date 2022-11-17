
def MaxofTwo(a,b):
    if a>b:
        print(a," is Greater")
    else:
        print(b," is Greater")

def MaxofThree(a,b,c):
    if a>b:
        if a>c:
            print(a," is Greater")
        else:
            print(c," is Greater")
    elif b>c:
        print(b," is Greater")
    else:
        print(c," is Greater")

def EvenOdd(a):
    if a%2==0:
        print(a," is Even")
    else:
        print(a," is Odd")

def Prime(a):
    if a%2==0:
        print(a," is not a Prime")
    else:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print(a,"is not a Prime")
                break
            else:
                print(a," is a Prime")

def Fibonacci(n):
    a,b=0,1

    while b<n:
        print(b,end=" ")
        a,b = b,a+b
print()
        
        
            
            




















        
