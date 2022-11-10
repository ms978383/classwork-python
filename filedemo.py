file = open("tops.txt","w")
file.write("this is file management using python")
file.close()

print("file created successfully")

print("*"*80)

file = open("tops.txt","r")
print(file.read())
file.close()

print("*"*80)

file = open("tops.txt","a")
file.write("\n with appended.")
file.close()
print("appended successfully")            
            
