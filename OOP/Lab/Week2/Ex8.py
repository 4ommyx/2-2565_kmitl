# leap yaer = (year % 4 = 0)
# dd,dm,dy = 0,0,0
# d1,d2,m1,m2,y1,y2,d = 0,0,0,0,0,0,0

# def is_leap(y):
#     print(y,"is LEAP YEARS !!")

def date_diff(bf,af):
    d1,d2,m1,m2,y1,y2,d =0,0,0,0,0,0,0

    bfs = bf.split("-")
    for i in range(len(bfs)):
        bfs[i] = int(bfs[i])
    #print(bfs)

    afs = af.split("-")
    for i in range(len(afs)):
        afs[i] = int(afs[i])
    #print(afs)

    d1,d2 = bfs[0],afs[0]
    m1,m2 = bfs[1],afs[1]
    y1,y2 = bfs[2],afs[2]
    #print(d1,d2)

    while True :
        if (d1 == d2) and (m1 == m2) and (y1 == y2):
            
            return d
        else :

            if d1 == 31 and (m1 == 1 or m1 == 3 or m1 == 5 or m1 == 7 or m1 == 8 or m1 == 10 )  :
                m1+= 1
                d1 = 0

            elif d1 == 30 and (m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11)  :
                m1+= 1
                d1 = 0

            elif d1 == 28 and (m1 == 2) and (y1 % 4 != 0) :
                m1+= 1
                d1 = 0

            elif d1 == 28 and (m1 == 2) and (y1 % 4 == 0 or y1 % 100 != 0 or y1 % 400 != 0)  :
                d1 += 1
                d += 1

                if d1 == 29 and (m1==2):
                    m1+= 1
                    d1 = 0


        if d1 == 31 and (m1 ==12):
            y1+= 1
            m1 = 1
            d1 = 0


        d1+=1
        d+=1

def is_leap(y):

    print(y,"is LEAP YEARS !!")

def day_of_year (day,month,year):

    dd,dm,dy = 0,0,0

    if (year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
        is_leap(year)
        day_in_year(366)

        if month >=3:
            dy = 1
        else:
            pass
    else:
        day_in_year(366)

    for i in range(1,month):
        if i>=1 and i<=7 and i%2 == 1:
            dm+=31
        elif i>=1 and i<=7 and i%2 == 0 and i !=2:
            dm+=30 
        elif i == 2:
            dm+=28
        elif i>=8 and i<=12 and i%2 == 0:
            dm+=31
        elif i>=8 and i<=12 and i%2 ==1:
            dm+=30
        else:
            break
    dd = day
    return(dd+dm+dy)

def day_in_year(n):
    print("day in year :",n)

print(day_of_year(26,9,2024))

dif = date_diff("1-1-1999","28-2-2021")
print(dif+1,"day")

# print(day_of_year(26,9,2023))
