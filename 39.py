def combinationSum(candidates, target):
    ans = []
    DFS(candidates, [], ans, target)
    return ans

def DFS(nums, path, ans, target):
    s = sum(path)
    if s == target:
        ans.append(path[:])
        return 0
    if s > target:
        return -1

    for i in nums:
        if len(path) > 0 and i < path[-1]:
            continue
        path.append(i)
        sign = DFS(nums, path, ans, target)
        path.pop()
        if sign == -1:
            return


if __name__ == '__main__':
    arr = [2,3,6,7]
    target = 7
    ans = combinationSum(arr, target)
    print(ans)
    twoArr = [[1,2,3],[4,5,6],[7,8,9]]
    twoArr.reverse()
    print(twoArr)
    print(twoArr[1:len(twoArr[0])][1:len(twoArr)])

    print('i--')
    for i in range(5,0,-1):
        print(i)