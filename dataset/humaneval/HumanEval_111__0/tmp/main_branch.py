from typing import *


def histogram(test):
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in list1:
        print('[LINE]9[/LINE] may be hit')
        if (list1.count(i) > t) and i != '':
            print('[LINE]9[/LINE] is hit')
            t = list1.count(i)
    print('[LINE]11[/LINE] may be hit')
    if t > 0:
        print('[LINE]11[/LINE] is hit')
        for i in list1:
            print('[LINE]13[/LINE] may be hit')
            if (list1.count(i) == t):
                print('[LINE]13[/LINE] is hit')

                dict1[i] = t
    return dict1

histogram('a b c d g')