# Ваша задача:
#
#     Создайте новую функцию def test_function
#     Создайте другую функцию внутри функции inner_function, функция должна печатать значение "Я в области видимости функции test_function"
#     Вызовите функцию inner_function внутри функции test_function
#     Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
#     Полученный код напишите в ответ к домашему заданию

def test_function():
    print("Я вызываю функцию inner_function")

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
print()

try:
    inner_function()
except NameError as e:
    print("Ошибка:", e)
