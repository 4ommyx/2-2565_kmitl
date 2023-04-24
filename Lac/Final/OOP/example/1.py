class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(("My name is : {} : I'm {} years old").format(self.name, self.age))

p1 = People("Nattawut", "20")
p1.display()