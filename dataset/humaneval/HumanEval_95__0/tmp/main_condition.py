from typing import *


def check_dict_case(dict):
    print(f'[ITE][LOC]4[/LOC][VAR]len(dict.keys()) == 0[/VAR][VAL]{len(dict.keys()) == 0}[/VAL][/ITE]')
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            print(f'[ITE][LOC]10[/LOC][VAR]isinstance(key, str) == False[/VAR][VAL]{isinstance(key, str) == False}[/VAL][/ITE]')
            if isinstance(key, str) == False:
                state = "mixed"
                break
            print(f'[ITE][LOC]13[/LOC][VAR]state == "start"[/VAR][VAL]{state == "start"}[/VAL][/ITE]')
            if state == "start":
                print(f'[ITE][LOC]14[/LOC][VAR]key.isupper()[/VAR][VAL]{key.isupper()}[/VAL][/ITE]')
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

check_dict_case({"STATE":"NC", "ZIP":"12345" })