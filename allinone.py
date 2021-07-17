class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
        
    def add_product(self, new_product):
        self.product_list.append(new_product.name)
        return self
    
    def inflation(self, percent_increase):
        Product.update_price(percent_change=percent_increase, is_increased=True)
    
    def set_clearance(self, category, percent_discount):
        self.category = category
        self.percent_discount = percent_discount * .01
    
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    
    def update_price (self, percent_change, is_increased):
        self.percent_change = percent_change * .01
        self.is_increased = is_increased
        
        if(self.is_increased == True):
            print(self.price)
            self.price += (self.price * self.percent_change)
            print(self.price)
            
        return self
    
    def print_info(self,):
        print(f"Product : {self.name} \nCategory : {self.category} \n Price : ${self.price}")
        return self
        

product1 = Product("Super Slicer 3000", 250, "Small Appliances")
product1.print_info()  
blender1 = Product("Mini Blender", 60, "Small Appliances")
store1 = Store("Fresh Market")
print(product1.name)
store1.add_product(product1)
store1.add_product(blender1)
print(store1.product_list)
blender1.update_price(20, True)



print(store1.product_list)