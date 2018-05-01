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
    delete.destroy()
    
def proceed():
        list1=listfromfile()
        mname=t1.get()
        fa = open("movie_details.txt", "w")
        n=len(list1)
        for i in range(0,n):
            if(mname==list1[i][0]):
                continue
            else:
                string = list1[i][0] + "\t" +list1[i][1] + "\t" +list1[i][2] + "\t" +list1[i][3] + "\t" +list1[i][4]
            fa.write(string)       
        fa.close()
        messagebox.showinfo("Deleted", "Record deleted successfully!!")

def show():
    print("show")
    l1=getvalues(t1.get())
    global s2, s3, s4, s5, t2
    s2=l1[0]
    s3=l1[1]
    s4=l1[2]
    s5=l1[3]
    l2=Label(delete,text="Director's name: ")
    l2.grid(row=3,column=1)
    t2=Label(delete,text=s2)
    t2.grid(row=3,column=2)
    l3=Label(delete,text="Genre: ")
    l3.grid(row=4,column=1)
    t3=Label(delete,text=s3)
    t3.grid(row=4,column=2)
    l4=Label(delete,text="Duration of the movie: ")
    l4.grid(row=5,column=1)
    t4=Label(delete,text=s4)
    t4.grid(row=5,column=2)
    l5=Label(delete,text="Release date: ")
    l5.grid(row=6,column=1)
    t5=Label(delete,text=s5)
    t5.grid(row=6,column=2)
    dele=Button(delete,text="Are You Sure You want to delete this record??", command=proceed)
    dele.grid(row=7,column=1, columnspan=2)

def ch(event):
    if(find(t1.get())):
        show()
    else:
        messagebox.showerror("INVALID", "No Record Found!!")
        s1.set(" ")
###########################################################################
def DELETE():
    global delete
    delete=Tk()
    delete.title("Delete a record")
    l=Label(delete,text="Enter the movie you want to delete: ")
    l.grid(row=1,column=1,columnspan=2)
    l1=Label(delete, text="Movie Name: ")
    l1.grid(row=2,column=1)
    global s1, t1
    s1=StringVar()
    t1=Entry(delete,textvariable=s1)
    t1.grid(row=2,column=2)
    t1.focus()
    exit=Button(delete,text="Exit",command=end)
    exit.grid(row=1,column=3)
    delete.geometry("350x200")
    t1.bind("<Return>", ch)
    delete.mainloop()
