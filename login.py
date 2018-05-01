from details import getdet
from tkinter import *
from tkinter import messagebox
import time

def clear():
    s1.set(" ")
    s2.set(" ")
    
def check():
    if(len(t1.get()) and len(t2.get())):
        print("CHECKED")
        time.sleep(2)
        login.destroy()
        getdet()
    else:
        messagebox.showinfo("INVALID", "Field Cannot Be Empty!!")
       

def nextp():
    global login
    login = Tk()
    login.title("LOGIN PAGE")
    l1=Label(login,text="Username: ")
    l2=Label(login,text="Password: ")
    global s1, s2, t1, t2
    s1=StringVar()
    s2=StringVar()
    t1=Entry(login,textvariable=s1)
    t2=Entry(login,textvariable=s2)
    t1.focus()
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    t1.grid(row=1,column=2)
    t2.grid(row=2,column=2)
    sub=Button(login,text="Submit",command=check)
    sub.grid(row=3,column=1)
    cl=Button(login,text="Clear", command=clear)
    cl.grid(row=3,column=2)
    login.mainloop()
