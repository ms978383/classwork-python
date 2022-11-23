from tkinter import *
import tkinter.messagebox as msg

root=Tk()


root.geometry("350x400")
root.title("MY TKINTER EXAMPLE")
root.resizable(width="false",height="false")


#labels

id=Label(root,text="ID NO :")
id.place(x=50,y=50)

fname=Label(root,text="First Name :")
fname.place(x=50,y=100)

lname=Label(root,text="Last Name :")
lname.place(x=50,y=150)

email=Label(root,text="E-Mail :")
email.place(x=50,y=200)

mobile=Label(root,text="Mobile No. :")
mobile.place(x=50,y=250)

#Entry (means-textarea)

id=Entry()
id.place(x=140,y=50)

fname=Entry()
fname.place(x=140,y=100)

lname=Entry()
lname.place(x=140,y=150)

email=Entry()
email.place(x=140,y=200)

mobile=Entry()
mobile.place(x=140,y=250)

#button

insert=Button(root,text="INSERT" ,bg="grey" ,fg="white" ,font=("algerian",10))
insert.place(x=40,y=300)

search=Button(root,text="SEARCH" ,bg="grey" ,fg="white" ,font=("algerian",10))
search.place(x=107,y=300)

update=Button(root,text="UPDATE" ,bg="grey" ,fg="white" ,font=("algerian",10))
update.place(x=185,y=300)

delete=Button(root,text="DELETE" ,bg="grey" ,fg="white" ,font=("algerian",10))
delete.place(x=260,y=300)





















































