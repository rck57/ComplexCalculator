from tkinter import *

# frame that looks like a complex number with inputs
class ComplexNumRow(Frame):
    def __init__(self, parent, hasLeftLabel, leftLabel):
        Frame.__init__(self, parent)
        self.parent = parent

        self.realinput = Text(self, height=1, width=6)
        self.imaginput = Text(self, height=1, width=6)
        self.plus = Label(self, text="+", font=("Century Gothic", 16))
        self.i = Label(self, text="i", font=("Century Gothic", 16))
        self.leftlabel = Label(self, text=leftLabel, font=("Century Gothic", 12))

        if hasLeftLabel:
            self.leftlabel.pack(side=LEFT)

        self.realinput.pack(side=LEFT)
        self.plus.pack(side=LEFT)
        self.imaginput.pack(side=LEFT)
        self.i.pack(side=LEFT)

    def getRealInput(self):
        try:
            return int(self.realinput.get("1.0",END))
        except ValueError:
            return 0

    def getImagInput(self):
        try:
            return int(self.imaginput.get("1.0",END))
        except ValueError:
            return 0

    def disableInput(self):
        self.realinput.configure(state=DISABLED)
        self.imaginput.configure(state=DISABLED)

    def enableInput(self):
        self.realinput.configure(state=NORMAL)
        self.imaginput.configure(state=NORMAL)

    def changeRealInput(self, value):
        self.realinput.delete("1.0", END)
        try:
            self.realinput.insert("1.0",value)
        except ValueError:
            self.realinput.insert("1.0", value)

    def changeImagInput(self, value):
        self.imaginput.delete("1.0", END)
        try:
            self.imaginput.insert("1.0",value)
        except ValueError:
            self.imaginput.insert("1.0", value)
