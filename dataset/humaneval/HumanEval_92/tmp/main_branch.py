from typing import *
def any_int(x, y, z):
    
    print('[LINE]3[/LINE] may be hit')
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        print('[LINE]3[/LINE] is hit')
        print('[LINE]4[/LINE] may be hit')
        if (x+y==z) or (x+z==y) or (y+z==x):
            print('[LINE]4[/LINE] is hit')
            return True
        return False
    return False

any_int(2, 3, 1)