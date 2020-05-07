#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
import tkinter as tk
from tkinter import messagebox
#
# button = tk.Button(root)
# text box = tk.Entry(root)
# label = tk.Label(root)
#
root = tk.Tk()
# the following two lines below were a mistake - the canvas and buttons below
# were not showing. Better to size the canvas - and the window will resize to
# show the canvas.
#
# root.geometry('640x480+20+20')
# root.minsize(640,480)

# THE MENU

def menuCommand(action):
    if action == 'E':
        root.destroy()
    else:
        messagebox.showinfo('Menu Item Pressed', 'You Pressed a Menu Item')

menu = tk.Menu(root)
fmnu = tk.Menu(menu, tearoff = 0)
fmnu.add_command(label='New', command=lambda: menuCommand('N'))
fmnu.add_command(label='Open', command=lambda: menuCommand('O'))
fmnu.add_command(label='Save', command=lambda: menuCommand('S'))
fmnu.add_separator()
fmnu.add_command(label='Exit', command=lambda: menuCommand('E'))
menu.add_cascade(menu=fmnu, label='File')
root.config(menu = menu)

# TWO FRAMES

frame1 = tk.Frame(root)
frame1.pack(fill = tk.BOTH, expand = True)

frame2 = tk.Frame(root)
frame2.pack(fill = tk.BOTH, expand = True)

# THE CANVAS

c = tk.Canvas(frame1)
c.pack(fill = tk.BOTH, expand = True, padx = 4, pady = 4)
c.config(width = 640, height = 480)
c.config(borderwidth = 0, highlightthickness = 0)
# line1 = c.create_line(0, 0, 640, 480)
# c.itemconfig(line1, fill = 'blue', width = 2)
rect1 = c.create_rectangle(1,1,639,479, outline = 'blue', width = 2)

# GLOBALS - Hold Canvas Items
cItems = {}
str1 = tk.StringVar()

def getCoords():
    c = str1.get()
    c = c.split(',')
    # remove whitespace
    totalItems = len(c)
    counter = 0
    errors = 0
    while counter < totalItems:
        try:
            c[counter] = int(c[counter])
        except:
            errors += 1
        counter += 1
    if errors > 0:
        return None
    elif (len(c) % 2) != 0:
        return None
    else:
        return c

def getColourWidth():
    c = str1.get()
    c = c.split(',')
    if len(c) != 2:
        return None
    c[0] = c[0].strip()     # object colour
    c[1] = c[1].strip()     # object width

    return c


# THE BUTTONS

def addLine():
    coords = getCoords()
    if coords == None:
        return
    # lines could be formed from more than one segment.
    while len(coords) >= 4:
        tmp = c.create_line(coords[0], coords[1], coords[2], coords[3])
        c.itemconfig(tmp, fill = 'blue', width = 2)
        cItems['line{}'.format(len(cItems))] = tmp
        coords = coords[2:]

def formatLines():
    cw = getColourWidth()
    if cw != None:
        for item in cItems:
            if 'line' in item:
                c.itemconfig(cItems[item], fill = cw[0], width=cw[1])

img = tk.PhotoImage(width = 1, height = 1)
btn1 = tk.Button(frame2, text = "line", image = img, width=50, height=50)
btn1.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn1.configure(foreground = 'blue')
btn1.configure(command = addLine)
btn1.grid(row = 0, column = 0)

btn2 = tk.Button(frame2, text = "rect", image = img, width = 50, height = 50)
btn2.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn2.configure(foreground = 'blue')
btn2.grid(row = 0, column = 1)

btn3 = tk.Button(frame2, text = "oval", image = img, width = 50, height = 50)
btn3.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn3.configure(foreground = 'blue')
btn3.grid(row = 0, column = 2)

btn4 = tk.Button(frame2, text = "poly", image = img, width = 50, height = 50)
btn4.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn4.configure(foreground = 'blue')
btn4.grid(row = 0, column = 3)

txt1 = tk.Entry(frame2, width = 25, textvariable = str1, foreground = 'yellow', background = 'black')
txt1.configure(insertbackground = 'white', insertwidth = 4)
txt1.configure(font = ('Comic Sans', 12, 'normal'))
txt1.grid(row = 0, column = 4, padx = 10)

lbl1 = tk.Label(frame2, text = 'Coordinate pairs\nfor rendered objects')
lbl1.configure(font = ('Comic Sans', 10, 'normal'))
lbl1.configure(anchor = tk.E, justify = tk.LEFT, relief = tk.GROOVE, borderwidth = 2)
lbl1.configure(padx = 10, pady = 5)
lbl1.grid(row = 0, column = 5)

# colour changes
btn5 = tk.Button(frame2, text = "c/w", image = img, width=50, height=50)
btn5.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn5.configure(foreground = 'blue')
btn5.configure(command = formatLines)
btn5.grid(row = 1, column = 0)

root.mainloop()
