a=(input("Enter your name:"))
b=int(input("enter your id no : "))
w1=int(input("enter your maths no : "))
w2=int(input("enter your english no : "))
w3=int(input("enter your hindi no : "))
total=w1+w2+w3

per=total/3
print("total marks:",total)
print("per:",per)

if per>=90:
    print("distinction")
elif per>=80:
    print ("1st division")
elif per>=70:
    print ("2nd division")
elif per>=60:
    print ("3rd division")
elif per>=50:
    print (" pass by grace")
else:
    print("fail")

            
