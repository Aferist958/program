import re


class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for words in file:
                    words = words.lower()
                    words = re.sub(r'[^\w\s]', '', words)
                    words = words.split()
                    all_words[i] = words
                    global b
                    b = words


    def find(self, word):
        a = {}
        word = word.lower()
        index1 = b.index(word)
        for i in self.file_names:
            a[i] = index1
            return a


    def count(self, word):
        a = {}
        word = word.lower()
        c = 0
        for i in b:
            if word == i:
                c += 1
        for i in self.file_names:
            a[i] = c
            return a




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего