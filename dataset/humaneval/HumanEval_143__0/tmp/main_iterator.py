from typing import *


def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        print(f'[ITE][LOC]6[/LOC][VAR]word[/VAR][VAL]{word}[/VAL][/ITE]')
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            print(f'[ITE][LOC]10[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

words_in_sentence("there is no place available here")