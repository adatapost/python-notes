no = 10
a1 = lambda a,b: a+b
mul = lambda x,y:  x *  y
max_no = lambda x,y: x if x > y else y

print(a1,type(a1))

# Call the anonymous function
p = a1(10,20)
print(p, mul(4,5))
print(max_no(3,4))