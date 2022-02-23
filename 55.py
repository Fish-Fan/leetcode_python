def canJump(nums):
    use = [True] + [False] * (len(nums) - 1)
    return DFS(nums, 0, use)



def DFS(nums, target, use):
    n = len(nums)

    for i, v in enumerate(nums):
        if use[i]:
            nextUse = [False] * n
            for j in range(1, v + 1):
                target = i+j
                if target < n:
                    nextUse[target] = True
                if target == n-1:
                    return True
            signal = DFS(nums, target, nextUse)
            if signal:
                return True


if __name__ == '__main__':
    arr = [8]
    ans = canJump(arr)
    print(ans)