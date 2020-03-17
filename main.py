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
def text_generator():
    file = input('Имя файла: ')
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
    print(text, lst_of_words)
