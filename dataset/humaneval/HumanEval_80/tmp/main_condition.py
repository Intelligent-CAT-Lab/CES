from typing import *
def is_happy(s):
    print(f'[ITE][LOC]2[/LOC][VAR]len(s) < 3[/VAR][VAL]{len(s) < 3}[/VAL][/ITE]')
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      print(f'[ITE][LOC]7[/LOC][VAR]s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2][/VAR][VAL]{s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]}[/VAL][/ITE]')
      print(f'[ITE][LOC]7[/LOC][VAR]s[i] == s[i+2][/VAR][VAL]{s[i] == s[i+2]}[/VAL][/ITE]')
      print(f'[ITE][LOC]7[/LOC][VAR]s[i] == s[i+1][/VAR][VAL]{s[i] == s[i+1]}[/VAL][/ITE]')
      print(f'[ITE][LOC]7[/LOC][VAR]s[i+1] == s[i+2][/VAR][VAL]{s[i+1] == s[i+2]}[/VAL][/ITE]')
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

is_happy("a") 