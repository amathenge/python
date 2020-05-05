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

'''
    This class uses a default grid layout
'''
class CalcApp:
    def __init__(self, root):
        self.root = root
        self.img1 = tk.PhotoImage(width = 1, height = 1)
        self.mem = tk.StringVar()

    def setTitle(self, title):
        self.root.title(title)

    def run(self):
        self.root.mainloop()

    def addDisplay(self):
        self.txt1 = tk.Entry(self.root)
        self.txt1.configure(font = ('Cascadia Code PL', 12, 'normal'))
        self.txt1.configure(foreground = 'yellow', background = 'black')
        self.txt1.configure(insertbackground = 'blue', insertwidth = '4')
        self.txt1.grid(row = 0, column = 0, columnspan = 3, sticky='nsew',
                       padx = 5, pady = 5)

    def addMemoryDisplay(self):
        self.lbl1 = tk.Label(self.root, textvariable = self.mem)
        self.lbl1.configure(font = ('Cascadia Code PL', 12, 'normal'))
        self.lbl1.configure(foreground = 'white', background = 'black')
        self.lbl1.grid(row = 5, column = 0, padx = 5, pady = 5, columnspan = 3, sticky = tk.E+tk.W+tk.N+tk.S)

    def getCommand(self):
        return self.txt1.get()

    def deleteCommand(self):
        self.txt1.delete(0, tk.END)

    def updateCommand(self,item):
        self.deleteCommand()
        self.txt1.insert(0, item)

    def buildCommand(self, item):
        txt = self.getCommand()
        txt += str(item)
        self.updateCommand(txt)

    def memAction(self, action):
        if action == 'M':
            txt = self.getCommand()
            while '=' in txt:
                txt = txt[0:txt.rfind('=')]
            self.mem.set(txt)
        elif action == 'M+':
            tmp1 = self.mem.get().strip()
            if len(tmp1) > 0:
                sPos = '+('
                ePos = ')'
            else:
                sPos = ''
                ePos = ''
            tmp2 = self.getCommand()
            while '=' in tmp2:
                tmp2 = tmp2[0:tmp2.rfind('=')]
            tmp3 = tmp1 + sPos + tmp2 + ePos
            self.mem.set(tmp3)
        elif action == 'CM':
            self.mem.set('')
        elif action == 'CA':
            self.mem.set('')
            self.deleteCommand()
        elif action == 'MG':
            self.updateCommand(self.mem.get())

    def doMath(self):
        try:
            res = eval(self.getCommand())
            res = str(res)
        except ZeroDivisionError:
            res = 'EDIV-0'
        except:
            res = 'ERR-SYN'
        txt = self.getCommand()
        txt += '=' + res
        self.updateCommand(txt)

    def addOperations(self):
        self.ops = {}
        self.opsNames = ['=','+','-','*','/','.','(',')','.','M','M+','CM','CA','MG']
        self.opsPos = [(0,3),(1,3),(2,3),(3,3),(4,3),(4,1),(4,0),(4,2),(5,3),(6,0),(6,1),(6,2),(6,3),(7,0)]
        totalItems = len(self.opsNames)
        counter = 0
        while counter < totalItems:
            self.ops[self.opsNames[counter]] = tk.Button(self.root, text = self.opsNames[counter], image = self.img1, compound = 'center')
            self.ops[self.opsNames[counter]].configure(width = 50, height = 50)
            if self.opsNames[counter] == '=':
                self.ops[self.opsNames[counter]].configure(command = self.doMath)
            elif self.opsNames[counter] in ['M','M+','CM','CA','MG']:
                self.ops[self.opsNames[counter]].configure(command = lambda vCounter=counter: self.memAction(self.opsNames[vCounter]))
            else:
                self.ops[self.opsNames[counter]].configure(command = lambda vCounter=counter: self.buildCommand(self.opsNames[vCounter]))
            self.ops[self.opsNames[counter]].grid(row = self.opsPos[counter][0], column = self.opsPos[counter][1], padx = 5, pady = 5)
            counter += 1

    def addNum(self, num, pos):
        tBtn = tk.Button(self.root, text = str(num), image = self.img1, compound = 'center')
        tBtn.configure(width = 50, height = 50)
        tBtn.configure(command = lambda : self.buildCommand(num))
        tBtn.grid(row = pos[0], column = pos[1], padx = 5, pady = 5)
        return tBtn

    def addNumbers(self):
        self.btnNames = ['1','2','3','4','5','6','7','8','9']
        self.btnPos = [(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)]
        self.btns = {}
        totalItems = len(self.btnNames)
        counter = 0
        while counter < totalItems:
            self.btns[self.btnNames[counter]] = self.addNum(self.btnNames[counter],self.btnPos[counter])
            counter += 1

    def buildGUI(self):
        self.addDisplay(self)
        self.addNumbers(self)
        self.addOperations(self)

    def keyAction(self, event):
        if event.keysym == 'Return':
            self.doMath()

    def keyMemory(self, event):
        self.memAction('M+')

    def keyClear(self, event):
        self.memAction('CA')

    def bindKeys(self):
        self.root.bind('<KeyPress>', lambda e: self.keyAction(e))
        self.root.bind('<Control-m>', lambda e: self.keyMemory(e))
        self.root.bind('<Control-M>', lambda e: self.keyMemory(e))
        self.root.bind('<Control-c>', lambda e: self.keyClear(e))
        self.root.bind('<Control-C>', lambda e: self.keyClear(e))

    def addHelp(self):
        self.lblHelp = tk.Label(self.root)
        helpstring = 'HELP:\ntype formula in the bar\n'
        helpstring += 'ctrl+m = add from formula to memory\n'
        helpstring += 'ctrl+c = clear memory and formula'
        self.lblHelp.configure(text = helpstring)
        self.lblHelp.configure(font = ('Cascadia Code PL', 8, 'normal'))
        self.lblHelp.configure(anchor = tk.N, justify = tk.LEFT, relief = tk.SUNKEN)
        self.lblHelp.grid(row = 7, column = 1, columnspan = 3, sticky = tk.N+tk.S+tk.E+tk.W)

App = CalcApp(tk.Tk())
App.setTitle('Python Calculatoar with Classes')
# in a second iteration of this App, we'll put all of this in a doGUI() method
App.addDisplay()
App.addOperations()
App.addNumbers()
App.addMemoryDisplay()
App.bindKeys()
App.addHelp()
App.run()
