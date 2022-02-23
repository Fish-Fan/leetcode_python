def searchMatrix(matrix, target):
    m, n = len(matrix[0]), len(matrix)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

    if right < 0:
        return False
    endRow, startRow = right, right
    while startRow-1 >= 0 and matrix[startRow-1][0] < target and matrix[startRow-1][m - 1] > target:
        startRow -= 1


    while startRow <= endRow:
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[startRow][mid] == target:
                return True
            elif matrix[startRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        startRow += 1

    return False

if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    ans = searchMatrix(matrix, 5)
    print(ans)