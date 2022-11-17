class person:


    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def showdetails(self):
        print("first name:",self.fname)
        print("last name:",self.lname)
        print("email:",self.email)

fname = input("enter first name:")
lname = input("enter last name:")
email = input("enter email:")

p = person(fname,lname,email)
p.showdetails()

