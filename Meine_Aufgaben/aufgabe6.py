class MyShop:
 
    def __init__(self):
        self.product = []

    def checkitem(self, name):
        for i in self.product:
            if name == i[0]:
                return True
        return False

        
    def additem(self, name, cost):
        if self.checkitem(name):
            print(f"{name} schon vorhanden")
        else:    
            self.product.append ([name, cost]) 
            print(self.product)

    def __str__(self):
        return f"{self.product}"





shop=MyShop()
shop.additem ("Auto",1000)
shop.additem ("Auto",1000)
print (shop)