class Data:
    def __init__(self):
        self.message = ""
    def show(self):
        print(self.message)
        return self
        
    def set(self,message):
        self.message = message
        return self
        
    def append(self,message):
        self.message = self.message + message
        return self
        

q = Data().set("Hi").append(" Reena!").show().show().append("\nI'm Meena! How are you?").show()
 
