def numIslands( grid) -> int:
    global ans
    ans = 0
    pathMap = {}
    m, n = len(grid[0]), len(grid)
    for i in range(n):
        for j in range(m):
            DFS(grid, i, j, pathMap, m, n, 5)
            DFS(grid, i-1, j, pathMap, m, n, 0)
            DFS(grid, i, j+1, pathMap, m, n, 1)
            DFS(grid, i+1, j, pathMap, m, n, 2)
            DFS(grid, i, j-1, pathMap, m, n, 3)
    return ans


# 0:↑, 1:→，2:↓, 3:←
def DFS(grid, i, j, pathMap, m, n, direction):
    global ans
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if (grid[i][j] == '0') or (i, j) in pathMap:
        return
    if not ((i - 1, j) in pathMap or (i + 1, j) in pathMap or (i, j - 1) in pathMap or (i, j + 1) in pathMap):
        ans += 1
    pathMap[(i, j)] = 1

    if direction == 0:
        if i - 1 >= 0 and (i - 1, j) not in pathMap:
            DFS(grid, i - 1, j, pathMap, m, n, 0)
        if j + 1 < m and (i, j - 1) not in pathMap:
            DFS(grid, i, j + 1, pathMap, m, n, 1)
        if j - 1 >= 0 and (i, j - 1) not in pathMap:
            DFS(grid, i, j - 1, pathMap, m, n, 3)
    elif direction == 1:
        if i - 1 >= 0 and (i - 1, j) not in pathMap:
            DFS(grid, i - 1, j, pathMap, m, n, 0)
        if i + 1 < n and (i + 1, j) not in pathMap:
            DFS(grid, i + 1, j, pathMap, m, n, 2)
        if j + 1 < m and (i, j + 1) not in pathMap:
            DFS(grid, i, j + 1, pathMap, m, n, 1)
    elif direction == 2:
        if i + 1 < n and (i + 1, j) not in pathMap:
            DFS(grid, i + 1, j, pathMap, m, n, 2)
        if j - 1 >= 0 and (i, j - 1) not in pathMap:
            DFS(grid, i, j - 1, pathMap, m, n, 3)
        if j + 1 < m and (i, j + 1) not in pathMap:
            DFS(grid, i, j + 1, pathMap, m, n, 1)
    elif direction == 3:
        if i + 1 < n and (i + 1, j) not in pathMap:
            DFS(grid, i + 1, j, pathMap, m, n, 2)
        if i - 1 >= 0 and (i - 1, j) not in pathMap:
            DFS(grid, i - 1, j, pathMap, m, n, 0)
        if j - 1 >= 0 and (i, j - 1) not in pathMap:
            DFS(grid, i, j - 1, pathMap, m, n, 1)

if __name__ == '__main__':
    grid = [["1","1","1","1","1","0","1","1","1","1"],["1","0","1","0","1","1","1","1","1","1"],["0","1","1","1","0","1","1","1","1","1"],["1","1","0","1","1","0","0","0","0","1"],["1","0","1","0","1","0","0","1","0","1"],["1","0","0","1","1","1","0","1","0","0"],["0","0","1","0","0","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","1"],["1","1","1","1","1","1","1","1","0","1"],["1","0","1","1","1","1","1","1","1","0"]]
    ans = numIslands(grid)