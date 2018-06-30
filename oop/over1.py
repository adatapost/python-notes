class Product():
    def __init__(self, id=0, name = ""):
        self.id = id
        self.name = name
    def __eq__(self,other):
        return self.id == other.id and self.name == other.name
    def __ge__(self,other):
        return self.id >= other.id and self.name >= other.name

    def __str__(self):
        return F"Id: {self.id}, Mame: {self.name}"        

# Test 

p1 = Product(10,"Pen")
p2 = Product(14, "Pen")

print(p1 >= p2)
print(str(p1))
print(p1, p2)
        
