import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def item1():
    return Phone("iPhone 14", 120000, 5, 2)


def test_init(item1):
    assert item1.name == "iPhone 14"
    assert item1.price == 120000
    assert item1.quantity == 5
    assert item1.number_of_sim == 2


def test__str__():
    item1 = Phone("iPhone 14", 120000, 5, 2)
    assert Phone.__str__(item1) == "iPhone 14"


def test__repr__():
    """
    Проверка магического метода repr
    """
    item1 = Phone("iPhone 14", 120000, 5, 2)
    assert Phone.__repr__(item1) == "Phone('iPhone 14', 120000, 5, 2)"


def test__add__():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item2 = Item("Смартфон", 10000, 20)
    assert Phone.__add__(phone1, item2) == 25


