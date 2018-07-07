class Student:
    def __init__(self, roll = 0, name = ""):
        self.roll = roll
        self.name = name 

class Subject:
    def __init__(self, name = "", total = 0, obtain = 0):
        self.name = name
        self.total  = total
        self. obtain = obtain

class Semester:
    def __init__(self,sem_no):
        self.sem_no = sem_no
        self.marks = []
    def add_mark(self,subject,total,obtain):
        self.marks.append( Subject( subject, total, obtain ))

class Marksheet:
    def __init__(self, student):
        self.student = student
        self.semesters = [] 
    def show(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)
        for s in self.semesters:
            print(s.sem_no)
            for m in s.marks:
                print(m.name, m.total, m.obtain)

    def disp(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)
        s1 = ""
        for i in range(len(self.semesters)):
            s1 = s1 +  str(self.semesters[i].sem_no) + "\t\t\t"
        print(s1)
        

        
    def add_sem(self,sem):
        self.semesters.append(sem)

# Test - 1
s1 = Student(10,"Reena")
mk = Marksheet(s1)  

sem1 = Semester(5)
sem2 = Semester(6)
sem3 = Semester(7)

# add sems to marksheet object
mk.semesters.append(sem1)
mk.add_sem(sem2)
mk.add_sem(sem3)

sem1.marks.append( Subject("Sub1",100,78)  )
sem1.marks.append(Subject("Sub2", 100, 68))
sem1.marks.append(Subject("Sub3", 100, 98))

sem2.add_mark("S1",50,45)
sem2.add_mark("S2",50,45)
sem2.add_mark("S3", 50, 45)

sem3.add_mark("P1", 50, 35)
sem3.add_mark("P2", 50, 45)
sem3.add_mark("P3", 50, 65)

mk.disp()
      
 



        
    
