def get_closest_vowel(word):
    if len(word) < 3:
        return " "

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    print(f'[ITE][LOC]6[/LOC][VAR]range((len(word) - 2), 0, (- 1))[/VAR][VAL]{list(range((len(word) - 2), 0, (- 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR](len(word) - 2)[/VAR][VAL]{(len(word) - 2)}[/VAL][/ITE]')
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return " "

get_closest_vowel('ba')
