from datetime import date

class Person:
    def __init__(self, title, fname, lname, dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.dob = dob

    def __str__(self):
        return "{} {} {} {}".format(self.title, self.fname, self.lname, self.dob)


class PersonV2:
    def __init__(self, title, fname, lname, titleTh, fnameTh, lnameTh, dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.titleTh = titleTh
        self.fnameTh = fnameTh
        self.lnameTh = lnameTh
        self.dob = dob

    def __str__(self):
        return "{} {} {}\n{} {} {}\n{}" \
            .format(self.title, self.fname, self.lname,
                    self.titleTh, self.fnameTh, self.lnameTh,
                    self.dob)

class PersonName:
    def __init__(self, title, fname, lname):
        self.title = title
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {} {}".format(self.title, self.fname, self.lname)

class PersonV3:
    def __init__(self, nameEn, nameTh, dob):
        self.nameTh = nameTh
        self.nameEn = nameEn
        self.dob = dob

    def __str__(self):
        return "EN : {}\nTH : {}\ndate : {}".format(self.nameEn, self.nameTh, self.dob)


print(Person("Mr.", "Peter", "Parker", date(1995, 10, 4)))
print("*" * 40)
print(PersonV2("Mr.", "Peter", "Parker",
                  "นาย", "ปีเตอร์", "ปาร์คเกอร์",
                  date(1995, 10, 4)))
print("*" * 40)
print(PersonV3(PersonName("Mr.", "Peter", "Parker"), PersonName("นาย", "ปีเตอร์", "ปาร์คเกอร์"), date(1995, 10, 4)))
