low,up = 0,0
mes = str(input())
for i in range(len(mes)):
  if mes[i].islower():
    low+=1
  elif mes[i].isupper():
    up+=1
  else:
    pass
print(low)
print(up)