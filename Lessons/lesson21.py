# Ваша задача:
#
#     Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
#     Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Unknown"


class Nissan(Car, Vehicle):
    def __init__(self):
        Car.__init__(self)  # они тут не особо нужны
        Vehicle.__init__(self)  #

        self.price = 1500000
        self.vehicle_type = "car"

    def horse_powers(self):
        return "200"


my_car = Nissan()

print(f"Vehicle type: {my_car.vehicle_type}")
print(f"Price: {my_car.price}")
print(f"Horse powers: {my_car.horse_powers()}")
