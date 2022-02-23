

def DFS(nums, preNum, n, level, path, ans):
    if len(path) == n:
        ans.append(path[:])
        return

    for i,v in enumerate(nums):
        tmpArr = []
        if i == 0:
            for i in nums:
                tmpArr.append(i)
            DFS(tmpArr, 1, n, level+1, path+[0], ans)
            preNum = 1
        else:
            if preNum == 1:
                tmpArr.append(1)
                tmpArr.append(0)
                DFS(tmpArr, 1, n, level+1, path+[1], ans)
            else:
                tmpArr.append(0)
                tmpArr.append(1)
                DFS(tmpArr, 0, n, level+1, path+[0], ans)

if __name__ == '__main__':
    ans = []
    n = 2
    DFS([0,1], None, n, 0, [], ans)
    print(ans)