#!/usr/bin/python3
from tkinter import Tk, Label, Button, Entry

root = Tk()

e = Entry(root, width=50,bg='white',fg='blue',borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    hello = "Hello " + e.get()+"!"
    myLabel = Label(root,text=hello)
    myLabel.pack()

# Creating a Label Widget
myButton = Button(root, text="Enter your name", command=myClick, fg='blue', bg='#ffffff')
myButton.pack()

root.mainloop()