n = 2000

while True :
    if n % 7 == 0 and n % 35 != 0:
        print(n,end=",")
    elif n == 3201:
        break
    n+=1