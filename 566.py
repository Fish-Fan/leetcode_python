def matrixReshape( mat, r: int, c: int):
    m, n = len(mat[0]), len(mat)
    total = m * n
    if total % c != 0 or r * c != m * n:
        return mat

    ans = [[0 for i in range(c)] for j in range(r)]
    c1, c2 = 0, 0
    while c1 < total:
        loc1 = location(c1, n, m)
        loc2 = location(c2, r, c)
        ans[loc2[0]][loc2[1]] = mat[loc1[0]][loc1[1]]
        c1 += 1
        c2 += 1
    return ans


def location(count, r, c):
    loc = []
    row = count // c
    column = count % c
    loc.append(row)
    loc.append(column)
    return loc

if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 4
    c = 1
    ans = matrixReshape(mat, r, c)
    print(ans)

