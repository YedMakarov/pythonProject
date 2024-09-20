# Задача "Найдёт везде"

class WordsFinder:
    file_names = ()

    def __init__(self, *file_name):
        self.file_name = file_name
        self.file_names = self.file_name

    def get_all_words(self):
        all_words = {}

        for next_file in self.file_name:
            with open(next_file, encoding='utf-8') as file:
                data = (file.read().replace('\n', ' ')).lower()

                # chars_to_remove = ",.=!?;:-"
                chars_to_remove = [",", ".", "=", "!", "?", ";", ":"]
                for symbol in chars_to_remove:
                    data = data.replace(symbol, "")

                chars_to_remove = [" - "]
                for symbol in chars_to_remove:
                    data = data.replace(symbol, " ")

                all_words[next_file] = data.split()

        return all_words

    def find(self, word):
        word = word.lower()
        dict_return = {}

        for file_name, word_list in self.get_all_words().items():
            for i in range(len(word_list)):
                if word == word_list[i]:
                    dict_return[file_name] = i + 1
                    break

        return dict_return

    def count(self, word):
        word = word.lower()
        dict_return = {}

        for file_name, word_list in self.get_all_words().items():
            word_count = 0
            for i in range(len(word_list)):
                if word == word_list[i]:
                    word_count += 1
                    dict_return[file_name] = word_count

        return dict_return


# Main

# var = "Hello World!"
# print(var[2:7:2])
#
# birth_date = {'Олег': 1995, 'Никита': 1978, 'Алексей': 2002, 'Александр': 1989}
# print(birth_date['Александр'])
#
# my_set = {10, 20, 30}
# my_set.add(20)
# print(my_set)
#
# son_age = 5
# my_age = "30"
# print(son_age * my_age)

finder2 = WordsFinder('test_file.txt', 'test_file1.txt', 'test_file2.txt')

# finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
