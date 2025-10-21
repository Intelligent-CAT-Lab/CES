from typing import List


def all_prefixes(string: str) -> List[str]:
    result = []

    print(f'[ITE][LOC]7[/LOC][VAR]range((len(string) - 1))[/VAR][VAL]{list(range((len(string) - 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR](len(string) - 1)[/VAR][VAL]{(len(string) - 1)}[/VAL][/ITE]')
    for i in range(len(string)-1):
        result.append(string[:i+1])
    return result

all_prefixes('asdfgh')
