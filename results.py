from tkinter import *
import cnr

class Results(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.sum = cnr.ComplexNumRow(self, False, "Sum")
        self.diff = cnr.ComplexNumRow(self, False, "Difference")
        self.product = cnr.ComplexNumRow(self, False, "Product")

        self.sum.pack(side=TOP)
        self.diff.pack(side=TOP)
        self.product.pack(side=TOP)

        self.sum.disableInput()
        self.diff.disableInput()
        self.product.disableInput()

    def calcResults(self, real1, imag1, real2, imag2):
        self.sum.enableInput()
        self.sum.changeRealInput(real1 + real2)
        self.sum.changeImagInput(imag1 + imag2)
        self.sum.disableInput()

        self.diff.enableInput()
        self.diff.changeRealInput(real1 - real2)
        self.diff.changeImagInput(imag1 - imag2)
        self.diff.disableInput()

        self.product.enableInput()
        self.product.changeRealInput((real1 * real2) - (imag1 * imag2))
        self.product.changeImagInput((imag1 * real2) + (real1 * imag2))
        self.product.disableInput()

