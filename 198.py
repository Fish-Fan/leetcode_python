def rob(nums) -> int:
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[2]

    maxValue = dp[0]
    for i in range(3, n):
        dp[i] = dp[i - 2] + nums[i]
        maxValue = max(maxValue, dp[i])

    return maxValue

if __name__ == '__main__':
    rob([1,2,3,1])