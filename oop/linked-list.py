class Student:
    def __init__(self,roll = 0, name =""):
        self.roll = roll
        self.name = name
        self.link = None   # Self reference variable

class StudentList:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self,roll, name):
        t = Student(roll,name)
        if self.first == None:
            self.first = self.last = t
        else:
            self.last.link = t
            self.last = t
    def show(self):
        t = self.first
        while t!=None:
            print(t.roll, t.name)
            t = t.link

         

s1 = StudentList()
s1.add(10,"A")
s1.add(20,"T")
s1.add(3,"G")
s1.add(31,"G1")
s1.add(23,"3G")
s1.show()


 
 

