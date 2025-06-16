class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item_id, name, quantity, price):
        if any(item['id'] == item_id for item in self.inventory):
            print("❌ Item ID already exists.")
            return
        self.inventory.append({
            'id': item_id,
            'name': name,
            'quantity': quantity,
            'price': price
        })
        print("✅ Item added.")

    def remove_item(self, item_id):
        for item in self.inventory:
            if item['id'] == item_id:
                self.inventory.remove(item)
                print("✅ Item removed.")
                return
        print("❌ Item not found.")

    def update_quantity(self, item_id, new_quantity):
        for item in self.inventory:
            if item['id'] == item_id:
                item['quantity'] = new_quantity
                print("✅ Quantity updated.")
                return
        print("❌ Item not found.")

    def view_inventory(self):
        if not self.inventory:
            print("📦 Inventory is empty.")
        else:
            print("\n📦 Current Inventory:")
            for item in self.inventory:
                print(f"  ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    manager = InventoryManager()

    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            item_id = input("Enter item ID: ").strip()
            name = input("Enter item name: ").strip()
            quantity = get_valid_int("Enter quantity: ")
            price = get_valid_float("Enter price: ")
            manager.add_item(item_id, name, quantity, price)

        elif choice == '2':
            item_id = input("Enter item ID to remove: ").strip()
            manager.remove_item(item_id)

        elif choice == '3':
            item_id = input("Enter item ID to update: ").strip()
            new_quantity = get_valid_int("Enter new quantity: ")
            manager.update_quantity(item_id, new_quantity)

        elif choice == '4':
            manager.view_inventory()

        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
