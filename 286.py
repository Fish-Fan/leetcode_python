def wallsAndGates( rooms) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    directions = [(-1, 0), [1, 0], [0, -1], [0, 1]]
    m, n = len(rooms[0]), len(rooms)
    for i in range(n):
        for j in range(m):
            if rooms[i][j] == 0:
                mem = {}
                dfshelper(m, n, i, j, directions, mem, rooms, 0)



def dfshelper( m, n, i, j, directions, mem, rooms, value):
    mem[(i, j)] = value
    rooms[i][j] = min(rooms[i][j], value)
    for d in directions:
        a, b = i + d[0], j + d[1]
        if a < 0 or a >= n or b < 0 or b >= m or rooms[a][b] == -1 or (a, b) in mem:
            continue
        tmpMem = mem.copy()
        dfshelper(m, n, a, b, directions, tmpMem, rooms, value + 1)


if __name__ == '__main__':
    # rooms = [[0,2147483647,-1,2147483647,2147483647,-1,-1,0,0,-1,2147483647,2147483647,0,-1,2147483647,2147483647,2147483647,2147483647,0,2147483647,0,-1,-1,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,-1,0,0,-1,0,0,0,2147483647,0,2147483647,-1,-1,0,-1,0,0,0,2147483647],[2147483647,0,-1,2147483647,0,-1,-1,-1,-1,0,0,2147483647,2147483647,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,0,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,0,2147483647,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,2147483647,0,-1,2147483647,-1,-1,-1,0,2147483647]]
    rooms = [[0, 2147483647], [2147483647, 2147483647]]
    wallsAndGates(rooms)