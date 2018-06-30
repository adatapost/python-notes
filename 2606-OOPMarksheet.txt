Example: Marksheet-1

class Student:
    """To represent student data """
    def __init__(self, roll=0, name=""):
        self.roll = roll
        self.name = name

class Subject:
    """To represent subject, total marks and ontain marks"""
    def __init__(self, name="", total=0, obtain=0):
        self.name = name
        self.total = total
        self.obtain = obtain

class Semester:
    """Semester and result of n subjects per semester"""
    def __init__(self, sem_no):
        self.sem_no = sem_no
        self.marks = []

    def add_mark(self, subject, total, obtain):
        self.marks.append( Subject(subject, total, obtain) )

class Marksheet:
    """Marksheet takes student object and set of semesters object"""
    def __init__(self, student):
        self.student = student
        self.semesters = []

    def add_sem(self, sem):
        self.semesters.append(sem)

    def disp(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)

        total_sem = len(self.semesters)
        # Print semester name horizontally
        s1 = ""
        for i in range(total_sem):
            s1 += "Semester\t\t"
        print(s1)
        print("--------------------------------------------------")
        
        s1 = ""
        for i in range(total_sem):
            s1 = s1 + str(self.semesters[i].sem_no) + "\t\t\t"
        print(s1)

        # Print first records of marks of each semester
        s1 = F"{self.semesters[0].marks[0].name} {self.semesters[0].marks[0].obtain}/{self.semesters[0].marks[0].total}"
        s1 += F"\t\t{self.semesters[1].marks[0].name} {self.semesters[1].marks[0].obtain}/{self.semesters[1].marks[0].total}"
        s1 += F"\t\t{self.semesters[2].marks[0].name} {self.semesters[2].marks[0].obtain}/{self.semesters[2].marks[0].total}"
        print(s1)

        # Print second records of marks of each semester
        s1 = F"{self.semesters[0].marks[1].name} {self.semesters[0].marks[1].obtain}/{self.semesters[0].marks[1].total}"
        s1 += F"\t\t{self.semesters[1].marks[1].name} {self.semesters[1].marks[1].obtain}/{self.semesters[1].marks[1].total}"
        s1 += F"\t\t{self.semesters[2].marks[1].name} {self.semesters[2].marks[1].obtain}/{self.semesters[2].marks[1].total}"
        print(s1)

        # Print third records of marks of each semester
        s1 = F"{self.semesters[0].marks[2].name} {self.semesters[0].marks[2].obtain}/{self.semesters[0].marks[2].total}"
        s1 += F"\t\t{self.semesters[1].marks[2].name} {self.semesters[1].marks[2].obtain}/{self.semesters[1].marks[2].total}"
        s1 += F"\t\t{self.semesters[2].marks[2].name} {self.semesters[2].marks[2].obtain}/{self.semesters[2].marks[2].total}"
        print(s1)

# Test - 1
s1 = Student(10, "Reena")
mk = Marksheet(s1)

sem1 = Semester(1)
sem2 = Semester(2)
sem3 = Semester(3)

# add sems to marksheet object
mk.add_sem(sem1)
mk.add_sem(sem2)
mk.add_sem(sem3)

sem1.add_mark("A1", 100, 78)
sem1.add_mark("A2",100,60)
sem1.add_mark("A3",100,80)

sem2.add_mark("S1", 50, 45)
sem2.add_mark("S2", 50, 41)
sem2.add_mark("S3", 50, 45)

sem3.add_mark("P1", 50, 35)
sem3.add_mark("P2", 50, 40)
sem3.add_mark("P3", 50, 35)

mk.disp()


Example: Marksheet - 2

class Student:
    """To represent student data """
    def __init__(self, roll=0, name=""):
        self.roll = roll
        self.name = name

class Subject:
    """To represent subject, total marks and ontain marks"""
    def __init__(self, name="", total=0, obtain=0):
        self.name = name
        self.total = total
        self.obtain = obtain
    def get(self):
        return F"{self.name} {self.obtain}/{self.total}"

class Semester:
    """Semester and result of n subjects per semester"""
    def __init__(self, sem_no):
        self.sem_no = sem_no
        self.marks = []

    def add_mark(self, subject, total, obtain):
        self.marks.append( Subject(subject, total, obtain) )
    def get(self,index):
        return F"{self.marks[index].get()}"
        
        

class Marksheet:
    """Marksheet takes student object and set of semesters object"""
    def __init__(self, student):
        self.student = student
        self.semesters = []

    def add_sem(self, sem):
        self.semesters.append(sem)

    def disp(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)

        total_sem = len(self.semesters)
        # Print semester name horizontally
        s1 = ""
        for i in range(total_sem):
            s1 += "Semester\t\t"
        print(s1)
        print("--------------------------------------------------")
        
        s1 = ""
        for i in range(total_sem):
            s1 = s1 + str(self.semesters[i].sem_no) + "\t\t\t"
        print(s1)

        # Print all records of marks of each semester
        for i in range(total_sem):
            s1 = F"{self.semesters[0].get(i)}"
            s1 += F"\t\t{self.semesters[1].get(i)}"
            s1 += F"\t\t{self.semesters[2].get(i)}"
            print(s1)

# Test - 1
s1 = Student(10, "Reena")
mk = Marksheet(s1)

sem1 = Semester(1)
sem2 = Semester(2)
sem3 = Semester(3)

# add sems to marksheet object
mk.add_sem(sem1)
mk.add_sem(sem2)
mk.add_sem(sem3)

sem1.add_mark("A1", 100, 78)
sem1.add_mark("A2",100,60)
sem1.add_mark("A3",100,80)

