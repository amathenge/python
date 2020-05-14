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

'''
Globals
'''
str1 = tk.StringVar()   # for the edit box.

'''
Callbacks
'''
def drawShape():
    s = str1.get()
    if len(s) < len('type(1,2,3,4)'):
        messagebox.showinfo('Error', "input error: {}".format(s))
    else:
        cmd = s[0:4].lower()
        if cmd not in ('line', 'rect', 'oval', 'poly'):
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        cmd1 = s[4:]
        pos1 = cmd1.find('(')
        if pos1 == -1:
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        pos2 = cmd1.rfind(')')
        if pos2 == -1:
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        # if we're here, we may have good data.
        data = cmd1[pos1+1:pos2]
        messagebox.showinfo('Data', 'you have {}, {}'.format(cmd, data))

frame1 = tk.Frame(root)
frame1.pack(fill = tk.BOTH, expand = True)
frame2 = tk.Frame(root)
frame2.pack(fill = tk.BOTH, expand = True)
frame3 = tk.Frame(root)
frame3.pack(fill = tk.BOTH, expand = True)

# canvas in the first frame
# label with instructions in the second frame
# text box and a single button in the third frame.

c = tk.Canvas(frame1)
c.pack(fill = tk.BOTH, expand = True, padx = 4, pady = 4)
c.config(width = 640, height = 480)
c.config(borderwidth = 0, highlightthickness = 0)

str2 = 'How to draw objects on the canvas above:\n'
str2 += "for a circle:\n  oval: (x,y,r) [where x,y are coordinate, r is radius]\n"
str2 += "for a rect:\n  rect: (x,y,x2,y2) [x,y are top/left and x2,y2 are bottom/right]\n"
str2 += "for a line:\n  line: similar to rect\n"
str2 += "for a polygon:\n  poly: (x,y,x2,y2,x3,y3...) - must be at least 3 pairs\n"
lbl1 = tk.Label(frame2, text = str2)
lbl1.configure(font = ('Courier New', 12, 'normal'))
lbl1.configure(anchor = tk.NW, justify = tk.LEFT, relief = tk.GROOVE, borderwidth = 2)
lbl1.configure(padx = 10, pady = 5)
# when the parent is stretched, the label will stick to the left side.
lbl1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
'''
  fill option: it determines whether to use up more space or keep "one's own" dimensions.
  expand option: it deals with the expansion of parent widget.
'''
txt1 = tk.Entry(frame3, width = 25, textvariable = str1, foreground = 'yellow', background = 'black')
txt1.configure(insertbackground = 'white', insertwidth = 4)
txt1.configure(font = ('Comic Sans', 12, 'normal'))
txt1.pack(side = tk.LEFT, padx = 20, pady = 20)

img = tk.PhotoImage(width = 1, height = 1)
btn1 = tk.Button(frame3, text = " Draw ", image = img, width=100, height=30)
btn1.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn1.configure(foreground = 'blue')
btn1.configure(command = drawShape)
btn1.pack(side = tk.LEFT, padx = 40)

root.mainloop()
