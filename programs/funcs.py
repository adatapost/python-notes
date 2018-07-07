# Functions to perform addition of two numbers

# No parameter and no return value
def add1():
    """This is the function that input two values and print the sum"""
    no1 = int(input("No :"))
    no2 = int(input("No :"))
    print("Addition : ", no1+no2)

# No parameter but returns
def add2():
    '''
    This function input two integer value returns the sum
    '''
    no1 = int(input("No :"))
    no2 = int(input("No :"))
    return no1+no2

# Parameters and no return 
def add3(no1,no2):
    print("Addition : ", no1+no2)

# Parameters and returns
def add4(no1, no2):
    return no1+no2

# Call
add1()
p = add2()
print("Result is " , p + 10)
add3(50,4)
a = int(input("Enter first No : "))
b = int(input("Enter second No : "))
add3(a,b)
p = add4(4,5)
print(p)
p = add4(20,p)
print(p)
p=add4(a,b)
print(p)
p = add4( add4(4,5), add4(add4(2,5),4))
print(p)