sem2.add_mark("S1", 50, 45)
sem2.add_mark("S2", 50, 41)
sem2.add_mark("S3", 50, 45)

sem3.add_mark("P1", 50, 35)
sem3.add_mark("P2", 50, 40)
sem3.add_mark("P3", 50, 35)

mk.disp()


Example: Marksheet - 3

class Student:
    """To represent student data """
    def __init__(self, roll=0, name=""):
        self.roll = roll
        self.name = name

class Subject:
    """To represent subject, total marks and ontain marks"""
    def __init__(self, name="", total=0, obtain=0):
        self.name = name
        self.total = total
        self.obtain = obtain
    def get(self):
        return F"{self.name} {self.obtain}/{self.total}"

class Semester:
    """Semester and result of n subjects per semester"""
    def __init__(self, sem_no):
        self.sem_no = sem_no
        self.marks = []

    def add_mark(self, subject, total, obtain):
        self.marks.append( Subject(subject, total, obtain) )
    def get(self,index):
        return F"{self.marks[index].get()}"

class Marksheet:
    """Marksheet takes student object and set of semesters object"""
    def __init__(self, student):
        self.student = student
        self.semesters = []

    def add_sem(self, sem):
        self.semesters.append(sem)

    def disp(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)

        total_sem = len(self.semesters)
        # Print semester name horizontally
        s1 = ""
        for i in range(total_sem):
            s1 += "Sem\t\t"
        print(s1)
        print("--------------------------------------------------")
        
        s1 = ""
        for i in range(total_sem):
            s1 = s1 + str(self.semesters[i].sem_no) + "\t\t"
        print(s1)

        # Print all records of marks of each semester
        total_sub = len(self.semesters[0].marks)
        for i in range(total_sub):
            s1 = ""
            for j in range(total_sem):
                s1 += F"{self.semesters[j].get(i)}\t"
            print(s1)

# Test - 1
s1 = Student(10, "Reena")
mk = Marksheet(s1)

sem1 = Semester(1)
sem2 = Semester(2)
sem3 = Semester(3)
sem4 = Semester(4)

# add sems to marksheet object
mk.add_sem(sem1)
mk.add_sem(sem2)
mk.add_sem(sem3)
mk.add_sem(sem4)

sem1.add_mark("A1", 100, 78)
sem1.add_mark("A2",100,60)
sem1.add_mark("A3",100,80)

sem2.add_mark("S1", 50, 45)
sem2.add_mark("S2", 50, 41)
sem2.add_mark("S3", 50, 45)

sem3.add_mark("P1", 50, 35)
sem3.add_mark("P2", 50, 40)
sem3.add_mark("P3", 50, 35)

sem4.add_mark("R1", 50, 35)
sem4.add_mark("R2", 50, 40)
sem4.add_mark("R3", 50, 35)

mk.disp()


Example: Marksheet - 4


class Student:
    """To represent student data """
    def __init__(self, roll=0, name=""):
        self.roll = roll
        self.name = name

class Subject:
    """To represent subject, total marks and ontain marks"""
    def __init__(self, name="", total=0, obtain=0):
        self.name = name
        self.total = total
        self.obtain = obtain
    def get(self):
        return F"{self.name} {self.obtain}/{self.total}"

class Semester:
    """Semester and result of n subjects per semester"""
    def __init__(self, sem_no):
        self.sem_no = sem_no
        self.marks = []

    def add_mark(self, subject, total, obtain):
        self.marks.append( Subject(subject, total, obtain) )
    def get(self,index):
        return F"{self.marks[index].get()}"

class Marksheet:
    """Marksheet takes student object and set of semesters object"""
    def __init__(self, student):
        self.student = student
        self.semesters = []

    def add_sem(self, sem):
        self.semesters.append(sem)

    def disp(self):
        print("Roll : ", self.student.roll)
        print("Name : ", self.student.name)

        total_sem = len(self.semesters)
        # Print semester name horizontally
        s1 = ""
        for i in range(total_sem):
            s1 += "Sem\t\t"
        print(s1)
        print("--------------------------------------------------")
        
        s1 = ""
        for i in range(total_sem):
            s1 = s1 + str(self.semesters[i].sem_no) + "\t\t"
        print(s1)

        # Print all records of marks of each semester
        total_sub = len(self.semesters[0].marks)
        for i in range(total_sub):
            s1 = ""
            for j in range(total_sem):
                s1 += F"{self.semesters[j].get(i)}\t"
            print(s1)

class Result:
    def __init__(self,roll = 0, name = ""):
        self.student  =  Student(roll, name )
        self.mk = Marksheet(self.student)

    def show(self):
        self.mk.disp()
    def add_sem(self,sem_no):
        self.mk.add_sem( Semester(sem_no) )
    def get_sem(self,index):
        return self.mk.semesters[index]
    def add_mark(self,index, subject, total, obtain):
        self.get_sem(index).add_mark( subject, total, obtain )


# Test 

p = Result(10,"Reena")
p.add_sem(5)
p.add_sem(6)
p.add_sem(7)

p.get_sem(0).add_mark("A1",100,40)
p.add_mark(0,"A2",100,47)
p.add_mark(0,"A3",100,80)

p.add_mark(1,"P1", 100, 40)
p.add_mark(1,"P2", 100, 47)
p.add_mark(1,"P1", 100, 80)

p.get_sem(2).add_mark("R1", 100, 40)
p.get_sem(2).add_mark("R2", 100, 47)
p.get_sem(2).add_mark("R1", 100, 80)

p.show()




