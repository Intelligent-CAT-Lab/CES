def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            print(f'[ITE][LOC]5[/LOC][VAR]grid[i][j] == 1[/VAR][VAL]{grid[i][j] == 1}[/VAL][/ITE]')
            if grid[i][j] == 1:
                temp = []
                print(f'[ITE][LOC]7[/LOC][VAR]i != 0[/VAR][VAL]{i != 0}[/VAL][/ITE]')
                if i != 0:
                    temp.append(grid[i][j])

                print(f'[ITE][LOC]10[/LOC][VAR]j != 0[/VAR][VAL]{j != 0}[/VAL][/ITE]')
                if j != 0:
                    temp.append(grid[i][j])

                print(f'[ITE][LOC]13[/LOC][VAR]i != n - 1[/VAR][VAL]{i != n - 1}[/VAL][/ITE]')
                if i != n - 1:
                    temp.append(grid[i][j])

                print(f'[ITE][LOC]16[/LOC][VAR]j != n - 1[/VAR][VAL]{j != n - 1}[/VAL][/ITE]')
                if j != n - 1:
                    temp.append(grid[i][j])

                val = min(temp)

    ans = []
    for i in range(k):
        print(f'[ITE][LOC]23[/LOC][VAR]i % 2 == 0[/VAR][VAL]{i % 2 == 0}[/VAL][/ITE]')
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans

minPath([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7)
