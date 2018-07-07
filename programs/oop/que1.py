class Question:
  def __init__(self,question,option1,option2,option3,correct_option):
      self.question = question
      self.option1 = option1
      self.option2 = option2
      self.option3 = option3
      self.correct_option = correct_option
      self.user_choice = 0
  def show(self):
      print("Question :", self.question)
      print("1. ", self.option1)
      print("2. ", self.option2)
      print("3. ", self.option3)
      self.user_choice = int(input("Enter choice : "))
  def is_correct(self):
      return self.correct_option ==   self.user_choice

# Test the code
#a = Question("What?","A","B","C",2)
#a.show()
# print("You're right!!") if a.is_correct() else print("You're wrong!!!")

qs = [Question("W","A","B","C",1), Question("R","","","",3)]
for a in qs:
    a.show()

for a in qs:
    print(a.question, a.is_correct())    
