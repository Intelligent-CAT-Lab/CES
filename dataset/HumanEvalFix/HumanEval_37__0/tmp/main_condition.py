def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    odds.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    print(f'[ITE][LOC]7[/LOC][VAR]len(evens) > len(odds)[/VAR][VAL]{len(evens) > len(odds)}[/VAL][/ITE]')
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

tuple(sort_even([5, 3, (- 5), 2, (- 3), 3, 9, 0, 123, 1, (- 10)]))
