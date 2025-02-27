def main():
    from customers import Customer
    from staffs import Staff
    from orders import Order
    from stores import Store
    from order_items import OrderItem
    from categories import Category
    from products import Product
    from stocks import Stock
    from brands import Brand
    
    customer = Customer(1, "name", "la_st_name", "1234567890", "name@example.com", "123 Street", "City", "State", "000000")
    print(f"Customer: {customer.first_name} {customer.last_name}")
    
    order = Order(101, 1, "Shipped", "2023-01-01", "2023-01-05", "2023-01-04", 10, 5)
    print(f"Order ID: {order.order_id}, Status: {order.order_status}, Customer ID: {order.customer_id}")
    

main()
