a = 10

def test():
    global a
    a = 50  
    print(a) 

print(a)
test()  
print(a)  

 