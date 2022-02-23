from collections import defaultdict
def solution(v_arr, e_arr, path):
    # build vertices mapping
    d = {}
    idx = 0
    for v in v_arr:
        d[v] = idx
        idx += 1

    # initialise the grid
    grid = [[0 for i in range(len(v_arr))] for j in range(len(v_arr))]
    for v1, v2 in e_arr:
        idx1, idx2 = d[v1], d[v2]
        grid[idx1][idx2] = 1
        grid[idx2][idx1] = 1
    print(grid)
    # traverse the path
    for i, v in enumerate(path):
        idx = d[v]
        count = 0
        for j in range(len(v_arr)):
            if grid[idx][j] == 1:
                grid[idx][j] = 0
                grid[j][idx] = 0
                count += 1
        if count == 0 and i != len(path)-1:
            return v
    return 'yes'








if __name__ == '__main__':
    # # first input: vertices
    # v_arr = ['A', 'B', 'C', 'D']
    # # second input: edges
    # e_arr = [('A', 'B'), ('A', 'D'), ('B', 'D'), ('A', 'C')]
    # # third input: designated path
    # path = ['C', 'A', 'D', 'B']

    # # first input: vertices
    # v_arr = ['A', 'B', 'C', 'D']
    # # second input: edges
    # e_arr = [('A', 'B'), ('A', 'D'), ('B', 'D'), ('A', 'C')]
    # # third input: designated path
    # path = ['D', 'A', 'B', 'C']

    # # first input: vertices
    # v_arr = ['A', 'B', 'C']
    # # second input: edges
    # e_arr = [('B', 'A'), ('C', 'B')]
    # # third input: designated path
    # path = ['C', 'B', 'A']

    # first input: vertices
    v_arr = ['X', 'Y', 'Z', 'Q']
    # second input: edges
    e_arr = [('X', 'Y'), ('Y', 'Q'), ('Y', 'Z')]
    # third input: designated path
    path = ['Z', 'Y', 'Q', 'X']

    ans = solution(v_arr, e_arr, path)
    print(ans)

