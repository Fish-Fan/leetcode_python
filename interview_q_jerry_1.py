# Question link: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9bf87dc7-c47f-4374-9bba-5e47561ee41f/17891645547545_.pic.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220223T143933Z&X-Amz-Expires=86400&X-Amz-Signature=b2b58354d6d781a4d4164999252bcb55873153bd55d5e3647333f9d9163f208e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%2217891645547545_.pic.jpg%22&x-id=GetObject
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

