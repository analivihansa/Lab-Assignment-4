from product import Product
from inventory import Inventory


def main():

    store_inventory = Inventory()

    product1 = Product("Apple", 0.50, 100)
    product2 = Product("Banana", 0.30, 150)

    store_inventory.add_product(product1)
    store_inventory.add_product(product2)

    print("Products in inventory:")
    for product in store_inventory.list_products():
        print(product)

    print(f"Total number of products: {store_inventory.total_products()}")


