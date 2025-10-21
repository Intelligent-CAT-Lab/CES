def digitSum(s):
    print('[LINE]1[/LINE] may be hit')
    if s == "":
        print('[LINE]1[/LINE] is hit') 
        return 0 
    return sum(ord(char) if char.islower() else 0 for char in s)

digitSum('aAaaaXa')