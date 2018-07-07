day, month, year = 29, 22, 2018  

valid = False   # Control or status 

if month==1 or month==3 or month==5 or month==7 \
               or month==8 or month==10 or month==12:
   valid = day>=1 and day<=31
elif month==4 or month==6 or month==9 or month==11:
   valid = day>=1 and day<=30
elif month==2:
   valid = day>=1 and day<=29 if year % 4 == 0 else day>=1 and day<=28

if valid:
   print("Valid Date!")
else:
   print("Invalid Date")
