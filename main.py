import store


newProduct = store.product.Product("TV", 3000, "electronics")
test_store = store.Store("Fresh Market")
product1 = store.product.Product("Mouse", 60, "PC Peripherals")
test_store.add_product(newProduct)
newProduct.print_info()
test_store.add_product(product1)
test_store.sell_product(1)
print(test_store.product_list)