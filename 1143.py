def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text2) > len(text1):
        return longestCommonSubsequence(text2, text1)
    m, n = len(text1), len(text2)
    dp = [0 for i in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[j - 1] == text2[i - 1]:
                dp[j] += 1
            else:
                dp[j] = max(dp[j - 1], dp[j])
    return dp[-1]

def longestCommonSubstring(text1, text2):
    if len(text2) > len(text1):
        return longestCommonSubstring(text2, text1)
    m, n = len(text1), len(text2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    ans = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    return ans

if __name__ == '__main__':
    # tex1, text2 = 'bsbininm', 'acjmjkbkjkve'
    # ans = longestCommonSubsequence(tex1, text2)
    # print(ans)
    text1, text2 = 'abcdxabcde', 'abcdeabcdx'
    ans = longestCommonSubstring(text1, text2)
    print(ans)