# Program: Calculate the next date of given date

d,m,y = 28,2,2012

if m==1 or m == 3 or \
            m == 5 or m == 7 \
               or m == 8 or m == 10 or m == 12:
   if d == 31 and m == 12:
      y = y + 1
      m = 1
      d = 1
   elif d == 31:
      m = m + 1
      d = 1
   else:
      d = d + 1
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d == 30:
        m = m + 1
        d = 1
    else: 
        d = d + 1
elif m == 2:
    if y % 4 == 0:
       if d == 29:
          m = m + 1
          d = 1
       else:
          d = d + 1
    else:
       if d == 28:
          m = m + 1
          d = 1
       else:
          d = d + 1

print("Next Date : ", d,"-", m,"-",y)


