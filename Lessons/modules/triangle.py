from Lessons.modules.figure import Figure
import math


# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure
#     Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
#     Метод get_square возращает площадь треугольника.

class Triangle(Figure):

    def __init__(self, sides=(1, 1, 1), color=(0, 0, 0)):
        if len(sides) != 3:
            sides = (1, 1, 1)

        super().__init__(sides, color)
        self.__height = self.calculate_triangle_height(*sides)

    @staticmethod
    def calculate_triangle_height(a, b, c):
        h_squared = a ** 2 + b ** 2 - c ** 2
        h = math.sqrt(abs(h_squared))
        return h

    def get_height(self):
        return self.__height

    def get_square(self):
        # Вычисляет площадь треугольника по формуле Герона.
        #  нет проверок на корректность сторон треугольника
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        s = (a + b + c) / 2.0
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
