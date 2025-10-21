from typing import *
def digitSum(s):
    print('[LINE]2[/LINE] may be hit')
    if s == "": return 0
        print('[LINE]2[/LINE] is hit')
    return sum(ord(char) if char.isupper() else 0 for char in s)
digitSum("You arE Very Smart") 