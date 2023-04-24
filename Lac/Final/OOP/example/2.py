class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def afterY(self, year):
        self.year = self.age+year
        print("Before : {} is {} years old".format(self.name, self.age))
        print("After  : {} is {} years old".format(self.name, self.year))

h1 = Human("Nattawut", 20)
h1.afterY(99)