class Medal:
    def __init__(self,country=None, gold=0, silver=0, bronze=0):
        self.g = gold
        self.s = silver
        self.b = bronze
        self.country = country
    
    def showTotal(self):
        total = self.g + self.s + self.b
        return "{} | Total is : {} ".format(self.country, total)
    
    def showMedal(self):
        return "GOLD : {} SILVER : {} BRONZE : {}".format(self.g, self.s, self.b)
    
# th = Medal("Thailand", 10, 5, 15)
# jp = Medal("Japan", 12, 2, 23)

# print(th.showTotal())
# print(th.showMedal())
# print("-----------------------")
# print(jp.showTotal())
# print(jp.showMedal())