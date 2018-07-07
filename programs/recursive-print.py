def print_no(n):
    if n <= 10:
      return n + print_no(n+1)
    return 0

# Call the function

result = print_no(1)
print(result)
