title = "Marksheet"
marks = [55,44,66,77,4]
subjects = ["Maths","Gujarati","English","Hindi","PT"]

print( title.center(40," ") )
print( "".center(40,"-"))
index = 0
for m in marks:
    #print( subjects[index], str(m).rjust(40 - len(subjects[index])," ") )
    print( subjects[index].ljust(30,"."), str(m).rjust(10,"*")  )
    index+=1
    
