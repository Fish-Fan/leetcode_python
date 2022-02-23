def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        tmp = 0
        for j in nums:
            if i - j >= 0:
                tmp += dp[i - j]
        dp[i] = tmp

    return dp[-1]

