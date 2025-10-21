from typing import *
def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    print(f'[ITE][LOC]5[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(n):
        print(f'[ITE][LOC]6[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i != 0:
                    temp.append(grid[i - 1][j])

                if j != 0:
                    temp.append(grid[i][j - 1])

                if i != n - 1:
                    temp.append(grid[i + 1][j])

                if j != n - 1:
                    temp.append(grid[i][j + 1])

                val = min(temp)

    ans = []
    print(f'[ITE][LOC]24[/LOC][VAR]range(k)[/VAR][VAL]{list(range(k))}[/VAL][/ITE]')
    print(f'[ITE][LOC]24[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans

minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) 