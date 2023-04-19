# Method and use case diagram

# Setter / Getter
# เป็น Method ที่ทำหน้าที่อ่านข้อมูลและสามารถเปลี่ยนแปลงข้อมูลในคลาสได้
# Setter : ทำหน้าที่เปลี่ยนแปลงข้อมูล
# Getter : ทำหน้าที่อ่านข้อมูลหรือนำข้อมูลจากในคลาสมาใช้นอกคลาสได้

# Getter (Return ข้อมูลที่เราต้องการไว้ในฟังก์ชั่นในคลาส)
# class Player:
#     def __init__(self,position,number):
#         self.__pos = position
#         self.__num = number
#     def display(self):
#         print("Position : {} | Number :{} ".format(self.__pos,self.__num))
#     # getter
#     def title(self):
#         return self.__num
#     def get_title(self):
#         return self.__num
     
#     # setter
#     def s_title(self,num):
#         self.__num = num
#     def set_title(self,num):
#         self.__num = num

# #getter
# player1 = Player("as",5)
# print(player1.title())
# print(player1.get_title())

# #setter
# player1.set_title(10)
# player1.display()

# closures (เป็นการทำให้ตัวแปรที่กำหนดเป็น Free variable)

# def out_num(num):

#     def in_num():
#         print("Num is : ",num)
    
#     return in_num
# out = out_num(200)
# out()

# method (กำหนดพฤติกรรมของ obj)
# ----------------------------

# Instance method / Class method / Static method 

# 1.Instance 
# ----------
# (คือ method ที่เป็นของ obj ใดๆ / โดยสามารถเข้าถึง attribute ของ obj นั้นๆได้)จึงต้องมี self นำหน้า

# การเรียกใช้ method
# ---------------
# <obj>.<method>(argument)
# obj1.display("aom")

# การใช้ __str__ method 
# (จะถูกเรียกใช้เมื่อ print obj)
# -------------------
# class Aom:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return self.name + " " + str(self.age)
#     # static
#     def calcu(kg):
#         return kg*0.5
    
# obj1 = Aom("nattawut",19)
# print(obj1)
# print(Aom.calcu(290))

# 2.Static 
# ---------- 
# method ที่ไม่มีการใช้ attribute ในคลาส ดังนั้นจึงสามารถเรียกใช้ได้โดยไม่ต้องสร้าง obj
# เรียกใช้โดย <class>.<method>(argument)

# 3.Class
# ------- 
# เป็นคลาสที่ใช้ในการทำ Constructor แบบอื่นๆ ได้ (cls คือ constructor)

# Usecase diagarm
# -------------- 
# การหาความต้องการของซอฟท์แวร์ แสดงให้เห็นถึงว่าซอฟท์แวร์ที่จะพัฒนานั้นสามารถทำอะไรได้บ้าง
# แบ่งเป็น 3 ส่วนหลักๆ
# Actor   : ผู้ใช้งานแต่ละกลุ่ม 
# Usecase : การทำงานที่ผู้ใช้สามารถทำได้
# Connection : ความสัมพันธ์ที่เกี่ยวข้องกัน

# 1. <<extends>> : ใช้เป็นคสพโดยเหมือนสิ่งที่เป็นลูกกับแม่ syntax [set(แม่) <--<<extends>>-- subset(ลูก)]
# Ex. search <--<<extends>>-- search by movie title , search by cinema
# 2. <<include>> : ใช้เป็นคสพโดยการจะทำสิ่งหนึ่งต้องผ่านการทำอีกสิ่งหนึ่งก่อน syntax [(สิ่งที่ต้องทำก่อนถึงจะไปอีกการทำงาน) <--<<include>>-- (เป้าหมาย)]
# Ex. assign seat <--<<include>>-- create book

# usecase description (การอธิบายรายละเอียดการทำงานของ use case)