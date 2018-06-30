class Date:
    def __init__(self, d =0, m = 0, y = 0):
        self.d = d
        self.m = m
        self.y = y

    def is_leap(self):
        return self.y % 4 == 0

    def set(self,d,m,y):
        self.m = m
        self.d = d
        self.y = y

    def indian_format(self):
        return F"{self.d}/{self.m}/{self.y}"

    def is_valid(self):
        """Date validation"""
        if self.m in [1,3,5,7,8,10,12]:
            return self.d>=1 and self.d<=31
        elif self.m in [4,6,9,11]:
            return self.d>=1 and self.d<=30
        elif self.m == 2:
            return self.d>=1 and self.d<=29 if self.is_leap() else self.d>=1 and self.d<=28
        return False
    
    def next(self):
        t = Date(self.d, self.m, self.y)
        if t.m in [1,3,5,7,8,10,12]:
            if t.d == 31 and t.m == 12:
                t.d = 1
                t.m = 1
                t.y += 1

        return t
    def previous(self):
        pass
    
    def day_of_year(self):
        days = [0,31, 31+28, 31+28+31, 31+28+31+30, 31+28+31+30+31]
        return  days[self.m-1] + self.d + 1 if self.is_leap else 0

p = Date(30,5,2006)
q = p.next().next().next()
q.show()

# Test - 1 
a = Date()  # Create an object
a.d = 10
a.m = 2
a.y = 2017
print(a.d, a.m, a.y)
if a.is_leap():
    print("It is leap year!")
else:
    print("Not leap")

# Test - 2
x = Date()
x.set(30,1,2000)
print(x.is_leap())
print(x.indian_format())

# Test - 3
z = Date()
z.set(29,2,2001)
print(z.is_valid())


# Test - 4
p = Date()
p.set(20,2,2002)
print(p.day_of_year())