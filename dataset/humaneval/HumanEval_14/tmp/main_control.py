from typing import *
def all_prefixes(string: str) -> List[str]:
    result = []

    print(f'[ITE][LOC]5[/LOC][VAR]range(len(string))[/VAR][VAL]{list(range(len(string)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]len(string)[/VAR][VAL]{len(string)}[/VAL][/ITE]')
    for i in range(len(string)):
        result.append(string[:i+1])
    return result

all_prefixes('asdfgh') 