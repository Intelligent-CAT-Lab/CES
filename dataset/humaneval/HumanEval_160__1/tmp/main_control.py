from typing import *


def do_algebra(operator, operand):
    expression = str(operand[0])
    print(f'[ITE][LOC]6[/LOC][VAR]zip(operator, operand[1:])[/VAR][VAL]{list(zip(operator, operand[1:]))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]operator[/VAR][VAL]{operator}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]operand[1:][/VAR][VAL]{operand[1:]}[/VAL][/ITE]')
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return (expression)
    return eval(expression)

do_algebra(['+', '*', '-'], [2, 3, 4, 5])