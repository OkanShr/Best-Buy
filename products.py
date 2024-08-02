class Product:
    """
    A class that represents a product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        active (bool): Whether the product is active (in stock) or not.

    Methods:
        get_quantity() -> int:
            Returns the current quantity of the product.

        set_quantity(quantity):
            Sets the quantity of the product.
            If the quantity is set to 0, the product is deactivated.

        is_active() -> bool:
            Returns True if the product is active (quantity > 0),
            otherwise False.

        show() -> str:
            Returns a string representation of the product's name, price,
            and quantity.

        buy(quantity) -> float:
            Buys a given quantity of the product, updates the quantity,
            and returns the total price.
            Raises ValueError if the quantity is negative or
            exceeds the available stock.

        deactivate():
            Deactivates the product by setting its active status to False.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new instance of the Product class.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial quantity of the product.

        Raises:
            NameError: If name is an empty string.
            ValueError: If price or quantity is negative.
        """
        if not name:
            raise NameError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Returns whether the product is active (in stock) or not.
        """
        return self.active

    def show(self) -> str:
        """
        Returns a string representation of the product's name, price,
        and quantity.
        """
        return (f"{self.name}, Price: ${self.price:.2f},"
                f" Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product, updates the quantity,
        and returns the total price.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is negative
            or exceeds the available stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity can't be negative")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price

    def deactivate(self):
        """
        Deactivates the product by setting its active status to False.
        """
        self.active = False
