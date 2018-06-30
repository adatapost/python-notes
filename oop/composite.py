class Address:
    def __init__(self, city="", pin=0):
        self.city = city
        self.pin = pin

class Student:
    def __init__(self, roll = 0, name = "", local = None, postal = None):
        self.roll = roll
        self.name = name
        self.local = local
        self.postal = postal

# Test - 2

p = Student(10,"Meena",Address("Meh",384001),Address("Pat",499393))
print(p.roll, p.name, p.local.city, p.local.pin, p.postal.city, p.postal.pin)
