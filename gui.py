from tkinter import *

w = Tk()
w.title("My application")
w.geometry("600x300")
w.configure(bg="aqua")

def multiply():
    x1 = int(E1.get())
    x2 = int(E2.get())
    p = x1 * x2
    var.set(p)

def clear():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)

var = StringVar()
l1 = Label(w,text="Quantity",bg="aqua")
l2 = Label(w,text="Price",bg="aqua")
l3 = Label(w,text="Total",bg="aqua")
l1.grid(row = 1, sticky=W)
l2.grid(row = 2, sticky=W)
l3.grid(row = 3, sticky=W)

E1=Entry(w)
E2=Entry(w)
E3=Entry(w, text="", textvariable=var)

#position entries
E1.grid(row=1,column=1)
E2.grid(row=2, column=1)
E3.grid(row=3, column=1)

# Create and position buttons
B1 = Button(w,text="calculate", command=multiply)
B2 = Button(w, text="clear", command=clear)

B1.grid(row="4", column="0")
B2.grid(row="4", column="1")

w.mainloop()




