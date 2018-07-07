# Fibonacii number

a, b, n = 0, 1, 1
#print(a,b, end = " ")
while n <= 10:
  c = a + b
  print(a, end=" ")
  a, b = b, c
  n = n + 1
