class Student:
    def __init__(self, roll = 0, name = ""):
        self.roll = roll 
        self.name = name
        self.link = None

class StudentList:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self,std):
        if self.first == None:
            self.first = self.last = std
        else:
            self.last.link = std
            self.last = std
    
    def add_first(self,std):
        std.link = self.first
        self.first = std

    def insert_before(self,name, std):
        t = self.first
        while t.link!=None and t.link.name!=name:
            t = t.link
        if t!=None:
            std.link = t.link
            t.link = std

    def remove(self, name):
        t = self.first
        while t.link != None and t.link.name != name:
            t = t.link
        if t.link!=None:
            t.link = t.link.link
             

    def traverse(self):
        t = self.first
        while t!=None:
            print(t.roll, t.name)
            t = t.link

# Test - 1
a = StudentList()
a.add( Student(10,"Reena") )
a.add( Student(20,"Meena") )
a.add( Student(30,"Seena") )
a.add_first(Student(1, "A"))
a.add_first(Student(4, "B"))

a.insert_before("Reena",Student(101, "Sita"))
a.insert_before("A",Student(102, "Seeeta"))

a.remove("Seema")
a.remove("A")
a.traverse()
