from typing import List, Tuple
from products import Product


class Store:
    """
    A class that represents a store containing products.

    Attributes:
        products (List[Product]): A list of products in the store.

    Methods:
        add_product(product):
            Adds a product to the store's inventory.

        remove_product(product):
            Removes a product from the store's inventory.

        show_products():
            Displays details of all products in the store.

        get_total_quantity() -> int:
            Returns the total quantity of all products in the store.

        get_all_products() -> List[Product]:
            Returns a list of all active products in the store.

        order(shopping_list: List[Tuple[Product, int]]) -> float:
            Processes an order for a list of products and their quantities,
            and returns the total price.
            Raises ValueError if any product in the shopping list is not found in the store.
    """

    def __init__(self, products=None):
        """
        Initializes a new instance of the Store class.

        Args:
            products (List[Product], optional): The initial
            list of products in the store. Defaults to None.
        """
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If the product is not of type Product.
        """
        if not isinstance(product, Product):
            raise ValueError("Not of type Product")
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        Args:
            product (Product): The product to remove.

        Raises:
            ValueError: If the product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store")

    def show_products(self):
        """
        Displays details of all products in the store.
        """
        for product in self.products:
            print(product.show())

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[Product]: A list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if isinstance(product, Product) and product.get_quantity() > 0:
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order for a list of products and their quantities,
        and returns the total price.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples,
                where each tuple contains a Product and an integer quantity.

        Returns:
            float: The total price of the order.

        Raises:
            ValueError: If any product in the shopping list is not found in the store.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} not found in store")
            total_price += product.buy(quantity)
        return total_price
