class Player:
    def __init__(self, name=None, number=None) :
        self.name = name
        self.number = number
    
    def display(self):
        return "Name : {} | Number : {}".format(self.name, self.number)

p1 = Player("De Gea", "1")
print(p1.display())
p2 = Player("Bruno", "8")
print(p2.display())
p3 = Player(number="19")
print(p3.display())
# print(a)
# print(p3.number)


    

