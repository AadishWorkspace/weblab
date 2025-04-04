class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store item details
    
    def add_item(self, item_id, item_name, stock_count, price):
        if item_id in self.items:
            print("Item ID already exists.")
        else:
            self.items[item_id] = {
                "item_name": item_name,
                "stock_count": stock_count,
                "price": price
            }
            print("Item added successfully!")
    
    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]["stock_count"] = stock_count
            if price is not None:
                self.items[item_id]["price"] = price
            print("Item updated successfully!")
        else:
            print("Item ID not found.")
    
    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item ID not found.")

# Example usage:
inventory = Inventory()
inventory.add_item(1, "Laptop", 10, 999.99)
inventory.add_item(2, "Phone", 20, 499.99)
inventory.update_item(1, stock_count=8)
print(inventory.check_item_details(1))
