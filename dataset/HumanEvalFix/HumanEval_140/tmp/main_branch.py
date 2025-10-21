def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        print('[LINE]5[/LINE] may be hit')
        print('[LINE]7[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        print('[LINE]12[/LINE] may be hit')
        if text[i] == " ":
            print('[LINE]5[/LINE] is hit')
            end += 1
        else:
            print('[LINE]7[/LINE] is hit')
            print('[LINE]8[/LINE] may be hit')
            if end - start > 2:
                print('[LINE]8[/LINE] is hit')
                new_text += "-"+text[i]
            elif end - start > 0:
                print('[LINE]10[/LINE] is hit')
                new_text += "_"*(end - start)+text[i]
            else:
                print('[LINE]12[/LINE] is hit')
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    print('[LINE]16[/LINE] may be hit')
    print('[LINE]18[/LINE] may be hit')
    if end - start > 2:
        print('[LINE]16[/LINE] is hit')
        new_text += "-"
    elif end - start > 0:
        print('[LINE]18[/LINE] is hit')
        new_text += "__"
    return new_text

fix_spaces('Mudasir Hanif ')