from typing import *
def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        print(f'[ITE][LOC]5[/LOC][VAR]len(word) == 1[/VAR][VAL]{len(word) == 1}[/VAL][/ITE]')
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            print(f'[ITE][LOC]8[/LOC][VAR]len(word)%i == 0[/VAR][VAL]{len(word)%i == 0}[/VAL][/ITE]')
            if len(word)%i == 0:
                flg = 1
        print(f'[ITE][LOC]10[/LOC][VAR]flg == 0 or len(word) == 2[/VAR][VAL]{flg == 0 or len(word) == 2}[/VAL][/ITE]')
        print(f'[ITE][LOC]10[/LOC][VAR]flg == 0[/VAR][VAL]{flg == 0}[/VAL][/ITE]')
        print(f'[ITE][LOC]10[/LOC][VAR]len(word) == 2[/VAR][VAL]{len(word) == 2}[/VAL][/ITE]')
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

words_in_sentence("This is a test") 