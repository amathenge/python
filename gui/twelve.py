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

def mouseClick(event):
    global prev
    prev = event
    print("type: {}".format(event.type))
    print("widget: {}".format(event.widget))
    print("mouse num: {}".format(event.num))
    # these coordinates are relative to the canvas.
    print("x: {}".format(event.x))
    print("y: {}".format(event.y))
    # these coordinates are relative to the entire screen.
    print("x_root: {}".format(event.x_root))
    print("y_root: {}".format(event.y_root))

def draw(event):
    global prev
    c.create_line(prev.x, prev.y, event.x, event.y)
    prev = event

c = tk.Canvas(root)
c.config(width = 640, height = 480)
c.config(borderwidth = 0, highlightthickness = 0)
c.bind('<ButtonPress>', mouseClick)
c.bind('<B1-Motion>', draw)

c.pack()

# button presses on the canvas



root.mainloop()
