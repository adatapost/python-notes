class Product:
    def __init__(self,name="",qty=0,unit="",rate=0):
        self.name = name
        self.qty = qty
        self.rate = rate
        self.unit = unit
    def amount(self):
        return self.qty * self.rate

class Bill:
    def __init__(self,bill_no=0,bill_date="",customer_name=""):
        self.bill_no = bill_no
        self.bill_date = bill_date
        self.customer_name = customer_name
        self.items = []

    def add_item(self,product):
        self.items.append( product )

    def input_item(self):
        self.add_item(Product(input("Name : "), int(input("Qty : ")),
                              input("Unit :"), int(input("Rate : "))))

    def show(self):
        print("--------------------------------------------------------------")    
        print("Bill No: ", self.bill_no,"           Bill Date : ",self.bill_date)
        print("--------------------------------------------------------------")
        print("#  Name                        Qty    Unit     Rate     Amount")
        print("--------------------------------------------------------------")
        count = 1
        total = 0
        for item in self.items:
            print(count,item.name,"\t\t", item.qty, "\t", item.unit, "\t",item.rate,"\t", item.amount() )
            count += 1
            total += item.amount()
        print("--------------------------------------------------------------")
        print("                                               Total : ", total)
        print("--------------------------------------------------------------")

# Main

a = Bill(10,"22-Jun-2018","Mr. A")
choice = "y"
while choice in ["y","yes","Y"]:
    a.input_item()
    choice = input("Want to continue... ?(yes/y/Y) : ")

a.show()



        
