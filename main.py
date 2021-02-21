from tkinter import *
import inputs

class Calculator():
    def __init__(self):
        self.box = Tk()

        self.frame1 = Frame(self.box)
        self.frame2 = Frame(self.box)

        self.toplabel = Label(self.box, text="Complex Calculator")
        self.toplabel.configure(font=("Century Gothic", 24))
        self.toplabel.pack(side=TOP)

        self.inputs = inputs.Inputs(self.frame2)
        self.inputs.pack(side=LEFT)
        self.frame1.pack(side=TOP)
        self.frame2.pack(side=TOP)
        self.box.mainloop()

Calculator()


