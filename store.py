from product import Product
class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
        
    def sell_product(self, id):
        print(f"Removing {self.product_list[id]}")
        self.product_list.remove(self.product_list[id])
        
    def inflation(self, percent_increase):
        self.percent_increase = percent_increase * .001
    
    def set_clearance(self, category, percent_discount):
        self.category = category
        self.percent_discount = percent_discount * .01
        
        
        


new_store = Store("Albertsons")
new_store.add_product("TV")
new_store.add_product("Blender")
print(new_store.product_list)
# new_store.sell_product(1)
print(new_store.product_list)
for i in new_store.product_list:
    print(id(i))
  