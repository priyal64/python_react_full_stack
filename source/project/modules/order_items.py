class OrderItem:
    def __init__(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_id = order_id
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount
