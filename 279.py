import math
def numSqures(n):
    # if n < 0:
    #     return 0
    # elif n <= 3:
    #     return n
    #
    # dp = [0] * (n + 1)
    # dp[0] = 0
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 3
    #
    # for i in range(4, n + 1):
    #     dp[i] = i
    #     for j in range(1, i + 1):
    #         if j * j <= i:
    #             dp[i] = min(dp[i], dp[i - j * j] + 1)
    #         else:
    #             break
    #
    # return dp[n]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        m = int(math.sqrt(i))
        minCount = i
        for j in range(1, m + 1):
            tmp = dp[i - j * j] + 1
            minCount = min(minCount, tmp)
        dp[i] = minCount

    return dp[-1]

if __name__ == '__main__':
    print(numSqures(12))
