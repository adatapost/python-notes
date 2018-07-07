# Problem : Calculate the day of year
# e.g 2-2-2018   33rd day of the year 2018
# e.g 12-12-2018   ?  ( 31 + 28 + 31 + 30 + 31 + 2)

d, m, y = 31,12, 2018
total_days = d
m -= 1

if m == 11:
    total_days += 30  # total_days = total_days + 30
    m -= 1
if m == 10:
    total_days += 31
    m -= 1
if m == 9:
    total_days += 30
    m -= 1
if m == 8:
    total_days += 31
    m -= 1
if m == 7:
    total_days += 31
    m -= 1
if m == 6:
    total_days += 30
    m -= 1
if m == 5:
    total_days += 31
    m -= 1    
if m == 4:
    total_days += 30
    m -= 1    
if m == 3:
    total_days += 31
    m -= 1
if m == 2:
    total_days += 29 if y % 4 == 0 else 28
    m -= 1    
if m == 1:
    total_days += 31

print("Day of year : ", total_days)    
    


    







