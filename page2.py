from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time

def booking():
    if (city.current()!=0):
        print("Booking...")
        time.sleep(1)
        print("Booking Confirmed")
        messagebox.showinfo("Confirmed", "Booking Confirmed!!")
        page2.destroy()
    else:
        print("Select correct option!!")

def listfromfile(filename):
    fr = open(filename, "r")
    data= fr.readlines()
    innerl=[]
    for i in data:
        innerl.append(i.split())
    print(innerl)
    fr.close()
    return innerl

def getvalues(list1,value0):
    j=0
    print(value0)
    for i in list1:
       if(value0==i[j]):
           print(i[1:])
           return i[1:]
        
def gettheatres(event):
    if (city.current()!= 0):
        list1 = listfromfile("city-theatre.txt")
        #t = tuple(getvalues(list1,city.get()))
        l2=Label(page2,text="Select Your Theatre: ")
        th= ("Choose-Theatre",)+ tuple(getvalues(list1,city.get()))
        print(th)
        global theatre
        theatre=Combobox(page2,state="readonly")
        theatre.config(values=th)
        theatre.current(0)
        theatre.bind("<<ComboboxSelected>>", getmovies)
        l2.grid(row=2,column=1)
        theatre.grid(row=2,column=2)
    else:
        print("Select correct option!!")
        messagebox.showerror("ALERT", "Select correct option!!")

def getmovies(event):
    if (theatre.current()!= 0):
        list1 = listfromfile("theatre-movie.txt")
        #t1 = tuple(getvalues(list1,theatre.get()))
        l3=Label(page2,text="Select Your Movie: ")
        th= ("Choose-Movie",)+ tuple(getvalues(list1,theatre.get()))
        print(th)
        global movies
        movies=Combobox(page2,state="readonly")
        movies.config(values=th)
        movies.current(0)
        movies.bind("<<ComboboxSelected>>", gettimings)
        l3.grid(row=3,column=1)
        movies.grid(row=3,column=2)
    else:
        print("Select correct option!!")
        messagebox.showinfo("ALERT", "Select correct option!!")

def gettimings(event):
    if (movies.current()!= 0):
        list1 = listfromfile("timings.txt")
        l2 = getvalues(list1,movies.get())
        print(l2)
        l4=Label(page2,text="Timings: ")
        l4.grid(row=4,column=1,columnspan=3)        
        j,k = 5,1
        for i in l2:
            l=Label(page2, text=i)
            l.grid(row=j, column=k)
            k= k+1
            if(k==4):
                j=j+1
                k=1
    else:
        print("Select correct option!!")
        messagebox.showinfo("ALERT", "Select correct option!!")

###################################################
def main():
    global page2, city
    page2=Tk()
    page2.title("PAGE2")
    l1=Label(page2,text="Enter Your City: ")
    city=Combobox(page2, state="readonly")
    city['values']= ("Select-Your-City", "Ahmedabad", "Bengluru", "Chandigarh", "Chennai", "Kolkata", "Mumbai", "NCR-Delhi", "Pune", "Surat")
    city.current(0)
    city.bind("<<ComboboxSelected>>", gettheatres)
    l1.grid(row=1,column=1)
    city.grid(row=1,column=2)
    b1=Button(page2,text="Proceed to book ->",command=booking)
    b1.grid(row=7,column=1,columnspan=2)
    page2.mainloop()
