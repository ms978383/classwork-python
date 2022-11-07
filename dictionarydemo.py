d={1:"mahesh",2:"ramesh",3:"suresh",4:"dev",5:"harsh"}
print(d)

print(d[3])

d1=d.copy()
print(d1)

print(d.get(5))

print(d.items())

print(d.keys())

print(d.values())

print(d.pop(5))
print(d)

print(d.popitem())
print(d)

d3={4:"manas",5:"yash"}
d.update(d3)
print(d)

d[2]="Ram"
print(d)

d[3]="shyam"
print(d)

for i in d:
    print(i,":",d[i])









