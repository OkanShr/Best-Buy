import store
from products import Product


def start(store_obj):
    while True:
        print("\n===== Welcome to the Store Management System =====")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\nProducts in store:")
            store_obj.show_products()

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal quantity of all products in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            print("\nSelect products to order:")
            products = store_obj.get_all_products()
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")
            print("0. Done ordering")

            while True:
                selection = input("Enter product number to order (0 to finish): ").strip()
                if selection == "0":
                    break
                try:
                    selection = int(selection)
                    if 1 <= selection <= len(products):
                        product_to_order = products[selection - 1]
                        quantity_to_order = int(input(f"Enter quantity for '{product_to_order.name}': ").strip())
                        shopping_list.append((product_to_order, quantity_to_order))
                    else:
                        print("Invalid selection. Please enter a valid product number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if shopping_list:
                total_price = store_obj.order(shopping_list)
                print(f"\nTotal price of the order: ${total_price:.2f}")

        elif choice == "4":
            print("Thank you for using the Store Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)

# Start the user interface
start(best_buy)
