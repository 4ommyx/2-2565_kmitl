class Mcm:
    def __init__(self, m, cm):
        self.m = m
        self.cm = cm
        self.mt = self.m*100 + self.cm

    def __str__(self):
        return "{}'{}\"".format(self.m, self.cm)

    def __add__(self, other):  # overload + operator
        x = self.mt + other.mt
        i = x // 100
        j = x % 100
        return Mcm(i, j)

    # def __sub__(self, other):  # overload - operator
    #     x = self.inches - other.inches
    #     f = x // 12
    #     i = x % 12
    #     return FootInch(f, i)

    # def __mul__(self, other):
    #     x = self.inches * other.inches
    #     f = x // 12
    #     i = x % 12
    #     return FootInch(f, i)


    # def __divmod__(self, other):
    # https://docs.python.org/3/library/functions.html#divmod
    #     x = self.inches * other.inches
    #     f = x // 12
    #     i = x % 12
    #     return FootInch(f, i)



m1 = Mcm(2, 150)
m2 = Mcm(3, 0)
m = m1 + m2
print(m)
# ma = m1.__add__(m2)
# m5 = m1 - m2
# # m6 = m1 * m2
# print(m)
# print(ma)
# print(m5)
# # print(m6)