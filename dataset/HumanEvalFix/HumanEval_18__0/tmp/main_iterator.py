def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring)):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if string[i:i+len(substring)] == substring:
            times += 1

    return times

how_many_times('xyxyxyx', 'x')
