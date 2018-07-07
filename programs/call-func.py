max = 5
def print_matrix(style = 1, row = max, col = max):
  if style == 1:
    for a in range(1, row + 1):
      for b in range(1, col + 1 ):
          print(1, end = " ")
      print()
  elif style == 2:
    for a in range(1, row + 1):
      for b in range(1, col + 1 ):
          print(a, end = " ")
      print()
  elif style == 3:
    for a in range(1, row + 1):
      for b in range(1, col + 1 ):
          print(b, end = " ")
      print()
  elif style == 4:
    for a in range(1, row + 1):
      c = a
      for b in range(1, col + 1 ):
          print(c, end = " ")
          c += 1
      print()


print_matrix()  
print_matrix(2) 
print_matrix(4) 
print_matrix(4,4,20) 
    
    