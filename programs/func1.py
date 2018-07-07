def my_line(n):
    print()
    for a in range(n):
        print("-",end="")

# Call functions
n = int(input("Enter value : "))
my_line(n) 
print("\nHello, Python")      
my_line(40)

for i in range(20):
    my_line(i)
