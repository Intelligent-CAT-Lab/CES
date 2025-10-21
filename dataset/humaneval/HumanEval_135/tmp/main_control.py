from typing import *
def can_arrange(arr):
    ind=-1
    i=1
    print(f'[ITE][LOC]5[/LOC][VAR](i < len(arr))[/VAR][VAL]{(i < len(arr))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]len(arr)[/VAR][VAL]{len(arr)}[/VAL][/ITE]')
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

can_arrange([1,2,4,3,5])