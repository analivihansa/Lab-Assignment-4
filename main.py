from product import Product
from inventory import Inventory
from supplier import Supplier

def main():

    store_inventory = Inventory()

    product1 = Product("Orange", 0.80, 200)
    product2 = Product("Banana", 0.30, 150)
    product3 = Product("Apple", 0.50, 100)

    store_inventory.add_product(product1)
    store_inventory.add_product(product2)
    store_inventory.add_product(product3)

    print("Products in inventory:")
    for product in store_inventory.list_products():
        print(product)

    print(f"Total number of products: {store_inventory.total_products()}")

    store_inventory.remove_product("Banana")
    print("Products in inventory after removing Banana:")
    for product in store_inventory.list_products():
        print(product)

    print(f"Total number of products after removal: {store_inventory.total_products()}")
    
    supplier = Supplier("Fresh Fruits Ltd.")
    supplier.add_product(apple)
    supplier.add_product(orange)

    print("Supplier details:")
    print(supplier)

    print("Products supplied by the supplier:")
    for product in supplier.list_products():
        print(product)


if __name__ == "__main__":
    main()

