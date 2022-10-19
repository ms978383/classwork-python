s1="string slicing for Mahesh Kumar"
print(s1.center(50,"*"))

#  012345678901  +
s="Mahesh kumar"
#  210987654321  -

print()
print("positive slicing".center(50,"*"))
print()
print(s[:])
print(s[0:6])
print(s[7:])
print(s[3:9])
print(s[0:6:2])
print()
print("Negative slicing".center(50,"*"))
print()
print(s[-12:])
print(s[:-6])
print(s[-5:-2])
print(s[-9:-3])
print(s[::-1])
