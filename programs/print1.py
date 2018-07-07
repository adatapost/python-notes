def print_border(value):
    for a in range(1, value):
        for b in range(1, value):
            if a == 1 or b == 1 or a == value-1 or b == value-1:
                print(1, end = ' ')
            else:
                print(0, end = ' ')
        print()  # Newline

# Call the function
print_border(5)
print_border(20)
     

