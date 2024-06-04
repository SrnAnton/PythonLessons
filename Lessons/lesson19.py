# Ваша задача:
#
#     Создайте новый класс Buiding с атрибутом total
#     Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
#     В цикле создайте 40 объектов класса Building и выведите их на экран командой print
#     Полученный код напишите в ответ к домашнему заданию

class Building:
    total = 0

    def __init__(self):
        Building.total += 1

    def __repr__(self):
        return f"Object #{Building.total}"


buildings = [Building() for _ in range(40)]
for building in buildings:
    print(building)

one_other_building = Building()

print(Building.total)
