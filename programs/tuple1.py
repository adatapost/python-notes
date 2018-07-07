# Tuples represent student records
students = (10,"Reena",(55,66,77,88,44)),(40, "Seena", (55, 66, 37, 86, 44))
for student in students:
    for p in student[:2]:
       print(p, end = "  ") 
    total = 0
    for m in student[2]:
        print(m, end = " ")
        total += m
    print(" = ",total)        
    
