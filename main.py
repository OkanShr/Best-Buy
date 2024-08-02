import store
from products import Product


def list_products(store_obj):
    """
    Display all products currently available in the store.

    Args:
        store_obj (Store): The Store object containing the products to display.
    """
    print("\nProducts in store:")
    store_obj.show_products()


def show_total_quantity(store_obj):
    """
    Display the total quantity of all products in the store.

    Args:
        store_obj (Store): The Store object containing the products.

    Prints:
        The total quantity of all products in the store.
    """
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal quantity of all products in store: {total_quantity}")


def make_order(store_obj):
    """
    Allow the user to make an order by selecting products and quantities.

    Args:
        store_obj (Store): The Store object containing the products to order.

    Prompts the user to select products and their quantities,
    and prints the total price of the order.
    """
    shopping_list = []
    print("\nSelect products to order:")
    products = store_obj.get_all_products()
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")
    print("0. Done ordering")

    while True:
        selection = input("Enter product number "
                          "to order (0 to finish): ").strip()
        if selection == "0":
            break
        try:
            selection = int(selection)
            if 1 <= selection <= len(products):
                product_to_order = products[selection - 1]
                qty_to_order = int(input(f"Enter quantity for "
                                         f"'{product_to_order.name}'"
                                         f": ").strip())
                shopping_list.append((product_to_order, qty_to_order))
            else:
                print("Invalid selection. "
                      "Please enter a valid product number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        total_price = store_obj.order(shopping_list)
        print(f"\nTotal price of the order: ${total_price:.2f}")


def start(store_obj):
    """
    Function to start the store management system.

    Args:
        store_obj (Store): The Store object to manage.

    Displays a menu-driven interface for the user to interact with the store:
        1. List all products in store
        2. Show total quantity in store
        3. Make an order
        4. Quit
    """
    menu_options = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order,
    }

    while True:
        print("\n===== Welcome to the Store Management System =====")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "4":
            print("Thank you for using the Store Management System. Goodbye!")
            break

        selected_option = menu_options.get(choice)
        if selected_option:
            selected_option(store_obj)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()
