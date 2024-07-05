# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
#
#     Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#     Примените os.path.join для формирования полного пути к файлам.
#     Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#     Используйте os.path.getsize для получения размера файла.
#     Используйте os.path.dirname для получения родительской директории файла.

import os
from pathlib import Path
from datetime import datetime


# Функция для вывода информации о файле
def print_file_info(file_path):
    # Получаем полный путь к файлу
    full_path = os.path.join(directory, file_path)
    # Проверяем, существует ли файл
    if os.path.exists(full_path):
        # Получаем размер файла
        file_size = os.path.getsize(full_path)
        # Получаем время последнего изменения файла
        last_modified = datetime.fromtimestamp(os.path.getmtime(full_path))
        # Выводим информацию о файле
        print(f"Файл: {file_path}")
        print(f"\tРазмер: {file_size} байт")
        print(f"\tПоследнее изменение: {last_modified}")
    else:
        print(f"Файл '{file_path}' не найден.")


# Переменная для хранения пути к каталогу
directory = input("Введите путь к каталогу: ")

# Обходим каталог с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем относительный путь к файлу
        relative_path = os.path.join(root, file)
        # Выводим информацию о файле
        print_file_info(relative_path)
