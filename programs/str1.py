# Convert Unicode to Bytes and Bytes to Unicode
name = "હેલ્લો"   # Instance of str class
print( name[5] )
print( len(name))

# convert str (unicode) to bytes
name_b = name.encode()
print(name_b)
print( len(name_b) )
# convert bytes to unicode
name_u = name_b.decode()
print( name_u)


 
