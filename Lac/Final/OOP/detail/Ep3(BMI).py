class Bmi:
    def __init__(self, kg, cm):
        self.w = kg
        self.h = cm
    
    def bmiValue(self):
        value = (self.w)/((self.h/100)**2)
        return value
    
    def bmiDetail(self):
        
        if self.bmiValue() > 30:
            mes = "Fat"
        elif self.bmiValue() > 25 and self.bmiValue()<=30:
            mes = "Fat.5"
        elif self.bmiValue() > 18.5 and self.bmiValue()<=25:
            mes = "Balance"
        else:
            mes = "Error"
        return mes
    
    def showData(self):
        return "BMI : {:.2f} | {}".format(self.bmiValue(), self.bmiDetail())
    
    # __str__ : สามารถ return string ของคลาสได้
    def __str__(self):
        return "BMI : {:.2f} | {}".format(self.bmiValue(), self.bmiDetail())

lis = [Bmi(70,170),Bmi(80,180),Bmi(90,185),Bmi(100,180)]     
print(Bmi(70, 170))

for i in lis:
    print(i)

# print(aom.bmiValue())
# print(aom.bmiDetail())
# print(aom.showData())
        