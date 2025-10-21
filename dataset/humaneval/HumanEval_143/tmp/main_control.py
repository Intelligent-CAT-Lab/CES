from typing import *
def words_in_sentence(sentence):
    new_lst = []
    print(f'[ITE][LOC]4[/LOC][VAR]sentence.split()[/VAR][VAL]{sentence.split()}[/VAL][/ITE]')
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        print(f'[ITE][LOC]8[/LOC][VAR]range(2, len(word))[/VAR][VAL]{list(range(2, len(word)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]len(word)[/VAR][VAL]{len(word)}[/VAL][/ITE]')
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

words_in_sentence("This is a test") 