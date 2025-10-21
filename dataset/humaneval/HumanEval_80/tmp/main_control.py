from typing import *
def is_happy(s):
    if len(s) < 3:
      return False

    print(f'[ITE][LOC]6[/LOC][VAR]range((len(s) - 2))[/VAR][VAL]{list(range((len(s) - 2)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR](len(s) - 2)[/VAR][VAL]{(len(s) - 2)}[/VAL][/ITE]')
    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

is_happy("a") 