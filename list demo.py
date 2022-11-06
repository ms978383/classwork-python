s="List_Demo"
print(s.center(70,"*"))
l=[1,2,3,1.1,2.1,3.1,True,False,0,1,"tops","tech",2,0,0]
print(l)
l.append(100)
print(l)

l1=l.copy()
print(l1)

l2=l
print(l2)

l2.append(200)
print(l2)

l.pop()
print(l)

l.remove("tops")
print(l)

#l.reverse()
#print(l)

l.insert(9,7)
print(l)

#l.clear()
#print(l)


print(l.count(1))
print(l.count(0))

l2=[11,12,13,14]
l2.sort()
print(l2)

l3=[101,102,103]
print(l3)

l.extend(l3)
print(l)

print(l.index(103))

l.remove(102)
print(l)

l.reverse()
print(l)

for i in l:
    print(i)
    
print(11 in l2)    






