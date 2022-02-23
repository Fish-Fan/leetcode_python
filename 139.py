def solve( board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    ans = []
    m, n = len(board[0]), len(board)
    for i in range(1, m-1):
        DFS(0, i, m, n, board, [], ans, 2)
    for i in range(1, n-1):
        DFS(i, 0, m, n, board, [], ans, 1)
    for i in range(1, m-1):
        DFS(n - 1, i, m, n, board, [], ans, 0)
    for i in range(1, n-1):
        DFS(i, m - 1, m, n, board, [], ans, 3)
    print(ans)

# 0:↑, 1:→，2:↓, 3:←
def DFS( i, j, m, n, board, path, ans, direction):
    if board[i][j] == 'X':
        if len(path) > 0:
            ans.append(path[:])
        return

    if i == 0:
        DFS(i + 1, j, m, n, board, path + [(i, j)], ans, 2)
    elif j == 0:
        DFS(i, j + 1, m, n, board, path + [(i, j)], ans, 1)
    elif i == n - 1:
        DFS(i - 1, j, m, n, board, path + [(i, j)], ans, 0)
    elif j == m - 1:
        DFS(i, j - 1, m, n, board, path + [(i, j)], ans, 3)
    else:
        if direction == 0:
            DFS(i + 1, j, m, n, board, path + [(i, j)], ans, 2)
            DFS(i, j + 1, m, n, board, path + [(i, j)], ans, 1)
            DFS(i, j - 1, m, n, board, path + [(i, j)], ans, 3)
        elif direction == 1:
            DFS(i + 1, j, m, n, board, path + [(i, j)], ans, 2)
            DFS(i, j + 1, m, n, board, path + [(i, j)], ans, 1)
            DFS(i - 1, j, m, n, board, path + [(i, j)], ans, 0)
        elif direction == 2:
            DFS(i, j + 1, m, n, board, path + [(i, j)], ans, 1)
            DFS(i - 1, j, m, n, board, path + [(i, j)], ans, 0)
            DFS(i, j - 1, m, n, board, path + [(i, j)], ans, 3)
        else:
            DFS(i + 1, j, m, n, board, path + [(i, j)], ans, 2)
            DFS(i - 1, j, m, n, board, path + [(i, j)], ans, 0)
            DFS(i, j - 1, m, n, board, path + [(i, j)], ans, 3)

if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "O", "X", "X"]]
    solve(board)