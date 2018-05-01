from tkinter import *
i=0
def listfromfile():
    global fr
    fr = open("movie_details.txt", "r")
    data= fr.readlines()
    innerl=[]
    for i in data:
        innerl.append(i.split("\t"))
    return innerl

def end():
    view.destroy()    

def first():
    print("first record")
    l1=listfromfile()
    s1=l1[0][0]
    s2=l1[0][1]
    s3=l1[0][2]
    s4=l1[0][3]
    s5=l1[0][4]
    t1=Label(view,text=s1)
    t1.grid(row=2,column=3)
    t2=Label(view,text=s2)
    t2.grid(row=3,column=3)
    t3=Label(view,text=s3)
    t3.grid(row=4,column=3)
    t4=Label(view,text=s4)
    t4.grid(row=5,column=3)
    t5=Label(view,text=s5)
    t5.grid(row=6,column=3)
    fr.close()

def nextr():
    print("next record")
    l1=listfromfile()
    print(l1)
    n=len(l1)
    global i
    if(i<=n-1):
        s1=(l1[i][0])
        s2=(l1[i][1])
        s3=(l1[i][2])
        s4=(l1[i][3])
        s5=(l1[i][4])
        t1=Label(view,text=s1)
        t1.grid(row=2,column=3)
        t2=Label(view,text=s2)
        t2.grid(row=3,column=3)
        t3=Label(view,text=s3)
        t3.grid(row=4,column=3)
        t4=Label(view,text=s4)
        t4.grid(row=5,column=3)
        t5=Label(view,text=s5)
        t5.grid(row=6,column=3)
        i=i+1
        fr.close()
    else:
        i=0
        nextr()
        
def last():
    print("last record")
    l1=listfromfile()
    n=len(l1)
    s1=l1[n-1][0]
    s2=l1[n-1][1]
    s3=l1[n-1][2]
    s4=l1[n-1][3]
    s5=l1[n-1][4]
    t1=Label(view,text=s1)
    t1.grid(row=2,column=3)
    t2=Label(view,text=s2)
    t2.grid(row=3,column=3)
    t3=Label(view,text=s3)
    t3.grid(row=4,column=3)
    t4=Label(view,text=s4)
    t4.grid(row=5,column=3)
    t5=Label(view,text=s5)
    t5.grid(row=6,column=3)
    fr.close()

###########################################################################
def VIEW():
    global view
    view=Tk()
    view.title("View a record")
    global s1, s2, s3, s4, s5
    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()
    l=Label(view,text="View All Records Here: ")
    l.grid(row=1,column=1,columnspan=3)
    l1=Label(view, text="Movie Name: ")
    l1.grid(row=2,column=2)
    l2=Label(view,text="Director's name: ")
    l2.grid(row=3,column=2)
    l3=Label(view,text="Genre: ")
    l3.grid(row=4,column=2)
    l4=Label(view,text="Duration: ")
    l4.grid(row=5,column=2)
    l5=Label(view,text="Release date: ")
    l5.grid(row=6,column=2)
    firstr=Button(view, text="View First record", command=first)
    firstr.grid(row=7,column=1)
    lastr=Button(view, text="View Last record", command=last)
    lastr.grid(row=7,column=3)
    nextrec=Button(view, text="View Next record", command=nextr)
    nextrec.grid(row=7,column=2)
    exit=Button(view,text="Exit",command=end)
    exit.grid(row=1,column=4)
    view.geometry("350x200")
    view.mainloop()
