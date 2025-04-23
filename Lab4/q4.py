class Restaurant:
    def __init__(self):
        self.menu_items = {}  # Dictionary to store menu items (name: price)
        self.book_table = []  # List to store booked table numbers
        self.customer_orders = []  # List to store customer orders
    
    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"{item_name} added to menu for ${price}")
    
    def book_tables(self, table_number):
        if table_number in self.book_table:
            print(f"Table {table_number} is already booked.")
        else:
            self.book_table.append(table_number)
            print(f"Table {table_number} booked successfully!")
    
    def customer_order(self, table_number, order_items):
        if table_number not in self.book_table:
            print(f"Table {table_number} is not booked.")
        else:
            self.customer_orders.append({"table_number": table_number, "order": order_items})
            print(f"Order placed for Table {table_number}: {order_items}")
    
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")
    
    def print_table_reservations(self):
        print("Booked Tables:", self.book_table)
    
    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['order']}")

# Example usage:
restaurant = Restaurant()
restaurant.add_item_to_menu("Pasta", 12.99)
restaurant.add_item_to_menu("Pizza", 15.99)
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.customer_order(1, ["Pasta", "Pizza"])
restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
