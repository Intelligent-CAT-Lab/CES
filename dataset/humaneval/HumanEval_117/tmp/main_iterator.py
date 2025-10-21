from typing import *
def select_words(s, n):
    result = []
    for word in s.split():
        print(f'[ITE][LOC]4[/LOC][VAR]word[/VAR][VAL]{word}[/VAL][/ITE]')
        n_consonants = 0
        for i in range(0, len(word)):
            print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result


select_words("Mary had a little lamb", 4) 