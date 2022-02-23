import sys
def coinChange(coins, amount):
    dp = [0] * (amount + 1)

    for i in range(1, amount + 1):
        minCount = sys.maxsize
        for j in coins:
            if i - j > 0 and dp[i - j] != 0:
                minCount = min(minCount, dp[i - j] + 1)
                dp[i] = minCount
            elif i - j == 0:
                dp[i] = 1
                break

    if dp[-1] == 0:
        return -1
    else:
        return dp[-1]


if __name__ == '__main__':
    ans = coinChange([1,2,5], 11)
    intList = [1,2,3]
    twoArr = [[10 for i in range(5)] for j in range(6)]
    for i in intList[::-1]:
        print(i)

    # python for 递减
    for i in range(5,0,-1):
        print('递减:' + str(i))