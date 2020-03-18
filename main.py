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


def generator(number_of_sentences, start_words, lst_of_words, stop_words):
    # number_of_sentences - колво предложений
    # start_words - список старт слов
    # lst_of_words - словарь слов
    # stop_words - список стоп слов

    import random
    for _ in range(number_of_sentences):
        word = start_words[random.randint(0, len(start_words) - 1)]
        counter = 1
        while word[-1] != '.' and counter != 19:
            print(word, end=' ')
            word = lst_of_words[word][random.randint(0, len(lst_of_words[word]) - 1)]
            counter += 1
        if counter == 19:
            print(stop_words[random.randint(0, len(stop_words) - 1)])


def text_generator():
    file = input()
    ptr = 0
    while ptr == 0:
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            print('Файл {} не найден.'.format(file))
            file = input('Введите имя файла: ')
            ptr = 0
        else:
            ptr = 1
    number = input('Количество генерируемых предложений: ')
    lst_of_words = []
    text = ''
    with open(file, 'r') as file_in:
        for string in file_in.readlines():
            text += string
        text = text.replace('\n', ' ')
        word = ''
        for i in text:
            if i == ' ':
                lst_of_words.append(word)
                word = ''
            else:
                word += i

    # text - весь текст из файла, \n удалены и заменены на пробел
    # lst_of_words - списочек всех слов из текста, знаки препинания сохранены (порезано по пробелам)
    print(text, lst_of_words, sep='\n')


text_generator()
