def match_parens(lst):
    def check(s):
        val = 0
        for i in s:
            print('[LINE]4[/LINE] may be hit')
            print('[LINE]6[/LINE] may be hit')
            if i == '(':
                print('[LINE]4[/LINE] is hit')
                val = val + 1
            else:
                print('[LINE]6[/LINE] is hit')
                val = val - 1
            print('[LINE]8[/LINE] may be hit')
            if val < 0:
                print('[LINE]8[/LINE] is hit')
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'yes' if check(S1) or check(S2) else 'no'

match_parens(['()(', ')'])