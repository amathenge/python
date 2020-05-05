#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk

root = tk.Tk()
# labels.

lbl1 = tk.Label(root, text='Label 1:')
lbl1.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl1.configure(foreground = 'blue')
lbl1.configure(background = 'grey')
lbl1.configure(width=10)
lbl1.configure(anchor='e')
lbl1.grid(row=0, column=0, pady=2, padx=5)

lbl2 = tk.Label(root, text='Label 2:')
lbl2.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl2.configure(foreground = 'white')
lbl2.configure(background = 'black')
lbl2.configure(width=10)
lbl2.configure(anchor='e')
lbl2.grid(row=1, column=0, pady=2, padx=5)

lbl3 = tk.Label(root, text='Label 3:')
lbl3.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl3.configure(foreground = 'red')
lbl3.configure(background = 'yellow')
lbl3.configure(width=10)
lbl3.configure(anchor='e')
lbl3.grid(row=3, column=0, pady=2, padx=5)

lbl4 = tk.Label(root, text='Label 4:')
lbl4.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl4.configure(foreground = 'yellow')
lbl4.configure(background = 'blue')
lbl4.configure(width=10)
lbl4.configure(anchor='e')
lbl4.grid(row=4, column=0, pady=2, padx=5)

# Text boxes

txt1 = tk.Entry(root)
txt1.configure(font = ('Cascadia Code PL', 11, 'normal'), foreground = 'white', background='black')
txt1.configure(insertbackground='yellow', insertwidth=8)
txt1.grid(row=0, column=1, padx=5)

txt1.focus()

btn1 = tk.Button(root)
btn1.configure(text='Quit', anchor='center')
btn1.configure(command = root.destroy)
btn1.configure(padx=10, width=15)
btn1.grid(row=5, column=1, pady=2, padx=10, sticky=tk.E)

def showText():
    txt = txt1.get()
    messagebox.showinfo(title='Entry Text', message=txt)

btn2 = tk.Button(root)
btn2.configure(text='Read Text', anchor='center')
btn2.configure(padx=10, width=15)
btn2.configure(command = showText)
btn2.grid(row=5,column=0,padx=10, pady=2, sticky=tk.W)


root.mainloop()
