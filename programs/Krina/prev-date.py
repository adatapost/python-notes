# Program: Calculate the previous date of given date
# Author : Mr. Yash
# Date : Saturday, 2nd June 2018

#
#  1 1 2018 =>  31 12 2017
#  1 2 2018 =>  31 1 2018

#  1 5 2018 =>  28 2 2018
#  1 3 2018 =>  28 2 2018

d, m, y = 1, 3, 2018

if m == 1 or m == 2 or m == 4 or \
           m == 6 or m == 8 or m == 9 or m == 11:
    if m == 1 and d == 1:
        m = 12
        d = 31
        y -= 1  # y = y - 1
    elif d == 1:
        d = 31
        m -= 1  # m = m - 1
    else:
        d -= 1  # d = d - 1

elif m == 5 or m == 7 or m == 10 or m == 12:
    if d == 1:
        d = 30
        m -= 1
    else:
        d -= 1
    
elif m == 3:
    if y % 4 == 0:
        if d == 1:
            d = 29
            m -= 1
        else:
            d -= 1
    else:
        if d == 1:
            d = 28
            m -= 1
        else:
            d -= 1

print("The previous date is:\n")
print(d,"-",m,"-",y)