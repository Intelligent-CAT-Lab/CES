def split_words(txt):
    print('[LINE]1[/LINE] may be hit')
    print('[LINE]3[/LINE] may be hit')
    print('[LINE]5[/LINE] may be hit')
    if " " in txt:
        print('[LINE]1[/LINE] is hit')
        return txt.split()
    elif "," in txt:
        print('[LINE]3[/LINE] is hit')
        return txt.replace(' ',',').split()
    else:
        print('[LINE]5[/LINE] is hit')
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

split_words('Hello,world!')