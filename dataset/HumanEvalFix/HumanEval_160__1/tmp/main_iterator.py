def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        print(f'[ITE][LOC]3[/LOC][VAR]oprt[/VAR][VAL]{oprt}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]oprn[/VAR][VAL]{oprn}[/VAL][/ITE]')
        expression+=expression + oprt + str(oprn)
    return (expression)

do_algebra(['+', '*', '-'], [2, 3, 4, 5])
