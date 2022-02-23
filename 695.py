def maxAreaOfIsland( grid) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    m, n = len(grid[0]), len(grid)

    ans = 0
    mem = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            else:
                ans = max(ans, dfs(grid, m, n, i, j, mem, directions))
    return ans


def dfs( grid, m, n, i, j, mem, directions):
    if (i, j) in mem:
        return 0

    count = 1
    mem[(i, j)] = True
    for d in directions:
        a, b = i + d[0], j + d[1]
        if a >= 0 and a < m and b >= 0 and b < n and (a, b) not in mem and grid[a][b] == 1:
            count += dfs(grid, m, n, a, b, mem, directions)
            mem[(a, b)] = True
    return count

if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ans = maxAreaOfIsland(grid)
    print(ans)