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

def keyAction(event):
    print("type: {}".format(event.type))
    print("widget: {}".format(event.widget))
    print("char: {}".format(event.char))
    print("keysym: {}".format(event.keysym))
    print("keycode: {}".format(event.keycode))

root.bind('<KeyPress>', keyAction)

root.mainloop()
