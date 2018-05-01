from login import nextp
from page2 import main
from tkinter import *
from tkinter import messagebox
def proceed():
    welcome.destroy()
    if(var.get()==1):
        main()
    if(var.get()==2):
        nextp()        
    
welcome = Tk()
welcome.title("WELCOME")
var =IntVar()
lb=Label(welcome, text="WELCOME!!", fg = "blue", bg="yellow",font = "Helvetica 16 bold italic")
lb.pack(pady=20)
lb2=Label(welcome, text="This is a Movie Details & Ticket Booking System", fg = "dark green", bg="yellow", font = "Times 14 bold")
lb2.pack()
lb3=Label(welcome, text="Select desired option and proceed: ", fg = "red",font = "Vrdana 12 italic")
lb3.pack(padx=50, pady=20)
book=Radiobutton(welcome, text="Book Ticket", variable=var, value=1)
book.pack(anchor=W, padx=50)
view=Radiobutton(welcome, text="View Details", variable=var, value=2)
view.pack(anchor=W, padx=50)
btn=Button(welcome,text="PROCEED ->", command=proceed)
btn.pack()
welcome.geometry("500x300")
welcome.mainloop()
