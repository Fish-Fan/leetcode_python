# pattern for matrix DFS
def solution(matrix):
    # initialise directions
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    m, n = len(matrix[0]), len(matrix)
    # initialise visisted dict
    visited = {}
    # iterate the matrix
    for i in range(m):
        for j in range(n):
            self.DFS(matrix, m, n, visited, i, j)


def DFS(self, matrix, m, n, visited, i, j, directions):
    if (i, j) in visited:
        return
    visited[(i, j)] = 1
    for d in directions:
        a, b = i + d[0], j + d[1]
        # check boundary and additonal condition
        if a < 0 or a >= n or b < 0 or b >= m or (addtional contions):
            continue
        self.DFS(matrix, m, n, visited, i, j)
