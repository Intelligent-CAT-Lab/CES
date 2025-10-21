from typing import *


def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(n):
            print(f'[ITE][LOC]8[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
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
    for i in range(k):
        print(f'[ITE][LOC]26[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans

minPath([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7)