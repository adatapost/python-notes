# String literal concatenation " " "" ' '
name = "First String" "Second String" "Third String" 'Last String'
print(name)

first_name = "Reena"
last_name = "Mohan"

# Concat the strings object (variables) using + opertor

full_name =  first_name + last_name
print(full_name)
full_name = first_name + " " + last_name
print(full_name)

# Convert number or other type into string using str() built-in function
no = 100
print( type(no), no)
s1 = str(no)
print( type(s1), s1)

info = "My roll is " + str(no)
print(info)


