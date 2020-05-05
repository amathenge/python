#!/usr/bin/env python
#
# Calculator GUI
#
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tony's Calculator")
# root.geometry('400x400+0+0')
root.minsize(height=200, width=200) # should change this when app is ready.

txt1 = tk.Entry(root)
txt1.configure(font = ('Cascadia Code PL', 12, 'normal'))
txt1.configure(foreground='yellow', background='black')
txt1.configure(insertbackground='blue', insertwidth=8)
# txt1.configure(state='disabled')
txt1.grid(row=0, column=0, columnspan=3, sticky=tk.E+tk.W+tk.S+tk.N, padx=5, pady=5)

def buildCommand(item):
    txt = txt1.get()
    txt += str(item)
    txt1.delete(0,tk.END)
    txt1.insert(0, txt)

def doMath():
    try:
        res = eval(txt1.get())
        res = str(res)
    except ZeroDivisionError:
        res = 'Error: [zero division]'
    except:
        res = 'Error: [Syntax]'
    txt = txt1.get()
    txt += '=' + res
    txt1.delete(0, tk.END)
    txt1.insert(0, txt)

# memory buffer stuff.
# globals are bad, but we'll use them
mem = tk.StringVar()
mem.set('')

def memAction(action):
    if action == 'M':
        txt = txt1.get()
        # remove the sum, if it's there
        while '=' in txt:
            txt = txt[0:txt.rfind('=')]
        mem.set(txt)
    elif action == 'M+':
        tmp1 = mem.get()
        tmp2 = txt1.get()
        while '=' in tmp2:
            tmp2 = tmp2[0:tmp2.rfind('=')]
        tmp3 = tmp1 + '+(' + tmp2 + ')'
        mem.set(tmp3)
    elif action == 'CM':
        mem.set('')
    elif action == 'CA':
        mem.set('')
        txt1.delete(0, tk.END)
    elif action == 'MG':
        txt1.delete(0, tk.END)
        txt1.insert(0, mem.get())
    else:
        pass

def keyAction(event):
    if event.keysym == 'Return':
        doMath()

def keyMemory(event):
    memAction('M+')

def keyClear(event):
    memAction('CA')

root.bind('<KeyPress>', keyAction)
root.bind('<Control-m>', keyMemory)
root.bind('<Control-c>', keyClear)

# equals button - next to entry box
# need pixel heights...
img1 = tk.PhotoImage(width=1, height=1)
btn1 = tk.Button(root, text = '=', image=img1, compound='center')
btn1.configure(width=50, height=50)
btn1.configure(command=doMath)
btn1.grid(row=0, column=3, padx=5, pady=5)

# other buttons
btn2 = tk.Button(root, text='1', image=img1, compound='center')
btn2.configure(width=50, height=50)
btn2.configure(command=lambda:buildCommand('1'))
btn2.grid(row=1, column=0, padx=5, pady=5)

btn3 = tk.Button(root, text='2', image=img1, compound='center')
btn3.configure(width=50, height=50)
btn3.configure(command=lambda:buildCommand('2'))
btn3.grid(row=1, column=1, padx=5, pady=5)

btn4 = tk.Button(root, text='3', image=img1, compound='center')
btn4.configure(width=50, height=50)
btn4.configure(command=lambda:buildCommand('3'))
btn4.grid(row=1, column=2, padx=5, pady=5)

btn5 = tk.Button(root, text='+', image=img1, compound='center')
btn5.configure(width=50, height=50)
btn5.configure(command=lambda:buildCommand('+'))
btn5.grid(row=1, column=3, padx=5, pady=5)

btn6 = tk.Button(root, text='4', image=img1, compound='center')
btn6.configure(width=50, height=50)
btn6.configure(command=lambda:buildCommand('4'))
btn6.grid(row=2, column=0, padx=5, pady=5)

btn7 = tk.Button(root, text='5', image=img1, compound='center')
btn7.configure(width=50, height=50)
btn7.configure(command=lambda:buildCommand('5'))
btn7.grid(row=2, column=1, padx=5, pady=5)

