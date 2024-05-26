from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply the promotion.

        Args:
            product (Product): The product on which the promotion is applied.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    A class representing a percentage discount promotion.
    """

    def __init__(self, name, percent):
        """
        Initializes a new instance of PercentDiscount.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount to apply (0-100).
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount promotion.

        Args:
            product (Product): The product on which the promotion is applied.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        original_price = product.price * quantity
        discount_amount = original_price * (self.percent / 100)
        discounted_price = original_price - discount_amount
        return discounted_price


class SecondHalfPrice(Promotion):
    """
    A class representing a second item at half price promotion.
    """

    def __init__(self, name):
        """
        Initializes a new instance of SecondHalfPrice.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the second item at half price promotion.

        Args:
            product (Product): The product on which the promotion is applied.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        if quantity < 2:
            return product.price * quantity

        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        discounted_price = (full_price_items * product.price +
                            half_price_items * (product.price / 2))
        return discounted_price


class ThirdOneFree(Promotion):
    """
    A class representing a buy 2, get 1 free promotion.
    """

    def __init__(self, name):
        """
        Initializes a new instance of ThirdOneFree.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the buy 2, get 1 free promotion.

        Args:
            product (Product): The product on which the promotion is applied.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.
        """
        full_price_items = quantity // 3 * 2
        free_items = quantity - full_price_items
        discounted_price = full_price_items * product.price
        return discounted_price
