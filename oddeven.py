"""
split: str ko list me convert karta h
"""
import random

data = open("data.txt","w")
for i in range(10):
    num=random.randint(1,999)
    data.write(str(num)+" ")
data.close()

data = open("data.txt","r")
s = data.read().split(" ")[:-1] 
print(s)

for i in s:
    print(int(i))
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

data.read().split(" ")[:-1]

for i in s:
    if int(i)%2==0:
        even.write(i+" ")
    else:
        odd.write(i+" ")
data.close()
even.close()
odd.close()

#read
print("data file content".center(80,"*"))
data=open("data.txt","r")
print(data.read())
data.close()

#even
print("even file content".center(80,"*"))
even=open("even.txt","r")
print(even.read())
even.close()

#odd
print("odd file content".center(80,"*"))
odd=open("odd.txt","r")
print(odd.read())
odd.close()
    










    



