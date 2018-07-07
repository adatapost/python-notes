# Problem - Input number and reverse it

no = int( input("Enter the number : ") )
rev = 0
while no > 0:
  rem = no % 10
  no = no // 10
  rev = rev * 10 + rem

print("Reverse number  : ", rev)
