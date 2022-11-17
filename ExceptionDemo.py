
"""
    Exception : It is an abnormal situation that araises during the Runtime
                of a Program.

                

    To handle Exception, we make use of
    1)try block
    2)except block
    3)else block
    4)finally block

    - try block will never be alone, it will have except/finally block atleast once
    - finally block will execute any how, even if the exception is generated or not.
    
"""
"""
num = int(input("Enter a No."))

div = num/0
print(div)


try:
    num = int(input("Enter No."))
    div = num/0
    print(div)
except:
    print("Exception Caught")


"""


while True:    
    try:
        n = float(input("Enter Value"))
        n1=int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")

print("Bye")













    
