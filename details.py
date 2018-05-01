from adding import ADD
from deleting import DELETE
from searching import SEARCH
from viewrec import VIEW
from tkinter import *
from tkinter import messagebox

def adding():
    ADD()

def delete():
    DELETE()

def view():
    VIEW()
    
def search():
    SEARCH()
    print("search")

def update():
    SEARCH()
    print("update")

def end():
    details.destroy()

###########################################################################
def getdet():
    global details
    details = Tk()
    details.title("DETAILS PAGE")
    l1=Label(details,text="Select your desired option:")
    l1.grid(row=1,column=1,columnspan=2)
    add=Button(details, text="Add a record", command=adding)
    add.grid(row=2,column=1)
    dlt=Button(details, text="Delete a record", command=delete)
    dlt.grid(row=2,column=3)
    viewr=Button(details, text="View records", command=view)
    viewr.grid(row=3,column=1, columnspan=3)
    srch=Button(details, text="Search record", command=search)
    srch.grid(row=4,column=1)
    updt=Button(details, text="Update record", command=update)
    updt.grid(row=4,column=3)
    exit=Button(details,text="Exit",command=end)
    exit.grid(row=5,column=2)
    details.geometry("350x200")
    details.mainloop()
