from tkinter import *
from tkinter import ttk
import random
root=Tk()
root.geometry("1000x1000")
root.config(bg="teal")
rad=StringVar(root," ")
firstname=StringVar()
lastname=StringVar()
def insertion():
    #Label widget
    full=Label(root,text="Full Name:",bg="white")
    full.place(x=460,y=60)
    FirstName=firstname.get()
    LastName=lastname.get()
    fir=Label(root,text=FirstName,font=('Calibri',12,'bold'),bg="white")
    las=Label(root,text=LastName,font=('Calibri',12,'bold'),bg="white")
    firstname.set("")
    lastname.set("")
    fir.place(x=530,y=60)
    las.place(x=600,y=60)
    gender=Label(root,text="Gender:",bg="white")
    gender.place(x=460,y=100)
    pri=Label(root,bg="white",text='')
    pri.place(x=530,y=100)
    pri.config(str(rad.get()))

def deletion():
    for i in list2:
        list2.delete(END,i)

def themecolor():
    n=random.randint(1,2) 
    if(n==1):
        list2.config(bg="lightpink")
    if(n==2):
        list2.config(bg="lightblue")

#ListBox widget
list1 = Listbox(root,width=30,height=18,font=("Arail", 14))
list2 = Listbox(root,width=30,height=18,font=("Arail", 14))
list1.place(x=10,y=10)
list2.place(x=450,y=10)

#Label widget
first=Label(root,text="First Name:",bg="white",font=("Arial",10,"bold"))
first.place(x=20,y=20)
last=Label(root,text="Last Name:",bg="white",font=("Arial",10,"bold"))
last.place(x=20,y=50)
gen=Label(root,text="Gender:",bg="white",font=("Arial",10,"bold"))
gen.place(x=20,y=80)
lang=Label(root,text="Languages:",bg="white",font=("Arial",10,"bold"))
lang.place(x=20,y=110)
email=Label(root,text="Email:",bg="white",font=("Arial",10,"bold"))
email.place(x=20,y=140)
add=Label(root,text="Address:",bg="white",font=("Arial",10,"bold"))
add.place(x=20,y=170)
state=Label(root,text="State:",bg="white",font=("Arial",10,"bold"))
state.place(x=20,y=330)
zipcode=Label(root,text="Zip:",bg="white",font=("Arial",10,"bold"))
zipcode.place(x=20,y=360)
card=Label(root,text="Credit Card Type:",bg="white",font=("Arial",10,"bold"))
card.place(x=20,y=390)
bill=Label(root,text="Billing Records",width=30,bg="grey",font=("Arial",15))
bill.place(x=450,y=10)
#Entry widget
fent=Entry(root,textvariable=firstname)
fent.place(x=140,y=20)
lent=Entry(root,textvariable=lastname)
lent.place(x=140,y=50)
#Radiobutton widget
male=Radiobutton(root,text="Male",value="Male",bg="white",variable=rad)
male.place(x=140,y=80)
female=Radiobutton(root,text="Female",value="Female",bg="white",variable=rad)
female.place(x=190,y=80)
#Checkbutton widget
tel=Checkbutton(root,text="Telugu",onvalue=0,offvalue=1,bg="white")
tel.place(x=140,y=110)
eng=Checkbutton(root,text="English",onvalue=0,offvalue=1,bg="white")
eng.place(x=200,y=110)
hin=Checkbutton(root,text="Hindi",onvalue=0,offvalue=1,bg="white")
hin.place(x=260,y=110)
#Label widget
eent=Entry(root)
eent.place(x=140,y=140)
#Listbox widget & scrollbar widget
scrollbar = Scrollbar(root, width=20,orient=VERTICAL)
scrollbar.place(x=320,y=170)
li = Text(root,width=16,height=6,font=("Arail", 14),yscrollcommand=scrollbar.set)
li.place(x=140,y=170)
#combobox widget
state=ttk.Combobox(root,values=["Choose State","Gujarat","Rajasthan","Maharashtra"],width=17)
state.place(x=140,y=330)
#Label widget
zent=Entry(root)
zent.place(x=140,y=360)
#combobox widget
card=ttk.Combobox(root,values=["Choose Credit Card","Visa","MasterCard"],width=20)
card.place(x=140,y=390)

#Button widget
insert=Button(root,text="Insert",width=7,font=("Arial",10,"bold"),command=insertion)
insert.place(x=370,y=95)
delete=Button(root,text="Delete",width=7,font=("Arial",10,"bold"),command=deletion)
delete.place(x=370,y=150)
theme=Button(root,text="Theme",width=7,font=("Arial",10,"bold"),command=themecolor)
theme.place(x=370,y=205)
root.mainloop()
