def numDecodings(s):
    n = len(s)
    dp = [0] * n

    # boundary cases
    if s[0] == '0':
        return 0
    if n == 2 and (int(s[0:2]) == 10 or int(s[0:2]) == 20):
        return 1

    dp[0] = 1

    for i in range(1, n):
        # check is valid
        if s[i] == '0' and s[i - 1] != '1' and s[i-1] != '2':
            return 0
        num = int(s[i - 1:i + 1])
        dp[i] = dp[i - 1] + checkCombinationIsValid(num)

    return dp[-1]


def checkCombinationIsValid(num):
    if num == 10 or num == 20:
        return -1
    if num > 10 and num <= 26:
        return 1
    return 0

if __name__ == '__main__':
    print(numDecodings('2101'))
    arr = [[1,2,3],[3,2,1]]
    for idx, val in enumerate(arr[1]):
        print(str(idx) + ':' + str(val))
