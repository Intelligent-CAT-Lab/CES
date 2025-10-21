from typing import *
def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]11[/LINE] may be hit')
        print('[LINE]13[/LINE] may be hit')
        if text[i] == " ":
            print('[LINE]6[/LINE] is hit')
            end += 1
        else:
            print('[LINE]8[/LINE] is hit')
            print('[LINE]9[/LINE] may be hit')
            if end - start > 2:
                print('[LINE]9[/LINE] is hit')
                new_text += "-"+text[i]
            elif end - start > 0:
                print('[LINE]11[/LINE] is hit')
                new_text += "_"*(end - start)+text[i]
            else:
                print('[LINE]13[/LINE] is hit')
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    print('[LINE]17[/LINE] may be hit')
    print('[LINE]19[/LINE] may be hit')
    if end - start > 2:
        print('[LINE]17[/LINE] is hit')
        new_text += "-"
    elif end - start > 0:
        print('[LINE]19[/LINE] is hit')
        new_text += "_"
    return new_text

fix_spaces("Example") 