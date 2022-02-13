from random import *
from word_list_001 import *
#word_list = word_list


def get_word():
    return choice(word_list)

print(get_word())