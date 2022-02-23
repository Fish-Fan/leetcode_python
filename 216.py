def combinationSum3(k, n):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = []
    DFS(nums, [], n, ans, k)
    return ans


def DFS(nums, path, target, ans, k):
    if k < 0 or target < 0:
        return -1
    if target == 0 and k == 0:
        ans.append(path)
        return -1

    for i, v in enumerate(nums):
        tmp = DFS(nums[i + 1:], path + [v], target - v, ans, k - 1)
        if tmp == -1:
            break


if __name__ == '__main__':
    k, n = 4, 1
    combinationSum3(k, n)

    myDict = {}
    myDict['A'] = [1]
    myDict['A'].append(2)
    myDict['B'] = [2]
    for key, value in myDict.items():
        print(key)
        print(value)
        print('---')

    string = str(1) + "->" + str(2)
    print(string)
    for i in range(1,4):
        print(i)