def print_nos(no1,no2):
    if no1>no2:
        print_nos(no2,no1)
    print(no1)
    if no1<no2:
        print_nos(no1+1, no2) 

print_nos(1,5)        


 
