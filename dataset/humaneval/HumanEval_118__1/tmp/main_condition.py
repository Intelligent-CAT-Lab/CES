from typing import *


def get_closest_vowel(word):
    print(f'[ITE][LOC]4[/LOC][VAR]len(word) < 3[/VAR][VAL]{len(word) < 3}[/VAL][/ITE]')
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word) - 2, 0, -1):
        print(f'[ITE][LOC]9[/LOC][VAR]word[i] in vowels[/VAR][VAL]{word[i] in vowels}[/VAL][/ITE]')
        if word[i] in vowels:
            print(f'[ITE][LOC]10[/LOC][VAR](word[i + 1] not in vowels) and (word[i - 1] not in vowels)[/VAR][VAL]{(word[i + 1] not in vowels) and (word[i - 1] not in vowels)}[/VAL][/ITE]')
            print(f'[ITE][LOC]10[/LOC][VAR]word[i + 1] not in vowels[/VAR][VAL]{word[i + 1] not in vowels}[/VAL][/ITE]')
            print(f'[ITE][LOC]10[/LOC][VAR]word[i - 1] not in vowels[/VAR][VAL]{word[i - 1] not in vowels}[/VAL][/ITE]')
            if (word[i + 1] not in vowels) and (word[i - 1] not in vowels):
                return word[i]
    return ""

get_closest_vowel("ba")