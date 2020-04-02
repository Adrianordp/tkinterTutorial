#!/usr/bin/python3
from tkinter import Tk, Label, Button

root = Tk()

def myClick():
    myLabel = Label(root,text='Look! I clicked a button!!')
    myLabel.pack()

# Creating a Label Widget
myButton = Button(root, text="Click me!", command=myClick, fg='blue', bg='#ffffff')
myButton.pack()

root.mainloop()
