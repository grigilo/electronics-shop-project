"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from config import ITEMS
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_name():
    """Тест проверки длины наименования товара (не больше 10 символов)"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "SkyPro университет"
    assert item1.name == "SkyPro уни"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класса из CSV файла"""
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки-числа"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("1.5") == 1


def test__repr__():
    """
    Проверка магического метода repr
    """
    item1 = Item("Смартфон", 10000, 20)
    assert Item.__repr__(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    """
    Проверка магического метода str
    """
    item1 = Item("Смартфон", 10000, 20)
    assert Item.__str__(item1) == 'Смартфон'


def test__add__():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item2 = Item("Смартфон", 10000, 20)
    assert Phone.__add__(item2, phone1) == 25


def test_instantiate_from_csv_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('')


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items_2.csv')
