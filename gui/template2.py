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


root.mainloop()
