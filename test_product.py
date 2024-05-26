import pytest
from products import Product


def test_create_normal_product():
    # Test that creating a normal product works
    product = Product("Test Product", price=10.0, quantity=5)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.quantity == 5
    assert product.is_active == True


def test_create_product_with_invalid_details():
    # Test that creating a product with invalid details (empty name, negative price) invokes an exception
    with pytest.raises(NameError):
        Product("", price=10.0, quantity=5)
    with pytest.raises(ValueError):
        Product("Test Product", price=-10.0, quantity=5)
    with pytest.raises(ValueError):
        Product("Test Product", price=10.0, quantity=-5)


def test_product_becomes_inactive_when_quantity_is_zero():
    # Test that when a product reaches 0 quantity, it becomes inactive
    product = Product("Test Product", price=10.0, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active == False


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    # Test that product purchase modifies the quantity and returns the right output
    product = Product("Test Product", price=10.0, quantity=5)
    total_price = product.buy(2)
    assert total_price == 20.0
    assert product.get_quantity() == 3


def test_buying_larger_quantity_than_exists_invokes_exception():
    # Test that buying a larger quantity than exists invokes an exception
    product = Product("Test Product", price=10.0, quantity=5)
    with pytest.raises(ValueError):
        product.buy(6)

# pytest test_product.py
