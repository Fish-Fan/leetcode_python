def pacificAtlantic( heights ):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m, n = len(heights), len(heights[0])
    pd, ad = {}, {}
    # find all pacific ocean
    for i in range(n):
        dfshelper(pd, heights, m, n, directions, 0, i)
    for i in range(1, m):
        dfshelper(pd, heights, m, n, directions, i, 0)
    # find all atlantic ocean
    for i in range(n):
        dfshelper(ad, heights, m, n, directions, m - 1, i)
    for i in range(m - 1):
        dfshelper(ad, heights, m, n, directions, n - 1, i)

    # calculating intersection
    tmp = set(pd.keys()).intersection(set(ad.keys()))
    ans = []
    for item in tmp:
        ans.append([item[0], item[1]])
    return ans


def dfshelper( visited, heights, m, n, directions, i, j):
    if (i, j) in visited:
        return
    for d in directions:
        a, b = i + d[0], j + d[1]
        if a < 0 or a >= m or b < 0 or b >= n or heights[a][b] < heights[i][j]:
            continue
        visited[(i, j)] = 1
        dfshelper(visited, heights, m, n, directions, a, b)

if __name__ == '__main__':
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    ans = pacificAtlantic(heights)
    print(ans)