class Person:
    def __init__(self, pid, fname, lname,):
        self.id = pid
        self.fname = fname
        self.lname = lname 

    def __str__(self):
        return "Name : {} {}".format(self.fname, self.lname)

class Player(Person):
    def __init__(self, pid, fname, lname, pos, nat):
        super().__init__(pid, fname, lname)
        self.pos = pos
        self.nat = nat

    def __str__(self):
        return "{} | Pos : {} | Nal : {}".format(super().__str__(), self.pos, self.nat)

class Exchange(Player):
    def __init__(self, pid, fname, lname, pos, nat, ex):
        super().__init__(pid, fname, lname, pos, nat)
        self.ex = ex

    def __str__(self):
        return "{} [From : {} --> To : {}] ".format(super().__str__(), self.nat, self.ex)
    
    def showData(self, date):
        self.date = date
        return "{} | {}".format(self.__str__(), self.date)



print(Person("1","Nattawut","Chayauam"))
print(Player("2","Music","Auyueng","CDM","HJG"))
print(Exchange("3","Mewon","Auei","LW","HJG","TH"))

p1 = Exchan ge("4","Mewon","Auei","LW","HJG","TH")
print(p1.showData("4-22-23"))