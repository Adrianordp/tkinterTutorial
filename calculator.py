#!/usr/bin/python3
from tkinter import Tk, Label, Button, Entry

f_num = 0
operation = 0

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=30, bg='white',fg='blue',borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

def button_add():
    global f_num, operation
    operation = 0
    f_num = int(e.get())
    e.delete(0,'end')

def button_subtract():
    global f_num, operation
    operation = 1
    f_num = int(e.get())
    e.delete(0,'end')

def button_multiply():
    global f_num, operation
    operation = 2
    f_num = int(e.get())
    e.delete(0,'end')

def button_divide():
    global f_num, operation
    operation = 3
    f_num = int(e.get())
    e.delete(0,'end')

def button_equal():
    global f_num, operation
    s_num = int(e.get())
    e.delete(0,'end')
    
    if operation == 0:
        e.insert(0,f_num+s_num)
    elif operation == 1:
        e.insert(0,f_num-s_num)
    elif operation == 2:
        e.insert(0,f_num*s_num)
    elif operation == 3:
        e.insert(0,f_num/s_num)

def button_clear():
    e.delete(0, 'end')

def button_click(number):
    e.insert('end',number)

button_1 = Button(root, text="1", padx=40,pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40,pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40,pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40,pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40,pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40,pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40,pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40,pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40,pady=20, command=lambda: button_click(0))

button_add      = Button(root, text="+"    , padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-"    , padx=42, pady=20, command=button_subtract)
button_multiply = Button(root, text="*"    , padx=41, pady=20, command=button_multiply)
button_divide   = Button(root, text="/"    , padx=42, pady=20, command=button_divide)
button_equal    = Button(root, text="="    , padx=88, pady=20, command=button_equal)
button_clear    = Button(root, text="Clear", padx=76, pady=20, command=button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


root.mainloop()