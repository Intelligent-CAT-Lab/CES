from typing import *
def select_words(s, n):
    result = []
    print(f'[ITE][LOC]4[/LOC][VAR]s.split()[/VAR][VAL]{s.split()}[/VAL][/ITE]')
    for word in s.split():
        n_consonants = 0
        print(f'[ITE][LOC]6[/LOC][VAR]range(0, len(word))[/VAR][VAL]{list(range(0, len(word)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]len(word)[/VAR][VAL]{len(word)}[/VAL][/ITE]')
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result


select_words("Mary had a little lamb", 4) 