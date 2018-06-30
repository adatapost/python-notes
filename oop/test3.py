class MyCalc:
    def __init__(self):
        self.no = 0
    def add(self,no):
        self.no += no
        return self
    def mul(self,no):
        self.no *= no
        return self
    def show(self):
        print(self.no)
        return self

MyCalc().add(30).add(20).add(-5).show().mul(2).show()

