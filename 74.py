def searchMatrix(matrix, target):
    m, n = len(matrix[0]), len(matrix)
    # get the fitst col arr
    firstCol = []
    for i in range(n):
        firstCol.append(matrix[i][0])

    rowPos = binarysearch(firstCol, 0, n - 1, target) - 1
    colPos = binarysearch(matrix[rowPos], 0, m - 1, target)

    if rowPos != None and colPos != None and colPos < m and matrix[rowPos][colPos] == target:
        return True
    else:
        return False


def binarysearch( nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == '__main__':
    arr = [[1],[3]]
    ans = searchMatrix(arr, 1)
    strArr = ["A","B","C"]
    strArr1 = ["A","B","C"]
    print("".join(strArr))