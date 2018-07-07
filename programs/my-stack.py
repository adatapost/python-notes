# Stack implementation using list
def push(stack,item):
    stack.append(item)

def pop(stack):
    stack.pop()

# Call the functions
stack_nos = []
stack_students = []

push(stack_nos,10)    
push(stack_nos,20)
push(stack_nos,30)

pop(stack_nos)
print( stack_nos)
pop(stack_nos)
print(stack_nos)

push(stack_students,(10,"Reena"))
push(stack_students, (30, "Meena"))
push(stack_students, (60, "Seena"))

print(stack_students)
pop(stack_students)
pop(stack_students)
print(stack_students)

