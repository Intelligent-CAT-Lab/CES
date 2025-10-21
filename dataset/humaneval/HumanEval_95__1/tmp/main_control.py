from typing import *


def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        print(f'[ITE][LOC]9[/LOC][VAR]dict.keys()[/VAR][VAL]{dict.keys()}[/VAL][/ITE]')
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
            else:
                break
        return state == "upper" or state == "lower"

check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})