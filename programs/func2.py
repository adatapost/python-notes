def my_line(ch,n):
   print()
   for a in range(n):
     print(ch, end = "")

my_line("*", 10)
#my_line(40,"#")  # Error 
my_line( n = 20, ch = "%")  # Positional parameters
my_line( ch = "@", n = 50 )  # Positional parameters
