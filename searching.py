from tkinter import *
from tkinter import messagebox

def listfromfile():
    fr = open("movie_details.txt", "r")
    data= fr.readlines()
    innerl=[]
    for i in data:
        innerl.append(i.split("\t"))
    fr.close()
    return innerl

def getvalues(value0):
    list1=listfromfile()
    j=0
    print(value0)
    for i in list1:
       if(value0==i[j]):
           print(i[1:])
           return i[1:]

def find(value0):
    flag=0
    list1=listfromfile()
    for i in list1:
       if(value0==i[0]):
           flag=1
           break
    if(flag==1):
        return True
    else:
        return False

def end():
    search.destroy()
    
def clear():
    s2.set(" ")
    s3.set(" ")
    s4.set(" ")
    s5.set(" ")
    
def tofile(list1, mname):
    fa = open("movie_details.txt", "w")
    n=len(list1)
    for i in range(0,n):
        if(mname==list1[i][0]):
            string = mname + "\t" + t2.get() + "\t"+ t3.get() + "\t" + t4.get() + "\t"+ t5.get() + "\n"
        else:
            string = list1[i][0] + "\t" +list1[i][1] + "\t" +list1[i][2] + "\t" +list1[i][3] + "\t" +list1[i][4]
            fa.write(string)       
    fa.close()
    
def upd():
    if(len(t3.get())and len(t4.get())and len(t5.get())):
        list1=listfromfile()
        m=t1.get()
        tofile(list1, m) 
        messagebox.showinfo("UPDATED", "Record UPDATED successfully!!")
        show()
    else:
        messagebox.showinfo("INVALID", "Field Cannot Be Empty!!")

def update():
    print("Update")
    global t3, t4, t5
    t2=Entry(search,textvariable=s2)
    t2.grid(row=3,column=2)
    t3=Entry(search,textvariable=s3)
    t3.grid(row=4,column=2)
    t4=Entry(search,textvariable=s4)
    t4.grid(row=5,column=2)
    t5=Entry(search,textvariable=s5)
    t5.grid(row=6,column=2)
    upd2=Button(search,text="Are You Sure??", command=upd)
    upd2.grid(row=7,column=1)
    cl=Button(search,text="Clear", command=clear)
    cl.grid(row=7,column=2)

def show():
    print("show")
    l1=getvalues(t1.get())
    global s2, s3, s4, s5, t2
    s2=l1[0]
    s3=l1[1]
    s4=l1[2]
    s5=l1[3]
    l2=Label(search,text="Director's name: ")
    l2.grid(row=3,column=1)
    t2=Label(search,text=s2)
    t2.grid(row=3,column=2)
    l3=Label(search,text="Genre: ")
    l3.grid(row=4,column=1)
    t3=Label(search,text=s3)
    t3.grid(row=4,column=2)
    l4=Label(search,text="Duration of the movie: ")
    l4.grid(row=5,column=1)
    t4=Label(search,text=s4)
    t4.grid(row=5,column=2)
    l5=Label(search,text="Release date: ")
    l5.grid(row=6,column=1)
    t5=Label(search,text=s5)
    t5.grid(row=6,column=2)
    upd=Button(search,text="Update Record", command=update)
    upd.grid(row=7,column=1)

def ch(event):
    if(find(t1.get())):
        show()
    else:
        messagebox.showerror("INVALID", "No Record Found!!")
        s1.set(" ")
###########################################################################
def SEARCH():
    global search
    search=Tk()
    search.title("Search a record")
    l=Label(search,text="Enter the movie you want to search: ")
    l.grid(row=1,column=1,columnspan=2)
    l1=Label(search, text="Movie Name: ")
    l1.grid(row=2,column=1)
    global s1, t1
    s1=StringVar()
    t1=Entry(search,textvariable=s1)
    t1.grid(row=2,column=2)
    t1.focus()
    exit=Button(search,text="Exit",command=end)
    exit.grid(row=1,column=3)
    search.geometry("350x200")
    t1.bind("<Return>", ch)
    search.mainloop()
