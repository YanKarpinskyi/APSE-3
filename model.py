class Order:
    def __init__(self, order_id, customer_name, product, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Product: {self.product}, Quantity: {self.quantity}"

class OrderRepository:
    def __init__(self):
        self.orders = []
        self.next_order_id = 1

    def add_order(self, customer_name, product, quantity):
        order = Order(self.next_order_id, customer_name, product, quantity)
        self.orders.append(order)
        self.next_order_id += 1

    def get_all_orders(self):
        return self.orders