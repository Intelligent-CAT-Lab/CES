def valid_date(date):
    try:
        date = date.strip()
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        print('[LINE]5[/LINE] may be hit')
        if month < 1 or month > 12:
            print('[LINE]5[/LINE] is hit')
            return False
        print('[LINE]7[/LINE] may be hit')
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            print('[LINE]7[/LINE] is hit')
            return False
        print('[LINE]9[/LINE] may be hit')
        if month in [4,6,9,11] and day < 1 or day > 30:
            print('[LINE]9[/LINE] is hit')
            return False
        print('[LINE]11[/LINE] may be hit')
        if month == 2 and day < 1 or day > 29:
            print('[LINE]11[/LINE] is hit')
            return False
    except:
        return False

    return True

valid_date('15-01-2012')