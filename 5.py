def longestPalindrome(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    maxLen = 0
    start = 0
    end = 0
    for leap in range(1,n):
        i = 0
        for j in range(i+leap,n):
            if s[i] == s[j] and dp[i+1][j-1] != 0:
                dp[i][j] = dp[i+1][j-1] + 2
                if leap == 1:
                    dp[i][j] = 2
            if dp[i][j] > maxLen:
                maxLen = dp[i][j]
                start = i
                end = j
            i += 1



    return s[start:end+1]

if __name__ == '__main__':
    array = [2,7,11,15]
    tempMap = {}
    for i,v in enumerate(array):
        tempMap[i] = v
    if tempMap.get(2) is not None:
        print(tempMap)