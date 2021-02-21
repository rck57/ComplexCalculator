from tkinter import *
import inputs
import results

class Calculator():
    def __init__(self):
        self.box = Tk()

        self.frame1 = Frame(self.box)
        self.frame2 = Frame(self.box)

        self.toplabel = Label(self.box, text="Complex Calculator", font=("Century Gothic", 24))
        self.toplabel.pack(side=TOP)

        self.inputs = inputs.Inputs(self.frame2)
        self.inputs.pack(side=LEFT, padx=50)

        self.evalbutton = Button(self.inputs, text="Evaluate", command=self.calculate)
        self.evalbutton.pack(side=TOP)

        self.resultslabels = Frame(self.frame2)
        self.sum = Label(self.resultslabels, text="Sum", font=("Century Gothic", 12), anchor="w", width=8)
        self.diff = Label(self.resultslabels, text="Difference", font=("Century Gothic", 12), anchor="w", width=8)
        self.product = Label(self.resultslabels, text="Product", font=("Century Gothic", 12), anchor="w", width=8)
        self.sum.pack(side=TOP)
        self.diff.pack(side=TOP)
        self.product.pack(side=TOP)
        self.resultslabels.pack(side=LEFT)

        self.results = results.Results(self.frame2)
        self.results.pack(side=LEFT)

        self.frame1.pack(side=TOP, pady=10)
        self.frame2.pack(side=TOP, pady=10)
        self.box.mainloop()

    def calculate(self):
        real1 = self.inputs.getReal1()
        imag1 = self.inputs.getImag1()
        real2 = self.inputs.getReal2()
        imag2 = self.inputs.getImag2()
        print(real1)
        try:
            self.results.calcResults(real1, imag1, real2, imag2)
        except ValueError:
            self.results.calcResults(0,0,0,0)

Calculator()


