from Lessons.modules.figure import Figure
import math


# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure
#     Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
#     Метод get_square возращает площадь круга (можно рассчитать как через длину, так и через радиус).

# я сделал наоборот

class Circle(Figure):

    def __init__(self, length=0, color=(0, 0, 0)):
        super().__init__([length], color)

        self.set_sides(self.__len__())

    def get_square(self):
        return math.pi * self.get_radius() ** 2

    def get_radius(self):
        return self.get_sides()[0] / (2 * math.pi)
