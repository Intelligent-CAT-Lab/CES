def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        print(f'[ITE][LOC]5[/LOC][VAR]text[i] == " "[/VAR][VAL]{text[i] == " "}[/VAL][/ITE]')
        if text[i] == " ":
            end += 1
        else:
            print(f'[ITE][LOC]8[/LOC][VAR]end - start > 2[/VAR][VAL]{end - start > 2}[/VAL][/ITE]')
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    print(f'[ITE][LOC]16[/LOC][VAR]end - start > 2[/VAR][VAL]{end - start > 2}[/VAL][/ITE]')
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "__"
    return new_text

fix_spaces('Mudasir Hanif ')
