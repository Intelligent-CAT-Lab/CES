from typing import *
def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        print('[LINE]5[/LINE] may be hit')
        if len(word) == 1:
            print('[LINE]5[/LINE] is hit')
            flg = 1
        for i in range(2, len(word)):
            print('[LINE]8[/LINE] may be hit')
            if len(word)%i == 0:
                print('[LINE]8[/LINE] is hit')
                flg = 1
        print('[LINE]10[/LINE] may be hit')
        if flg == 0 or len(word) == 2:
            print('[LINE]10[/LINE] is hit')
            new_lst.append(word)
    return " ".join(new_lst)

words_in_sentence("This is a test") 