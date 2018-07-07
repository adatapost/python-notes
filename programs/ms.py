d,m,y,hh,mm,ss = 1,6,2018,11,10,20

days = y * 365 + m * 30 + d
seconds = days * 24 * 3600 + hh * 3600 + mm * 60 + ss
ms =  seconds * 1000
print(ms, "ms")