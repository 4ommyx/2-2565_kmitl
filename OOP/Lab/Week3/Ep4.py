
def char_count(str):
# สร้าง dict | ans = {}
  ans = dict()
  for i in str:
    # ค่าที่มี key , value เท่ากัน จะไม่มีการอัพเดทค่า 
    # แต่ถ้า value เปลี่ยน ค่าจะถูกอัพเดตด้วย 
    # ans[i] = str.count(i) 
    # คือการใส่ค่าไว้ใน dict โดย i = key , str.count(i) = value
    ans[i] = str.count(i)
  return ans

a = 'aasasaa'
print(char_count(a))