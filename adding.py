from tkinter import *
from tkinter import messagebox
import os.path

def getvalues(value0):
    if(os.path.exists("movie_details.txt")):
        f=open("movie_details.txt")
        re=f.read(1)
        if(not re):
            f.close()
            return False
        else:
            fr = open("movie_details.txt", "r")
            data= fr.readlines()
            list1=[]
            for i in data:
                list1.append(i.split("\t"))
            fr.close()
            flag=0
            print(value0)
            for i in list1:
               if(value0==i[0]):
                   flag=1
                   break
            if(flag==1):
                return True
            else:
                return False
    else:
        return False

def end():
    insert.destroy()
    
def clear():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    t1.focus()

def finish():
    l2.destroy()
    t2.destroy()
    l3.destroy()
    t3.destroy()
    l4.destroy()
    t4.destroy()
    l5.destroy()
    t5.destroy()

def tofile():
    fa = open("movie_details.txt", "a")
    string = t1.get() + "\t" + t2.get() + "\t"+ t3.get() + "\t" + t4.get() + "\t"+ t5.get() + "\n"
    fa.write(string)
    fa.close()
    
def add():
    if(len(t1.get())and len(t2.get())and len(t3.get())and len(t4.get())and len(t5.get())):
        tofile() 
        messagebox.showinfo("ADDED", "Record added successfully!!")
        clear()
        finish()
    else:
        messagebox.showinfo("INVALID", "Field Cannot Be Empty!!")    

def show():
    print("show")
    global s2, s3, s4, s5, t2, t3, t4, t5, l2, l3, l4, l5
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()
    l2=Label(insert,text="Director's name: ")
    l2.grid(row=3,column=1)
    t2=Entry(insert,textvariable=s2)
    t2.grid(row=3,column=2)
    t2.focus()
    l3=Label(insert,text="Genre: ")
    l3.grid(row=4,column=1)
    t3=Entry(insert,textvariable=s3)
    t3.grid(row=4,column=2)
    l4=Label(insert,text="Duration of the movie: ")
    l4.grid(row=5,column=1)
    t4=Entry(insert,textvariable=s4)
    t4.grid(row=5,column=2)
    l5=Label(insert,text="Release date: ")
    l5.grid(row=6,column=1)
    t5=Entry(insert,textvariable=s5)
    t5.grid(row=6,column=2)
    ad=Button(insert,text="Add Record", command=add)
    ad.grid(row=7,column=1)

def ch(event):
    if(getvalues(t1.get())):
        print("else")
        messagebox.showerror("INVALID", "Record already exists!!")
        s1.set(" ")
    else:
        show()
###########################################################################
def ADD():
    global insert
    insert=Tk()
    insert.title("Add a record")
    l=Label(insert,text="Enter the details for the new record: ")
    l.grid(row=1,column=1,columnspan=2)
    l1=Label(insert, text="Movie Name: ")
    l1.grid(row=2,column=1)
    global s1, t1
    s1=StringVar()
    t1=Entry(insert,textvariable=s1)
    t1.grid(row=2,column=2)
    cl=Button(insert,text="Clear", command=clear)
    cl.grid(row=7,column=2)
    exit=Button(insert,text="Exit",command=end)
    exit.grid(row=1,column=3)
    insert.geometry("350x200")
    t1.bind("<Return>", ch)
    insert.mainloop()
