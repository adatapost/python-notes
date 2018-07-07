def question_paper():
    questions = []
    result = []
    correct = 0
    questions.append(["Question1?", "Op1", "Op2", "Op3", 1,0])
    questions.append(["Question2?", "Op11", "Op21", "Op31", 2,0])
    questions.append(["Question3?", "Op12", "Op22", "Op32", 3,0])
    for a in questions:
        print(a[0])
        print("\t1.",a[1])
        print("\t2.", a[2])
        print("\t3.", a[3])
        a[5] = int(input("Enter the choice : "))
        message = "Correct" if a[4] == a[5] else "Incorrect"
        if a[4] == a[5]:
            correct+=1
        result.append(F"Answer of question({a[0]}) is {message} ")
    result.append(F"Total correct answers : {correct}")
    result.append(F"Total incorrect answers : {(len(questions)-correct)}")
    result.append( round( correct / len(questions) * 100,2 ) )
    for m in result:
        print(m)        
     
        
question_paper()
