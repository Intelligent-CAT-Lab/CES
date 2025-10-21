def special_factorial(n):
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        i *= n
        fact_i *= i
        special_fact *= fact_i
    return special_fact

special_factorial(4)
