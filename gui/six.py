#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font

#
# button = tk.Button(root)
# text box = tk.Entry(root)
# label = tk.Label(root)
#
root = tk.Tk()
root.title('Text Editor')

def menuCommand(action):
    if action == 'N':
        f = messagebox.askyesnocancel('New File', 'Clear Window?')
        if f == True:
            txt.delete('1.0','end')
    elif action == 'O':
        f = filedialog.askopenfilename(filetypes = (
            ('Python Source', '*.py'),
            ('HTML Source', '*.html;*.htm'),
            ('Text Files', '*.txt'),
            ('All Files', '*.*')
            )
                                       )
        if f != '':
            o = open(f, 'r')
            txt.delete('1.0', 'end')
            txt.insert('1.0', o.read())
            o.close()
    elif action == 'S':
        f = filedialog.asksaveasfilename(filetypes = (
            ('Python Source', '*.py'),
            ('HTML Source', '*.html;*.htm'),
            ('Text Files', '*.txt'),
            ('All Files', '*.*')
            )
                                         )
        if f != '':
            o = open(f, 'w')
            o.write(txt.get('1.0', 'end'))
            o.close()

    elif action == 'E':
        f = messagebox.askyesnocancel('Quit', 'Quit Application?')
        if f == True:
            root.destroy()

menu = tk.Menu(root)
fmnu = tk.Menu(menu, tearoff = 0)
fmnu.add_command(label='New', command=lambda: menuCommand('N'))
fmnu.add_command(label='Open', command=lambda: menuCommand('O'))
fmnu.add_command(label='Save', command=lambda: menuCommand('S'))
fmnu.add_separator()
fmnu.add_command(label='Exit', command=lambda: menuCommand('E'))
menu.add_cascade(menu=fmnu, label='File')

root.config(menu = menu)

def updateStats(event):
    t = txt.get('1.0', 'end')
    t = t.replace('\n','')
    c = len(t)
    outStr = 'Statistic\n\n'
    outStr += '{:4>} chars'.format(c)
    l = int(txt.index('end').split('.')[0])-1
    outStr += '\n'
    outStr += '{:4>} lines'.format(l)
    mr = int(txt.index(tk.INSERT).split('.')[0])
    mc = int(txt.index(tk.INSERT).split('.')[1])+1
    outStr += '\n'
    outStr += '[r:{} c:{}]'.format(mr,mc)
    
    s.set(outStr)

txt = scrolledtext.ScrolledText(root)
txt.configure(font = ('Cascadia Code PL', 12, 'normal'))
txt.configure(background = 'black')
txt.configure(foreground = 'yellow')
txt.configure(insertbackground = 'white')
txt.configure(insertwidth = 4)
txt.bind('<KeyRelease>', updateStats)
txt.bind('<Button>', updateStats)
# set the tabstop for the font.
fnt1 = font.Font(font=txt['font'])
tabw = fnt1.measure(' '*4)
txt.configure(tabs=tabw)
txt.grid(row=0, column=0, sticky = 'nsew', padx=5, pady=5)

s = tk.StringVar()
s.set('Statistics')
lbl = tk.Label(root)
lbl.configure(anchor=tk.NW)
lbl.configure(justify=tk.LEFT)
lbl.configure(textvariable = s)
lbl.configure(font = ('Courier New', 11, 'bold'))
lbl.configure(foreground = 'blue')
lbl.configure(relief=tk.SUNKEN)
lbl.grid(row=0, column=1, sticky = 'nsew', padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()
