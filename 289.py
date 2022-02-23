from copy import deepcopy
def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board[0]), len(board)

    for i in range(n):
        for j in range(m):
            count = countAlive(board, i, j)
            if count < 2 and board[i][j] == 1:
                board[i][j] = 2
            elif (count == 2 or count == 3) and board[i][j] == 1:
                board[i][j] = 1
            elif count > 3 and board[i][j] == 1:
                board[i][j] = 2
            elif count == 3 and board[i][j] == 0:
                board[i][j] = 3

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1

    return board


def countAlive(board, x, y):
    m, n = len(board[0]), len(board)
    start, end = [0, 0], [x, y]
    if x - 1 >= 0:
        start[0] = x - 1
    if x + 1 < n:
        end[0] = x + 1
    if y - 1 >= 0:
        start[1] = y - 1
    if y + 1 < m:
        end[1] = y + 1
    count = 0
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if i == x and j == y:
                continue
            if board[i][j] == 1 or board[i][j] == 2:
                count += 1
    return count


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # ans = gameOfLife(board)
    strs = 'cba'
    