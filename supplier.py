class Supplier:
    def _init_(self, name, products=None):
        self.name = name
        self.products = products if products is not None else []

    def _str_(self):
        return f"Supplier: {self.name}, Products: {[product.name for product in self.products]}"

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def list_products(self):
        return self.products
