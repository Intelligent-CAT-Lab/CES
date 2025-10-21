def check_dict_case(dict):
    print('[LINE]1[/LINE] may be hit')
    print('[LINE]3[/LINE] may be hit')
    print('[LINE]13[/LINE] may be hit')
    print('[LINE]15[/LINE] may be hit')
    print('[LINE]17[/LINE] may be hit')
    print('[LINE]20[/LINE] may be hit')
    if len(dict.keys()) == 0:
        print('[LINE]1[/LINE] is hit')
        return False
    else:
        print('[LINE]3[/LINE] is hit')
        state = "start"
        for key in dict.keys():

            print('[LINE]7[/LINE] may be hit')
            if isinstance(key, str) == False:
                print('[LINE]7[/LINE] is hit')
                state = "mixed"
                break
            print('[LINE]10[/LINE] may be hit')
            if state == "start":
                print('[LINE]10[/LINE] is hit')
                print('[LINE]11[/LINE] may be hit')
                if key.isupper():
                    print('[LINE]11[/LINE] is hit')
                    state = "upper"
                elif key.islower():
                    print('[LINE]13[/LINE] is hit')
                    state = "lower"
                else:
                    print('[LINE]15[/LINE] is hit')
                    break
            elif (state == "upper" and not key.isupper()) and (state == "lower" and not key.islower()):
                print('[LINE]17[/LINE] is hit')
                    state = "mixed"
                    break
            else:
                print('[LINE]20[/LINE] is hit')
                break
        return state == "upper" or state == "lower" 

check_dict_case({'p': 'pineapple', 'A': 'banana', 'B': 'banana'})