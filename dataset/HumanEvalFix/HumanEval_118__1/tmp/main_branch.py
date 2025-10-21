def get_closest_vowel(word):
    print('[LINE]1[/LINE] may be hit')
    if len(word) < 3:
        print('[LINE]1[/LINE] is hit')
        return " "

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        print('[LINE]6[/LINE] may be hit')
        if word[i] in vowels:
            print('[LINE]6[/LINE] is hit')
            print('[LINE]7[/LINE] may be hit')
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                print('[LINE]7[/LINE] is hit')
                return word[i]
    return " "

get_closest_vowel('ba')