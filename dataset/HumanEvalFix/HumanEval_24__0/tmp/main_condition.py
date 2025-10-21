def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        print(f'[ITE][LOC]2[/LOC][VAR]n - i == 0[/VAR][VAL]{n - i == 0}[/VAL][/ITE]')
        if n - i == 0:
            return i

largest_divisor(49)
