class Date:
    def __init__(self, d = 0 , m = 0, y = 0):
      self.d = d
      self.m = m
      self.y = y
    def indian_format(self):
        return F"{self.d}/{self.m}/{self.y}"


# Test teh code
x = Date(10, 2, 2002)
a = Date()
print(a.indian_format())
print(x.indian_format())
