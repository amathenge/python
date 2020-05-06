#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
import tkinter as tk

#
# button = tk.Button(root)
# text box = tk.Entry(root)
# label = tk.Label(root)
#
root = tk.Tk()
c = tk.Canvas(root)
c.pack()
c.config(width = 640, height = 480)
c.config(borderwidth = 0, highlightthickness = 0)
l1 = c.create_line(20,20,630,470, fill = 'blue', width = 2)
l2 = c.create_line(1, 1, 639, 1, fill = 'blue', width = 1)
l3 = c.create_line(1, 1, 1, 479, fill = 'blue', width = 1)
l4 = c.create_line(1, 479, 639, 479, fill = 'blue', width = 1)
l5 = c.create_line(639, 1, 639, 479, fill = 'blue', width = 1)

lbl1 = tk.Label(c)
str1 = tk.StringVar()
str1.set('placeholder - 1234567890\nSecond Line\nThird Line')
lbl1.configure(anchor = tk.NW)
lbl1.configure(justify = tk.LEFT)
lbl1.configure(font = ('Courier New', 10, 'bold'))
lbl1.configure(textvariable = str1, width = 77, height = 3)
lbl1.configure(relief = 'sunken', borderwidth = 2)
lbl1.place(x = 10,y = 420)

l6 = c.create_line(1, 1, 639, 479, fill = 'green', width = 1)
l7 = c.create_line(639, 1, 1, 479, fill = 'green', width = 1)

tmp = c.coords(l1)
str1.set('Coords of line were: {}'.format(tmp))
c.coords(l1, (640//4), (480//2), (640//4)*3, (480//2))
tmp = c.coords(l1)
tmp2 = str1.get()
str1.set('New={}\nold={}'.format(tmp, tmp2))
c.itemconfigure(l1, fill = 'red')

l8 = c.create_line(5, 5, 635, 5, 635, 475, 5, 475, 5, 5)
c.itemconfigure(l8, fill = 'black', width = 2)

l9 = c.create_line(50, 50, 590, 50, 590, 430, 50, 430, 50, 50)
c.itemconfigure(l9, fill = 'green', width = 2)

l10 = c.create_line(100, 100, 540, 100, 540, 380, 100, 380, 100, 100)
c.itemconfigure(l10, fill = 'blue', width = 2)

l11 = c.create_line((640//4), (480//2), (640//2), (480//4), (640//4)*3, (480//2))
c.itemconfigure(l11, smooth = True)
# c.itemconfigure(l11, splinesteps = 200)
l12 = c.create_line((640//4), (480//2), (640//2), (480//4)*3, (640//4)*3, (480//2))
c.itemconfigure(l12, smooth = True)

root.mainloop()
