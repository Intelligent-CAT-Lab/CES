def digitSum(s):
    print(f'[ITE][LOC]1[/LOC][VAR]s == ""[/VAR][VAL]{s == ""}[/VAL][/ITE]')
    if s == "": return 0
    return sum(ord(char) if char.islower() else 0 for char in s)

digitSum('aAaaaXa')
