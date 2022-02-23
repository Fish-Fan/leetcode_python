def longestIncreasingPath( matrix) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(matrix[0]), len(matrix)
    mem = {}
    ans = 0
    for i in range(n):
        for j in range(m):
            DFS(matrix, m, n, i, j, directions, mem, 0)

    for key in mem.keys():
        ans = max(ans, mem.get(key))
    return ans


def DFS( matrix, m, n, i, j, directions, mem, length):
    if  (i, j) in mem:
        return
    mem[(i, j)] = 1
    for d in directions:
        a, b = i + d[0], j + d[1]
        if a < 0 or a >= n or b < 0 or b >= m or matrix[a][b] <= matrix[i][j]:
            continue
        DFS(matrix, m, n, a, b, directions, mem, length+1)
        mem[(i, j)] = max(mem[(i, j)], 1 + mem[(a, b)])



if __name__ == '__main__':
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    ans = longestIncreasingPath(matrix)
    print(ans)