products = []
class Product:
    def __init__(self, product_name, brand_id, category_id, model_year, list_price):
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price
        products.append(self)
    def __repr__(self):
        return f"Product({self.product_name})"