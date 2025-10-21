from typing import *


def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            print(f'[ITE][LOC]8[/LOC][VAR]word[i].lower() not in ["a", "e", "i", "o", "u"][/VAR][VAL]{word[i].lower() not in ["a", "e", "i", "o", "u"]}[/VAL][/ITE]')
            if word[i].lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        print(f'[ITE][LOC]10[/LOC][VAR]n_consonants == n[/VAR][VAL]{n_consonants == n}[/VAL][/ITE]')
        if n_consonants == n:
            result.append(word)
    return result

select_words("Mary had a little lamb", 3)