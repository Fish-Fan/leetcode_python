def exist(board, word):
    m, n = len(board[0]), len(board)
    ans = []
    for i in range(n):
        for j in range(m):
            DFS(board, i, j, word)

    if len(ans) > 0:
        return True
    else:
        return False


def DFS( board, i, j, target):
    if len(target) == 0:
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or target[0] != board[i][j]:
        return False

    tmp = board[i][j]
    board[i][j] = '#'
    ans = DFS(board, i-1, j, target[1:]) or DFS(board, i, j+1, target[1:]) or DFS(board, i+1, j, target[1:]) or DFS(board, i, j-1, target)
    board[i][j] = tmp
    return ans


if __name__ == '__main__':
    arr = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
     ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
     ["a", "a", "b", "a", "a", "b"]]
    word = "aabbbbabbaababaaaabababbaaba"
    print(len(word))

    nums = [1,2,3,4]
    print(nums[:2])

    ans = exist(arr, word)
    print(ans)