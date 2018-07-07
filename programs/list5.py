# Function takes two numbers and returns addition, multiplication
# subtraction, division, modulo and power result in the form of
# list object --- A function returns the "list" object

def calc(no1,no2):
    return [no1+no2, no1-no2, no1*no2, no1/no2, no1%no2, no1 ** no2 ]

#Call
result = calc(10,3)
for r in result:
    print(r)
