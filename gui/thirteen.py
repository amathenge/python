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


origin = None
lastPoint = None
finalpoint = None


'''
def mouseClick(event):
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
'''

def setOrigin(event):
    global origin
    global lastPoint
    origin = event
    lastPoint = origin

def drawLine(event):
    global origin
    global lastPoint
    c.create_line(origin.x, origin.y, lastPoint.x, lastPoint.y, fill = 'white')
    c.create_line(origin.x, origin.y, event.x, event.y, fill = 'black')
    lastPoint = event

def closeLine(event):
    global origin
    global lastPoint
    c.create_line(origin.x, origin.y, lastPoint.x, lastPoint.y, fill = 'white')
    c.create_line(origin.x, origin.y, event.x, event.y, fill = 'black')

c = tk.Canvas(root)
c.config(width = 640, height = 480)
c.config(borderwidth = 0, highlightthickness = 0)
c.config(background = 'white')
c.bind('<ButtonPress-1>', setOrigin)
c.bind('<B1-Motion>', drawLine)
c.bind('<ButtonRelease-1>', closeLine)

c.pack()

# button presses on the canvas



root.mainloop()