btn8 = tk.Button(root, text='6', image=img1, compound='center')
btn8.configure(width=50, height=50)
btn8.configure(command=lambda:buildCommand('6'))
btn8.grid(row=2, column=2, padx=5, pady=5)

btn9 = tk.Button(root, text='-', image=img1, compound='center')
btn9.configure(width=50, height=50)
btn9.configure(command=lambda:buildCommand('-'))
btn9.grid(row=2, column=3, padx=5, pady=5)

btn10 = tk.Button(root, text='7', image=img1, compound='center')
btn10.configure(width=50, height=50)
btn10.configure(command=lambda:buildCommand('7'))
btn10.grid(row=3, column=0, padx=5, pady=5)

btn11 = tk.Button(root, text='8', image=img1, compound='center')
btn11.configure(width=50, height=50)
btn11.configure(command=lambda:buildCommand('8'))
btn11.grid(row=3, column=1, padx=5, pady=5)

btn12 = tk.Button(root, text='9', image=img1, compound='center')
btn12.configure(width=50, height=50)
btn12.configure(command=lambda:buildCommand('9'))
btn12.grid(row=3, column=2, padx=5, pady=5)

btn13 = tk.Button(root, text='*', image=img1, compound='center')
btn13.configure(width=50, height=50)
btn13.configure(command=lambda:buildCommand('*'))
btn13.grid(row=3, column=3, padx=5, pady=5)

btn14 = tk.Button(root, text='(', image=img1, compound='center')
btn14.configure(width=50, height=50)
btn14.configure(command=lambda:buildCommand('('))
btn14.grid(row=4, column=0, padx=5, pady=5)

btn15 = tk.Button(root, text='0', image=img1, compound='center')
btn15.configure(width=50, height=50)
btn15.configure(command=lambda:buildCommand('0'))
btn15.grid(row=4, column=1, padx=5, pady=5)

btn16 = tk.Button(root, text=')', image=img1, compound='center')
btn16.configure(width=50, height=50)
btn16.configure(command=lambda:buildCommand(')'))
btn16.grid(row=4, column=2, padx=5, pady=5)

btn17 = tk.Button(root, text='/', image=img1, compound='center')
btn17.configure(width=50, height=50)
btn17.configure(command=lambda:buildCommand('/'))
btn17.grid(row=4, column=3, padx=5, pady=5)

lbl1 = tk.Label(root, textvariable=mem)
lbl1.configure(font = ('Cascadia Code PL', 12, 'normal'))
lbl1.configure(foreground='yellow', background='black')
lbl1.grid(row=5, column=0, padx=5, pady=5, columnspan=3, sticky=tk.E+tk.W+tk.N+tk.S)

btn18 = tk.Button(root, text='.', image=img1, compound='center')
btn18.configure(width=50, height=50)
btn18.configure(command=lambda:buildCommand('.'))
btn18.grid(row=5, column=3, padx=5, pady=5)

btn19 = tk.Button(root, text='M', image=img1, compound='center')
btn19.configure(width=50, height=50)
btn19.configure(command=lambda:memAction('M'))
btn19.grid(row=6, column=0, padx=5, pady=5)

btn20 = tk.Button(root, text='M+', image=img1, compound='center')
btn20.configure(width=50, height=50)
btn20.configure(command=lambda:memAction('M+'))
btn20.grid(row=6, column=1, padx=5, pady=5)

btn21 = tk.Button(root, text='CM', image=img1, compound='center')
btn21.configure(width=50, height=50)
btn21.configure(command=lambda:memAction('CM'))
btn21.grid(row=6, column=2, padx=5, pady=5)

btn22 = tk.Button(root, text='CA', image=img1, compound='center')
btn22.configure(width=50, height=50)
btn22.configure(command=lambda:memAction('CA'))
btn22.grid(row=6, column=3, padx=5, pady=5)

btn23 = tk.Button(root, text='MG', image=img1, compound='center')
btn23.configure(width=50, height=50)
btn23.configure(command=lambda:memAction('MG'))
btn23.grid(row=7, column=0, padx=5, pady=5)


root.mainloop()
