from enum import Enum
# OOP EP1 (Object,Class)
# --------------------- 
# Class คือแม่แบบของ Object โดยจะต้องกำหนดรายละเอียดของ Class ก่อนจึงจะสร้าง Object ได้
# (Class เป็นต้นแบบในการผลิต Object) , (กำหนดชื่อ Class โดยใช้พิมพ์ใหญ่ไว้ตัวแรกของภาษา Eng)

# โครงสร้าง Class
# ------------- 
# Header ชื่อคลาส 
# Body บอกรายละเอียดในคลาส (method,detail,attribute)
# Header 
# class Name:
#     # method
#     def __init__(self,name,age):
#         # attribute (self.name / ใช้ได้ทั้งคลาส)
#         self.name = name
#         self.age = age

# Instance attrbute / parameter
# -----------------------------
# def __init__(self,name,age):
#         # attribute (self.name / ใช้ได้ทั้งคลาส)
#         self.name = name
#         self.age = age
# age คือพารามิเตอร์ที่ส่งเข้ามา 
# self.age คือ Instance attribute(ใช้ได้ทั้ง class) 
# Object,Instance ความหมายเดียวกัน

# enum Class
# ----------  
# เป็นคลาสที่เก็บค่าคงตัวซึ่ง จะรวบรวมค่าคงที่ในเรื่องใดเรื่องหนึ่งไว้ในคลาสเดียวกัน 
# คลาสชนิดนี้เรียกว่า enum class import ตามนี้ (from enum import Enum) 
# วิธีการใช้งานเหมือน dict {name:value}
class SeatType(Enum):
    ONE, TWO, THREE, FOUR = 1, 2, 3, 4
print(SeatType['ONE'].value)
for i in SeatType:
    print(i.name,"=",i.value)

# การเข้าถึง,แก้ไข Instance Attribute (Object) 
# ----------------------------------
# หากต้องการเข้าถึงข้อมูลแต่ละ Instance
# <Instance(Object)>.<Attrubute>
# การเปลี่ยนแปลงค่าของ Instance 
# <Instance(Object)>.<Attrubute> = <new_value>
# กรณีที่ใช้แค่ภายใน Class เดียวกัน สามารถใช้ self แทนชื่อของ Instance ได้เลย
# <self>.<Attribute> = <new_value>