import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_sum = self.price * self.quantity
        return total_sum

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        проверка длины наименования
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """
        инициализирующий экземпляры класса
        """
        cls.all = []
        with open(csv_file, encoding="windows-1251") as f:
            data = csv.DictReader(f)
            for i in data:
                cls(str(i['name']), float(i['price']), int(i['quantity']))

    @staticmethod
    def string_to_number(str_num):
        """
        статический метод, возвращающий число из числа-строки
        """
        number = float(str_num)
        return int(number)

