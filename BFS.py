from collections import deque
def bfs(board, i, j, directions, visited, q, targetNum, levelNum, m, n):
    path = 0
    while len(q) > 0:
        path += 1
        l = len(q)
        while l != 0:
            l -= 1
            current = q.popleft()
            i, j = current[0], current[1]
            if (i, j) not in visited:
                board[i][j] = targetNum
                visited[(i, j)] = True
                for d in directions:
                    a, b = i + d[0], j + d[1]
                    if a >= 0 and a < n and b >= 0 and b < m and board[a][b] == levelNum:
                        q.append((a, b))
    print(path)


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append((0,0))
    bfs(grid, 0, 0, directions, {}, q, 2, 1, len(grid[0]), len(grid))
    print(grid)
