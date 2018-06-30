class Person:
    def __init__(self, name="", father = None, mother = None):
        self.name = name
        self.father = father
        self.mother = mother
        self.spouse = None

    def partner(self,other):
        self.spouse = other
        other.spouse = self
   
# Main

m1 = Person("M")        
m2 = Person("N")
m1.partner(m2)

m3 = Person("V",m1,m2)
m4 = Person("S")
m4.partner(m3)

m5 = Person("K",m3,m4)
m6 = Person("Y",m3,m4)

print(m5.name, m5.father.name, m5.father.father.name )
