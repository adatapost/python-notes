class Date:
    def __init__(self):
        # fields or members -- These are not variables
        self.day = 0
        self.month = 0
        self.year = 0
        

# p and q are two variables

p = Date()   # Creates an object and return its memory reference to "p"
q = Date()   # Creates another object 

p.day = 10
q.day = 2
p.month = 2
p.year = 2010
q.month = 5
q.year = 2010

print(p.day, p.month, p.year)
print(q.day, q.month, q.year)
 
 
