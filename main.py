# Case - study

# This program generates a set number of sentences using a text file and
# Markov's chains.

# Developers : Daniel A.         (35%),
#              Zemtseva A.       (30%),
#              Torgasheva A.     (%).


import random

# Choosing of language.
language = input('Choose your language:\n1. English\n2. Russian\n3.'
                 ' French\n').lower()
while True:
    if language == 'english' or language == 'en' or \
            language == 'e' or language == '1':
        import lc_en as lc

        break
    elif language == 'russian' or language == 'ru' or \
            language == 'r' or language == '2':
        import lc_ru as lc

        break
    elif language == 'french' or language == 'fr' or \
            language == 'f' or language == '3':
        import lc_fr as lc

        break
    language = input('Please, choose language from proposed: ')


def open_file():
    """
    Function that checks whether the entered name of file is correct.
    :return: correct name of file
    """
    file = input(lc.TXT_INPUT_FILE_NAME)
    while True:
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            print(lc.TXT_FILE_NOT_FOUND.format(file))
            file = input(lc.TXT_INPUT_FILE_NAME)
        else:
            return file


def input_number():
    """
    Function that checks whether the entered number of sentences is correct.
    :return: correct number of sentences
    """
    number_of_sentences = input(lc.TXT_INPUT_NUMBER_OF_SENTENCES)
    while True:
        try:
            number_of_sentences = int(number_of_sentences)
        except ValueError:
            print(lc.TXT_ERROR)
            number_of_sentences = input(lc.TXT_INPUT_NUMBER_OF_SENTENCES)
        else:
            print()
            return number_of_sentences


def text_to_words(file):
    """
    Function that creates a list of all words from the text.
    :param file: name of the file to use
    :return: list of all words from the text
    """
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
    """
    Function that creates a list of unique words from list of all words.
    :param lst_of_words: list of all words from the text
    :return: list of unique words from the text
    """
    lst_of_unique_words = []
    for word in lst_of_words:
        if word not in lst_of_unique_words:
            lst_of_unique_words.append(word)
    return lst_of_unique_words


def initial_words(lst_of_words):
    """
    Function that creates a list of start-words from list of all words.
    :param lst_of_words: list of all words from the text
    :return: list start-words from the text
    """
    start_words = []
    for words in lst_of_words:
        if words[0].isupper() and words.find('.') == -1:
            start_words.append(words)
    return start_words


def final_words(lst_of_words):
    """
    Function that creates a list of final words from list of all words.
    :param lst_of_words: list of all words from the text
    :return: list stop-words from the text
    """
    stop_words = []
    for words in lst_of_words:
        if words.find('.') != -1 or words.find('!') != -1 or words.find('?') != -1:
            stop_words.append(words)
    return stop_words


def dictionary(lst_of_unique_words, all_words):
    """
    Function which creates a dictionary, in which the key is a unique word
     from the text (link) and the value is a list of words that follow it
     in the text (connections).
    :param lst_of_unique_words: list of unique words
    :param all_words: list of all words from the text
    :return: dictionary of links and connections
    """
    links_and_connections = {}
    for word in lst_of_unique_words:
        following_words = []
        for i in range(len(all_words) - 1):
            if word == all_words[i] and all_words[i + 1] not in following_words:
                following_words.append(all_words[i + 1])
        links_and_connections[word] = following_words
    return links_and_connections


def generator(number_of_sentences, start_words, links_and_connections,
              stop_words):
    """
    Function that generates sentences using Markov's chains.
    :param number_of_sentences: number of sentences to generate
    :param start_words: list start-words from the text
    :param links_and_connections:
    :param stop_words: list stop-words from the text
    :return: None
    """
    for _ in range(number_of_sentences):
        word = start_words[random.randint(0, len(start_words) - 1)]
        counter = 1
        print(word, end=' ')
        while True:
            word = links_and_connections[word][random.randint(0, len(links_and_connections[word]) - 1)]
            if word.find('.') != -1:
                if counter >= 5:
                    print(word)
                    break
                else:
                    counter += 1
                    print(word[:word.find('.')], end=' ')
            else:
                if counter < 19:
                    counter += 1
                    print(word, end=' ')
                else:
                    print(stop_words[random.randint(0, len(stop_words) - 1)])
                    break


def main():
    file = open_file()
    number_of_sentences = input_number()

    all_words = text_to_words(file)
    start_words = initial_words(all_words)
    stop_words = final_words(all_words)
    links_and_connections = dictionary(unique_words(all_words), all_words)

    generator(number_of_sentences, start_words, links_and_connections,
              stop_words)


if __name__ == '__main__':
    main()
