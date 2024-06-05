from Lessons.modules.figure import Figure


# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure.
#     Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
#     Метод get_volume, возвращает объём куба.

class Cube(Figure):

    def __init__(self, side_size=1, color=(0, 0, 0)):
        super().__init__([side_size] * 12, color)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def get_square(self):
        return 6 * self.get_sides()[0] ** 2

    def __len__(self):
        return 12 * self.get_sides()[0]
