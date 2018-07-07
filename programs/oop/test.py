class Test:
    def __init__(self):
        self.no = 0

# Test
def one(x):
    x = 10
def two(x):
    x = 10

a = Test()     # Mutable Test object
b = 2            # Immutable int object

one(b) 
two(a)  

print(a.no,b)   # 0 2
