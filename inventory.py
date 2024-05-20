from product import Product


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products

    def remove_product(self, name):
        self.products = [product for product in self.products if product.name != name]

    def total_products(self):
        return len(self.products)