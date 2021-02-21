from tkinter import *

class Inputs(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.input1 = InputRow(self)
        self.input2 = InputRow(self)
        self.evalbutton = Button(self, text="Evaluate", command=self.getResults)

        self.input1.pack(side=TOP)
        self.input2.pack(side=TOP)
        self.evalbutton.pack(side=TOP)

    def getResults(self):
        print("hi")

class InputRow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.realinput = Text(self, height=1, width=6)
        self.imaginput = Text(self, height=1, width=6)
        self.plus = Label(self, text="+")
        self.i = Label(self, text="i")

        self.realinput.pack(side=LEFT)
        self.plus.pack(side=LEFT)
        self.imaginput.pack(side=LEFT)
        self.i.pack(side=LEFT)