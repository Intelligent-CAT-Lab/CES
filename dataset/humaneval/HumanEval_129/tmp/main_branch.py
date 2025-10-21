from typing import *
def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            print('[LINE]6[/LINE] may be hit')
            if grid[i][j] == 1:
                print('[LINE]6[/LINE] is hit')
                temp = []
                print('[LINE]8[/LINE] may be hit')
                if i != 0:
                    print('[LINE]8[/LINE] is hit')
                    temp.append(grid[i - 1][j])

                print('[LINE]11[/LINE] may be hit')
                if j != 0:
                    print('[LINE]11[/LINE] is hit')
                    temp.append(grid[i][j - 1])

                print('[LINE]14[/LINE] may be hit')
                if i != n - 1:
                    print('[LINE]14[/LINE] is hit')
                    temp.append(grid[i + 1][j])

                print('[LINE]17[/LINE] may be hit')
                if j != n - 1:
                    print('[LINE]17[/LINE] is hit')
                    temp.append(grid[i][j + 1])

                val = min(temp)

    ans = []
    for i in range(k):
        print('[LINE]24[/LINE] may be hit')
        print('[LINE]26[/LINE] may be hit')
        if i % 2 == 0:
            print('[LINE]24[/LINE] is hit')
            ans.append(1)
        else:
            print('[LINE]26[/LINE] is hit')
            ans.append(val)
    return ans

minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) 