def solve( board) -> None:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(board[0]), len(board)
    mem = {}
    # top
    for i in range(m):
        if board[0][i] == 'O' and (0, i) not in mem:
            dfshelper(board, m, n, mem, 0, i, directions)
    # right
    for i in range(n):
        if board[i][m - 1] == 'O' and (i, m - 1) not in mem:
            dfshelper(board, m, n, mem, i, m - 1, directions)
    # bottom
    for i in range(m):
        if board[n - 1][i] == 'O' and (n - 1, i) not in mem:
            dfshelper(board, m, n, mem, n - 1, i, directions)
    # left
    for i in range(n):
        if board[i][0] == 'O' and (i, 0) not in mem:
            dfshelper(board, m, n, mem, i, 0, directions)

    ans = [['X' for i in range(m)] for j in range(n)]
    for key in mem.keys():
        ans[key[0]][key[1]] = 'O'
    return ans


def dfshelper( board, m, n, mem, i, j, directions):
    if (i, j) in mem:
        return
    mem[(i, j)] = 1
    for d in directions:
        a, b = i + d[0], j + d[1]
        if a < 0 or a >= n or b < 0 or b >= m or board[a][b] == 'X':
            continue
        dfshelper(board, m, n, mem, a, b, directions)

if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solve(board)
