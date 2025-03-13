from model import OrderRepository
from view import OrderView
from viewmodel import OrderViewModel

def main():
    order_repository = OrderRepository()
    order_view = OrderView()
    order_view_model = OrderViewModel(order_repository, order_view)

    while True:
        print("\n1. Show all orders")
        print("2. Add new order")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            order_view_model.show_orders()
        elif choice == '2':
            order_view_model.add_new_order()
        elif choice == '3':
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()