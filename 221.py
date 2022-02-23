def maximumSquare(matrix):
    # # boundary cases
    # if len(matrix) == 0:
    #     return 0
    #
    # m = len(matrix[0])
    # n = len(matrix)
    # arr = [[0 for x in range(m)] for y in range(n)]
    # maxNum = 0
    #
    # # init arr
    # for i in range(m):
    #     arr[0][i] = int(matrix[0][i])
    #     if arr[0][i] == 1:
    #         maxNum = 1
    # for i in range(n):
    #     arr[i][0] = int(matrix[i][0])
    #     if arr[i][0] == 1:
    #         maxNum = 1
    #
    # if m == 1 or n == 1:
    #     return maxNum
    # else:
    #     for i in range(1, n):
    #         for j in range(1, m):
    #             if matrix[i][j] == "0":
    #                 arr[i][j] = 0
    #             else:
    #                 minNum = min(arr[i - 1][j - 1], min(arr[i - 1][j], arr[i][j - 1]))
    #                 arr[i][j] = minNum + 1
    #                 maxNum = max(maxNum, arr[i][j])
    #
    # return maxNum * maxNum

    m = len(matrix[0])
    n = len(matrix)

    # boundary case
    if m == 0 or n == 0:
        return 0
    maxNum = 0
    if m < 3 or n < 3:
        for subMatrix in matrix:
            for item in subMatrix:
                if item == 1:
                    maxNum = 1

    dp = [[0 for i in range(m)] for j in range(n)]

    for i in range(m):
        dp[0][i] = int(matrix[0][i])
    for i in range(n):
        dp[i][0] = int(matrix[i][0])


    for i in range(1, n):
        for j in range(1, m):

            minValue = min(dp[i - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1]))
            if int(matrix[i][j]) == 0:
                dp[i][j] = 0
            elif minValue == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = minValue + 1
            maxNum = max(maxNum, dp[i][j])

    return maxNum * maxNum





if __name__ == '__main__':
    maximumSquare([["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]])