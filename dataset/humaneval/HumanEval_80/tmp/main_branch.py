from typing import *
def is_happy(s):
    print('[LINE]2[/LINE] may be hit')
    if len(s) < 3:
        print('[LINE]2[/LINE] is hit')
      return False

    for i in range(len(s) - 2):
      
      print('[LINE]7[/LINE] may be hit')
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
          print('[LINE]7[/LINE] is hit')
        return False
    return True

is_happy("a") 