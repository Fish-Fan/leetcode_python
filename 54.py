def spiralOrder(matrix):
    ans = []
    spiralTraverse(matrix, ans, 0, len(matrix)-1, 0, len(matrix[0])-1)
    return ans


def spiralTraverse(matrix, ans, startRow, endRow, startCol, endCol):
    if startRow > endRow and startCol > endCol:
        return

    # traverse first row
    for i in range(startCol, endCol + 1):
        ans.append(matrix[startRow][i])

    # traverse last column
    for i in range(startRow + 1, endRow + 1):
        ans.append(matrix[i][endCol])

    # traverse last row
    #if startRow != endRow:
    for i in range(endCol - 1, startCol-1, -1):
        ans.append(matrix[endRow][i])
    # traverse first column
    # if startCol != endCol:
    for i in range(endRow - 1, startRow, -1):
        ans.append(matrix[i][startCol])

    spiralTraverse(matrix, ans, startRow + 1, endRow - 1, startCol + 1, endCol - 1)

if __name__ == '__main__':
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    arr.pop(0)
    print(list(zip(*arr)))
    print(arr[::-1])

    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(list(zip(arr1, arr2)))
