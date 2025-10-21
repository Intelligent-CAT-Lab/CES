from typing import *


def histogram(test):
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in list1:
        print(f"[ITE][LOC]9[/LOC][VAR](list1.count(i) > t) and i != ''[/VAR][VAL]{(list1.count(i) > t) and i != ''}[/VAL][/ITE]")
        print(f"[ITE][LOC]9[/LOC][VAR]i != ''[/VAR][VAL]{i != ''}[/VAL][/ITE]")
        print(f'[ITE][LOC]9[/LOC][VAR]list1.count(i) > t[/VAR][VAL]{list1.count(i) > t}[/VAL][/ITE]')
        if (list1.count(i) > t) and i != '':
            t = list1.count(i)
    print(f'[ITE][LOC]11[/LOC][VAR]t > 0[/VAR][VAL]{t > 0}[/VAL][/ITE]')
    if t > 0:
        for i in list1:
            print(f'[ITE][LOC]13[/LOC][VAR]list1.count(i) == t[/VAR][VAL]{list1.count(i) == t}[/VAL][/ITE]')
            if (list1.count(i) == t):

                dict1[i] = t
    return dict1

histogram('a b c d g')