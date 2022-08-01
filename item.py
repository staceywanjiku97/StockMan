class Product:
    def __init__(self, product_name: str):
        self.product_id = -1
        self.name = product_name
    def print_name(self):
        print(self.name)
    def gen_id(self):
        print('Generating id')

   
if __name__ == "__main__":
    product = Product("Cooking Oil")
    product.nothing()
    product.print_name()