class Product:
    def __init__(self, name = "", qty = 0, rate = 0, avail = False):
        self.name = name
        self.qty = qty 
        self.rate = rate 
        self.avail = avail 
    def amount(self):
        return self.qty * self.rate

class ProductRepository:
    def __init__(self):
        self.products = []
        # Mock data
        self.products.append( Product("Pencil",10,4,True))
        self.products.append( Product("Pen",10,10,False))
        self.products.append( Product("Mouse",1,400,True))
        self.products.append(Product("Keyboard", 2, 1200, False))

    #Generate methods
    def available_products(self):
        for p in self.products:
            if p.avail:
                yield p

    def available_products_by_rate(self, start, end):
        for p in self.products:
            if p.avail and (p.rate>=start and p.rate<=end):
                yield p

    # Generate that takes anonymous method as parameter
    def filter(self, func):
        for p in self.products:
            if func(p):
                yield p

# Test
# 
pr = ProductRepository()

# Define anonymous function

print("List by available..")
f1 = lambda x : x.avail 
for p in pr.filter(f1):
    print(p.name, p.rate, p.qty, p.amount())

print("List by available and rate>50.")
f1 = lambda p: p.avail and p.rate>50
for p in pr.filter(f1):
    print(p.name, p.rate, p.qty, p.amount())


print("List all products where rate in between 1 to 50 rs")
for p in pr.filter( lambda x: x.rate>=1 and x.rate<=50):
    print(p.name, p.rate, p.qty, p.amount())

name = input("Enter the product name to search : ")
for p in pr.filter(lambda x: x.name.startswith(name)):
    print(p.name, p.rate, p.qty, p.amount())


#print("List of available products!")
#for p in pr.available_products():
#    print(p.name, p.qty, p.rate, p.amount())

#print("List of available products!")
#for p in pr.available_products_by_rate(100,5000):
#    print(p.name, p.qty, p.rate, p.amount())


