# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
#
#     Функция count_calls подсчитывающая вызовы остальных функций.
#     Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
#     Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#
# Пункты задачи:
#
#     Создать переменную calls = 0 вне функций.
#     Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
#     Создать функцию string_info с параметром string и реализовать логику работы по описанию.
#     Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
#     Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
#     Вывести значение переменной calls на экран(в консоль).

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(s):
    count_calls()
    return len(s), s.upper(), s.lower()


def is_contains(s, lst):
    count_calls()
    return any(s.lower() in item.lower() for item in lst)


# Вызов функции count_calls
print(calls)

input_string = "Hello, World!"
result = string_info(input_string)
print(f"Длина строки: {result[0]}")
print(f"Строка в верхнем регистре: {result[1]}")
print(f"Строка в нижнем регистре: {result[2]}")

# Вызов функции is_contains
search_list = ["hello", "world", "python"]
search_string = "Hello"
if is_contains(search_string, search_list):
    print("Строка 'Hello' содержится в списке.")
else:
    print("Строка 'Hello' не содержится в списке.")

print(calls)
