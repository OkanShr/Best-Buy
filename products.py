from abc import ABC, abstractmethod
from promotions import Promotion


class Product(ABC):
    """
    A class that represents a product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        promotion (Promotion): The promotion applied to the product (optional).
        is_active (bool): Whether the product is active or not.

    Methods:
        get_quantity() -> int:
            Returns the current quantity of the product.

        show() -> str:
            Returns a string representation of the product's
            name, price, quantity, and active status.

        buy(quantity) -> float:
            Buys a given quantity of the product, updates the quantity,
             and returns the total price.
            Prints an error message if the quantity is negative or
            exceeds the available stock.
            Deactivates the product when quantity reaches zero.

        set_promotion(promotion: Promotion):
            Sets a promotion to be applied to the product.

        remove_promotion():
            Removes the promotion from the product.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new instance of the Product class.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial quantity of the product.

        Raises:
            ValueError: If name is empty, price or quantity is negative.
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
        self.promotion = None  # No initial promotion
        self.is_active = True  # Product is active by default

    def is_active(self) -> bool:
        """
        Returns the status of the product
        """
        return self.is_active

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.
        """
        return self.quantity

    def show(self) -> str:
        """
        Returns a string representation of the product's name,
        price, quantity, and active status.
        """
        promotion_info = f" (Promotion: {self.promotion.name})" \
            if self.promotion else ""
        active_status = "Active" if self.is_active else "Inactive"
        return (f"{self.name}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}, "
                f"Status: {active_status}{promotion_info}")

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product, updates the quantity,
         and returns the total price.
        Applies any promotion if set.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        # Calculate the total price with promotion if applicable
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity -= quantity

        # Deactivate the product if quantity becomes zero
        if self.quantity == 0:
            self.is_active = False

        return total_price

    def set_promotion(self, promotion: Promotion):
        """
        Sets a promotion to be applied to the product.

        Args:
            promotion (Promotion): The promotion to apply to the product.
        """
        self.promotion = promotion

    def remove_promotion(self):
        """
        Removes the promotion from the product.
        """
        self.promotion = None


class NonStockedProduct(Product):
    """
    A class that represents a non-stocked product, inherits from Product.
    Non-stocked products have a fixed price and quantity of 1.
    """

    def __init__(self, name, price):
        """
        Initializes a new instance of NonStockedProduct.

        Args:
            name (str): The name of the non-stocked product.
            price (float): The price of the non-stocked product.
        """
        super().__init__(name, price, quantity=1)

    def buy(self, quantity) -> float:
        """
        Override the buy method for non-stocked products to always
        return the fixed price.
        Applies any promotion if set.

        Args:
            quantity (int): The quantity of the non-stocked product to "buy".

        Returns:
            float: The fixed price of the non-stocked product.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")

        # Apply promotion if set
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            return self.price

        return total_price

    def show(self) -> str:
        """
        Override the show method to include the price.
        """
        promotion_info = f" (Promotion: {self.promotion.name})" \
            if self.promotion else ""
        active_status = "Active" if self.is_active else "Inactive"
        return (f"{self.name}, Price: ${self.price:.2f}, "
                f"Status: {active_status}{promotion_info}")


class LimitedProduct(Product):
    """
    A class that represents a limited quantity product, inherits from Product.
    Limited products have a maximum quantity that can be purchased.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a new instance of LimitedProduct.

        Args:
            name (str): The name of the limited product.
            price (float): The price of the limited product.
            quantity (int): The initial quantity of the limited product.
            maximum (int): The maximum quantity of the limited product
             that can be purchased.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """
        Override the buy method for limited products to check against
         the maximum quantity.
        Applies any promotion if set.

        Args:
            quantity (int): The quantity of the limited product to buy.

        Returns:
            float: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")

        if quantity > self.maximum:
            raise ValueError(f"Maximum purchase quantity exceeded. "
                             f"Maximum is {self.maximum}")

        # Apply promotion if set
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity -= quantity

        # Deactivate the product if quantity becomes zero
        if self.quantity == 0:
            self.is_active = False

        return total_price

    def show(self) -> str:
        """
        Override the show method to include the maximum quantity and price.
        """
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        active_status = "Active" if self.is_active else "Inactive"
        return (f"{self.name}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}, Maximum: {self.maximum}, "
                f"Status: {active_status}{promotion_info}")
