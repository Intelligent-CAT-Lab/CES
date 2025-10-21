def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            print('[LINE]5[/LINE] may be hit')
            if grid[i][j] == 1:
                print('[LINE]5[/LINE] is hit')
                temp = []
                print('[LINE]7[/LINE] may be hit')
                if i != 0:
                    print('[LINE]7[/LINE] is hit')
                    temp.append(grid[i][j])

                print('[LINE]10[/LINE] may be hit')
                if j != 0:
                    print('[LINE]10[/LINE] is hit')
                    temp.append(grid[i][j])

                print('[LINE]13[/LINE] may be hit')
                if i != n - 1:
                    print('[LINE]13[/LINE] is hit')
                    temp.append(grid[i][j])

                print('[LINE]16[/LINE] may be hit')
                if j != n - 1:
                    print('[LINE]16[/LINE] is hit')
                    temp.append(grid[i][j])

                val = min(temp)

    ans = []
    for i in range(k):
        print('[LINE]23[/LINE] may be hit')
        print('[LINE]25[/LINE] may be hit')
        if i % 2 == 0:
            print('[LINE]23[/LINE] is hit')
            ans.append(1)
        else:
            print('[LINE]25[/LINE] is hit')
            ans.append(val)
    return ans

minPath([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7)