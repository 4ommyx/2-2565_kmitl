# โดยปกติเช่น c ตัวแปรจะชี้ไปที่ข้อมูลของตัวเอง (storng typing)
# แต่กับ python ตัวแปรจะขี้ไปยัง adds  (dynamic typing)
# ทำให้ค่าตัวแปรใน python เปลี่ยนแปลงได้ตลอดเวลา

# หา adds โดย id(var)
# ---------------------
# a = "aom"
# print(a)  
# print("Before :",a,"| id :",id(a)) # addrees
# a = 200
# print(a)
# print("After  :",a,"| id :",id(a))

# ตั้งตัวแปรโดยใช้ snake case
# -----------------------

# การหาร
# ------- 
# 5/2 = 2.5
# 5//2 = 2
# การใช้ (//) เป็นการ floor divition

#การยกกำลัง
# --------
# (5**3) = 5*5*5

# string operater
# ---------------
# print("aom"+" nattawut") # การต่อ string ("aomnattawut")
# print("aom "*5) # การปริ้นคำซ้ำๆ n ครั้ง     ("aom aom aom aom aom")
# str [start:stop:step] defalt step = 1
# mes = "1234567"
# print(mes)
# print(mes[0])  
# print(mes[-1]) 
# print(mes[0:3:1]) 
# print(mes[0:3:2]) 
# print(mes[-1:-10:-1])

# boolen
# -------
# มี 2 ค่า True False
# empty none 0 ถื่อว่า false นอกนั้น true

# operater พิเศษ
# -------------
# "a" i "abc" 
# จะ return ค่าเป็น True / False

# logic 
# -----
# 1.AND ถ้า x เป็น False จะ Return ค่า x เลย ไม่สนค่า y | แต่ถ้า x เป็น Ture  จึงจะดูค่า y
# 2.OR  ถ้า x เป็น Ture  จะ Return ค่า x เลย ไม่สนค่า y | แต่ถ้า x เป็น False จึงจะดูค่า y

# print in python
# --------------- 
# คำสั่ง print จะขึ้นบรรทัดใหม่เสมอ 
# หากไม่ให้ขึ้นบรรทัดใหม่ให้ใช้ (end='') 
# end='aom' หมายถึงหากทำการปริ้นแล้วให้ทำการแสดงคำว่า "aom" ด้วย

# split () เป็นคำสั่งในการแยก string ()
# ---------------------------------
# โดย string ที่แยกได้จะเก็บในรูปแบบของ list 
# ex1 a = 10/20/30 
# b = a.split(/) 
# print(a) = [10,20,30]

# ex2 a = 2 32 221
# b = a.split() 
# print(a) = [2,32,221] 
# ข้อมูลที่ได้เป็น str

