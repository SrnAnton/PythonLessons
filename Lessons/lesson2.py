# Напишите 4 переменных которые буду обозначать следующие данные:
#
#     Количество выполненных ДЗ (запишите значение 12)
#     Количество затраченных часов (запишите значение 1.5)
#     Название курса (запишите значение 'Python')
#     Время на одно задание (вычислить используя 1 и 2 переменные)
#
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

completed_tasks = 12
time = 1.5
course_name = 'Python'
time_spent = time / completed_tasks
result = f"Курс: {course_name}, всего задач: {completed_tasks}, затрачено часов: {time}, среднее время выполнения {time_spent} часа."
print(result)
