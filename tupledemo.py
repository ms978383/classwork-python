t = (1,2,3,1.1,2.2,3.3,True,"tops",False,10,[],1.1,1,2.2,True,"python")
print(t)

print(t.index(10))
print(len(t))
print(t.count(1))

print(t[10])
t[10].append(1000)
print(t[10])
t[10].append(2000)
print(t[10])


for i in t:
    print(i)

print("python" in t)    


