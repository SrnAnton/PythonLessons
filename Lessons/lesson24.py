class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower().translate({ord(c): None for c in '",.:!?;-'}).split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        found_lines = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:
                index = words.index(word)
                found_lines[file_name] = index + 1  # Позиция начинается с 1
            except ValueError:
                pass
        return found_lines

    def count(self, word):
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = sum(1 for _ in filter(lambda x: x == word, words))
        return counts


# Пример использования
finder = WordsFinder('test_file.txt')

# Получение всех слов из файлов
all_words = finder.get_all_words()
print(all_words)

# Поиск слова 'TEXT'
found_lines = finder.find('TEXT')
print(found_lines)

# Подсчет количества слов 'teXT'
counts = finder.count('teXT')
print(counts)
