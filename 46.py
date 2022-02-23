def permutation(nums):
    res = []
    dfs(nums, [], [False]*len(nums), res)
    return res

def dfs(nums, path, visited, res):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i,v in enumerate(nums):
        if visited[i]:
            continue
        else:
            path.append(v)
            visited[i] = True
            dfs(nums, path, visited, res)
            path.pop()
            visited[i] = False

if __name__ == '__main__':
    arr = [1,2,3,4]
    ans = permutation(arr)
    print(ans)
    arr.reverse()
    print(arr)