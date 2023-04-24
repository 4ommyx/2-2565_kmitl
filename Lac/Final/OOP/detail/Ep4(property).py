class Player:
    def __init__(self, number, position, name):
        self.num = number
        self.pos = position
        self.name = name

    def display(self):
        return "Name : {} | Position : {} | Number : {} ".format(self.name, self.pos, self.num)
    
    @property
    def display1(self):
        return "Name : {} | Position : {} | Number : {} ".format(self.namee, self.position, self.number)
    
    @property
    def position(self):
        return self.pos
    
    @property
    def namee(self):
        return self.name
    
    @property
    def number(self):
        return self.num

    def __str__(self):
        return "Name : {} | Position : {} | Number : {} ".format(self.namee, self.position, self.number)

# property คือเป็นการมองแบบตัวแปรทั้งที่ระบุเป็นฟังก์ชั่น ซึ่งต่างจากการเรียกใช้ method 
# เพราะการเรียกใช้ method จะต้องระบุ () ส่วน property ไม่ต้องระบุ สามามารถระบุ obj.function ได้เลย

p1 = Player("10","CF","Rashford")
print(p1.display())

print(p1.display1)
print(p1.namee)
print(p1.position)
print(p1.number)

lis = [Player("10","CF","Rashford"), Player("10","CF","Rashford"), Player("10","CF","Rashford"), Player("10","CF","Rashford"), Player("10","CF","Rashford")]
for a in lis :
    print(a)