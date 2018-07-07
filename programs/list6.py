# Understand the mutability of list object -- This object can be changed/
# updated anywhere -- within the global scope or localscope
def test(nos):
    nos[0] = 9
    nos.append(40)

#Call
a = [10,20]
print(a)
test(a)
print(a)
