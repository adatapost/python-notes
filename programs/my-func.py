# It is good practice to define the function at begin of program


def add(no1, no2):
    return no1+no2


def sub(no1, no2):
    return no1 - no2


def mul(no1, no2):
    return no1 * no2


def div(no1, no2):
    return no1 / no2

# Put atlease one blank line between two definitions

# Now, call the functions


no = add(10, 20)
print(no)
print(add(40, 5))
print(mul(4, 5))
print(div(4, 5))

p = add(10,sub(4,mul(4,5)))
print(p)
