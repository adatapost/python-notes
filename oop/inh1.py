class Person:
    def __init__(self, name = "", age = 0):
        self.age = age
        self.name = name
    def show(self):
        print("Name : ",self.name, "Age : ",self.age)

class Student(Person):
    def __init__(self,name = "", age = 0, standard = 0):
        super().__init__(name,age)
        self.standard = standard
    def show(self):
        super().show()
        print("Standard :", self.standard )

class Teacher(Person):
    def __init__(self, name = "", age = 0, subject = ""):
        super().__init__(name,age)
        self.subject = subject
    def show(self):
        super().show()
        print("Subject :", self.subject )

    
# Test 

s = Student("Meena",10,5)
s.show()
t = Teacher("Raj",40,"Maths")
t.show()

people = [s,t, Teacher("Reena",30,"Science"), Student("Keena",7,2) ]
for p in people:
    p.show()
 
