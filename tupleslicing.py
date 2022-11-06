s="tuple_slicing_demo"
print(s.center(80,"*"))
#  0 1 2 3 4 5   6   7   8    9     0 1   2         3        4       5      6  +
t=(1,2,3,4,5,2.1,3.1,4.1,True,False,0,1,[10,20,30],"tops","career","python",10)
#  7 6 5 4 3 2    1   0   9    8    7 6   5         4        3       2      1  -
print(t)

print("positive_value".center(80,"*"))

print(t[1:9])
print(t[:7])
print(t[13:])
print(t[2:5:2])
print(t[::4])

print("negative_value".center(80,"*"))

print(t[-4:-12])
print(t[:-6])
print(t[-4:])
print(t[-3:-12:-2])
print(t[::-1])




