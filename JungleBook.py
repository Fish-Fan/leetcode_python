from collections import deque, defaultdict
def predators(arr):
    roots = []
    leaves = []
    d = defaultdict(list)
    for i, v in enumerate(arr):
        if v == -1:
            roots.append(i)
        else:
            d[v].append(i)

    q = deque()
    for i in roots:
        q.append(i)
    # using BFS traverse
    while q:
        n = len(q)
        print(q)
        while n > 0:
            n -= 1
            current = q.popleft()
            if current in d:
                tmp_arr = d[current]
                for i in tmp_arr:
                    q.append(i)

if __name__ == '__main__':
    predator_arr = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
    predators(predator_arr)