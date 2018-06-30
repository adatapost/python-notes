class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def add(self,q):
        # Create temporary object
        t = Point()
        t.x = self.x + q.x 
        t.y = self.y + q.y 
        return t

    def sub(self, q):
        return Point( self.x - q.x, self.y - q.y)
        
    
# Test - 1
p = Point(10,20)
q = Point(20, 40)

r = p.add(q) 
print(r.x, r.y)

s = p.sub(q)
print(s.x, s.y)

s = q.sub(p)
print(s.x, s.y)

k = Point(4,5).add( Point(3,4) )
 
print(k.x, k.y)
 
