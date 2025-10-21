from typing import *


def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    print(f"[ITE][LOC]6[/LOC][VAR]s[-1] == 'y' or s[-1] == 'Y'[/VAR][VAL]{s[-1] == 'y' or s[-1] == 'Y'}[/VAL][/ITE]")
    print(f"[ITE][LOC]6[/LOC][VAR]s[-1] == 'y'[/VAR][VAL]{s[-1] == 'y'}[/VAL][/ITE]")
    print(f"[ITE][LOC]6[/LOC][VAR]s[-1] == 'Y'[/VAR][VAL]{s[-1] == 'Y'}[/VAL][/ITE]")
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

vowels_count("bYe")