class Point:

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def add(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def show(self):
        print(self.x, self.y)

# Examine the Point actions

p = Point(30,40)
q = Point(3,4)

p.add(q).add(p).add(q).sub( Point(1,2) ) .show()
p.show()
q.show()

Point(1,2).add( Point(2,3).sub( Point(3,4)) ).add( Point(5,6 )).show()
