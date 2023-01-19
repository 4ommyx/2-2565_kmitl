# leap yaer = (year % 4 = 0)
# dd,dm,dy = 0,0,0

def is_leap(y):

    print(y,"is LEAP YEARS !!")

# def day_in_year(n):
#     print("day in year",n)

def day_of_year (day,month,year):
    dd,dm,dy = 0,0,0

    if (year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
        is_leap(year)
        # day_in_year(366)
        if month >=3:
            dy = 1
        else:
            pass
    else:
        pass
        # day_in_year(365)
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

print(day_of_year(26,9,2024))
