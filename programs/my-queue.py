# Queue implementation using list - First In First Out
def push(queue, item):
    queue.append(item)

def pop(queue):
    queue.remove( queue[0] )

# Call the functions
nos = []
students = []

push(nos, 10)
push(nos, 20)
push(nos, 30)

pop(nos)
print(nos)
pop(nos)
print(nos)

push(students, (10, "Reena"))
push(students, (30, "Meena"))
push(students, (60, "Seena"))

print(students)
pop(students)
pop(students)
print(students)
