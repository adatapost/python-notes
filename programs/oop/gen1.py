def simple_generator():
    cities = ["mehsana","Patan","Rajkot", "Surat"]      
    for c in cities:
        yield { c.title(), c.upper(), c.lower(), len(c) }
       

p1 = simple_generator()
p1_list = list( p1 )
p1_set = set( p1 )
print(p1)
print(p1_list)
print(p1_set)

  
    
