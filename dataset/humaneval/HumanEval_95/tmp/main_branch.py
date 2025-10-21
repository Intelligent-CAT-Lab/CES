from typing import *
def check_dict_case(dict):
    print('[LINE]2[/LINE] may be hit')
    print('[LINE]4[/LINE] may be hit')
    print('[LINE]14[/LINE] may be hit')
    print('[LINE]16[/LINE] may be hit')
    print('[LINE]18[/LINE] may be hit')
    print('[LINE]21[/LINE] may be hit')
    if len(dict.keys()) == 0:
        print('[LINE]2[/LINE] is hit')
        return False
    else:
        print('[LINE]4[/LINE] is hit')
        state = "start"
        for key in dict.keys():

            print('[LINE]8[/LINE] may be hit')
            if isinstance(key, str) == False:
                print('[LINE]8[/LINE] is hit')
                state = "mixed"
                break
            print('[LINE]11[/LINE] may be hit')
            if state == "start":
                print('[LINE]11[/LINE] is hit')
                print('[LINE]12[/LINE] may be hit')
                if key.isupper():
                    print('[LINE]12[/LINE] is hit')
                    state = "upper"
                elif key.islower():
                    print('[LINE]14[/LINE] is hit')
                    state = "lower"
                else:
                    print('[LINE]16[/LINE] is hit')
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                print('[LINE]18[/LINE] is hit')
                    state = "mixed"
                    break
            else:
                print('[LINE]21[/LINE] is hit')
                break
        return state == "upper" or state == "lower" 

check_dict_case({"p":"pineapple", "b":"banana"}) 