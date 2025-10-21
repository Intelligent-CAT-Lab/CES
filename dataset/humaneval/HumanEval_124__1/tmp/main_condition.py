from typing import *


def valid_date(date):
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        print(f'[ITE][LOC]8[/LOC][VAR]month < 1 or month > 12[/VAR][VAL]{month < 1 or month > 12}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]month < 1[/VAR][VAL]{month < 1}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]month > 12[/VAR][VAL]{month > 12}[/VAL][/ITE]')
        if month < 1 or month > 12:
            return False
        print(f'[ITE][LOC]10[/LOC][VAR]month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31[/VAR][VAL]{month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31}[/VAL][/ITE]')
        print(f'[ITE][LOC]10[/LOC][VAR]day > 31[/VAR][VAL]{day > 31}[/VAL][/ITE]')
        print(f'[ITE][LOC]10[/LOC][VAR]month in [1, 3, 5, 7, 8, 10, 12][/VAR][VAL]{month in [1, 3, 5, 7, 8, 10, 12]}[/VAL][/ITE]')
        print(f'[ITE][LOC]10[/LOC][VAR]day < 1[/VAR][VAL]{day < 1}[/VAL][/ITE]')
        if month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31:
            return False
        print(f'[ITE][LOC]12[/LOC][VAR]month in [4, 6, 9, 11] and day < 1 or day > 30[/VAR][VAL]{month in [4, 6, 9, 11] and day < 1 or day > 30}[/VAL][/ITE]')
        print(f'[ITE][LOC]12[/LOC][VAR]day > 30[/VAR][VAL]{day > 30}[/VAL][/ITE]')
        print(f'[ITE][LOC]12[/LOC][VAR]month in [4, 6, 9, 11][/VAR][VAL]{month in [4, 6, 9, 11]}[/VAL][/ITE]')
        print(f'[ITE][LOC]12[/LOC][VAR]day < 1[/VAR][VAL]{day < 1}[/VAL][/ITE]')
        if month in [4, 6, 9, 11] and day < 1 or day > 30:
            return False
        print(f'[ITE][LOC]14[/LOC][VAR]month == 2 and day < 1 or day > 29[/VAR][VAL]{month == 2 and day < 1 or day > 29}[/VAL][/ITE]')
        print(f'[ITE][LOC]14[/LOC][VAR]day > 29[/VAR][VAL]{day > 29}[/VAL][/ITE]')
        print(f'[ITE][LOC]14[/LOC][VAR]month == 2[/VAR][VAL]{month == 2}[/VAL][/ITE]')
        print(f'[ITE][LOC]14[/LOC][VAR]day < 1[/VAR][VAL]{day < 1}[/VAL][/ITE]')
        if month == 2 and day < 1 or day > 29:
            return False
    except BaseException:
        return False

    return True
valid_date('04-2003')

valid_date('04-2003')