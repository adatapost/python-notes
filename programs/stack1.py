# Sequential Search
nos = [10,2,33,-5,3,5,6,33,3,2]

search = int( input("Enter the no : "))
r = -1
count = nos.count(search)  # Returns occurences 
if count!=0:
    for i in range(count):
      r = nos.index(search, r+1)
      print(f"Found at {r}")
else:
    print("Not found")

    

 

 
