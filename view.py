class OrderView:
    def show_all_orders(self, orders):
        if not orders:
            print("No orders found.")
        else:
            for order in orders:
                print(order)

    def get_order_details(self):
        customer_name = input("Enter customer name: ")
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        return customer_name, product, quantity