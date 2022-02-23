from collections import Counter

def findcommon(s1, s2):
    if len(s1) < len(s2):
        return findcommon(s2, s1)
    m, n = len(s1), len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                continue
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__ == '__main__':
    s1, s2 = 'abcdxabcde', 'abcdeabcdx'
    ans = findcommon(s1,s2)
    print(ans)