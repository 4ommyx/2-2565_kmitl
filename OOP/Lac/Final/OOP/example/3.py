class ComplexNumber:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine
    def getValue(self):
        if self.imagine >=0:
            a = "{} + {}".format(self.real, self.imagine)
        else:
            self.imagine = abs(self.imagine)
            a = "{} - {}".format(self.real, self.imagine)
        return a
n1 = ComplexNumber(2, 9)
n2 = ComplexNumber(2, -9)
print(n1.getValue())
print(n2.getValue())