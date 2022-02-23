def maxProfit(prices):
    n = len(prices)
    dp = [0] * n

    if n < 2:
        return 0

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            profit = prices[i] - prices[j]
            if profit > 0 and j >= 2:
                profit += dp[j - 2]
            dp[i] = max(dp[i - 1], profit)

    return dp[-1]

if __name__ == '__main__':
    ans = maxProfit([1,2,3,0,2])
    print(ans)
    print(float('-inf'))