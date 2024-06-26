from breezypythongui import EasyFrame

class Sum(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="First Num:", row=0, column=0)
        self.first = self.addIntegerField(value=0, row=0, column=1)
        self.addLabel(text="Second Num:", row=1, column=0)
        self.second = self.addIntegerField(value=0, row=1, column=1)
        self.addLabel(text="Sum:", row=2, column=0)
        self.result = self.addIntegerField(value=0, row=2, column=1)
        self.addButton(text="Generate", row=3, column=0, columnspan=2, command=self.calculate_sum)
    
    def calculate_sum(self):
        x = self.first.getNumber()
        y = self.second.getNumber()
        s = x + y
        self.result.setNumber(s)

Sum().mainloop()
