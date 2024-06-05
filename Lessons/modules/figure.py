import abc


# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
#
#     Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
#     Атрибуты(публичные): filled(закрашенный, bool)

# И методами:
#
#     Метод get_color, возвращает список RGB цветов.
#     Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
#     Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
#     Метод set_sides принимает неограниченное кол-во сторон, проверяет корректность переданных данных, если данные корректны, то меняет __sides на новый список, если нет, то оставляет прежние.
#     Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
#     Метод __len__ должен возвращать периметр фигуры.

class Figure(abc.ABC):
    def __init__(self, sides=None, color=(0, 0, 0)):

        if sides is None:
            sides = [0]

        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r=None, g=None, b=None):
        if r is not None and g is not None and b is not None:
            if self.__is_valid_color(r, g, b):
                self.__color = [r, g, b]
            else:
                print("Некорректные данные цвета.")
        else:
            print("Необходимо указать все три компонента цвета.")

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        valid_sides = [side for side in sides if 0 < side]
        if len(valid_sides) == self.sides_count:
            self.__sides = valid_sides
        else:
            print("Некорректное количество сторон.")

    @property
    def sides_count(self):
        return len(self.__sides)

    @abc.abstractmethod
    def get_square(self):
        pass

    def __len__(self):
        return sum(self.__sides)

    def __repr__(self):
        return f"{self.__class__.__name__}"
