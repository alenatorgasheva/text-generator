# Case - study

# This program

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# Tasks:
#       АЛИНА
#   - все слова (список)
#   - /n заменить на пробел
#   - оформление программы (код ревью, комменты и т.д.)
#   - локализация
#
#       НАСТЯ
#   - список старт-слов
#   - слова после уникального (словарь: ключи - из списка уникальных слов, значение - слово в тексте после ключа)
#
#       АЛЁНА
#   - уникальные слова (список)
#   - случайный вывод (не забыть про конец предложения!)

# звенья    - ключи
# связи     - значения


def open_file():
    file = 'example.txt'
    ptr = 0
    while True:
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            print('Файл {} не найден.'.format(file))
            file = input('Введите имя файла: ')
            ptr = 0
        else:
            return file


def text_to_words(file):
    all_words = []
    text = ''
    with open(file, 'r') as file_in:
        for string in file_in.readlines():
            text += string
        text = text.replace('\n', ' ')
        word = ''
        for i in text:
            if i == ' ':
                all_words.append(word)
                word = ''
            else:
                word += i
    return all_words


def unique_words(lst_of_words):
    # lst_of_unique_words - списочек уникальных слов
    # lst_of_words - список всех слов
    lst_of_unique_words = []
    for word in lst_of_words:
        if word not in lst_of_unique_words:
            lst_of_unique_words.append(word)
    return lst_of_unique_words


def initial_words(lst_of_words):
    # lst_of_start_words - списочек старт-слов
    # lst_of_words - список всех слов
    start_words = []
    for words in lst_of_words:
        if words[0].isupper():
            start_words.append(words)
    return start_words


def final_words(lst_of_words):
    # lst_of_final_words - списочек конечных слов
    # lst_of_words - список всех слов
    stop_words = []
    for words in lst_of_words:
        if words[-1] == '.' or words[-1] == '!' or words[-1] == '?':
            stop_words.append(words)
    return stop_words


def dictionary(lst_of_unique_words, all_words):
    links_and_connections = {}
    for word in lst_of_unique_words:
        following_words = []
        for i in range(len(all_words) - 1):
            if word == all_words[i] and all_words[i + 1] not in following_words:
                following_words.append(all_words[i + 1])
        links_and_connections[word] = following_words
    return links_and_connections


def generator(number_of_sentences, start_words, links_and_connections, stop_words):
    # number_of_sentences - колво предложений
    # start_words - список старт слов
    # lst_of_words - словарь слов
    # stop_words - список стоп слов

    import random
    for _ in range(number_of_sentences):
        word = start_words[random.randint(0, len(start_words) - 1)]
        counter = 1
        print(word, end=' ')
        while word[-1] != '.' and counter < 19:
            word = links_and_connections[word][random.randint(0, len(links_and_connections[word]) - 1)]
            counter += 1
            print(word, end=' ')
        if counter == 19 and word[-1] != '.':
            print(stop_words[random.randint(0, len(stop_words) - 1)])
        else:
            print()


def main():
    file = open_file()

    all_words = text_to_words(file)
    start_words = initial_words(all_words)
    stop_words = final_words(all_words)
    links_and_connections = dictionary(unique_words(all_words), all_words)

    number_of_sentences = int(input('Введите число предложений: '))
    generator(number_of_sentences, start_words, links_and_connections, stop_words)


main()
