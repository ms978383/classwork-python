import UDF


while True:
    print()
    print("*"*50)
    print("Press 1. MaxOfTwo")
    print("Press 2. MaxOfThree")
    print("Press 3. EvenOdd")
    print("Press 4. Prime No.")
    print("Press 5. Fibonacci Series")
    print("Press 6. Exit")
    print("*"*50)
    choice = int(input("Enter your Choice ? "))
                 
    if choice==1:
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        UDF.MaxofTwo(a,b)
    elif choice==2:
         a = int(input("Enter A : "))
         b = int(input("Enter B : "))
         c = int(input("Enter C : "))
         UDF.MaxofThree(a,b,c)
    elif choice==3:
         a = int(input("Enter No : "))
         UDF.EvenOdd(a)
    elif choice==4:
         a = int(input("Enter No : "))
         UDF.Prime(a)
    elif choice==5:
        a = int(input("Enter No : "))
        UDF.Fibonacci(a)
    elif choice==6:
        break
            






















