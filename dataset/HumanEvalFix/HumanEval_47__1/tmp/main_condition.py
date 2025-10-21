def median(l: list):
    l = sorted(l)
    print(f'[ITE][LOC]2[/LOC][VAR]len(l) % 2 == 1[/VAR][VAL]{len(l) % 2 == 1}[/VAL][/ITE]')
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0

median([(- 10), 4, 6, 1000, 10, 20])
