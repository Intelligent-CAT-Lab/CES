from typing import *
def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    print('[LINE]4[/LINE] may be hit')
    if s[-1] == 'y' or s[-1] == 'Y':
        print('[LINE]4[/LINE] is hit')
        n_vowels += 1
    return n_vowels

vowels_count("abcde") 