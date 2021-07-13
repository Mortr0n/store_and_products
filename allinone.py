class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
        
    def add_product(self, new_product):
        
    
    
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price (self, percent_change, is_increased):
        self.percent_change = percent_change
        self.is_increased = is_increased
        
        if(self.is_increased == True):
            self.price += (self.price * self.percent_change)
    
    def print_info(self,):
        print(f"Product : {self.name} \nCategory : {self.category} \n Price : ${self.price}")
        

product1 = Product("Super Slicer 3000", 250, "Small Appliances")
product1.print_info()