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

r1 = c.create_rectangle(5, 5, 635, 475)
c.itemconfigure(r1, outline = 'blue', width = 2)

o1 = c.create_oval(10, 10, 630, 470)
c.itemconfigure(o1, outline = 'orange', width = 2)

a1 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a1, outline = 'red', width = 2)
c.itemconfigure(a1, start = 1, extent = 43)
a2 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a2, outline = 'red', width = 2)
c.itemconfigure(a2, start = 46, extent = 43)
a3 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a3, outline = 'red', width = 2)
c.itemconfigure(a3, start = 91, extent = 43)
a4 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a4, outline = 'red', width = 2)
c.itemconfigure(a4, start = (90+45+1), extent = 43)
a5 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a5, outline = 'red', width = 2)
c.itemconfigure(a5, start = 181, extent = 43)
a6 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a6, outline = 'red', width = 2)
c.itemconfigure(a6, start = (180+46), extent = 43)
a7 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a7, outline = 'red', width = 2)
c.itemconfigure(a7, start = 271, extent = 43)
a8 = c.create_arc(20, 20, 620, 460)
c.itemconfigure(a8, outline = 'red', width = 2)
c.itemconfigure(a8, start = (270+46), extent = 43)

p1 = c.create_polygon(10, 240, (640//6), (480//6), 320, 10,
                      (640//6)*5, (480//6), 630, 240,
                      (640//6)*5, (480//6)*5, 320, 470,
                      (640//6), (480//6)*5, 10, 240)
c.itemconfigure(p1, outline = 'blue', width = 2, fill = '')
p2 = c.create_polygon(50, 240, (640//6)+40, (480//6)+40, 320, 50,
                      ((640//6)*5)-40, (480//6)+40, 630-40, 240,
                      ((640//6)*5)-40, ((480//6)*5)-40, 320, 430,
                      (640//6)+40, ((480//6)*5)-40, 50, 240)
c.itemconfigure(p2, outline = 'blue', width = 2, fill = '')

t1 = c.create_text(320, 240, text = 'Python Tkinter')
c.itemconfigure(t1, font = ('Cascadia Code PL', 32, 'bold'))
img1 = tk.PhotoImage(file = "C:\\Users\\andrew\\Pictures\\logo-512.png")
img1 = img1.subsample(2, 2)
i1 = c.create_image(320, 240, image = img1)
c.lift(t1)
c.lower(i1)

root.mainloop()
