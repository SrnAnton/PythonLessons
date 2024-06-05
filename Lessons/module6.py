from Lessons.modules.circle import Circle
from Lessons.modules.cube import Cube
from Lessons.modules.triangle import Triangle

# a = Triangle()
# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77)  # Изменится
# cube1.set_color(300, 70, 15)  # Не изменится
# print(circle1.get_color())
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменитсяa
# circle1.set_sides(15)  # Изменится
# print(cube1.get_sides())
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

figures = [Circle(5, (250, 240, 230)), Triangle((3, 4, 6), (100, 110, 120)), Cube(1, (90, 90, 90))]

for figure in figures:
    print(figure)
    print(f"Площадь: {figure.get_square()}")
    print(f"Длина/Периметр: {len(figure)}")
    print(f"Стороны: {figure.get_sides()}")
    print(f"Количесто сторон: {figure.sides_count}")
    print(f"Цвет: {figure.get_color()}")

    if isinstance(figure, Cube):
        print(f"Объем: {figure.get_volume()}")

    if isinstance(figure, Circle):
        print(f"Радиус: {figure.get_radius()}")

    if isinstance(figure, Triangle):
        print(f"Высота: {figure.get_height()}")

    print()
