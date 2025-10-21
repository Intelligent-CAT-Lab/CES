def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        print(f'[ITE][LOC]2[/LOC][VAR]b[/VAR][VAL]{b}[/VAL][/ITE]')
        a, b = b, a % b
    return b

greatest_common_divisor(144, 60)
