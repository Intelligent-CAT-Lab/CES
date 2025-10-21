from typing import *


def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            print('[LINE]8[/LINE] may be hit')
            if a[i:i + l] == pat[j:j + l]:
                print('[LINE]8[/LINE] is hit')
                return True
    return False

cycpattern_check("efef","fee")