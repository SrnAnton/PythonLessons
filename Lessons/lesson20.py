# Ваша задача:
#
#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и метод def horse_powers, которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите метод horse_powers
#     Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите метод horse_powers

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Неизвестно"


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000

    def horse_powers(self):
        return "200"


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1200000

    def horse_powers(self):
        return "150"


# Пример создания объекта и вызова методов
my_car = Nissan()
print(f"Цена автомобиля Nissan: {my_car.price}")
print(f"Мощность двигателя автомобиля Nissan: {my_car.horse_powers()}")

my_other_car = Kia()
print(f"Цена автомобиля Kia: {my_other_car.price}")
print(f"Мощность двигателя автомобиля Kia: {my_other_car.horse_powers()}")
