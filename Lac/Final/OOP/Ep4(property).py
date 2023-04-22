class Player:
    def __init__(self, number, position, name):
        self.num = number
        self.pos = position
        self.name = name

    def display(self):
        return "Name : {} | Position : {} | Number : {} ".format(self.name, self.pos, self.number)
    
    @property
    def position(self):
        return self.pos
    
    @property
    def namee(self):
        return self.name
    
    @property
    def number(self):
        return self.num
    

    
p1 = Player("10","CF","Rashford")
print(p1.display())
print(p1.namee)
print(p1.position)
print(p1.number)