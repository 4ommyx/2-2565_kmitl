n = input("")
s = n.split(' ')
print(s)
for i in range(4):
    s[i] = int(s[i])
print(type(s[1]))
print(s)

h=s[2]-s[0]
m=s[3]-s[1]
print("h : ",h)
print("m : ",m)
if m<=15 and h == 0 :
    print(0)
elif h<=3 and m == 0 :
    print(h*10) 
elif h<=2 and m >=1 :
    print((h+1)*10)
elif h==3 and m >=1 :
    print(50)
elif h>=4 and h<=6 and m == 0 :
    print(30+((h-3)*20)) 
elif h>=4 and h<=5 and m >= 1 :
    print(30+((h-2)*20))
elif h >= 6 :
    print(200)
else :
    pass