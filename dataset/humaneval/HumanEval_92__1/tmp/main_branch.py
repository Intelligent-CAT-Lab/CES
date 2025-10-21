from typing import *


def any_int(x, y, z):

    print('[LINE]5[/LINE] may be hit')
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        print('[LINE]5[/LINE] is hit')
        print('[LINE]6[/LINE] may be hit')
        if (x + y == z) or (x + z == y) or (y + z == x):
            print('[LINE]6[/LINE] is hit')
            return True
        return False
    return False

any_int(3,4,7)