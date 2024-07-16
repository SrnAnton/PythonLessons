# Даны несколько списков, состоящих из строк
# first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#
#     В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
#     В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
#     В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.
#
#
# Пример результата выполнения программы:
# Пример выполнения кода:
# print(first_result)
# print(second_result)
# print(third_result)
# Вывод на консоль:
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Создание списка с длиной строк из first_strings, где длина строк не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Создание списка пар слов одинаковой длины из first_strings и second_strings
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# Создание словаря с парами ключ-значение, где ключ - строка, а значение - длина строки
# Условие записи пары в словарь - чётная длина строки
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
