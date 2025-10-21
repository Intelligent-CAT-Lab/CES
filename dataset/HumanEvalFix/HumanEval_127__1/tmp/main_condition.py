def intersection(interval1, interval2):
    def is_prime(num):
        print(f'[ITE][LOC]2[/LOC][VAR]num == 1 or num == 0[/VAR][VAL]{num == 1 or num == 0}[/VAL][/ITE]')
        print(f'[ITE][LOC]2[/LOC][VAR]num == 1[/VAR][VAL]{num == 1}[/VAL][/ITE]')
        print(f'[ITE][LOC]2[/LOC][VAR]num == 0[/VAR][VAL]{num == 0}[/VAL][/ITE]')
        if num == 1 or num == 0:
            return False
        print(f'[ITE][LOC]4[/LOC][VAR]num == 2[/VAR][VAL]{num == 2}[/VAL][/ITE]')
        if num == 2:
            return True
        for i in range(2, num):
            print(f'[ITE][LOC]7[/LOC][VAR]num%i == 0[/VAR][VAL]{num%i == 0}[/VAL][/ITE]')
            if num%i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    print(f'[ITE][LOC]14[/LOC][VAR]length > 0[/VAR][VAL]{length > 0}[/VAL][/ITE]')
    if length > 0:
        return "YES"
    return "NO"

intersection(((- 1), 1), (0, 4))
