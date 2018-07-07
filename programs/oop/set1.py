students = []
students.append( {"roll": 10, "name": "Raj" })
students.append({"roll": 11, "name": "Raj1"})
students.append( {"roll": 12, "name": "Raj2" })

for p in students:
    for m in p:
        print(m, p[m])