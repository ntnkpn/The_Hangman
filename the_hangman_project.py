from random import *
from word_list_001 import *


def get_word():
    word = choice(word_list).upper()
    print((word))
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''

    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Приветсвую в Виселице 1.0!')
    while True and tries > 0:
        print(f'Количество оставшихся попыток: {tries} {display_hangman(tries)}')
        print(f'Загаданное слово: {word_completion}')
        print('Введите букву!')
        user_char = input().upper()
        if len(user_char) == 1 and user_char.isalpha():

            if user_char in guessed_letters:
                print(f'Букву {user_char} вы уже называли')

            elif user_char not in word:
                print(f'Буквы {user_char} нет в слове')
                tries -= 1
                guessed_letters.append(user_char)  # Добавляет букву в список названных

            elif user_char in word:
                print(f'Буква {user_char} имеется в слове!')
                guessed_letters.append(user_char)  # Добавляет букву в список названных
                word_char_list = list(word_completion)  # создает список из символов _
                right_char_index_lst = [i for i in range(len(word)) if word[i] == user_char]
                # добавляет номера индексов верных букв в список

                for index in right_char_index_lst:
                    word_char_list[index] = user_char  # заменяет символы _ на угаданную букву в списке
                word_completion = ''.join(word_char_list)  # делает из списка строку
                if '_' not in word_completion:
                    guessed = True
                    break

        print(display_hangman(tries))
        print(word_completion)
    if guessed:
        print(f'Молодец! Вы отгадали слово правильно: \n{word}')
    else:
        print(f'Тоби пизда. Слово было {word}')






play(get_word())
