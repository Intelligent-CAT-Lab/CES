def how_many_times(string: str, substring: str) -> int:
    times = 0

    print(f'[ITE][LOC]4[/LOC][VAR]range((len(string) - len(substring)))[/VAR][VAL]{list(range((len(string) - len(substring))))}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR](len(string) - len(substring))[/VAR][VAL]{(len(string) - len(substring))}[/VAL][/ITE]')
    for i in range(len(string) - len(substring)):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times

how_many_times('xyxyxyx', 'x')
