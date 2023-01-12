# n = int(input(""))
# tes = n
# rev = 0
# rem = 0
palin = []

def palindrome (n):
    tes = n
    rev = 0
    rem = 0
    while True :
        if n > 0 :
            rem = n % 10
            rev = (rev*10) + rem
            n = n//10
        elif n <= 0 :
            break

    if rev == tes :
        #print(tes)
        palin.append(tes)
        print(i,"*",j,tes)


i,j = 1000,1000
while i>=100:
    while j >= 100:
        n = i*j
        palindrome(n)
        # print(i,j,n)
        j-=1
    i -= 1
    j = 1000

# print(palin)
# palin.sort()
# print(palin)
# print(palin[-1])