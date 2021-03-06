def rob(nums):
    n = len(nums)
    # boundary cases
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp1 = [0] * (n - 1)
    dp2 = [0] * (n - 1)

    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])

    dp2[0] = nums[1]
    dp2[1] = max(nums[1], nums[2])
    for i in range(3, n):
        dp2[i - 1] = max(dp2[i - 3] + nums[i], dp2[i - 2])

    ans = max(dp1[-1], dp2[-1])
    return ans

if __name__ == '__main__':
    print(rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))