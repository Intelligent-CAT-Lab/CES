def pluck(arr):
    print(f'[ITE][LOC]1[/LOC][VAR]len(arr) == 0[/VAR][VAL]{len(arr) == 0}[/VAL][/ITE]')
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    print(f'[ITE][LOC]3[/LOC][VAR]evens == [][/VAR][VAL]{evens == []}[/VAL][/ITE]')
    if(evens == []): return []
    return [arr.index(min(evens)), min(evens)]

pluck([4, 2, 3])
