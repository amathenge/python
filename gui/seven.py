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

    def doMath(self):
        pass

    def addOperations(self):
        self.ops = {}
        self.opsNames = ['=','+','-','*','/','.','(',')']
        self.opsPos = [(0,3),(1,3),(2,3),(3,3),(4,3),(4,1),(4,0),(4,2)]
        totalItems = len(self.opsNames)
        counter = 0
        while counter < totalItems:
            self.ops[self.opsNames[counter]] = tk.Button(self.root, text = self.opsNames[counter], image = self.img1, compound = 'center')
            self.ops[self.opsNames[counter]].configure(width = 50, height = 50)
            if self.opsNames[counter] == '=':
                self.ops[self.opsNames[counter]].configure(command = self.doMath)
            else:
                self.ops[self.opsNames[counter]].configure(command = lambda : self.buildCommand(self.opsNames[counter]))
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



App = CalcApp(tk.Tk())
App.setTitle('Python Calculatoar with Classes')
# in a second iteration of this App, we'll put all of this in a doGUI() method
App.addDisplay()
App.addOperations()
App.addNumbers()
App.run()
