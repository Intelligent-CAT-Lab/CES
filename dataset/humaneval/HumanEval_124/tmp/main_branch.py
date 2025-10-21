from typing import *
def valid_date(date):
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        print('[LINE]6[/LINE] may be hit')
        if month < 1 or month > 12:
            print('[LINE]6[/LINE] is hit')
            return False
        print('[LINE]8[/LINE] may be hit')
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            print('[LINE]8[/LINE] is hit')
            return False
        print('[LINE]10[/LINE] may be hit')
        if month in [4,6,9,11] and day < 1 or day > 30:
            print('[LINE]10[/LINE] is hit')
            return False
        print('[LINE]12[/LINE] may be hit')
        if month == 2 and day < 1 or day > 29:
            print('[LINE]12[/LINE] is hit')
            return False
    except:
        return False

    return True

valid_date('03-11-2000') 