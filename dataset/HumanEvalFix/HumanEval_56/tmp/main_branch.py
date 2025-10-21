def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        print('[LINE]3[/LINE] may be hit')
        print('[LINE]5[/LINE] may be hit')
        if b == ">":
            print('[LINE]3[/LINE] is hit')
            depth += 1
        else:
            print('[LINE]5[/LINE] is hit')
            depth -= 1
        print('[LINE]7[/LINE] may be hit')
        if depth < 0:
            print('[LINE]7[/LINE] is hit')
            return False
    return depth == 0

correct_bracketing('<<><>>')