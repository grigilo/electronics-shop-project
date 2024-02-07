class Phone:
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        return self.quantity + other.quantity
