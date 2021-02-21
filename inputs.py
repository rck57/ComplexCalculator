from tkinter import *
import cnr

class Inputs(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.input1 = cnr.ComplexNumRow(self, True, "Input 1")
        self.input2 = cnr.ComplexNumRow(self, True, "Input 2")

        self.input1.pack(side=TOP)
        self.input2.pack(side=TOP)

    def getReal1(self):
        return self.input1.getRealInput()

    def getImag1(self):
        return self.input1.getImagInput()

    def getReal2(self):
        return self.input2.getRealInput()

    def getImag2(self):
        return self.input2.getImagInput()

