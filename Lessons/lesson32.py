# Задача:
# Дано 2 списка:
# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
# Необходимо создать 2 генераторных сборки:
#
#     В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
#     В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения строк в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
#
#
# Пример результата выполнения программы:
# Пример выполнения кода:
# print(list(first_result))
# print(list(second_result))
# Вывод в консоль:
# [1, 2]
# [False, False, True]

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_word) - len(second_word) for first_word, second_word in zip(first, second) if
                len(first_word) != len(second_word))

second_result = (first_word == second_word for index, first_word in enumerate(first) for second_word in
                 second[index::len(first)])

# Вывод результатов
print(list(first_result))
print(list(second_result))
