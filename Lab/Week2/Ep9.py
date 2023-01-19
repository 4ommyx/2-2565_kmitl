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

            d+=1
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

            elif d1 == 31 and (m1 ==12):
                y1+= 1
                m1 = 1
                d1 = 0     
            if (d1 == 30 and (m1 == 1 or 3 or 5 or 5 or 8 or 10 or 12)) or  (d1 == 31 and (m1 == 9 or 4 or 6 or 11 )) or d1 == 32 :
                return -1
    


a = date_diff("1-1-2018","1-1-2020")
print(a)