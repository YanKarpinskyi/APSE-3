class OrderViewModel:
    def __init__(self, order_repository, order_view):
        self.order_repository = order_repository
        self.order_view = order_view

    def show_orders(self):
        orders = self.order_repository.get_all_orders()
        self.order_view.show_all_orders(orders)

    def add_new_order(self):
        customer_name, product, quantity = self.order_view.get_order_details()
        self.order_repository.add_order(customer_name, product, quantity)
        print("Order added successfully!")